# coding: utf-8
import readyamlfile, ipconfig, cron_apt, openssh, sshkey, fail2ban, logwatch, user_create, rkhunter
import sys
import os

conf = sys.argv[1] 
vars = readyamlfile.read_conf(conf)

openssh.openssh_install(vars["sshd"])
ipconfig.set_ipconfig(vars["network"])
cron_apt.cron_apt_config(vars["cron_apt"])
fail2ban.fail2ban_jail(vars["fail2ban_jail"])
fail2ban.fail2ban_default(vars["fail2ban_default"])
logwatch.logwatch_install(vars["logwatch"])
user_create.admin_create(vars["account"])
rkhunter.rkhunter_install(vars["rkhunter"])
