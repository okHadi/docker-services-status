from app import app
from flask import render_template
import subprocess           # imports subprocess, the subprocess module allows you to spawn new processes
import contextlib
import os
from flask import render_template

@app.route('/')
def services():
    subprocess.run("chmod 700 app/web-beta.pem", shell=True)        #editable data, add your own key
    bash = os.popen("ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i app/web-beta.pem root@ckweb-beta.ddns.net sudo docker ps")
    output = bash.read()
    file_path = 'app/templates/services.txt'
    with open(file_path, "w") as o:
        with contextlib.redirect_stdout(o):
            print(output)
            
    subprocess.run('bash app/templates/docker.sh', shell=True)
    
    return render_template('home.html')       #returns the file on the server



if __name__ == "__main__":
    app.run()
