import subprocess
import os
from types import *

dbs = {
    "DPNK": ["dpnk"],
    "K8S": [
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

for instance, db_names in dbs:
    access_flags: List[str] = ["host", "port"]
    access_flags = [
        "--flag=" + os.environ.get(instance + "_" + flag.upper())
        for flag in access_flags
    ]
    os.environ["PGPASSWORD"] = os.environ.get(instance + "_DOADMIN_PASSWORD")
    for db in db_names:
        os.chdir("{parent}/{name}/".format(parent=pg_backup_parent_dir, name=db))
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

mariadb_backup_parent_dir = "/backup/dbs/mariadb/"

os.makedirs(mariadb_backup_parent_dir)

access_flags: List[str] = ["password", "port", "user", "host"]
access_flags = [
    "--" + flag + "=" + os.environ.get("MARIADB_" + flag.upper())
    for flag in access_flags
]
subprocess.run(["mysqldump", "--all-databases"] + access_flags)

