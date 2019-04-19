import os
import eel

eel.init("web")

@eel.expose
def multiply(a, b):
	print(a * b)

@eel.expose
def navigate(destination):
	eel.printWeb("Refreshing")
	eel.clearDirMap()
	eel.setCurrentDir(destination)
	if(os.path.isdir(destination)):
		for folder in os.listdir(destination):
			eel.linkTo("* " + folder, os.path.join(destination, folder))
	else:
		with open(destination) as f:
			eel.printWeb("Loading file")
			content = f.readlines()
			eel.displayContent(content)

@eel.expose
def openFile(file):
	eel.printWeb("Opening file")
	os.startfile(file)

eel.printWeb("Launching Eel Browser")

for folder in os.listdir("C:\\"):
	eel.linkTo("* " + folder, os.path.join("C:\\", folder))

eel.start("index.html")