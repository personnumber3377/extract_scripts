
import os

TEST_DIR = "data/"

def main():
	# Main function
	files = os.listdir(TEST_DIR)
	i = 0
	for f in files:
		# print("Now doing: "+str(f), end="")
		fh = open(TEST_DIR+f, "r")
		protocol = fh.read()
		fh.close()
		# Now open the stuff...
		if "Content-Disposition:" in protocol:
			# Save the thing...
			# print(protocol)
			if "<protocol>" in protocol:
				if "</protocol>" not in protocol:
					continue
				the_request = protocol[protocol.index("<protocol>")+len("<protocol>"):protocol.index("</protocol>")]
			elif "<protocol nocheck=\"yes\">" in protocol:
				# <protocol nocheck="yes">
				the_request = protocol[protocol.index("<protocol nocheck=\"yes\">")+len("<protocol nocheck=\"yes\">"):protocol.index("</protocol>")]
			elif "<protocol1>" in protocol:
				the_request = protocol[protocol.index("<protocol1>")+len("<protocol1>"):protocol.index("</protocol1>")]
			else:
				the_request = None
			if the_request:
				the_request = the_request.replace("\n", "\r\n")
				the_request = the_request.replace("\r\r\n", "\r\n")
				print(the_request,end="")
				print(protocol)
				if the_request.startswith("\r\n"):
					the_request = the_request[2:]
				fh = open("out2/"+str(i), "w")
				fh.write(the_request)
				fh.close()
				i += 1

	return

if __name__=="__main__":
	main()
	exit()
