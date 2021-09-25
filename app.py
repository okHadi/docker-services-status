from flask import Flask     # imports flask
import subprocess           # imports subprocess, the subprocess module allows you to spawn new processes
from subprocess import check_output

app = Flask(__name__)       

@app.route('/')
def services():
    subprocess.call("chmod +rx docker.sh", shell=True)           #turns docker.sc into an executeable by shell
    bash = subprocess.call("./check-docker-services-status/docker.sh")                       #starts the docker.sh
    with open('services.txt') as file:                             # opens the txt made by the bash
     services = file.read()                                      #reads the file
    return services                                                 #returns the file on the server



if __name__ == "__main__":
    app.run()