import psutil, os
import pdb
import subprocess as sp
id = 0
p = None

while p == None:
	for proc in psutil:
		psutil.process_iter()
		if "PROCEXP" in str(proc.name):
				p = proc
for maps in p.memory_maps():
	for m in maps:
		print(m)
p = pdb.Pdb()