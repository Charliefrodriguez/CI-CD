#Source: easyaslinux.com
#Python2 and 3 compatible

# got from https://www.easyaslinux.com/tutorials/devops/how-to-trigger-a-jenkins-job-remotely-from-python-script/

import requests

# jenkins_job_name = "dynamic_ci"              
# Jenkins_url = "http://localhost:8080"
# jenkins_user = "charles_rodriguez"
# jenkins_pwd = "Chuck1394!"
# buildWithParameters = True
# jenkins_params = {'token': 'uxWpXKFm9o', 
#                   'result2':'success',
#                   'result1': 'success'}

def trigger_job(jenkins_job_name: str, Jenkins_url : str, jenkins_user : str, jenkins_pwd: str, buildWithParameters: bool, jenkins_params : dict) -> None:
	try:
		auth=(jenkins_user, jenkins_pwd)
		crumb_data= requests.get("{0}/crumbIssuer/api/json".format(Jenkins_url),auth = auth,headers={'content-type': 'application/json'})
		if str(crumb_data.status_code) == "200":

			if buildWithParameters:
				data = requests.get("{0}/job/{1}/buildWithParameters".format(Jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params,headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})
			else:
				data = requests.get("{0}/job/{1}/build".format(Jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params,headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})

			if str(data.status_code) == "201":
				print ("Jenkins job is triggered")
			else:
				print ("Failed to trigger the Jenkins job")

		else:
			print("Couldn't fetch Jenkins-Crumb")
			raise 

	except Exception as e:
		print ("Failed triggering the Jenkins job")
		print ("Error: " + str(e))