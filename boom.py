import sys, os, pickle

# TODO: Support more operating systems
def to_clipboard(value):
	from AppKit import NSPasteboard
	pb = NSPasteboard.generalPasteboard()
	pb.clearContents()
	pb.writeObjects_([value])

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

def main():
	b = Boom()
	# See if they specified a command as the first argument
	if sys.argv[1] == 'find':
		b.find(sys.argv[2])
		return True
	# Delete?
	elif sys.argv[1] == 'rm':
		b.rm(sys.argv[2])
		return True
		
	# Set?
	try:
		b.set(sys.argv[1], sys.argv[2])
		print("\033[92m [OK!] \033[0m Key '%s' now has value:\n %s" % (sys.argv[1], sys.argv[2]))
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