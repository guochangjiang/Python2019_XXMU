import subprocess
return_code = subprocess.Popen(r'C:\Windows\System32\cmd.exe')
print(return_code.pid)
