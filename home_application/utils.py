# -*- coding: utf-8 -*-
from datetime import datetime
from models import ResourceData
import base64


def get_job_instance_id(client, biz_id, ip):
    script_content = base64.b64encode(
        """
        #!/bin/bash
        MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
        DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}')
        CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
        DATE=$(date "+%Y-%m-%d %H:%M:%S")
        echo -e "$DATE|$MEMORY|$DISK|$CPU"
        """
    )
    args = {
        'bk_biz_id': biz_id,
        'script_content': script_content,
        'account': 'root',
        'ip_list': [{
            'bk_cloud_id': 0,
            'ip': ip
        }]
    }
    resp = client.job.fast_execute_script(**args)
    if resp.get('result'):
        job_instance_id = resp.get('data').get('job_instance_id')
    else:
        job_instance_id = -1
    return resp.get('result'), job_instance_id


def get_job_log_content(client, biz_id, job_instance_id):
    args = {
        'bk_biz_id': biz_id,
        'job_instance_id': job_instance_id,
    }
    resp = client.job.get_job_instance_log(**args)
    is_finished = False
    log_content = ''
    latest_time = ''
    if resp.get('result'):
        data = resp.get('data')[0]
        if data.get('is_finished'):
            is_finished = True
            log_content = data['step_results'][0]['ip_logs'][0]['log_content']
            ip = data['step_results'][0]['ip_logs'][0]['ip']
            latest_record = ResourceData.objects.filter(ip=ip).last()
            if latest_record is not None:
                latest_time = datetime.strftime(latest_record.exec_time, '%Y-%m-%d %H:%M:%S')
            try:
                logs = log_content.strip('\n').split('|')
                exec_time = datetime.strptime(logs[0], '%Y-%m-%d %H:%M:%S')
                ResourceData.objects.create(
                    exec_time=exec_time,
                    biz_id=biz_id,
                    ip=ip,
                    memory=float(logs[1][:-1]),
                    disk=int(logs[2][:-1]),
                    cpu=float(logs[3][:-1]),
                )
            except Exception, e:
                print(e)
    return is_finished, log_content, latest_time
