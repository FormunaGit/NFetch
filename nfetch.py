# Imports
import getpass # Gets Username
import platform
import socket # Gets hostname
import os, subprocess, re # For CPU finder
# Try: Except: imports for non-preinstalled modules
try: # Attempt to get Colorama
    from colorama import Fore, Back
except ImportError:
    print("Uh oh! Colorama is needed for coloring purposes! This script will end with an error!")

try: # Attempt to get [distro]
    import distro
except ImportError:
    print(Color.Red("Uh oh! Distro is required to identify what Linux distribution you are using! This script will end with an error!"))

try: # Attempt to get psutil
    import psutil
except ImportError:
    print(Color.Red("Uh oh! PSUTIL is required to identify your hardware! This script will end with an error!")) 

# Global Variables
system = platform.uname()

# Classes, Icons
class Icons: # OS Variables, Icons
    User = ""
    Monitor = "󰍹"
    CPU = "󰻠"
    class OS:
        isLinux = False
        useDistro = False
        Arch = "󰣇"
        Debian = ""
        Ubuntu = ""
        RedHat = "󱄛"
        Mageia = ""
        Raspbian = ""
        Fedora = " "
        Slackware = ""
        Tux = ""
        Unknown = ""
class Color: # Colorama, but easier
    def Red(text: str):
        return Fore.RED + text + Fore.RESET
    def Yellow(text: str):
        return Fore.YELLOW + text + Fore.RESET
    def Green(text: str):
        return Fore.GREEN + text + Fore.RESET
    def Cyan(text: str):
        return Fore.CYAN + text + Fore.RESET
class A: # ASCII mini-icons
    trc = "┐" # Top Right Corner
    tlc = "┌" # Top Left Corner
    brc = "┘" # Bottom Right Corner
    blc = "└" # Bottom Left Corner
    lh = "─" # Line Horizontal
    lv = "│" # Line Vertical
    lvl = "├" # Line Vertical + Line
    s = "◻" # Square
class InfoGen:
    def CPU():
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line,1)

def OSIcon(): # Generate Icon from OS
    if distro.id() == "ubuntu":
        return Icons.OS.Ubuntu
    elif distro.id() == "debian":
        return Icons.OS.Debian
    elif distro.id() == "arch":
        return Icons.OS.Arch
    elif distro.id() == "rhel":
        return Icons.OS.RedHat
    elif distro.id() == "raspbian":
        return Icons.OS.Raspbian
    elif distro.id() == "mageia":
        return Icons.OS.Mageia
    elif distro.id() == "fedora":
        return Icons.OS.Fedora
    elif distro.id() == "slackware":
        return Icons.OS.Slackware
    else:
        return Icons.OS.Tux

def generateFetch():
    print(Color.Red("┌───────────────") + Color.Yellow("NFETCH") + Color.Red("───────────────")) # Top Bar
    print(Color.Red(A.lvl) + f" {Icons.User} " + Color.Green(getpass.getuser()) + Color.Red("@") + Color.Yellow(socket.gethostname())) # Username and Hostname
    print(f"{Color.Red(A.lvl)} {OSIcon()} {Color.Cyan(distro.name())} {distro.version()} ({Color.Green(distro.codename())})") # OS NAme & Version
    print(f"{Color.Red(A.lvl)} {Icons.CPU}{Color.Yellow(InfoGen.CPU())}")
    print(Color.Red("└────────────────────────────────────"))

generateFetch()