''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' API                                                                     '''
''' *********************************************************************** '''

''' Requires password.py file in Conway directory containing g-mail account '''
''' 'EMAIL' and 'PASSWORD' for use as login credentials. Email will be sent '''
''' to address given in credentials.                                        '''

from flask import Flask, request, jsonify, render_template, url_for,\
                  copy_current_request_context
from flask_socketio import SocketIO
import threading
from threading import Thread, Event
from math import floor
import json

from Conway.password import EMAIL, PASSWORD
from Conway.main import *

# Setup basic web app
app = Flask(__name__, static_url_path='', template_folder="eric--web/templates", static_folder='eric--web/static')
'''static_url_path='/Users/kristinehess/Desktop/CS_320/Project_code/Github_Code/eric--web')'''
app.config['SECRET_KEY'] = 'secret!'
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False
app.use_reloader = False

# Start socketio app
socket = SocketIO(app)

# Server thread
thread = Thread()
thread_stop_event = Event()

# Render html templates
@app.route("/")
@app.route('/index/')
def login():
    return render_template("index.html")

@app.route('/createAccount/', methods=['GET'])
def createAccount():
	return render_template("createAccount.html")

@app.route('/home/', methods=['GET'])
def home():
	return render_template("home.html")
	
@app.route('/sim/', methods=['GET'])
def sim():
	return render_template("sim.html")
	
# Send contact e-mail
#@socket.event
@app.route('/home/', methods=['POST'])
def contact_us():
	import smtplib
	name = request.form.get("name")
	message = request.form.get("message")
	sendMessage = (f"Message sent from CGOL Contact Form\n{name}\n{message}")
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(EMAIL, PASSWORD)
	server.sendmail(
		request.form.get("email"),
		EMAIL,
		sendMessage)
	server.quit()
	feedback = "Thank you for contacting us."
	return render_template("home.html", feedback=feedback)

# Handle start button presses
@ socket.event
def get_start_state(start):
	print(f"\n{start}\n")
	# Start or Pause button pressed
	if start == "START":
		from Conway.main import start_flag, currentGeneration, newGen, Status
		from Conway.main import ROWS, COLUMNS, thread_is_alive, game_loop
		from Conway.Algorithms.alg import UpdateFunction, update
		from Conway.Algorithms.alg import SetInitialCells, initial_cells
		print("Start button was pressed")
		# Pause
		if start_flag == 1:
			start_flag = 2
			print(f"Flag = {start_flag}")
		# Start/Restart
		else:
			start_flag = 1
			print(f"Flag = {start_flag}")
			if thread_is_alive == 0:
				print("Starting game thread")
				thread_is_alive = 1
				response = json.dumps(currentGeneration, cls=Status)
				#print(f"\n{response}\n\n")
				socket.emit('renderGen', response)
				print("done with first emit")
				thread = socket.start_background_task(game_loop, start_flag)
		return '', 204

# Handle pause button presses
@ socket.event
def get_pause_state(pause):
	from Conway.main import start_flag
	print("Pause button was pressed")
	start_flag = 2
	return render_template("sim.html")

# Handle stop button presses
@ socket.event
def get_stop_state(stop):
	from Conway.main import start_flag, Cell, cellStats, Rules, rules
	from Conway.main import Status, currentGeneration, ROWS, COLUMNS
	from Conway.Algorithms.alg import Cells_Environment, world, SetInitialCells
	from Conway.Algorithms.alg import UpdateFunction, update, initial_cells
	print("Stop button was pressed")
	start_flag = 0
	response = json.dumps(world, cls=Cells_Environment)
	print("Seding terminating stats.")
	socket.emit('terminate', response)
	
	# Not stable- start save function
	if cellStats[0][0].stableAt < 0:
		print("Not stable, initiate save function")
		socket.emit('save', '')
	
	# Stable and end values reported. Reset and exit
	else:
		# Reset Variables for next iteration
		runProgram = 0
		algFlag = 0
		endFlag = -1
		for x in range(ROWS):
			for y in range(COLUMNS):
				cellStats[x][y].neighbors = 0
				cellStats[x][y].past = []
				cellStats[x][y].generations = 0
				cellStats[x][y].living = 0
				cellStats[x][y].dead = 0
				cellStats[x][y].stableAt = -1
		world.gen2stable = -1
		world.period = -1
		world.stable = -1
		world.living = []
		world.numLiving = 0
		world.changed = []
		world.numChanged = 0
	
	return '', 204
	
# user wishes to save file
@ socket.event
def saveFile(val):
	from Conway.main import start_flag, Cell, cellStats, Rules, rules
	from Conway.main import Status, currentGeneration, ROWS, COLUMNS
	from Conway.Algorithms.alg import Cells_Environment, world, SetInitialCells
	from Conway.Algorithms.alg import UpdateFunction, update, initial_cells
	from Conway.dennis_save.file_save_reduced import writeFile
	
	# save file
	if val == true:
		if (writeFile(" ", rules, currentGeneration, cellStats) < 0):
			print("Error saving file.")
	
	# Reset variables to clean up program to rerun
	runProgram = 0
	algFlag = 0
	endFlag = -1
	for x in range(ROWS):
		for y in range(COLUMNS):
			cellStats[x][y].neighbors = 0
			cellStats[x][y].past = []
			cellStats[x][y].generations = 0
			cellStats[x][y].living = 0
			cellStats[x][y].dead = 0
			cellStats[x][y].stableAt = -1
	world.gen2stable = -1
	world.period = -1
	world.stable = -1
	world.living = []
	world.numLiving = 0
	world.changed = []
	world.numChanged = 0
	
	return render_template("sim.html")

# Get grid size for sim
@ socket.event
def get_grid_size():
	from Conway.main import ROWS,COLUMNS
	return f"[{ROWS},{COLUMNS}]"
	
# Receive client request for cell thoughts and return
@ socket.event
def get_status_at(list):
	x = list[0]
	y = list[1]
	#from Conway.Alex_ThoughtProcess import
	#call function with x, y values of cell
	# have it return string to return to client
	return "This is what cell {x}, {y} is thinking."

# Get rules from website
@app.route('/sim/', methods=['POST'])
def get_rules():
	from Conway.main import start_flag, Cell, cellStats, Rules, rules
	from Conway.main import Status, currentGeneration, ROWS, COLUMNS
	from Conway.Algorithms.alg import Cells_Environment, world, SetInitialCells
	from Conway.Algorithms.alg import UpdateFunction, update, initial_cells
	#from Conway.dennis_save.file_save_reduced import writeFile
	
	args = request.form
	max = 36
	rules.shape = args.get("shape", type=int, default=4)
	
	rules.pattern = args.get("pattern", type=int, default=1)
	if rules.shape == 0:
		rules.shape = 4
	rules.min2live = args.get("min2live", type=int, default=2)
	if rules.pattern == 0:
		rules.pattern = 1
	rules.max2live = args.get("max2live", type=int, default=3)
	rules.min2spawn = args.get("min2spawn", type=int, default=3)
	rules.max2spawn = args.get("max2spawn", type=int, default=3)
	
	startCells = args.get("layout", type=int, default=1)
	if startCells == 0:
		startCells = 1
	
	print(f"\n\nRules = {rules.shape}, {rules.pattern}, {rules.min2live},"
	      f"{rules.min2spawn}\n\n")
	
	# Triangle
	if rules.shape == 3:
		if rules.pattern == 1:
			max = 12
			
		if rules.pattern == 2:
			max = 36
			
		if rules.pattern == 3:
			max = 11
	
	# Square
	if rules.shape == 4:
		if rules.pattern == 1:
			max = 8
			
		if rules.pattern == 2:
			max = 24
			
		if rules.pattern == 3:
			max = 8
	
	# Pentagon
	if rules.shape == 5:
		if rules.pattern == 1:
			max = 7
			
		if rules.pattern == 2:
			max = 22
			
		if rules.pattern == 3:
			max = 15
	
	# Hexagon
	if rules.shape == 6:
		if rules.pattern == 1:
			max = 6
		
		if rules.pattern == 2:
			max = 18
			
		if rules.pattern == 3:
			max = 18
			
	if (rules.min2live < 1 or rules.min2live > max or
		rules.min2spawn < 1 or rules.max2spawn > max):
		
		feedback1 = f"Current shape must have between 1 and {max} neighbors."
		return render_template("sim.html",feedback=feedback1)
		
	if (rules.max2live < rules.min2live or
	    rules.max2spawn < rules.min2spawn):
		
		feedback2 = "Minimum values must be smaller than maximum values."
		return render_template("sim.html",feedback=feedback2)
		
	# Set start cells and display on website
	# Random
	if startCells == 1:
		UpdateFunction.generate_rand(update, currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
		
	# Cross
	elif startCells == 2:
		SetInitialCells.cross_period3(initial_cells, currentGeneration, ROWS, COLUMNS)
	
	# Octagon
	elif startCells == 3:
		SetInitialCells.octagon_period5(initial_cells, currentGeneration, ROWS, COLUMNS)
	
	# Kok's Galaxy
	elif startCells == 4:
		SetInitialCells.koks_galaxy_period8(initial_cells, currentGeneration, ROWS, COLUMNS)
	
	# Custom Layout from User
	elif startCells == 5:
		# get cells from website
		# Temporary while not set up
		UpdateFunction.generate_rand(update, currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
		
	# Get saved Game
	else:
		def returnFile(filename):
			file = filename
		
		#socket.emit('load_game', '', callback=returnFile)
		
		# Reset variables for loading saved game
		runProgram = 0
		algFlag = 0
		endFlag = -1
		for x in range(ROWS):
			for y in range(COLUMNS):
				cellStats[x][y].neighbors = 0
				cellStats[x][y].past = []
				cellStats[x][y].generations = 0
				cellStats[x][y].living = 0
				cellStats[x][y].dead = 0
				cellStats[x][y].stableAt = -1
				
				currentGeneration[x][y].status = 0
		world.gen2stable = -1
		world.period = -1
		world.stable = -1
		world.living = []
		world.numLiving = 0
		world.changed = []
		world.numChanged = 0
		
		#loadGame(file, rules, currentGeneration, cellStats)
		
	response = json.dumps(currentGeneration, cls=Status)
	socket.emit('renderGen', response)
	
	feedback3 = "Rules have been set."
	return render_template("sim.html",feedback=feedback3)



