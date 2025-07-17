
import os

TEST_DIR = "data/"

def main():
	# Main function
	files = os.listdir(TEST_DIR)
	i = 0
	for f in files:
		# print("Now doing: "+str(f), end="")
		fh = open(TEST_DIR+f, "r")
		data = fh.read()
		fh.close()
		# Now open the stuff...
		if "Content-Disposition:" in data:
			# Save the thing...
			# print(data)
			if "<data>" in data:
				if "</data>" not in data:
					continue
				the_request = data[data.index("<data>")+len("<data>"):data.index("</data>")]
			elif "<data nocheck=\"yes\">" in data:
				# <data nocheck="yes">
				the_request = data[data.index("<data nocheck=\"yes\">")+len("<data nocheck=\"yes\">"):data.index("</data>")]
			elif "<data1>" in data:
				the_request = data[data.index("<data1>")+len("<data1>"):data.index("</data1>")]
			else:
				the_request = None
			if the_request:
				the_request = the_request.replace("\n", "\r\n")
				the_request = the_request.replace("\r\r\n", "\r\n")
				print(the_request,end="")
				print(data)
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
