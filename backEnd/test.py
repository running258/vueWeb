import subprocess

print('$ nslookup www.python.org')
# os.system("mitmdump selenium.py")
r = subprocess.call(['mitmdump', 'selenium.py'])
print('Exit code:', r)
