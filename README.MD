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

ansible-pull -U https://github.com/krtvand/s-logs-deploy -i "localhost," --ask-become-pass -e 'ansible_python_interpreter=/usr/bin/python3' --vault-password-file=vault_pass  deploy_to_alex.yml
```
