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
}

pg_backup_parent_dir = "/backup/dbs/postgress/"

os.makedirs(pg_backup_parent_dir)

for instance, db_names in dbs.items():
    access_flags: List[str] = ["host", "port"]
    access_flags = [
        "--flag=" + os.environ.get(instance + "_" + flag.upper())
        for flag in access_flags
    ]
    os.environ["PGPASSWORD"] = os.environ.get(instance + "_DOADMIN_PASSWORD")
    for db in db_names:
        this_dbs_dir = "{parent}{name}/".format(parent=pg_backup_parent_dir, name=db)
        os.makedirs(this_dbs_dir)
        os.chdir(this_dbs_dir)
        subprocess.run(
            [
                "pg_dump",
                "--blobs",
                "--create",
                "--format=d",
                "--username=doadmin",
                "--dbname=" + db_name,
            ]
            + access_flags
        )

##############################################################
# MARIADB ####################################################
##############################################################


mariadb_backup_parent_dir = "/backup/dbs/mariadb/"

os.makedirs(mariadb_backup_parent_dir)

access_flags: List[str] = ["password", "port", "user", "host"]
access_flags = [
    "--" + flag + "=" + os.environ.get("MARIADB_" + flag.upper())
    for flag in access_flags
]
subprocess.run(["mysqldump", "--all-databases"] + access_flags)

##############################################################
# RESTIC #####################################################
##############################################################

subprocess.run(["restic", "backup", "/backup/"])
