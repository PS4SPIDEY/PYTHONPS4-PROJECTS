import subprocess
import random

for i in range(10):
	a=random.randint(0,10)
	print(a)
	if a==1:
		subprocess.Popen(['cmd'])
	elif a==2:
		subprocess.Popen(['cmd'])
	elif a==3:
		print("Bye")