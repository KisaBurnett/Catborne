# CATBORNE
# A purrfectly ridiculous Bloodborne parody
# by Kisa Burnett for GAME-2341
# Game Scripting, Spring 2020

# Leads player through a sequence of scenes and prompts them to enter
# one of five commands. Different choices in different scenes lead to
# various outcomes.

# Offers a command list to player, and prompts them to try again if
# they enter an invalid command.

# Text is formatted for play in a window with a max line length of
# approximately 75 characters.


# Checks for a valid entry to start the game.
def gameStart(userInput):
	if str.upper(userInput) == "BEGIN":
		return True
	else:
		return False


# Prompts player to re-enter a command when invalid.
# Only used to start the game.
def tryAgainStart(userInput):
	while not gameStart(userInput):
		print("""
Invalid command. Please enter BEGIN and press return to start the game.
""")
		userInput = input("Enter your choice: ")
	return userInput


# Verifies the player's entry is valid.
def validEntry(userInput):
	if str.upper(userInput) == "TALK":
		return True
	elif str.upper(userInput) == "FIGHT":
		return True
	elif str.upper(userInput) == "STARE":
		return True
	elif str.upper(userInput) == "LOOK":
		return True
	elif str.upper(userInput) == "LEAVE":
		return True
	elif str.upper(userInput) == "CHECK":
		return True
	elif str.upper(userInput) == "HELP":
		return True
	elif str.upper(userInput) == "DREAM":
		return True
	else:
		return False


# Prompts player to re-enter a command when invalid.
# Used once the game has started.
def tryAgain(userInput):
	while not validEntry(userInput):
		print("""
Invalid command. Enter HELP for a list of valid commands.
""")
		userInput = input("Enter your choice: ")
	return userInput


# Display list of valid commands.
def commandList(dream):
	if dream:
		print("""Valid commands are:
TALK
FIGHT
STARE
LOOK
LEAVE
CHECK
DREAM""")
	else:
		print("""Valid commands are:
TALK
FIGHT
STARE
LOOK
LEAVE
CHECK""")


# Displays player's current milk level and weapon.
def statusCheck(milk, level, hasWpn, weapon):
	weaponList = {"1": "old sword", "2": "hammer", "3": "great sword"}
	print("""You are holding """ + str(milk) + """ bottles of milk.
You are level """ + str(level) + ".")
	if hasWpn:
		print("Your weapon is the " + weaponList.get(weapon) + ".")
	else:
		print("""You have no weapon. Idiot.""")


# Determines whether player should be prompted again for a command.
def sceneOneNext(userInput):
	goNext = {"TALK": True,
		"FIGHT": False,
		"STARE": True,
		"LOOK": False,
		"LEAVE": False,
		"HELP": False,
		"CHECK": False,
		"DREAM": False}

	proceed = goNext.get(str.upper(userInput))
	return proceed


# Displays appropriate story text according to player's input.
def sceneOne(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""'Where am I?' you ask the old cat.

He chuckles in a raspy, unsettling tone.

'All the Mousers ask the same thing when they wake,' he remarks. 'Not an
original one to be found in the lot o' ye. Yer in Yhowlnam, Mouser.'

He tosses a rusty and bloodied sword onto the floor by your bed. 'Best ye
learn to use this,' he sneers as he backs out of the room. 'And watch yer
back. The mousies are squeakin' loud this night.'

Once the old cat is gone, you slowly sit up and reach to pick up the sword.
It's then you realize your hand is a paw. A frantic inspection of yourself
reveals you're no longer human.

You've become... a cat.

At least you're a cat with a sword.""",
		"FIGHT":
"""You take a swipe at the old cat. He slaps you in the face hard with a
paw, and nearly knocks you out.

You don't stand a chance against him like this.""",
		"STARE":
"""You stare at the old cat in cold, inscrutable silence. He snorts at you
and shakes his head.

'Suit yerself,' he scoffs, starting out of the room. 'See if ye can make it
through the jaws of the mousies on yer own.'

Once the old cat is gone, you take hold of the bed's edge to pull yourself up.
It's then you realize your hand is a paw. A frantic inspection of yourself
reveals you're no longer a human.

You've become...

a cat.

A cat with no weapon and no memory of how you got here.

Great.""",
		"LOOK":
"""You lie on a dirty hospital bed, surrounded by old and questionable medical
equipment. A used blood transfusion kit is on a stand at your bedside. You
shudder to think what's been injected into you.

You see a door on the other side of the room, but the old cat stands between
it and you. It might as well be miles away.""",
		"LEAVE":
"""You try to stand up to leave, but your body is too weak. You collapse back
down on the bed.

The old cat snickers at you.""",
		"DREAM": "You have no dreams to dream."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Determines whether player should be prompted again for a command.
def sceneTwoNext(userInput):
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


# Displays appropriate story text according to player's input. Only executes
# if the player received a sword from the old cat in scene one.
def sceneTwoTalk(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You talk to yourself.

Since no one's here, no one can say you're crazy.""",
		"FIGHT":
"""You threaten your own shadow with your newfound weapon.

It isn't impressed.""",
		"STARE":
"""You stare at the ceiling menacingly. It says nothing.""",
		"LOOK":
"""This old, dark hospital room is disgusting. You're glad you were unconscious
for whatever was done to you earlier. You'll have nightmares of sepsis.

You see a door on the other side of the room. It looks like the only way out.""",
		"LEAVE":
"""You take a few practice swings with your new weapon. Despite your lack of
thumbs, you don't immediately throw it across the room. That's a good start.

Once you're confident in your ability to not stab yourself in the face, you
boldly head outside.""",
		"DREAM": "You have no dreams to dream."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Displays appropriate story text according to player's input. Only executes if
# the player did not receive a sword from the old cat in scene one.
def sceneTwoStare(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You talk to yourself.

Since no one's here, no one can say you're crazy.""",
		"FIGHT":
"""You threaten your own shadow with your bare paws.

It's probably laughing at you.""",
		"STARE":
"""You stare at the ceiling menacingly. It says nothing.""",
		"LOOK":
"""This old, dark hospital room is disgusting. You're glad you were unconscious
for whatever was done to you earlier. You'll have nightmares of sepsis.

You see a door on the other side of the room. It looks like the only way out.""",
		"LEAVE":
"""You spend a moment extending and sheathing your claws. They make you feel
powerful. You could tear up a thousand couches with no remorse.

You're not sure how they'll fare against the monster mouse you hear outside,
however.

Finally, you decide there's nothing for it but to set out for the world
outside.""",
		"DREAM": "You have no dreams to dream."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Determines whether player should be prompted again for a command.
def sceneThreeNext(userInput):
	goNext = {"TALK": False,
		"FIGHT": True,
		"STARE": False,
		"LOOK": False,
		"LEAVE": True,
		"HELP": False,
		"CHECK": False,
		"DREAM": False}
	proceed = goNext.get(str.upper(userInput))
	return proceed


# Displays appropriate story text according to player's input. Only executes
# if the player recieved a sword from the old cat in scene one.
def sceneThreeTalk(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You tell the rat that you are prepared to negotiate by either talking or
stabbing your sword into its eyeball until it yields. You'd rather talk, but
your sword would rather do some stabbing.

The rat replies with a horrible screech. Looks like talking is out.""",
		"FIGHT":
"""You lunge at the rat with a howling war cry you'll look back on in
embarrassment later. You thought it would make you sound fierce, but it came
out like your tail had just been caught beneath a rocking chair.

Luckily, your sword is less disappointing than you. The blade plunges through
the rat's flesh, cutting deep and sending a fountain of dark blood into the air.
The rat gurgles and flails, then collapses in a twitching heap on the floor. As
the life leaves its eyes, a small bottle of milk rolls out from under it. You
pick it up, and know instinctively it will benefit you later.

You watch the rat bleed to death, not about to turn your back on it until you know
it won't leap back up and attack you. Once the life drains completely from the
rat's eyes, you triumphantly leave the clinic. Now no one will ever hear about
that pathetic screeching sound you made a minute ago.""",
		"STARE":
"""You give the rat a menacing stare. It stares back, occasionally glancing at
your sword. Does it recognize the fact it's a weapon? Is that why it hasn't
pounced yet?""",
		"LOOK":
"""The rat stands between you and the door out of the clinic. The bones of some
poor soul lie on the ground by the rat, freshly stripped of meat. Could they
have belonged to the old cat? You never heard a scream or a fight back in the other
room, and you see no hat.

Whoever those bones belonged to, you'll avenge them with that new sword of yours.""",
		"LEAVE":
"""After careful consideration, you wonder if you can trick the horrible beast and
escape unscathed. You take a deep breath, then dart forward. The rat lunges with
a terrible screech, but with your quick and fancy cat feet, you're able to dodge
the snap of its wretched teeth. The rat crashes into a nearby cupboard, its head
smashing through the doors and becoming stuck.

With the beast occupied, you're able to dart out the door, safe and sound.
However, you can't help but wonder if risk would have brought worthy reward.""",
		"DREAM": "You have no dreams to dream."}
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
		milk = milk + 1
		return milk


# Displays appropriate story text according to player's input. Executes
# if player did not receive a sword from the old cat in scene one.
def sceneThreeStare(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You tell the rat that you are prepared to negotiate by either talking or
clawing its eyeballs until it yields. You'd rather talk, but you'll use your
paw talons if you have to!

The rat replies with a horrible screech. Looks like talking is out.""",
		"FIGHT":
"""You lunge at the rat, swinging your paws wildly with your claws unsheathed.
Grand visions of a heroic triumph flash through your mind as you flail around
in an attempt to scratch something important.

Those visions are promptly dashed when the rat snaps your throat with its razor
sharp teeth. Everything seems to move in slow motion as you fall to the ground,
and a single, final thought runs through your mind...

You probably shouldn't have given that old cat the silent treatment.""",
		"STARE":
"""You give the rat a menacing stare. It stares back, and takes an emboldened
step closer. It seems to know you're unarmed beyond your teeth and claws. You'll
need to act quickly!""",
		"LOOK":
"""The rat stands between you and the door out of the clinic. The bones of some
poor soul lie on the ground by the rat, freshly stripped of meat. Could they
have belonged to the old cat? You never heard a scream or a fight back in the other
room, and you see no hat.

Whoever those bones belonged to, you'll find a way to avenge them. Maybe you can
chew through the rat's throat or something...""",
		"LEAVE":
"""You try to run around the rat so you can avoid a fight. The rat lunges in front
of you with an ugly shriek, snapping at your throat. You won't be getting out of
here without some fancy claw-fu fighting.""",
		"DREAM": "You have no dreams to dream."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Determines whether player should be prompted again for a command.
def sceneFourNext(userInput):
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


# Displays appropriate story text according to player's input. Only executes if
# player survives the third scene.
def sceneFour(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You tell the moon you're very displeased with how the night is progressing
thus far.

It offers no solace.""",
		"FIGHT":
"""You try to pick a fight with a nearby broken lamp post. It ignores you,
even when you start to cry a little due to the crushing reality of your
current predicament.

It's probably too embarrassed on your behalf to resond, to be quite honest.""",
		"STARE":
"""You stare into the distance to see if you can figure out why cats do that all
the time. The only thing you get out of it is the realization your heightened
eyesight allows you to see exactly how doomed you are far more clearly.""",
		"LOOK":
"""Bloodstains and dried grass pepper the dirty cobblestone streets. You see
smoke from the smoldering remains of bonfires down a nearby alley, and upon
closer inspection, you realize they were used to burn grotesque corpses.

All of the doors and windows of the buildings around you are closed and shuttered.
Everything is darkened and hushed. If anyone's home, they're all hiding.""",
		"LEAVE":
"""After taking a deep breath, you pluck up your courage, tighten your grip on
your sword, and set out down the high street. Countless questions dance through
your mind, and the only way you'll find the answers is if you fight your way
through this terrible nightmare.

The hunt is on.""",
		"DREAM": "You have no dreams to dream."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Determines whether player should be prompted again for a command.
def sceneFiveNext(userInput):
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


# Displays appropriate story text according to player's input. Only executes
# if the player recieved a sword from the old cat in scene one.
def sceneFive(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You ask the plushie what she does here in this place. She lights up and purrs happily,
clearly tickled to be talking to you.

"I am here to take care of you, honerable Mouser," the plushie says. "You will
hunt beasts and mousies, collect milk from their corpses, and I will channel the
milk into your strength."

Yikes. You... didn't expect that to be quite so dark.

I'm sure it's cuter than she made it sound just now. Look how sweet she is!""",
		"FIGHT":
"""Something""",
		"STARE":
"""Something""",
		"LOOK":
"""Something""",
		"LEAVE":
"""Something"""}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Defines valid commands for the final prompt of the game.
def gameEnd(userInput):
	if str.upper(userInput) == "YES":
		return True
	elif str.upper(userInput) == "NO":
		return True
	else:
		return False


# Checks for a valid entry for the game end prompt.
def tryAgainEnd(userInput):
	while not gameEnd(userInput):
		print("")
		print("Invalid command. Please enter YES or NO and press return.")
		print("")
		userInput = input("Enter your choice: ")
	return userInput


# Exits the program regardless of which valid command
# the player enters. Because life is unfair, and so am I.
def goodbye(userInput):
	if str.upper(userInput) == "YES":
		print("\nTOO BAD, GOODBYE.\n\n")
	else:
		print("\nGOOD, JUST LEAVE.\n\n")


# Main Code

# Initializes variables that track which story progress
# choices the player makes throughout the game.
nextScene = False

hasDream = False

collectedMilk = 0
milkLevel = 1

hasWeapon = False
oldSword = False
hammer = False
greatSword = False
heldWeapon = ""

# textwrap is used to quickly format long blocks of text.
import textwrap

print("""----------CATBORNE----------

Choose your path carefully through the long night of the hunt.

Choices are made by typing TALK, FIGHT, STARE, LOOK, or LEAVE, and then pressing
the return key. Enter HELP at any time for a list of available commands.

Type BEGIN and press return to start the nightmare.
""")
entry = input("Enter your choice: ")
entry = tryAgainStart(entry)

print("""
------------------------------

'Welcome, Mouser.'

The croaky voice is the first thing to greet you as you slowly regain consciousness.
You open your eyes and find a grizzled old cat looming over you. He grins at you
from beneath his battered hat, and you see one of his fangs is missing, and his
eyes are bandaged with dirty cloth.

Where are you? Who is this cat? Why is he the same size as you?
""")

entry = input("Enter your choice: ")
entry = tryAgain(entry)

# Loops command prompts until player selects one that progresses the story.
while nextScene == False:
	nextScene = sceneOneNext(entry)
	# milk, level, hasWpn, weapon
	sceneOne(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
	if nextScene == False:
		print("")
		entry = input("Enter your choice: ")
		entry = tryAgain(entry)

# If player chose to talk to the old cat, arm player.
if str.upper(entry) == "TALK":
	hasWeapon = True
	oldSword = True
	heldWeapon = "1"
# Reset the nextScene check before proceeding.
nextScene = False

# Transition to clinic entrance.
print("""
With the old cat now gone, you are completely alone. You stand up slowly and
carefully, and discover you can still walk on two legs in your adorable cat body.
The distant, squeaky baying of some horrible rodent can be heard from outside.
You feel your journey has only just begun.

Which makes sense.

After all, you only just woke up.
""")
entry = input("Enter your choice: ")
entry = tryAgain(entry)

# Branches story according to whether or not the player is armed with the sword.
if hasWeapon:
	while nextScene == False:
		nextScene = sceneTwoNext(entry)
		sceneTwoTalk(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
else:
	while nextScene == False:
		nextScene = sceneTwoNext(entry)
		sceneTwoStare(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)

nextScene = False
print("""You go through the open door to the clinic lobby, and discover it's just
as horrible and dark as the room in which you awoke. Supplies and broken furniture
are strewn about, and there's a horrible smell that seems to follow you wherever
you go.

...oh, wait, that's you.

Let's hope there's a bath somewhere in Yhowlnam.

However, it quickly becomes apparent that hygiene is the least of your worries.
Across the lobby, between you and the clinic exit, is a gigantic, mange-ridden rat.

You freeze, but it's too late. The hideous thing lifts its head from the bones it
was gnawing, and looks directly at you. You'll need to think fast if you want to
survive a round with this beast!
""")
entry = input("Enter your choice: ")
entry = tryAgain(entry)

if hasWeapon:
	while nextScene == False:
		nextScene = sceneThreeNext(entry)
		collectedMilk = sceneThreeTalk(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
else:
	while nextScene == False:
		nextScene = sceneThreeNext(entry)
		sceneThreeStare(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)

# Ends the game according to whether or not the player was armed in scene three.
if hasWeapon:
	nextScene = False
	print("""You exit the clinic, and walk out onto a grim cobblestone street. The pale glow
from the moon overhead only makes the looming Victorian architecture around you
more oppressive. A cold wind cuts through your fur, and the far-off sounds of
beasts and dying victims chill you further. Your gruesome hunt in Yhowlnam has
only just begun.
""")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = sceneFourNext(entry)
		sceneFour(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)

	nextScene = False
	print("""After walking for a while, you come across a darkened lantern hanging from a
short staff in the middle of the cobblestone street. Curious, you reach out to light
it. The glow of the little flame soothes your nerves, and summons a small group of
spectral kittens at the base of the lantern's post. They greet you with spooky mews,
and you reach down to pet them. Just as your paw makes contact, the world around
you goes white, and then the white melts away to reveal a quiet, misty garden at
the base of a hill, atop which rests a worn down old chapel.

You stand up, puzzled for some reason. After all that's happened, you find THIS
weird? Really?

Old and weathered gravestones line the cobblestone path leading up to the chapel.
They're mostly unremarkable, aside from one, which has a small group of ghostly
kittens like the ones you saw by the lantern. A cat in a pretty dress and bonnet
kneels next to this gravestone, but she stands up on her hind legs when she notices
you, and clasps her front paws together as she turns to face you.

When you get a good look at the other cat's face, you realize she's actually a plush
toy, but an incredibly life-like one. She smiles gently at you, and speaks in a soft,
kindly tone.

"Hello, good Mouser. I am a plushie, here in this Catnap Dream to look after you."
""")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = sceneFiveNext(entry)
		print("")
		if nextScene == False:
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
else:
	nextScene = False
	print("""----------YOU DIED----------
""")

# Prompts player for last time before exiting.
print(textwrap.fill("Play again?", 75))
print("")
entry = input("Enter YES or NO: ")
entry = tryAgainEnd(entry)
goodbye(entry)
