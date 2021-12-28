import os, sys

USER = os.environ.get('SUDO_USER')

if USER == None:
    print('You must use sudo.')
    quit()

if sys.platform != 'linux':
	print('This only works on Linux. You are running on:', sys.platform)
	quit()

def errors(self):
        return self._errors

def colored(text, color):
    color = color.lower()
    colors = {
        "grey": "\033[1;30m%s\033[0m",
        "red": "\033[1;31m%s\033[0m",
        "green": "\033[1;32m%s\033[0m",
        "yellow": "\033[1;33m%s\033[0m",
        "blue": "\033[1;34m%s\033[0m",
        "purple": "\033[1;35m%s\033[0m",
        "cyan": "\033[1;36m%s\033[0m",
        "white": "\033[1;37m%s\033[0m",
    }
    return colors[color] % text

def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result

def do(msg="", cmd=""):
    print("[    ] %s..." % (msg), end='', flush=True)
    status, result = eval(cmd)
    if status == 0 or status == None or result == "":
        print('\r[ %s ]' % colored("OK", "green"))
        return True
    else:
        print('\r[%s]' % colored("Fail", "red"))
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      (msg, status, result))
        return False

conf = input('Run Updates? (Y/n)\n')

if conf == 'Y' or conf == 'y':
    try:
        do(msg='Update APT Package Manager',
            cmd='run_command("apt update")')
    except AttributeError:
        print('Update Failed.')
        quit()
    try:
        do(msg='Update Computer',
            cmd='run_command("sudo apt update && sudo apt upgrade")')
    except AttributeError:
        print('Update Failed')
        quit()
else:
    print('abort')