#######################--AMELIA--##########################


# Enters the Church area.
def churchOpen(waitTime):
	print("""Something""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def churchNext(userInput):
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
def churchOptions(userInput, dream, milk, level, hasWpn, weapon):
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
		milk = milk + 2
	return milk


# Transitions to the Amelia boss arena.
def ameliaOpen(waitTime):
	print("""Here is the opening text for Amelia.
""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def ameliaNext(userInput):
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
def ameliaOptions(userInput, dream, milk, level, hasWpn, weapon):
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
def ameliaFight(milk, level, won, waitTime):
	print("""
------------------------------
""")
	if level >= 10:
		print("""Here is the winning text.
""")
		milk = milk + 20
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won
