import sublime, sublime_plugin
import subprocess

class JLintCommand(sublime_plugin.WindowCommand):
  def run(self):
		print "jslint"
		print self.window.active_view().file_name()
		p = subprocess.Popen("start /b cscript " + sublime.packages_path() + "\\JLint\\JLint.js " + self.window.active_view().file_name(), stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)  
		i = 0
		for line in p.stdout:
			if i>2:
				print line.rstrip("\n")
			i = i+1
		p.wait()
