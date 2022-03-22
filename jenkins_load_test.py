#Source: easyaslinux.com
#Python2 and 3 compatible

from jenkins_job_trigger import trigger_job
from get_jenkins_job_status import jenkins_job_status 

import time

jenkins_job_name = "dynamic_ci"              
Jenkins_url = "http://localhost:8080"
jenkins_user = "charles_rodriguez"
jenkins_pwd = "Chuck1394!"
buildWithParameters = True
jenkins_params = {'token': 'uxWpXKFm9o', 
                  'result2':'success',
                  'result1': 'success'}

total_start = time.time()-0
for i in range(15):
    time_split_start = time.time()
    trigger_job(jenkins_job_name, Jenkins_url, jenkins_user, jenkins_pwd, buildWithParameters, jenkins_params)
    time.sleep(10)
    jenkins_job_status(job_name=jenkins_job_name,jenkins_user=jenkins_user,jenkins_password=jenkins_pwd)    
    time_split_end = time.time()  
    print(f"job {i} took {time_split_end - time_split_start - 10} seconds") 

total_end = time.time() 

print(f"total time elapsed {total_end-total_start-15*6} seconds")