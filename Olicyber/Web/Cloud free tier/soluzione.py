import subprocess

print(subprocess.run(["cat", "/flag.txt"], capture_output=True).stdout.decode())