from debian
run apt-get update
run apt-get install -y restic curl gnupg2 lsb-release mariadb-client
run curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
run echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
run apt-get update
run apt-get -y install postgresql-client-13
copy backup.py /