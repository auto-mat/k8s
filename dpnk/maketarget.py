#!/usr/bin/python3
import os
import sys
import subprocess
import shutil
import copy

target = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()

for source_dir in sys.argv[1:]:
  for file in os.listdir(source_dir):
    orig_path = os.path.join(source_dir, file)
    dest_dir = os.path.join("auto-generated", target, os.path.split(os.path.realpath(source_dir))[1])
    shutil.os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, file)
    env = copy.copy(os.environ)
    env["TARGET"] = target
    with open(orig_path) as fd:
      rendered = subprocess.check_output("envsubst",stdin=fd, env=env)
    with open(dest_path, "wb") as fd:
      fd.write(rendered)

