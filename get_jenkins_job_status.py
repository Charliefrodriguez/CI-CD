import json
import requests
import time


# got fromm https://www.easyaslinux.com/tutorials/devops/how-to-get-build-status-of-jenkins-job-using-python-script/ 



def jenkins_job_status(job_name: str,jenkins_user: str, jenkins_password: str) -> bool:
    auth=(jenkins_user, jenkins_password)
    try:
            #had to correct url and add in auth information
            url  = "http://localhost:8080/job/%s/lastBuild/api/json" %job_name   #Replace 'your_jenkins_endpoint' with your Jenkins URL
            while True:
                    data = requests.get(url,auth=auth,headers={'content-type': 'application/json'}).json() 
                    if data['building']:
                            time.sleep(1)
                    else:
                            if data['result'] == "SUCCESS":

                                    print("Job is success")
                                    return True
                            else:
                                    print("Job status failed")
                                    return False

                
    except Exception as e:
            print(str(e))
            return False


# job_name = "dynamic_ci"   #Give your job name here


# if __name__ == "__main__":

#         if jenkins_job_status(job_name,jenkins_user="charles_rodriguez",jenkins_password="Chuck1394!"):

#                 print("Put your autmation here for 'job is success' condition")

#         else:
#                 print("Put your autmation here for 'job is failed' condition")              
	