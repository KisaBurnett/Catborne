#######################--NOM--##########################


# Enters Pyrrgenwerth.
def pyrrgenwerthOpen(waitTime):
	print("""Something""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def pyrrgenwerthNext(userInput):
	goNext = {"TALK": False,
		"FIGHT": False,
		"STARE": False,
		"LOOK": False,
		"LEAVE": True,
		"HELP": False,
		"CHECK": False,
		"DREAM": False}
	proceed = goNext.get(str.upper(userInput))
	return proceed


# Displays appropriate story text according to player's input.
def pyrrgenwerthOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""Talk something""",
		"FIGHT":
"""Fight something""",
		"STARE":
"""Stare something""",
		"LOOK":
"""Look at something""",
		"LEAVE":
"""Leave with something"""}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))
	if str.upper(userInput) == "FIGHT":
		milk = milk + 4
	return milk


# Transitions to the Nom the Gluttonous Flea boss arena.
def nomOpen(waitTime):
	print("""Here is the opening text for Nom the Gluttonous Flea.
""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def nomNext(userInput):
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
def nomOptions(userInput, dream, milk, level, hasWpn, weapon):
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
def nomFight(milk, level, won, waitTime):
	print("""
------------------------------
""")
	if level >= 8:
		print("""Here is the winning text.
""")
		milk = milk + 16
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won

  # Resets the check to see if the boss is dead for the next area.
  bossDead = False

  # Loops area until Nom the Gluttonous Flea has been beaten by the player.
  while bossDead == False:
  	nextScene = False
  	pyrrgenwerthOpen(entryTime)
  	print("")
  	entry = input("Enter your choice: ")
  	entry = tryAgain(entry)

  	while nextScene == False:
  		nextScene = pyrrgenwerthNext(entry)
  		if str.upper(entry) == "DREAM":
  			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
  			print("")
  			pyrrgenwerthOpen(entryTime)
  			print("")
  			entry = input("Enter your choice: ")
  			entry = tryAgain(entry)
  		else:
  			collectedMilk = pyrrgenwerthOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
  			print("")
  			if nextScene == False:
  				time.sleep(entryTime)
  				entry = input("Enter your choice: ")
  				entry = tryAgain(entry)
  			else:
  				time.sleep(cinematicTime)

  	nextScene = False
  	nomOpen(entryTime)
  	entry = input("Enter your choice: ")
  	entry = tryAgain(entry)

  	while nextScene == False:
  		nextScene = nomNext(entry)
  		if str.upper(entry) == "FIGHT":
  			collectedMilk, bossDead = nomFight(collectedMilk, milkLevel, bossDead, cinematicTime)
  		else:
  			collectedMilk = nomOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
  			print("")
  			if nextScene == False:
  				time.sleep(entryTime)
  				entry = input("Enter your choice: ")
  				entry = tryAgain(entry)
  			else:
  				time.sleep(cinematicTime)
