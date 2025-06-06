# Bloodhound setup
## Commands for kali linux
#### Fix PGSQL Error

```bash
service postgresql start
sudo -u postgres psql
UPDATE pg_database SET datallowconn = TRUE WHERE datname = 'template1';
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'template1';
ALTER DATABASE template1 REFRESH COLLATION VERSION;
ALTER DATABASE postgres REFRESH COLLATION VERSION;
quit
```

#### Install Bloodhound and Setup
```bash
apt install bloodhound -y
bloodhound-setup
```
Login to neo4j at http://localhost:7474/ with default creds neo4j:neo4j and change the defautl password.
after password is changed, open /etc/bhapi/bhapi.json,
it will look like this
```bash
{
  "database": {
    "addr": "localhost:5432",
    "username": "_bloodhound",
    "secret": "bloodhound",
    "database": "bloodhound"
  },
  "neo4j": {
    "addr": "localhost:7687",
    "username": "neo4j",
    "secret": "neo4j"
  },
  "default_admin": {
    "principal_name": "admin",
    "password": "admin",
    "first_name": "Bloodhound",
    "last_name": "Kali"
  }
}
```
update your new neo4j password in the neo4j section, i set mine to toor.
```bash
{
  "database": {
    "addr": "localhost:5432",
    "username": "_bloodhound",
    "secret": "bloodhound",
    "database": "bloodhound"
  },
  "neo4j": {
    "addr": "localhost:7687",
    "username": "neo4j",
    "secret": "root"
  },
  "default_admin": {
    "principal_name": "admin",
    "password": "admin",
    "first_name": "Bloodhound",
    "last_name": "Kali"
  }
}
```
#### Load Bloodhound
`bloodhound`
you can access bloodhound at http://127.0.0.1:8080/ui/login
login with admin:admin, and change password.
- bydefault there is no data, either you can generate your own data from pentest environment or download sample data from https://github.com/user-attachments/files/17799530/ad_example_data.zip

