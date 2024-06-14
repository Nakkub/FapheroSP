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
        "Invasion Rounds During Break?": "OFF",
        "Multiple Invasions During Videos": "ON",
        "Invasion Chance Increase on Checkpoint": 10

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
        "Points per Perk": 2,
        '"Die Size Increase" Perk': "ON",
        "Increase Die Size by?": 2,
        '"Video Skip" Perk': "ON",
        '"No Invasions Next Round" Perk': "ON",
        '"Invasion Decrease" Perk': "ON",
        "Decrease Invasion Chance by what %?": 10, 
        '"Modifier Decrease" Perk': "ON",
        "Decrease Modifier Chance by what %?": 10
  
    }
    
    config["Curses"] = {
        "Curses?": "ON",
        "Base Curse Chance Percentage on Invasion": 20,
        "Chance of Curse Increase per Invasion": 3,
        "Chance of Curse Increase per Checkpoints": 7,
        '"Decrease Die Max Size" Curse': "ON",
        "Decrease Die Max by?": 2,
        '"Decrease Die Min Size" Curse': "ON",
        "Decrease Die Min by?": 2,
        '"Invasion Increase" Curse': "ON",
        "Increase Invasion Chance by what %?": 10, 
        '"Modifier Increase" Curse': "ON",
        "Increase Modifier Chance by what %?": 10,
        '"Go Back" Curse': "ON",
        "Max Rounds to go back?": 5,

    }

    config["Custom_File_Locations"] = {
        "MPV": r'C:/Games/Fap Land/Main Game/',
        "Fapland_Videos": r'C:/Games/Fap Land/Main Game/FapLand Videos/',
        "Modifiers": r'C:/Games/Fap Land/Main Game/modifiers',
        "Invastions": r'C:/Games/Fap Land/Main Game/invasion/',
        "Intervals": r'C:/Games/Fap Land/Main Game/intervals/'
    }

    with open("Game_Settings.txt", "w") as (my_settings):
            config.write(my_settings, space_around_delimiters=False)

def savedata(currentcheckpoint):
    save = ConfigParser()
    save.optionxform = str

    save['Save'] = {
        "Last Checkpoint": currentcheckpoint,
    }

    with open("SaveData.txt", "w") as (my_save):
            save.write(my_save, space_around_delimiters=False)
