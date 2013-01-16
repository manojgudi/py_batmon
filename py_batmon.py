# PYthon script
try:
        import pygtk
        pygtk.require("2.0")
except:
        print "check pygtk deps"
        sys.exit()

try:
        import gtk
        import gtk.glade
except:
        print "check gtk deps"
        sys.exit(1)

class front_end():
	def __init__(self):
		
		# path
		import os
		self.path = "/opt/py_batmon"
		os.chdir(self.path)
		
		# Set glade file
		self.gladefile ="./py_batmon.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		# Window
		self.window = self.glade.get_object("window1")
		self.window.show_all()
		self.window.connect("destroy",self.main_quit)
		
		# signals dic
		self.dic = {"on_button1_clicked":gtk.main_quit}
		self.glade.connect_signals(self.dic)
		
		
	def main(self):
		# Get label2
		self.label2 = self.glade.get_object("label2")
		
		# get value
		import subprocess as sp
		self.p1 = sp.Popen(["cat", "/sys/class/power_supply/battery/capacity"], stdout=sp.PIPE)
		self.battery_value = self.p1.communicate()[0]
		self.battery_value = str(self.battery_value)
		
		# put value
		self.label2.set_text(self.battery_value)
				
	def main_quit(self,widget):
		gtk.main_quit()
		
		
if __name__=='__main__':
	front_obj=front_end()
	front_obj.main()
	gtk.main()
