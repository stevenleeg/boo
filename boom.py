import sys, os, pickle

def to_clipboard(value):
	if sys.platform.startswith('darwin'):
		from AppKit import NSPasteboard
		pb = NSPasteboard.generalPasteboard()
		pb.clearContents()
		pb.writeObjects_([value])
	elif sys.platform.startswith('win32'):
		import win32clipboard
		win32clipboard.OpenClipboard()
		win32clipboard.SetClipboardText(value)
		win32clipboard.CloseClipboard()

class Boom:
	def __init__(self):
		self.boomfile = os.path.join(os.environ['HOME'], '.boom')
		
		try:
			f = open(self.boomfile, 'rb')
			self.data = pickle.load(f)
			f.close()
		except (IOError, EOFError):
			self.data = {}
			self.save()
			print("\033[94m [MEH] \033[0m .boom not found. I'll create it for you...")
	
	def save(self):
		f = open(self.boomfile, 'wb')
		pickle.dump(self.data, f)
		return True
	
	def get(self, key):
		try:
			return self.data[key]
		except KeyError:
			return None
	
	def set(self, key, value):
		self.data[key] = value
		self.save()
	
	def list(self):
		for key in self.data:
			print(key)
	
	def rm(self, key):
		del(self.data[key])
		self.save()
	
	def mv(self, key, to):
		self.data[to] = self.data[key]
		del(self.data[key])
		self.save()

def main():
	b = Boom()
	
	if len(sys.argv) == 1:
		print("Usage:\n Copy a key to clipboard: boo [key name] \n Setting a key: boo [key name] [value]")
		return
		
	# See if they specified a command as the first argument
	if sys.argv[1] == '-a':
		b.list()
		return True
	elif sys.argv[1] == '-m':
		try:
			b.mv(sys.argv[2], sys.argv[3])
			print("\033[92m [OK!] \033[0m Key %s is now known as %s." % (sys.argv[2], sys.argv[3]))
		except KeyError:
			print("\033[91m [NAH] \033[0m Key '%s' does not exist" % sys.argv[2])
		
		return True
 	# Delete?
	elif sys.argv[1] == '-r':
		try:
			b.rm(sys.argv[2])
			print("\033[92m [OK!] \033[0m Key %s has been removed." % (sys.argv[1]))
		except KeyError:
			print("\033[91m [NAH] \033[0m Key '%s' does not exist" % sys.argv[2])
		
		return True
	elif sys.argv[1] == "-p" || sys.argv[1] == '-e':
		value = b.get(sys.argv[2])
		if value is None:
			print("\033[91m [NAH] \033[0m Key '%s' does not exist" % sys.argv[2])
			return True
		print value

		return True
		
	# Set?
	try:
		value = " ".join(sys.argv[2:])
		if len(value) == 0:
			raise IndexError
		
		b.set(sys.argv[1], value)
		if '\n' in value:
			print("\033[92m [OK!] \033[0m Key '%s' now has value:\n%s" % (sys.argv[1], value))
		else:
			print("\033[92m [OK!] \033[0m Key '%s' now has value: %s" % (sys.argv[1], value))
		return
	except IndexError:
		pass
	
	# Otherwise, let's just get the key and send it to the clipboard
	value = b.get(sys.argv[1])
	
	if value is None:
		print("\033[91m [NAH] \033[0m Key '%s' does not exist" % sys.argv[1])
		return
	
	to_clipboard(value)
	print("\033[92m [OK!] \033[0m Key '%s' copied to clipboard." % sys.argv[1])
	return True

if __name__ == "__main__":
	main()
