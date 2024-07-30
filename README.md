# Fapland SP
## What is FapLand SP?
Fap Land Special Edition is a roguelike for playing FapHero rounds. 
Each fap hero round is like a space on a game board.
You must get to 100 to win.

## Installation
- Download the most recent release here: https://github.com/Nakkub/FapheroSP/releases (Will be under assets. Called Fapland.SP.Ver.0.X.zip)

- Place the 100 videos from Original Fapland in the "Fapland Videos" folder. Can be found here:

Part 1(1-65): https://mega.nz/#F!ckNSjADD!sh8KuJGzKGlYgKDv25kiFQ

Part 2(66-100): https://mega.nz/#F!EpNkjY7I!yNNrmuaoK_YlZq5weeuePA

- Place Invasion Videos in "invasion" folder. Any videos are allowed, but you can find invasions video packs here (Unpack the videos into the invasions folder):

Pack 1(Beats 3): https://gofile.io/d/lDki80

Pack 2(Beats 2, Marcurial 2, Pendulum, Secret Island Invasion): https://gofile.io/d/ZJU85E

- Add your favorite images to the intervals folder (GIFs and Videos are allowed if they are less than 2 seconds)
- Edit the "Game_Settings.txt" file to change settings to your liking
- Launch the game from "main_game.exe"

## Updating
- To update, simply copy the everything in the new Faphero SP Ver.0.X folder into the old one. Let everything replace the old files.
- The settings file is expanded every update, so you can't use the old one. If you delete it, playing the game will generate a new game settings file.

## Default Rules
- Start each turn by pressing roll and get a number from 1 to 6
- You will then move forward that many spaces and play the round asscociated the number on that space
- At random points during each round, short invasion rounds can interrupt play, stalling your gameplay
- Before each round and after invasions, there is a small chance for a modifier to added to the next round (Speed Up, Squeeze Shaft, etc)
- At the end of each round you will get a break and the turn starts again
- Checkpoint every 25 spaces
- Every played videos you will select a perk from 2 choices

### Some extra rules
- The chance for multiple invasions to occur during a round increases the farther up you go
- Some FH rounds have extra instructions included in the video itself (like holding your breath, using your other hand, etc). You do no have to obey those in video rules while playing Fap Land. Simply follow the beats. 
- Stopping at a check point doesn't reset your movement count. If you're on space 22 and roll a 6, you will stop at the checkpoint on 2, you will watch it, then continue on to space 28 and play that.

## Misc
- When you run the game for the first time, it will generate a Game_Settings and Savedata file where you can change features and modify certain features.
- If you want to reset the settings or save data, simply the delete the respective files and they will be generated again with the default settings.
- You may remove any of the videos in the intervals and invasions folders or add your own.
- You don't need to change the custom file locations in the settings file unless you change my folder structure or want to store the videos in a different place than the game.

## Changelog...
### Ver.0.4
- Changes
  - Added randomized rounds mode. 
    - The rolling, progression, invasion, modifiers and checkpoints work as normal. However, the video played at each round will be random and will not correspond to the round number
    - Videos will not repeat until all 96 have been played.
  - New Settings
    -  Modifier Chance Cap
    -  Invasion Chance Cap
    - Randomized Rounds
    - Randomized Invasion Chance
    - Randomized Modifier Chance
    - Chance of Curse per Invasion
- Fixes
  - Fixed crash when the minimum die size is larger than the maximum
  - Fixed bug where the rooms would decrease infinitely upon being cursed
  - Fixed bug where the checkpoint videos would play every time you moved negative spaces
  - Fixed bug where videos would play behind the game window instead of in front
### Ver.0.3
- Changes
  - Added Curse system. Every round has a chance to give a negative effect called a curse. The chance increases with every invasion.
    - "Go Back" Curse: Sends you back a few rounds. (Customizable)
    - "Decrease Die Max Size" Curse: Decrease the max size of the die you use for rolling, incrementally. (Customizable)
    - "Invasion Increase" Curse: Increase your invasion chance percentage. (Customizable)
    - "Modifier Increase" Curse: Increase your invasion chance percentage. (Customizable)
    - Curse Chance can increase during Invasions and Checkpoints. (Customizable)
  - New Settings
    -  Curse Toggles
    -  Curse Options
- Fixes
  - Fixed crash when perk list was depleted.
### Ver.0.2
- Changes
  - Added Point and Perk system. After getting enough points, you will get a choice of 2 perks to make gameplay easier. Each one stacks. Perks are lost on gameover regardless of your save settings.
    - "Skip Video" Perk: Lets you skip a 1 video instead of playing it. You can hoard multiple skips.
    - "Incease Die Size" Perk: Increase the size of the die you use for rolling, incrementally. (Customizable)
    - "Decrease Invasion Chance" Perk: Decrease your invasion chance percentage. (Customizable)
    - "Decrease Modifier Chance" Perk: Decrease your invasion chance percentage. (Customizable)
  - Invasion and Modifier Chance settings now shown on UI.
  - Invasion and Modifier Chance can increase at checkpoints
  - New Settings
    -  Perk Toggles
    -  Perk Options
    -  Multiple Invasions per Video
    -  Invasion Increase at Checkpoints
    -  Randomized Invasion and Modifier Chance
    
- Fixes
  - Loading and Saving fixed. Game will now save and load at checkpoints if you have the option set to ON.
  - When loading images, mpv will no longer load system files by mistake.
  - Will no longer crash if a folder isn't found.
  - Will no longer crash if value chance is set to zero.
  - Default settings rebalanced.

## Credits
### Fapland Videos
Sax, Ninza, Nananashi, Bastati, PsychoSplash, DannySir, N_N, OP is a f*ggot, Reverd, P, Raptor, Gu, Fryz3, Phantom Fapper, theblackndsage, SNanaya

### Invasion Videos(Fap Hero Beats 3)
PixelFH

### Original FapLand creator
Malu
