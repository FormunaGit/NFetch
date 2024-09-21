import distro
from colorama import Fore
import re
import subprocess

def get_base_system():
    with open('/etc/os-release', 'r') as f:
        data = f.read()
    match = re.search(r'ID_LIKE=(.*)', data)
    if match:
        return match.group(1).strip('"')
    else:
        return 'Unknown'

class NFI:
    OS = {
        'ubuntu': '',
        'debian': '',
        'rhel': '',
        'centos': '',
        'fedora': '',
        'opensuse': '',
        'sles': '',
        'amazon': '',
        'arch': '󰣇',
        'buildroot': '󰥯',
        'cloudlinux': '',
        'exherbo': '󰆚',
        'gentoo': '󰣨',
        'linuxmint': '󰣭',
        'mageia': '',
        'pidora': '/',
        'raspbian': '',
        'slackware': '',
        'openbsd': '',
        'netbsd': '󰉀',
        'freebsd': '',
        'midnightbsd': '󰽥',
        'rocky': '',
        'guix': '',
        'tux': '',
        # Advanced Find
        'endeavouros': '',
    }

def findIcon(dis=distro.id(), name=distro.name()):
    if dis in NFI.OS:
        return NFI.OS[dis]
    else:
        if name in NFI.OS:
            return NFI.OS[name]
        else:
            return NFI.OS['tux']
class C:
    def r(self, s):
        print(Fore.RED + s + Fore.RESET)
    def g(self, s):
        print(Fore.GREEN + s + Fore.RESET)
    def y(self, s):
        print(Fore.YELLOW + s + Fore.RESET)
    def b(self, s):
        print(Fore.BLUE + s + Fore.RESET)
    def m(self, s):
        print(Fore.MAGENTA + s + Fore.RESET)
    def c(self, s):
        print(Fore.CYAN + s + Fore.RESET)

class DataObtainer:
    def getPackageCount(self):
        if get_base_system() == 'arch':
            packageCount = subprocess.check_output('pacman -Q | wc -l', shell=True).decode('utf-8').strip()
            return packageCount
        else:
            return 'N/A'
    def getUser(self):
        return subprocess.check_output('whoami', shell=True).decode('utf-8').strip()
    def getHostname(self):
        return subprocess.check_output('hostname', shell=True).decode('utf-8').strip()
def cpuName():
    cpuinfo = open('/proc/cpuinfo', 'r').read().splitlines()
    for i in cpuinfo:
        if i.split(':')[0] == 'model name	':
            return i.split(':')[1].strip()
    return 'N/A'
def cpuCores():
    return subprocess.check_output('nproc', shell=True).decode('utf-8').strip()
def monitorSize():
    return subprocess.check_output('xdpyinfo | grep dimensions | sed -r \'s/^[^0-9]*([0-9]+x[0-9]+).*$/\\1/\'', shell=True).decode('utf-8').strip()


def promptConstructor():
    print(f'  |{DataObtainer().getUser()}@{DataObtainer().getHostname()}')
    print(f' {findIcon()} |{distro.name(pretty=True)}')
    print(f'  |{cpuName()} ({cpuCores()} cores)')
    print(f' 󰍹 |{monitorSize()}')
    print(f'  |{DataObtainer().getHostname()}')
    print(f' 󰏖 |{DataObtainer().getPackageCount()} ({get_base_system()})')

promptConstructor()