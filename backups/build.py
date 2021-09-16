#!/usr/bin/python3
import subprocess
result = subprocess.run("git diff --name-only HEAD~..HEAD | grep backups/", shell=True, capture_output=True)
if result.stdout:
    subprocess.run("docker build . -t auto0mat/k8s-backups:latest", shell=True)
    subprocess.run("docker login -u $DOCKER_USER -p $DOCKER_PASS", shell=True)
    subprocess.run("docker pus auto0mat/k8s-backups:latest")
