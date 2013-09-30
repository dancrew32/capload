import os
from subprocess import call
from time import time

# local file details
LOCAL = {
	'file': '%s.%s.png' % ('cap', int(time())),	
	'delete_after': True,
}

# remote server details
REMOTE = {
	'server': 'site.com',
	'user': 'username',
	'port': '22',
	'dir': {
		'start': '/var/www/',
	},
	'public_url': 'http://site.com/images/%s' % LOCAL.get('file'),
}

# scripts to run
CMD = {
	'capture': 'screencapture -s %s' % LOCAL.get('file'),
	'to_server': 'rsync -avzh -e "ssh -p%s" \'%s\' %s@%s:%s' % (
		REMOTE.get('port'),
		LOCAL.get('file'),
		REMOTE.get('user'),
		REMOTE.get('server'),
		REMOTE.get('dir').get('start'),
	),
	'copy_to_clipboard': 'pbcopy',
}

def run(cmd):
	""" Execute shell command """
	call(cmd, shell=True)
	#print cmd

def main():
	""" Capture and rsync image to remote server, copy url to clipboard """

	# capture
	run(CMD.get('capture'))

	# send to remote
	run(CMD.get('to_server'))

	# display and copy public url to clipboard
	url = REMOTE.get('public_url')
	run("echo '%s' | %s" % (url, CMD.get('copy_to_clipboard')))
	print url

	# Delete local screencapture?
	if (LOCAL.get('delete_after', False)):
		os.remove(LOCAL.get('file'))

if __name__ == '__main__':
	main()
