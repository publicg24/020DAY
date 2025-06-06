# Bloodhound setup
## Commands for kali linux
```bash
curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg
echo "deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable 5.x" | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt update && sudo apt install neo4j -y
sudo systemctl enable neo4j - this will creat a issue
sudo nano /etc/systemd/system/neo4j.service
```
 note:add the below configuration into the neo4j.service
```bash
                     [Unit]
                      Description=Neo4j Graph Database
                      After=network.target

                      [Service]
                       Type=simple
                          User=root
                        Group=root
                         ExecStart=/usr/bin/neo4j console
                        Restart=on-failure
                        Environment="NEO4J_HOME=/var/lib/neo4j"
                        LimitNOFILE=60000

                       [Install]
                       WantedBy=multi-user.target
```
```bash                  
6. >sudo systemctl daemon-reload
7. >sudo systemctl restart neo4j
8. >sudo systemctl status neo4j
```

now neo4j is ready
------------------------------------------------------------------------------------------
for bloodhound instilation used deepseek

credentials\
admin/admin default\
admin/12345@bloodhounD (modified password)
