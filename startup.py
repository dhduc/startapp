#!/usr/bin/python
import sys
import subprocess
import optparse
import string
from datetime import datetime

class UI:
	# Code
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    # Color
    ORANGE = '\033[33m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    LIGHTGRAY = '\033[97m'
    BLACK = '\033[98m'

    def echo(self) :
    	print 'echo'

class Main :

	def __init__(self) :
		param =  raw_input(UI.GREEN + 'Do you want to continue (y/n) ? ' + UI.ENDC)
		if param == 'y' :
			startup = Startup()
			startup.run()
		else :
			print UI.RED + 'Exit.' + UI.ENDC
			return

class Startup :

	tasks = [];

	def init(self) :
		tasks = [
			# Program
			['Skype', '', 'skype', '&'],
            ['Sublime Text', '', 'subl', ''],
			['Gedit', '', 'gedit', '&'],
			['Folder', '', 'nautilus', ''],
			# Browser
			['HR Site', 'http://hr.smartosc.com/login.php', 'google-chrome', ''],
			['Skype Web', 'https://web.skype.com/en/', 'google-chrome', ''],
			['Facebook', 'https://www.facebook.com/', 'google-chrome', ''],
			['Gmail', 'https://mail.google.com/mail/', 'google-chrome', '']
		]
		self.tasks = tasks
	
	def title(self) :
		print UI.GREEN + 'Startup Helper ' + UI.BLUE +  '@author ducdh' + '' + UI.ENDC
	
	def run(self) :
		self.init()
		self.title()		
		self.runTasks()		

	def runTasks(self) :
		tasks = self.tasks
		for name, path, program, option in tasks :
			print UI.GREEN + 'Open ' + name + UI.ENDC
			command = program + ' ' + path
			subprocess.call(command, shell=True)									

main = Main()	