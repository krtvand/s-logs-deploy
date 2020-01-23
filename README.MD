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
```bash
# docker_build_and_push_app_image
ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' docker_build_and_push_app_image.yml
```
