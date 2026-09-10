# Born2beroot

Born2beroot is a 42 system administration project based on a virtual machine.

## Goal

The project is about understanding the basics of Linux server administration:

- install and configure a virtual machine
- create and manage users and groups
- configure `sudo` rules
- connect to the VM with SSH
- configure a firewall
- check services and system information
- prepare a monitoring script

## Useful Commands

### Check System Information

```bash
hostname
whoami
cat /etc/os-release
uname -a
```

### Users And Groups

```bash
id
groups
getent group sudo
sudo adduser username
sudo usermod -aG sudo username
```

### SSH

On the VM, check the IP address:

```bash
hostname -I
```

From the Mac terminal, connect to the VM with SSH:

```bash
ssh student@VM_IP_ADDRESS
```

Example:

```bash
ssh student@10.0.0.15
```

This means the VM can be managed directly from the local machine terminal.

### Firewall

```bash
sudo ufw status
sudo ufw allow 4242
sudo ufw enable
```

### Services

```bash
systemctl status ssh
systemctl status ufw
```

### Disk And Memory

```bash
df -h
free -h
lsblk
```

### Processes

```bash
ps aux
top
```

## Notes

This folder is kept separate from the C projects because Born2beroot is focused on Linux system administration and virtual machines.
