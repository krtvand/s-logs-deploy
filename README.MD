### Deploy
sudo apt update
sudo apt install python3 python3-pip
pip3 install ansible
pip3 install docker-py

### Ansible development
```bash
# view encrypted vars
ansible-vault view --vault-password-file .vault_pass group_vars/all 
# decrypt encrypted vars 
ansible-vault decrypt --vault-password-file .vault_pass group_vars/all 
# encrypt vars
ansible-vault encrypt group_vars/all
```


### Deploy

 ***Alex deploy***
```bash
sudo pip3 install ansible

sudo mkdir /sorm_logs
sudo echo 'vault_pass' > /sorm_logs/.vault_pass
ansible-pull -U https://github.com/krtvand/s-logs-deploy --ask-become-pass alex_pull.yml
```
