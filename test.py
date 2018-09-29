import time, signal, os
from sh import gphoto2 as gp
from datetime import datetime as dt
import subprocess as sp


# Kill gphoto2 process upon start
def killgphoto():
	p = sp.Popen(['ps', '-A'], stdout=sp.PIPE)
	out, err = p.communicate()

	# Search for process for gphoto2
	for line in out.splitlines():
		if b'gvfsd-gphoto2' in line:
			# Kill this process
			pid = int(line.split(None, 1)[0])
			os.kill(pid, signal.SIGKILL)


# Take a photo
triggerCommand = ['--trigger-capture']
def takePhoto():
	gp(triggerCommand)
