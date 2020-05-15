# Transitions to the Purrgo's Wet Nurse boss arena.
def moonOpen(waitTime):
	print("""Here is the opening text for Moon Presence.
""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def moonNext(userInput):
	goNext = {"TALK": False,
		"FIGHT": True,
		"STARE": False,
		"LOOK": False,
		"LEAVE": False,
		"HELP": False,
		"CHECK": False,
		"DREAM": False}
	proceed = goNext.get(str.upper(userInput))
	return proceed


# Displays appropriate story text according to player's input.
def moonOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""Talk to something""",
		"STARE":
"""Stare at something""",
		"LOOK":
"""Look, more something""",
		"LEAVE":
"""Leave with something""",
		"DREAM": "The plushie can't save you here, coward."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Boss fight scene.
def moonFight(milk, level, won, waitTime):
	print("""
------------------------------
""")
	if level >= 12:
		print("""Here is the winning text.
""")
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


nextScene = False
moonOpen(entryTime)
entry = input("Enter your choice: ")
entry = tryAgain(entry)

while nextScene == False:
  nextScene = moonNext(entry)
  if str.upper(entry) == "FIGHT":
    collectedMilk, bossDead = moonFight(collectedMilk, milkLevel, bossDead, cinematicTime)
  else:
    collectedMilk = moonOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
    print("")
    if nextScene == False:
      time.sleep(entryTime)
      entry = input("Enter your choice: ")
      entry = tryAgain(entry)
    else:
      time.sleep(cinematicTime)
