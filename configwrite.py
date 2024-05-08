from configparser import ConfigParser

def loadconfig():
    config = ConfigParser()
    config.optionxform = str

    config["General"] = {
        "Start from Last Checkpoint?": "OFF",
        "Image Breaks between Rounds?": "ON",
        "Breaktime": 10

    }

    config["Invasions"] = {
        "Invasion Rounds?": "ON",
        "Invasion Rounds During Videos?": "ON",
        "Invasion Rounds During Break?": "ON",
        "Invasion Chance Percentage": 30
    }

    config["Modifiers"] = {
        "Modifiers?": "ON",
        "Speed Up Modifier": "ON",
        "Squeeze Shaft Modifier": "ON",
        "Hold Breath Modifier": "ON",
        "Modifier Chance Percentage": 10
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
        "Last Checkpoint": currentcheckpoint
    }

    with open("SaveData.txt", "w") as (my_save):
            save.write(my_save)
