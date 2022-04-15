''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' API                                                                     '''
''' *********************************************************************** '''
PASSWORD = 

from flask import Flask, request, jsonify, render_template, url_for,\
                  copy_current_request_context
from flask_socketio import SocketIO
import threading
from threading import Thread, Event
from math import floor
import json


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
	server.login("contact.game.of.life.2022@gmail.com", PASSWORD)
	server.sendmail(
		request.form.get("email"),
		"contact.game.of.life.2022@gmail.com",
		sendMessage)
	server.quit()
	feedback = "Thank you for contacting us."
	return render_template("home.html", feedback=feedback)

# Handle start button presses
@ socket.event
def get_start_state(start):
	print(f"\n{start}\n")
	# Start or Pause button pressed
	#if request.form.get("simForm") == "START":
	if start == "START":
		from Conway.main import start_flag, currentGeneration, newGen
		from Conway.main import ROWS, COLUMNS, thread_is_alive, game_loop
		from Conway.Algorithms.alg import UpdateFunction, update
		print("Start button was pressed")
		# Pause
		if start_flag == 1:
			start_flag = 2
		# Start/Restart
		else:
			start_flag = 1
			if thread_is_alive == 0:
				print("Starting game thread")
				thread_is_alive = 1
				
				# format newGen for sending to client
				listNewGen = []
				for i in range(ROWS):
					for j in range(COLUMNS):
						listNewGen.append(currentGeneration[i][j].status)
				print(f"\n\n{listNewGen}")
				response = json.dumps(listNewGen).encode('utf-8')
				print(f"\n{response}\n\n")
				socket.emit('renderGen', response)
				thread = socket.start_background_task(game_loop)
		return render_template("sim.html")

# Handle start button presses
@ socket.event
def get_stop_state(stop):
	# Stop button pressed
	#if request.form.get("simForm") == "STOP":
	if stop == "STOP":
		from Conway.main import start_flag
		print("Stop button was pressed")
		start_flag = 0
		return render_template("sim.html")
		
# Get rules from website
@app.route('/sim/', methods=['POST'])
def get_rules():
	from Conway.main import rules
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
		
	return render_template("sim.html")


'''# Update generation data for website rendering
@app.route('/sim/', methods=['GET'])
def renderGen():
	from Conway.main import newGen, ROWS, COLUMNS
	#self.send_response(200)
    #self.send_header("Content-type", "text/plain")
    #self.end_headers()
    #print(json.dumps(newGen, cls=Status))
	#self.wfile.write(bytes(json.dumps(newGen, cls=Status),"utf-8"))
	listNewGen = []
	for i in range(ROWS):
		for j in range(COLUMNS):
			listNewGen.append(newGen[i][j].status)
	            
	return Response(json.dumps(listNewGen), mimetype="/sim.html")'''
                
'''@app.route('/home/', methods=['POST'])
def update_rules():
	newRule = Rules()
	return jsonify(newRule)'''
	


# threading.Thread(target=lambda: app.run(port = 8080, debug = True, use_reloader = False)).start()
#socketio.run(app, port = 8080)
