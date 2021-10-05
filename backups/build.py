#!/usr/bin/python3
import subprocess
from subprocess import PIPE


result = subprocess.run("git diff --name-only $LAST_SUCCESSFUL_COMMIT~..HEAD | grep backups/", shell=True, stdout=PIPE)
if result.stdout:
    import os
    os.chdir("./backups/")
    subprocess.run("docker build . -t auto0mat/k8s-backups:$CIRCLE_BUILD_NUM", shell=True)
    subprocess.run("docker login -u $DOCKER_USER -p $DOCKER_PASS", shell=True)
    subprocess.run("docker push auto0mat/k8s-backups:$CIRCLE_BUILD_NUM", shell=True)
else:
    print("Nothing to build, backup files not changed.")
