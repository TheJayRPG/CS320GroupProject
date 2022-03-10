''' ********************************************************* '''
''' Custom Conway's Game of Life                              '''
'''                                                           '''
''' Python version 3.9??                                      '''
''' Designed using State Pattern                              '''
''' ********************************************************* '''

''' Import files from individual cool cams '''

from Algorithms.alg import *

#BEGIN: https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
hostName = "localhost"
serverPort = 8080
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        reqFile = open("src/website/graphics" + self.path, "r")
        #print(reqFile.read())
        self.wfile.write(bytes(reqFile.read(), "utf-8"))
        reqFile.close()
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))
		



#END: https://pythonbasics.org/webserver/
''' Import python files '''
import time

''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 20                              #700 - temp using restrictede space
COLUMNS = 20                           #1000 - temp using restricted space

''' Class holding rules for current game '''
''' Populated by API, used by all '''
''' Default rules for "square cells" set initially '''
class Rules:

	def __init__(self, ROWS, COLUMNS, shape = 4, pattern = 1, min2live = 2,
	    max2live = 3, min2spawn = 3, max2spawn = 3):
	    # If no values given default values will be used
		self.rows = ROWS
		self.columns = COLUMNS
		self.shape = shape            # options are 3,4,5,6 sides
		self.pattern = pattern        # 1= single layer, 2= double, 3= knight's move
		self.min2live = min2live
		self.max2live = max2live
		self.min2spawn = min2spawn
		self.max2spawn = max2spawn
				
rules = Rules(ROWS, COLUMNS)
		
''' Class holding cell statistics '''
''' Populated by Algorithms, used by ThoughtProcess and to print '''
''' Held in 2D array cellStats[row][column] '''
class Cell:
	# Define singleton
	neighbors = 0
	past = []          # list to hold last 30 cell states
	generations = 0
	living = 0
	dead = 0
				
cellStats = [[ Cell() for j in range(COLUMNS)] for _ in range(ROWS)]
		
''' Class to hold 2D array of currentGeneration '''
''' Initially populated by API when program in "stop state" '''
''' While running Algorithm creates nextGeneration cell state
    then updates currentGeneration with new data '''
class Status():
	# Set all cells to dead by default
	status = 0

# Two instances of class to avoid use before definition issue
currentGeneration = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]
newGen = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]

''' Structur to hold cell thoughts '''
class Thoughts:
	pass
	#def_init_(self):
	#	self. =
	#	self. =
		
	#	cellThoughts = [ [Thoughts()] * COLUMNS for _ in range(ROWS)]
		
''' Main loop for Game of Life '''
def main():

	while 1:
		algFlag = 0                 # Flag to track if first time through alg function
	
		''' Get rules and beginning currentGenerationm cell Status from API '''
		# rules = Rules
		# zoom = 0
		start = 1
		''' should be defined in API '''
		# start = getAPIinfo(rules, currentGeneration)
	
		# Get random initial cell status from algorithms
		UpdateFunction.generate_rand(update, currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
		# TEMPORARY
		# Draw image of initial generation of cells- could be here or inside next loop
		UpdateFunction.draw_generation(update, currentGeneration, ROWS, COLUMNS)
	
		while start == 1:
	
			''' Get current zoom level from API for rendering '''
			#zoom = getZoom()
		
			''' Update cell thought process '''
			#if (err = updateThoughtProcess(rules, currentGeneration[i][j], cellStats[i][j], cellThoughts[i][j])) != 0:
			''' Handle error with thought process '''
			#print("Error with thought process. Error code {err}\n")
	
			''' Render image '''
		
		
			'''if (err = renderImage(rules.shape, ROWS, COLUMNS, zoom, currentGeneration)) != 0:'''
			''' Handle error with image rendering '''
			#print("Error with image rendering. Error code {err}\n")
			
			''' Update currentGeneration Status using Algorithms '''
			#if (algorithmErr = updateStatus(rules, currentGeneration, cellStats)) != 0:
			''' Handle error with status update '''
			#print("Error with updating cell status. Error code {algorithmErr}\n")
			''' Algorithms '''
			if algFlag == 0:
				newGen = update.update_generation(currentGeneration, rules, cellStats)
			else:
				newGen = UpdateFunction.update_generation(update, newGen, rules, cellStats)
			algFlag = 1
	
			# Temp render updated generation of cells
			UpdateFunction.draw_generation(update, newGen, ROWS, COLUMNS)
		
			# temp sleep- later sleep is used for pause only
			start = 2
			#start = getAPIinfo(rules, currentGeneration)
		
			''' if start == 2 pause until "game" is resumeed '''
			while start == 2:
				time.sleep(0.5)          # pause 500 miliseconds
				start = 1
	
		''' Exited program before stability was reached. Report error. '''
		''' Save current game status '''
		#if algorithmErr == 1:
		#	print("Program exited prior to reaching stability\n")
		#	print("Saving curent program status.\n")
		
		#if (err = saveProgram(rules, currentGeneration, cellStats, cellThoughts)) != 0:
		#	''' Handle error saving game status '''
		#	print("Error saving game. Error code {err}\n")
	
#if __name__ == '__main__':
#	main()
	



#BEGIN: https://pythonbasics.org/webserver/		
import threading
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
#BEGIN: https://thispointer.com/python-how-to-create-a-thread-to-run-a-function-in-parallel/
    th = threading.Thread(target=main)
    th.start()
#END: https://thispointer.com/python-how-to-create-a-thread-to-run-a-function-in-parallel/
    

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    
#END: https://pythonbasics.org/webserver/

