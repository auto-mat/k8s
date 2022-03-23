#!/usr/bin/python3
import subprocess
import os
from typing import *

##############################################################
# POSTGRES ###################################################
##############################################################

dbs = {
    "DPNK": ["dpnk"],
    "SHARED_DB": [
        "dpnk-test",
        "klub-automat",
        "klub-brontosaurus",
        "klub-diakonie",
        "klub-investigace",
        "klub-test",
        "limesurvey",
        "mapa",
        "mapa-test",
    ],
    "METABASE_DB": ["metabase"],
}

pg_backup_parent_dir = "/backup/dbs/postgress/"

os.makedirs(pg_backup_parent_dir, exist_ok=True)

for instance, db_names in dbs.items():
    access_flags: List[str] = ["host", "port"]
    access_flags = [
        "--{}={}".format(flag, os.environ.get(instance + "_" + flag.upper()))
        for flag in access_flags
    ]
    os.environ["PGPASSWORD"] = os.environ.get(instance + "_DOADMIN_PASSWORD")
    for db_name in db_names:
        print("Backing up ", db_name, " from instance ", instance)
        this_dbs_dir = "{parent}{name}/".format(
            parent=pg_backup_parent_dir, name=db_name
        )
        os.makedirs(this_dbs_dir, exist_ok=True)
        os.chdir(this_dbs_dir)
        subprocess.run(
            [
                "pg_dump",
                "--blobs",
                "--create",
                "--format=d",
                "--username=doadmin",
                "--dbname=" + db_name,
                "--file=" + this_dbs_dir,
            ]
            + access_flags
        )

##############################################################
# MARIADB ####################################################
##############################################################


mariadb_backup_parent_dir = "/backup/dbs/mariadb/"

print("Backing up Mariadb")

os.makedirs(mariadb_backup_parent_dir, exist_ok=True)

access_flags: List[str] = ["password", "port", "user", "host"]
access_flags = [
    "--" + flag + "=" + os.environ.get("MARIADB_" + flag.upper())
    for flag in access_flags
]
cmd = ["mysqldump", "--all-databases"] + access_flags
cmd = " ".join(cmd) + " > " + mariadb_backup_parent_dir + "backup.sql"

subprocess.run(cmd, shell=True)

##############################################################
# RESTIC #####################################################
##############################################################

subprocess.run(["restic", "backup", "/backup/"])
