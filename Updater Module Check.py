from modulefinder import ModuleFinder

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
        

finder = ModuleFinder()
finder.run_script('Updater.py')

print('Checking \'Updater.py\' - May take a few moments...\n=========================================================')
print('%s:' % colored("Lodaed Modules", "green"))
for name, mod in finder.modules.items():
	print('%s: ' % name, end='')
	print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('%s:' % colored("Missing Modules", "red"))
print('\n'.join(finder.badmodules.keys()))
print('=========================================================\n%s' % colored("Missing modules can be ignored if program runs.", "blue"))
