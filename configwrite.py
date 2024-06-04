from configparser import ConfigParser

def loadconfig():
    config = ConfigParser()
    config.optionxform = str

    config["General"] = {
        "Start from Last Checkpoint?": "OFF",
        "Image Breaks between Rounds?": "ON",
        "Breaktime": 10,

    }

    config["Invasions"] = {
        "Invasion Rounds?": "ON",
        "Randomize Invasion Chance?": "OFF",
        "Invasion Chance Percentage": 25,
        "Invasion Rounds During Videos?": "ON",
        "Invasion Rounds During Break?": "ON",
        "Multiple Invasions During Videos": "ON",
        "Invasion Chance Increase on Checkpoint": 15

    }

    config["Modifiers"] = {
        "Modifiers?": "ON",
        "Randomize Modifier Chance?": "OFF",
        "Modifier Chance Percentage": 25,
        "Speed Up Modifier": "ON",
        "Squeeze Shaft Modifier": "ON",
        "Hold Breath Modifier": "ON",
        "Modifier Chance Increase on Checkpoint": 10,
    }

    config["Perks"] = {
        "Perks?": "ON",
        "Points per Perk": 3,
        '"Die Size Increase" Perk': "ON",
        "Increase Die Size by?": 2,
        '"Video Skip" Perk': "ON",
        #'"Pause Video" Perk': "ON",
        #"Allowed Pause Time": 10,
        '"Invasion Decrease" Perk': "ON",
        "Decrease Invasion Chance by what %?": 10, 
        '"Modifier Decrease" Perk': "ON",
        "Decrease Modifier Chance by what %?": 10
  
    }

    config["Custom_File_Locations"] = {
        "MPV": r'C:/Games/Fap Land/Main Game/',
        "Fapland_Videos": r'C:/Games/Fap Land/Main Game/FapLand Videos/',
        "Modifiers": r'C:/Games/Fap Land/Main Game/modifiers',
        "Invastions": r'C:/Games/Fap Land/Main Game/invasion/',
        "Intervals": r'C:/Games/Fap Land/Main Game/intervals/'
    }

    with open("Game_Settings.txt", "w") as (my_settings):
            config.write(my_settings)

def savedata(currentcheckpoint):
    save = ConfigParser()
    save.optionxform = str

    save['Save'] = {
        "Last Checkpoint": currentcheckpoint,
    }

    with open("SaveData.txt", "w") as (my_save):
            save.write(my_save)
