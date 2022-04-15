''' ********************************************************* '''
''' Custom Conway's Game of Life                              '''
'''                                                           '''
''' Python version 3.9??                                      '''
''' Designed using State Pattern                              '''
''' ********************************************************* '''

''' Import files from individual cool cams '''

from Conway.Algorithms.alg import *
from Conway.api import *


''' Import python files '''
import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 20                              #700 - temp using restrictede space
COLUMNS = 20                           #1000 - temp using restricted space
runProgram = 0
start_flag = 0				# 0 = stop, 1 = start, 2 = pause
algFlag = 0                 # Flag to track if first time through alg function
endFlag = -1                # Flag used to terminate program once stable
thread_is_alive = 0			# tracks if thread has been started
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
	stableAt = -1      # used as a flag in cell [0][0]
				
cellStats = [[ Cell() for j in range(COLUMNS)] for _ in range(ROWS)]
		
''' Class to hold 2D array of currentGeneration '''
''' Initially populated by API when program in "stop state" '''
''' While running Algorithm creates nextGeneration cell state
    then updates currentGeneration with new data '''
class Status(json.JSONEncoder):
	# Set all cells to dead by default
	status = 0
	def default(self,obj):
		return 1 - obj.status

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
		
''' Game iteration (single generation) for Game of Life '''
def game_loop():
	global currentGeneration
	global newGen
	global runProgram
	global start_flag
	global algFlag
	global endFlag
	
	while start_flag != 1:
		# wait loop if paused or stopped
		time.sleep(0.1)            # Sleep 100 ms
	
	# Get next generation of cells
	newGen = UpdateFunction.update_generation(update, newGen, rules, cellStats)

	# Check status of end flag. If stable and still life end drawing
	# new generations (currently changes start flag to 0 ending all
	# program cycles, but should just end getting and rendering new
	# generations).
	if cellStats[0][0].stableAt > 0:
		print((f"System has reached stability in {world.gen2stable} "\
			"generations \nand has an oscillation period of "\
			f"{world.period}."))
	if world.period == 1:
		print("Still Life Found")
		print("Terminating Program - Will hand control back to API"\
			"in future")
		start = 0
	elif endFlag == -1:
		print("Oscillating pattern has been found. Will terminate"\
		"after 2 oscillations")
		endFlag = 2 * world.period
	elif endFlag > 0:
		print(f"{endFlag} generations remain before termination")
		endflag -= 1
	else:
		print("Program Terminating - will hand control back to API"
			" in future.")
		start = 0
	
	# format newGen for sending to client
	listNewGen = []
	for i in range(ROWS):
		for j in range(COLUMNS):
			listNewGen.append(newGen[i][j].status)
			
	response = json.dumps(listNewGen).encode('utf-8')
	print(f"\n\n{response}\n\n")
	socket.emit('renderGen', response)
		

def main():
	global currentGeneration
	global newGen
		
	# Get random initial cell status from algorithms
	# will be updated if user chooses specific cell layout
	UpdateFunction.generate_rand(update, currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
	
if __name__ == '__main__':
	socket.run(app, port = 8080)


'''
#BEGIN: https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

hostName = "localhost"
serverPort = 8080
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        #print(self.path)
        if self.path == "/TILES" :
            print("OOPS")
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #print(self.path[-5:-1])
            #if self.path[-5:-1] == ".htm" :
                #reqFile = open("eric--web" + self.path, "r")                
            #else :
            reqFile = open("." + self.path, "r")
            #print(reqFile.read())
            self.wfile.write(bytes(reqFile.read(), "utf-8"))
            reqFile.close()
    def do_POST(self):
        print(self.path)
        if self.path == "/TILES" or self.path == "/eric--web/TILES":
            #print("HI")
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            #for x in newGen:
            #    for y in x:
            #        print(y.status,end=" ")
            #    print()
            #print(json.dumps(newGen, cls=Status))
            self.wfile.write(bytes(json.dumps(newGen, cls=Status),"utf-8"))
import threading
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
#BEGIN: https://thispointer.com/python-how-to-create-a-thread-to-run-a-function-in-parallel/
    th = threading.Thread(target=main)
    th.daemon = True
    th.start()
#END: https://thispointer.com/python-how-to-create-a-thread-to-run-a-function-in-parallel/
    

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
	
#END: https://pythonbasics.org/webserver/
'''
