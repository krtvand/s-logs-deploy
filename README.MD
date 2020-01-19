### Ansible development
```bash
# view encrypted vars
ansible-vault view --vault-password-file .vault_pass group_vars/all 
# decrypt encrypted vars 
ansible-vault decrypt --vault-password-file .vault_pass group_vars/all 
```


### Deploy
```bash
# docker_build_and_push_app_image
ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' docker_build_and_push_app_image.yml
```
