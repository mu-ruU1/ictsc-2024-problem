# Ansible

IKM の問題 VM を構築するための Ansible Playbook

## 事前準備

```bash
ansible-galaxy collection install community.general
cp hosts.yml.example hosts.yml
```

### hosts.yml の編集

- interface_ip
  - DNAT 環境下で管理対象ノードのアドレスと問題環境のアドレスが異なる場合に指定
  - 変数 false, 空文字の場合: `ansible_host`
- prob_user
  - 競技者ログインユーザ
  - 変数 false, 空文字の場合: `ansible_user`

## 実行

```bash
ansible-playbook playbook.yml
```
