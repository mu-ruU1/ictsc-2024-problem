# Ansible

IKM の問題 VM を構築するための Ansible Playbook

## 事前準備

```bash
ansible-galaxy collection install community.general
```

## 使い方

```bash
cp hosts.yml.example hosts.yml # Edit hosts.yml
ansible-playbook playbook.yml
```
