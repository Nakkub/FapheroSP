import os, random, time, datetime
from os import path
from os import listdir
from configparser import ConfigParser
import configwrite

#Checks for all your files.
time.sleep(0.75)
print("Welcome to Fap Land")
print("Checking Files...")
print("")
time.sleep(0.5)

#Configures Settings File
if path.exists("Game_Settings.txt"):
	print ("Config File Loaded!")
else:
	print("Config File was not found. Generating New Config...")
	configwrite.loadconfig()
	time.sleep(0.5)
	print("")

fap_config = ConfigParser()
fap_config.read("Game_Settings.txt")
file_config = fap_config['Custom_File_Locations']
inv_config = fap_config['Invasions']
mod_config = fap_config['Modifiers']
gen_config = fap_config['General']
time.sleep(0.5)

#Configures Save Data
if gen_config["Start from Last Checkpoint?"] == "ON":
	if path.exists("SaveData.txt"):
		print ("Save File Loaded!")
	else:
		print("No Save Data was not found. Generating Save File...")
		configwrite.savedata(1)
		time.sleep(0.5)
		print("")
	save_config = ConfigParser()
	save_config.read("SaveData.txt")
	savedata = save_config['Save']['Last Checkpoint']

#Sets any custom paths for the files
mpv_path = file_config['mpv']
fl_path = file_config["Fapland_Videos"]
inv_path = file_config["Invastions"]
mod_path = file_config["Modifiers"]
int_path = file_config["Intervals"]

#Checks for all necessary files
if path.exists("mpv.exe"):
	mpv_path = ""
	print("MPV Loaded!")
elif path.exists(mpv_path):
	print("MPV Loaded!")
else:
	print("")
	print("MPV.exe was not found.")
	print("")
time.sleep(0.5)

if path.exists("Fapland Videos/2.mp4"):
	fl_path = "Fapland Videos/"
	print("FapLand Videos Loaded!")
elif path.exists(fl_path):
	print("FapLand Videos Loaded")
else:
	print("")
	print("-Fapland Videos were not found.-")
	print("")
time.sleep(0.5)

if path.exists("invasions") and inv_config["Invasion Rounds?"] == "ON":
	inv_path = "invasions/"
	invexist = True
elif path.exists(inv_path) and inv_config["Invasion Rounds?"] == "ON":
	invexist = True
if invexist:
	print("Invasions Folder found!")
	if listdir(inv_path):
		print("Invasion Videos Loaded!")
		invexist = True
	else:
		print("")
		print("-No Invasion Videos were found.-")
		print("")
		invexist = False
else:
	print("")
	print("-Invasions Folder was not found.-")
	print("")
	invexist = False
time.sleep(0.5)

if path.exists("modifiers") and mod_config["Modifiers?"] == "ON":
	mod_path = "modifiers/"
	print ("Modifiers Folder Found!")
	modexist = True
elif path.exists(mod_path):
	print("Modifiers Folder Loaded!")
	modexist = True
else:
	print("")
	print("-Modifiers Folder was not found.-")
	print("")
	modexist = False
time.sleep(0.5)

if path.exists("intervals") and gen_config["Image Breaks between Rounds?"] == "ON":
	int_path = "intervals/"
	intexist = True
elif path.exists(int_path) and gen_config["Image Breaks between Rounds?"] == "ON":
	intexist = True
if intexist:
	print("Interval Images Folder Found!")
	if listdir(int_path):
		print("Interval Images Loaded!")
		intexist = True
	else:
		print("")
		print("-No interval images were found.-")
		print("")
		intexist = False
else:
	print("")
	print("-Invasions Folder was not found.-")
	print("")
	intexist = False
time.sleep(0.5)

time.sleep(0.5)
print("")

#Plays requested videos and processes invasions/modifiers
def video(currentval):
	file = str(currentval)
	if currentval == 1 and not path.exists("1.mp4"):
		file = "1 - Start"
	elif currentval % 25 == 0 and not path.exists("25.mp4"):
		if currentval != 100:
			file = str(currentval) + " - Checkpoint"
		else:
			file = str(currentval) + " - End"
	savepoint = 0
	lastinv = 0
	if int(inv_config["Invasion Chance Percentage"]) != 0:
		power = random.randint (1, (100 // int(inv_config["Invasion Chance Percentage"]))*10)
	else:
		power = False
	if int(mod_config["Modifier Chance Percentage"]) != 0:
		moddy = random.randint (1, (100 // int(mod_config["Modifier Chance Percentage"])))
	else: 
		moddy = 100
	while power < 10 and savepoint + 5 <= 80 and currentval % 25 != 0 and currentval != 1 and inv_config["Invasion Rounds?"] == "ON" and inv_config["Invasion Rounds During Videos?"] == "ON" and invexist:
		surprise = random.randint(savepoint + 5, 80)
		os.system(mpv_path + "mpv.exe " + '"' + fl_path + file + '.mp4"' + " -msg-level=all=no -fs -start=" + str(savepoint) + "%" + " -end=" + str(surprise) + "%")
		savepoint = surprise
		inv_unpicked = True
		while inv_unpicked:
			invader = random.choice(listdir(inv_path))
			if invader != lastinv:
				print("Invasion!")
				print("")
				os.system(mpv_path + "mpv.exe " + '"' + inv_path + invader + '"' + " -msg-level=all=no -fs")
				inv_unpicked = False
		power += 6 - (currentval // 25)
		print("Resuming...")
		print("")
		lastinv = invader
	if moddy == 1 and currentval % 25 != 0 and currentval != 1 and mod_config["Modifiers?"] == "ON" and modexist:
		unpicked = True
		while unpicked:
			modifier = random.randint(1, 3)
			if modifier == 1 and mod_config["Speed Up Modifier"] == "ON":
				unpicked = False
				print("Modifier: Speed Up")
				print("")
				os.system(mpv_path + "mpv.exe " + '"' + mod_path + "Speed Up" + '.mp4"' + " -msg-level=all=no -fs")
				os.system(mpv_path + "mpv.exe " + '"' + fl_path + file + '.mp4"' + " -msg-level=all=no -fs -start=" + str(savepoint) + "%" +" -speed=1.20"
				+ ' -sub-file="modifiers/Speed_Up.srt" -sub-scale=0.7 -sub-pos=0 -sub-color=1.0/1.0/1.0/0.55 -sub-border-size=0 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.2')
			elif modifier == 2 and mod_config["Squeeze Shaft Modifier"] == "ON":
				unpicked = False
				print("Modifier: Squeeze Shaft")
				print("")
				os.system(mpv_path + "mpv.exe " + '"' + mod_path + "SQUEEZE SHAFT" + '.mp4"' + " -msg-level=all=no -fs")
				os.system(mpv_path + "mpv.exe " + '"' + fl_path + file + '.mp4"' + " -msg-level=all=no -fs -start=" + str(savepoint) + "%"
			  	+ ' -sub-file="modifiers/SQUEEZE_SHAFT.srt" -sub-scale=0.7 -sub-pos=1 -sub-color=1.0/0.2/0.2/0.55 -sub-border-size=0 -sub-bold=yes -sub-font="Impact" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.3')
			elif modifier == 3 and mod_config["Hold Breath Modifier"] == "ON":
				unpicked = False
				print("Modifier: Hold Breath")
				print("")
				os.system(mpv_path + "mpv.exe " + '"' + mod_path + "Hold Breath" + '.mp4"' + " -msg-level=all=no -fs")
				os.system(mpv_path + "mpv.exe " + '"' + fl_path + file + '.mp4"' + " -msg-level=all=no -fs -start=" + str(savepoint) + "%"
			  	+ ' -sub-file="modifiers/Hold_Breath.srt" -sub-scale=1.0 -sub-pos=1 -sub-color=1.0/1.0/1.0/0.55 -sub-border-size=2 -sub-border-color=0.0/0.0/0.0/0.55 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.3')
			elif mod_config["Hold Breath Modifier"] == "OFF" and mod_config["Speed Up Modifier"] == "OFF" and mod_config["Squeeze Shaft Modifier"] == "OFF":
				print("No Modifiers Active...")
				print("")
				unpicked = False

	else:
		os.system(mpv_path + "mpv.exe " + '"' + fl_path + file + '.mp4"' + " -msg-level=all=no -fs -start=" + str(savepoint) + "%")

def image():
	if intexist and gen_config["Image Breaks between Rounds?"] == "ON":
		imageFile = os.listdir(int_path)
		random_file = random.choice(imageFile)
		fullImagePath = int_path + random_file
		breaktime = int(gen_config["Breaktime"])
		power = random.randint(1, (100 // (int(inv_config["Invasion Chance Percentage"])/2))*10)
		name, ext = os.path.splitext(random_file)
		if inv_config["Invasion Rounds During Break?"] == "ON" and power < 10 and invexist:
			invader = random.choice(listdir(inv_path))
			divsec = random.randint(1, breaktime)
			if ext == ".gif" or ext == ".mp4" or ext == ".webm":
				os.system(mpv_path + "mpv.exe " + '"' + fullImagePath + '"' + " -msg-level=all=no -fs -loop-file=" + str(divsec)
			  	+ ' -sub-file="modifiers/interval.srt" -sub-scale=0.7 -sub-pos=0 -sub-color=1.0/1.0/1.0/0.8 -sub-border-size=0 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.2')
			else: 
				os.system(mpv_path + "mpv.exe - -fs --image-display-duration=" + str(divsec) + ' "' + fullImagePath + '"' 
				+ ' -sub-file="modifiers/interval.srt" -sub-scale=0.7 -sub-pos=0 -sub-color=1.0/1.0/1.0/0.8 -sub-border-size=0 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.2')
			os.system(mpv_path + "mpv.exe " + '"' + inv_path + invader + '"' + " -msg-level=all=no -fs")
			breaktime = breaktime - divsec
		if ext == ".gif" or ext == ".mp4" or ext == ".webm":
			os.system(mpv_path + "mpv.exe " + '"' + fullImagePath + '"' + " -msg-level=all=no -fs -loop-file=" + str(breaktime)
			+ ' -sub-file="modifiers/interval.srt" -sub-scale=0.7 -sub-pos=0 -sub-color=1.0/1.0/1.0/0.8 -sub-border-size=0 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.2')
		else:
			os.system(mpv_path + "mpv.exe - -fs --image-display-duration=" + str(breaktime) + ' "' + fullImagePath + '"'
			+ ' -sub-file="modifiers/interval.srt" -sub-scale=0.7 -sub-pos=0 -sub-color=1.0/1.0/1.0/0.8 -sub-border-size=0 -sub-bold=yes -sub-font="Tahoma" -sub-shadow-offset=-3 -sub-shadow-color=0.0/0.0/0.0/0.2')

#Gets general settings in class
class generalsettings():
	def __init__(self):
		self.breaktime = gen_config["Breaktime"]
		self.checkp = gen_config["Start from Last Checkpoint?"]

def general():
	return generalsettings()

#Gets save file data for main
def loadsave():
	if gen_config["Start from Last Checkpoint?"] == "ON":
		return int(savedata)
	else:
		return 1

def saveit(checkpoint):
	if gen_config["Start from Last Checkpoint?"] == "ON":
		configwrite.savedata(checkpoint)

def deletesave():
	if path.exists("Savedata.txt"):
		os.remove("SaveData.txt")
random.seed(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))