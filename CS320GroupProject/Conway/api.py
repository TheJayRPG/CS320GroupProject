'' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' API                                                                     '''
''' *********************************************************************** '''

from flask import Flask, request, jsonify, render_template, url_for
import threading

from Conway.main import *

app = Flask(__name__, static_url_path='', template_folder="eric--web/templates", static_folder='eric--web/static')
'''static_url_path='/Users/kristinehess/Desktop/CS_320/Project_code/Github_Code/eric--web')'''
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False
app.use_reloader = False

'''web_rules = [
	{ 'shape_w' : 3,
	  'pattern_w' : 2,
	  'min2live_w' : 4,
	  'max2live_w' : 7,
	  'min2spawn_w' : 6,
	  'max2spawn_w' :8 }
]'''

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

# Get rules from user and populate python object
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
	
	print(f"rules = {rules.shape}, {rules.pattern}, {rules.min2live}, {rules.min2spawn}")
	
	'''# Set Conway's default values if left blank
	if rules.shape == "0":
		rules.shape = 4
	if rules.pattern == "0":
		rules.pattern = 1
	if rules.min2live == "":
		rules.min2live = 2
	if rules.max2live == "":
		rules.max2live = 3
	if rules.min2spawn == "":
		rules.min2spawn = 3
	if rules.max2spawn == "":
		rules.max2spawn = 3'''
	
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
		
	if (rules.max2live < rules.min2live or rules.max2spawn < rules.min2spawn):
		
		feedback2 = "Minimum values must be smaller than maximum values."
		return render_template("sim.html",feedback=feedback2)
		
	return render_template("sim.html")

'''# Update generation data for website rendering
@app.route('/sim/', methods=['POST'])
def updateGen(newGen):
	#self.send_response(200)
    #self.send_header("Content-type", "text/plain")
    #self.end_headers()
	self.wfile.write(bytes(json.dumps(newGen, cls=Status),"utf-8"))
		
	return render_template("sim.html", self.wfile)'''
                
'''@app.route('/home/', methods=['POST'])
def update_rules():
	newRule = Rules()
	return jsonify(newRule)'''
	


threading.Thread(target=lambda: app.run(port = 8080, debug = True, use_reloader = False)).start()
