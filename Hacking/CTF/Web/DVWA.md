# DVWA
-------------------------------------------
## DVWA (Damn Vulnerable Web Application)
Installation Steps
1. Update System Packages
```bash
sudo apt update && sudo apt upgrade -y
```
2. Install Required Packages
```bash
sudo apt install -y apache2 mariadb-server php php-mysqli php-gd libapache2-mod-php unzip
```
3. Configure MySQL/MariaDB
```bash
sudo mysql_secure_installation
```
Follow the prompts to set a root password and secure your installation.
4. Create DVWA Database and User
```bash
sudo mysql -u root -p
```
```sql
CREATE DATABASE dvwa;
CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
exit
```
```bash
sudo apt install -y apache2 mariadb-server php php-mysqli php-gd libapache2-mod-php unzip
```
3. Configure MySQL/MariaDB
```bash
sudo mysql_secure_installation
```
```bash
sudo mysql -u root -p
```
```sql
CREATE DATABASE dvwa;
CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
exit
```
```bash
Follow the prompts to set a root password and secure your installation.
4. Create DVWA Database and User
```bash
sudo mysql -u root -p
```
```sql
CREATE DATABASE dvwa;
CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
exit
```

```bash
sudo apt install -y apache2 mariadb-server php php-mysqli php-gd libapache2-mod-php unzip
```
3. Configure MySQL/MariaDB
```bash
sudo mysql_secure_installation
```
Follow the prompts to set a root password and secure your installation.
4. Create DVWA Database and User
```bash
sudo mysql -u root -p

In the MySQL prompt:
```sql
CREATE DATABASE dvwa;
CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
exit
```
5. Download and Install DVWA
```bash
cd /var/www/html
sudo wget https://github.com/digininja/DVWA/archive/master.zip
sudo unzip master.zip
sudo mv DVWA-master dvwa
sudo rm master.zip
```
6. Configure DVWA
```bash
cd dvwa/config
sudo cp config.inc.php.dist config.inc.php
sudo nano config.inc.php
```
Update these lines (use the credentials you created earlier):
php
```sql
$_DVWA['db_user'] = 'dvwa';
$_DVWA['db_password'] = 'p@ssw0rd';
$_DVWA['db_database'] = 'dvwa';

$_DVWA['recaptcha_public_key'] = '';
$_DVWA['recaptcha_private_key'] = '';
```
7. Set Permissions
```bash
sudo chown -R www-data:www-data /var/www/html/dvwa
sudo chmod -R 755 /var/www/html/dvwa
```
8. Restart Apache
```bash
sudo systemctl restart apache2
```
9. Access DVWA

Open your web browser and navigate to:
```text

http://your-server-ip/dvwa
```
```bash
sudo systemctl restart apache2
```
9. Access DVWA

Open your web browser and navigate to:
```text

http://your-server-ip/dvwa
```
10. On the DVWA login page:
```bash
    Default credentials: admin/password
    Click on "Create / Reset Database" button
    Log in with the credentials
```
