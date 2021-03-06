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

# Apologies for all of this being in one file. repl has been giving me issues
# with importing into main.


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


# Levels up player if they have collected milk.
def dream(milk, level, waitTime):
	nextLevel = level * 2
	print("""
------------------------------
""")
	if milk < nextLevel:
		print("""You strut into the Catnap Dream, not caring that you're about to waste
everyone's time. The plushie looks at the empty milk bottles you present her, and
then looks at you.

"Is this what they call a 'prank', good Mouser?" she asks dubiously. "I cannot
enhance your strength without sufficient milk. Your collected milk must equal twice
your current strength for me to embolden you. Please, go and slay the beast mousies,
and return with their succulent milk so I may assist you."

You return to the waking world with the sneaking suspicion the plushie will talk
smack about you with the spectral kittens once you leave.

Let's be real with each other. You deserve it.""")
	else:
		print("""You enter the Catnap Dream with the flourish of a conquering hero, and the
plushie claps for you in approval.

"Well done, Mouser," she praises. She takes your paw and purrs. "Now close your
eyes, and let the milk become your strength."

A surge of power smacks into you and nearly knocks you out. You manage not to lose
consciousness, and feel stronger, if not rather dizzy. The plushie releases your
paw and gives you a friendly wave as you stumble back to the Yhowlnam gravestone
and return to the waking world.""")
		while milk >= nextLevel:
			level = level + 1
			milk = milk - nextLevel
			nextLevel = level * 2
	time.sleep(waitTime)
	return milk, level


# Opening page for the game.
def titlePage(waitTime):
	print("""----------CATBORNE----------

A purrfectly ridiculous Bloodborne parody by Kisa Burnett.

Choose your path carefully through the long night of the hunt.

Choices are made by typing TALK, FIGHT, STARE, LOOK, or LEAVE, and then pressing
the return key. Enter HELP at any time for a list of available commands.

More commands will become available as you progress through your hunt.

Type BEGIN and press return to start the nightmare.
""")
	time.sleep(waitTime)


def opener(waitTime):
	print("""
------------------------------

"Welcome, Mouser."
""")
	time.sleep(1)
	print("""The croaky voice is the first thing to greet you as you slowly regain consciousness.
You open your eyes and find a grizzled old cat looming over you. He grins at you
from beneath his battered hat, and you see one of his fangs is missing, and his
eyes are bandaged with dirty cloth.

Where are you? Who is this cat? Why is he the same size as you?
""")
	time.sleep(waitTime)


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
""" "Where am I? you ask the old cat.

He chuckles in a raspy, unsettling tone.

"All the Mousers ask the same thing when they wake," he remarks. "Not an
original one to be found in the lot o' ye. Yer in Yhowlnam, Mouser."

He tosses a rusty and bloodied sword onto the floor by your bed. "Best ye
learn to use this," he sneers as he backs out of the room. "And watch yer
back. The mousies are squeakin' loud this night."

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

"Suit yerself," he scoffs, starting out of the room. "See if ye can make it
through the jaws of the mousies on yer own."

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


# Transitions between scene with old cat and player being alone.
def afterOldCat(waitTime):
	print("""With the old cat now gone, you are completely alone. You stand up slowly and
carefully, and discover you can still walk on two legs in your adorable cat body.
The distant, squeaky baying of some horrible rodent can be heard from outside.
You feel your journey has only just begun.

Which makes sense.

After all, you only just woke up.
""")
	time.sleep(waitTime)


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


####################--CLINIC LOBBY--###########################


# Transitions to clinic entrance first time.
def clinicEntrance(waitTime):
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
	time.sleep(waitTime)


# Executes when player is returned to the clinic after dying in the first fight.
def clinicReturn(longTime, shortTime):
	time.sleep(longTime)
	print("""
You are magically returned to the clinic lobby, ready to regain your feline dignity
and teach that horrible rat a lesson. Supplies and broken furniture are strewn
about, and there's a horrible smell that seems to follow you wherever you go.

...oh, wait, that's STILL you.

Lord, that really is horrible.

However, it quickly becomes apparent that hygiene remains the least of your worries.
Across the lobby, between you and the clinic exit, is your arch-nemesis, the rat.

Look how smug it is.

You freeze, but it's too late. The hideous thing lifts its head from the bones it
was gnawing, and looks directly at you. You'll need to think fast if you want to
survive a round with this beast!
""")
	time.sleep(shortTime)


# Determines whether player should be prompted again for a command.
def sceneThreeTalkNext(userInput):
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
the life leaves its eyes, two small bottles of milk rolls out from under it. You
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
		"DREAM": "You cannot dream in battle."}
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


# Determines whether player should be prompted again for a command.
def sceneThreeStareNext(userInput):
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


######################--EXIT CLINIC--###########################


# Transitions to next gameplay branch.
def sceneFourOpen(waitTime):
	print("""You exit the clinic, and walk out onto a grim cobblestone street. The pale glow
from the moon overhead only makes the looming Victorian architecture around you
more oppressive. A cold wind cuts through your fur, and the far-off sounds of
beasts and dying victims chill you further. Your gruesome hunt in Yhowlnam has
only just begun.
""")
	time.sleep(waitTime)


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


# Displays appropriate story text according to player's input.
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


###################--FIRST DREAM VISIT--########################


def dreamTransition(waitTime):
	print("""After walking for a while, you come across a darkened lantern hanging from a
short staff in the middle of the cobblestone street. Curious, you reach out to
light it. The glow of the little flame soothes your nerves, and summons a small
group of spectral kittens at the base of the lantern's post. They greet you with
spooky mews, and you reach down to pet them. Just as your paw makes contact...
""")
	time.sleep(waitTime)


# Transitions to next gameplay branch.
def sceneFiveOpen(waitTime):
	print("""The world around you goes white, and then the white melts away to reveal a quiet,
misty garden at the base of a hill, atop which rests a worn down old chapel.

You stand up, puzzled for some reason. After all that's happened, you find THIS
weird? Really?

Old and weathered gravestones line the cobblestone path leading up to the chapel.
They're mostly unremarkable, aside from one, which has a small group of ghostly
kittens huddled around it, mewing contentedly. A cat in a pretty dress and bonnet
kneels next to this gravestone, but she stands up on her hind legs when she notices
you, and clasps her front paws together as she turns to face you.

When you get a good look at the other cat's face, you realize she's actually a plush
toy, but an incredibly life-like one. She smiles gently at you, and speaks in a soft,
kindly tone.

"Hello, good Mouser. I am a plushie, here in this Catnap Dream to look after you."
""")
	time.sleep(waitTime)


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


# Displays appropriate story text according to player's input.
def sceneFive(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You ask the plushie what she does here in this place. She lights up and purrs
happily, clearly tickled to be talking to you.

"I am here to take care of you, honerable Mouser," the plushie says. "You will
hunt beasts and mousies, collect milk from their corpses, and I will channel the
milk into your strength."

Yikes. You... didn't expect that to be quite so dark.

I'm sure it's cuter than she made it sound just now. Look how sweet she is!""",
		"FIGHT":
"""You heroically fight the air in front of the plushie. She tilts her head and claps
for you in an encouraging manner. Your heart swells with pride, because nothing
is better than sweet, sweet validation.""",
		"STARE":
"""You stare at the plushie. She stares back at you.

Truly, yours is a love for the ages.""",
		"LOOK":
"""The garden around you is quiet and peaceful, if not a little strange. The chapel
up the hill is small, and littered with old books and broken weapons, along with
some bizarre tools you've never seen before.

Most of the gravestones have had their inscriptions rubbed away by time and are
now unreadable, but the one with the ghost kitten congregation reads, 'YHOWLNAM'.

The plushie cleans her face daintily with her paws while you explore your surroundings,
content. She seems to be happy to be near you.""",
		"LEAVE":
"""You return to the headstone labeled YHOWLNAM and start to stoop down next to it,
but the plushie stops you by placing a paw on your shoulder.

"Good Mouser," she says, "before you go..."

You stand back up to look at her curiously, and she gives a polite bow.""",
		"DREAM": "You are already dreaming and you can't go deeper."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))


# Displayed if player has collected milk.
def dreamLeaveLevel(waitTime):
	print(""""You have collected milk which can be used to increase your strength," the plushie
says. "I will channel them, and your power will grow."

The idea of becoming a walking tank excites you, and you nod eagerly. Unfortunately,
it immediately becomes clear you underestimated what increasing your strength
entailed, and the surge of power nearly knocks you onto your fuzzy cat butt. You
say something to the effect of, "Hnnngwhahuh," and stumble around a little, but
the plushie simply smiles and releases your paw.

"There," she says. "Return here with milk you collect from fallen beasts, and I
will continue to embolden you. Remember I can only strengthen you if you collect
an amount of milk equal to twice your current strength." She bows to you politely.
"Farewell, dear Mouser. May you find your worth in the milk of the waking world."

You wave dumbly and stagger back over to the Yhowlnam stone to transport back to
the waking world.

You now have a new command available. Use DREAM when not in battle to return and
level up.
""")
	time.sleep(waitTime)


# Displayed if player has no milk.
def dreamLeaveNoLevel(waitTime, hasWpn, hasSwrd, weapon):
	print(""""When you collect milk, return here, to the Dream," the plushie says. "I will use
them to embolden your spirit, and increase your strength. Remember I can only
strengthen you if you collect an amount of milk equal to twice your current
strength." She bows to you politely. "Farewell, dear Mouser. May you find your
worth in the milk of the waking world."

You wave to your new best friend and return to the Yhowlnam stone to transport
back to the waking world.

You now have a new command available. Use DREAM when not in battle to return and
level up.
""")
	if hasWpn == False:
		print("""Just before you leave, you find an old sword lying next to a gravestone. You pick
it up and decide the age-old mantra of "Finders Keepers" definitely applies here.
Time to make all the mousies pay for your prior humiliation.
""")
		weapon = "1"
		hasSwrd = True
		hasWpn = True
	return hasWpn, hasSwrd, weapon
	time.sleep(waitTime)


##########################--GASCLAW--###############################


# Transitions between the Catnap Dream and the player decisions back in Yhowlnam.
def gilpurrtOpen(waitTime):
	print("""You arrive next to a lantern with the friendly ghost kittens huddled around it.
The baying of horrible mousies can be heard in the distance, but there's another
sound much closer to you. It's a cat, apparently hacking up one horrific hairball
in a boarded-up house. The window is barred and curtained on the inside, but you
can still see the warm glow of lamps peeking through.

A large, diseased-looking rat rummages around in garbage nearby. It hasn't noticed
you, and looks fairly weak. You could likely take it down easily in a fight.""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def gilpurrtNext(userInput):
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
def gilpurrtOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You approach the window cautiously and ask if the cat within is all right. A
weary voice replies, "Oh, hello. There isn't much hope for me, I'm afraid. But
there's nothing to be done about that. Don't pity me."

You decide not to tell him that you weren't about to.

"You're a mouser, aren't you?" the unseen cat asks. "I can smell it a mile away.
Your kind always smells of milk and blood. Like you've never bathed a day in your
nine lives."

You stare into space and wonder if there's anyone in Yhowlnam who isn't an asshole.

"My name is Gilpurrt," the cat continues. "I would join you in your quest to end
this constant night, but I wouldn't be much use to you. Forgive me."

He breaks off into another hacking fit. You decide to leave him alone. As you back
away from the window, Gilpurrt saying, "Good luck on the hunt, Mouser." """,
		"FIGHT":
"""You creep over to the rat, sword in hand. The beast lifts its head, and you
freeze in place until it goes back to eating trash. It's not unlike you on a long
weekend: complacent and stuffing itself with garbage.

You spring forward and slash through the rat with a single blow. It screams and
falls to the ground, dead. A bottle of milk rolls out from beneath its corpse,
and you proudly pick it up. You kick the dead rat into the pile of trash and walk
away. It's only about a minute before you hear shuffling and squeaking. You turn
to look, and see another rat now rummaging through the refuse.

It seems there's no lack of vermin here.""",
		"STARE":
"""You stare at the window, you stare at the rat, you stare at the lantern. After
a moment of staring, the hacking cat behind the window asks, "Not much to do,
Mouser?"

Embarrassed, you try to look busy by sharpening your weapon.""",
		"LOOK":
"""The buildings around you are tall and dark, save for the lamplight that can
be seen just faintly through some barricaded windows and doors. It's impossible
to tell if there are actually living occupants in all of these residences.

The rat nearby digs busily through the pile of garbage and nibbles on the juiciest
bits. Gross. You're still positive you would be able to kill it without trouble.

Of course, you were positive you wouldn't wake up as a cat today.""",
		"LEAVE":
"""You stretch and shake out your paws to reinvigorate yourself, and then set out
for the next stage of your hunt. A chill down your spine tells you that things are
about to become more challenging.

The terrible howl from the dark streets ahead confirms your suspicion. That's not
good, is it?"""}
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


# Transitions to the Gasclaw boss arena.
def gasclawOpen(longTime, shortTime):
	print("""You pass through a few dark alleys and emerge in a graveyard shaded from the
moonlight by gnarled oak trees. A cold wind blows through the branches and makes
them creak and sway. But more chilling than the air is the tall figure of a cat,
hacking at a grotesque fallen beast with a bloodied ax. His wide-brimmed hat, scarf,
and coat are splattered with old and new blood.

"Rats all over the shop," the cat mutters darkly. "And not enough milk to spare."

Once his prey stops twitching, the cat lifts his head and turns to snarl at you.
Somehow, you magically know this cat's name is...
""")
	time.sleep(longTime)
	print("""Father Gasclaw.""")
	time.sleep(longTime)
	print("""
Or perhaps you're finally going insane. Who knows?

Just as you decide to see yourself out, Gasclaw charges toward you, swinging his
ax for your neck. You jump out of the way and grip your sword tightly. Oh, God.
You didn't sign up for this.

But you're in it now. Time to show your stuff.
""")
	time.sleep(shortTime)


# Determines whether player should be prompted again for a command.
def gasclawNext(userInput):
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
def gasclawOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You whimper out an attempt to ask if you can talk things out.

Father Gasclaw responds by aiming an ax blow at your head. You dodge, and the ax
slams into a gravestone and shatters it.

He's clearly not the chatty type.""",
		"STARE":
"""Stare? You want to stare at something with a crazed ax murderer trying to kill you?
Pick something smarter than that, you lunatic.""",
		"LOOK":
"""All of your attention is on the blood-thirsty Father Gasclaw doing his best to
turn you into minced meat. You long for ugly, squeaky mouse beasts. At least they
couldn't--oh, dear God, he was able to jump halfway across the graveyard to try
and slam his ax into your face just now. How did he do that?

Do something, hurry!""",
		"LEAVE":
"""You attempt to make a run for it, but Father Gasclaw streaks around you at a
shocking pace and blocks your path. He then attempts to hit you with his ax as
punishment, and the blade comes so close to you that it snips off some of your
whiskers.

This is bad.""",
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
def gasclawFight(milk, level, won, waitTime):
	bossReward = 8
	print("""
------------------------------

You spend some time running around the graveyard and whimpering as you frantically
dodge attack after attack. Finally, you sum up the courage to start dealing blows
of your own. You start feeling pretty good about yourself, and then Gasclaw shoots
you with a blunderbus. Then he snaps out the handle of his ax to lengthen his
attacks and becomes faster and more brutal. Neither of these things are enjoyable.
But you continue to survive by the skin of your sharp kitty teeth.
""")
	time.sleep(waitTime)
	if level > 3:
		milk = milk + bossReward
		won = True
		print("""Just as you think you're wearing him down, Father Gasclaw transforms into a hulking,
hideous version of himself, and casts aside his weapons in favor of attacking you
with his bare claws. His roars, thankfully, drown out the sound of your panicked
screaming.

You continue to persevere, and after what feels like an eternity, you manage to
slam your sword through Father Gasclaw's chest, piercing his heart. He gurgles
and falls to the ground, dead. Eight bottles of milk roll out from beneath his
corpse, but you don't pick them up until you poke his body with your sword and
confirm he is, indeed, the deadest he can be.
""")
		time.sleep(waitTime)
		print("""Pride and relief wash over you and you take a moment to triumphantly pump your
paws in the air. It's fine, you earned this little celebration.

Once you've appropriately savored your victory, you strike out for the next area
with a new pep in your step. Wait until you show the plushie how busy you've been.
""")
		time.sleep(waitTime)
		print("""On your way out, you notice an abandoned war hammer propped up against a gravestone.
You pick it up, and realize it's able to transform between being a sword and being
a hammer. It's heavy, but it's also awesome, and that's what really counts in a
weapon.

You discard your old sword, and swing your new hammer up onto your shoulder. Man,
if only you could take a selfie right now.
""")
	elif level == 1:
		milk = 0
		won = False
		print("""Sadly, this success story doesn't last for long. You fight valiantly for a few
minutes more, only to succumb to the unending brutality Father Gasclaw tirelessly
rains down upon you.

You crash to the ground, and as your vision fades, you see Father Gasclaw pick up
and consume the milk that rolls out from under you. What a jerk.

----------YOU DIED----------
""")
	else:
		milk = 0
		won = False
		print("""Just as you think you're wearing him down, Father Gasclaw transforms into a hulking,
hideous version of himself, and casts aside his weapons in favor of attacking you
with his bare claws. His roars, thankfully, drown out the sound of your panicked
screaming. You fight valiantly for a few minutes more, only to succumb to the
unending brutality Father Gasclaw tirelessly rains down upon you.

You crash to the ground, and as your vision fades, you see Father Gasclaw pick up
and consume the milk that rolls out from under you. What a jerk.

----------YOU DIED----------
""")
	time.sleep(waitTime)
	return milk, won


####################--MILK-STARVED BEAST--#########################


# Enters the chapel.
def chapelOpen(waitTime):
	print("""You emerge in a dreary little chapel that has definitely seen better days. The
sound of shuffling rats can be heard outside the building, but none of them come
near the doors. Maybe the strong scent of incense is driving them away.

A hairless cat wrapped in a cloak is huddled in a corner, fussing over his strange
collection of jars. Interesting. At least he doesn't look ready to attack you if
you speak to him.

In the center of the room is a familiar lantern with your ghost kitten friends.
They mew and wave in cheerful greeting, and you can't help but smile. Who would
have thought ghosts could be such cute little rascals?""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def chapelNext(userInput):
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
def chapelOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You approach the hooded dweller of the chapel, and he lifts his head with a
surprised sound when he notices you. He blinks his large, reflective eyes, then
says, "Oh, you must be... a mouser! Sorry about that. The incense must have masked
your scent."

At least you've got one thing going for you.

"Everyone's all locked up inside," the dweller explains, fidgeting with his jars.
"Waiting for all this to end. It always does!" His voice became upbeat there for
a moment, but it drops down to a grimmer tone when he adds, "But... it won't end
nicely. Not this time... Yhowlnam's done for."

You ask why that is. The dweller quickly shakes his head. "You're safe in here,
Mouser," he says instead. "The incense wards off the beasts. But I can't say as
to how safe you are out there. Do take care, won't you?"

He giggles nervously, and you give him an odd look as you slowly back away. Best
to just leave this guy alone, you think.""",
		"FIGHT":
"""You walk outside in search of the rats you can hear getting up to no good. It
doesn't take you long to find them. There are three milling outside the chapel,
nibbling on dead grass, scratching at rocks, and generally being a nuisance.

Your very heavy hammer makes very short work of all three. It also makes one hell
of a satisfying mess. You survey the devastation like the mentally ill protagonist
you are, and notice three more rats creeping out from a nearby sewer duct. You
scoop up the milk dropped by the smashed rat corpses, and warn the newcomers that
you'll be back with your hammer if they make noise.

They give you the terrifyingly brainless stare only a rabid rodent can manage.
It seems you can't intimidate the diseased.

For now, you return to the chapel.""",
		"STARE":
"""You stare at the wee spectral kittens in their ghoulish cuddle puddle by the lamp.
They squeak at you and bow their heads while pressing their paws together in prayer.
You don't know what their prayers are, but you know they're praying for you.

Which is good, because you need all the redemption you can get, you murderer. Father
Gasclaw was clergy. God probably isn't crazy about milk-guzzling drifters cutting
down priests.""",
		"LOOK":
"""The chapel is as grim and oppressive as the rest of Yhowlnam, but the light from
the lantern in the center of the room and the candles positioned along the walls
is somehow reassuring. The dweller mutters to himself as he obsessively cleans his
jars with his cloak. Your kitten friends yawn and purr sleepily around the lantern.

It's surprisingly peaceful here, even though you can still hear the rats milling
about outside. You're tempted to curl up and take a nap. Apparently, cats really
can sleep anywhere.""",
		"LEAVE":
"""Despite the overwhelming temptation to settle in for a nice catnap with the ghost
kittens, you know this hunt will never end if you don't get out there and continue
the bloodbath. You give a parting wave to the kittens, and to the dweller, and set
out down the path outside the chapel."""}
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
		milk = milk + 3
	return milk


# Transitions to the Milk-Starved Beast boss arena.
def milkBeastOpen(longTime, shortTime):
	print("""The road you follow takes you to a more derelict section of Yhowlnam, scarred by
burn marks from what must have been a widespread fire. You wind up at yet another
church. They seem popular in Yhowlnam. This one is far less reassuring than the
chapel maintained by the dweller, however.

An altar lies on the opposite side of the cavernous sanctuary, and your sharp cat
eyes can see a strange shape huddled down in front of it. You could mistake it for
a large corpse at first, but as you draw nearer, it stirs and begins crawling your
way. For a few seconds, you're able to pretend it's friendly.
""")
	time.sleep(longTime)
	print("""But then it rears up onto its hind legs and gives a scream that is most definitely
not friendly. It's a giant, cat, clearly starved beyond what a normal animal could
survive. You initially think the billowing material over its head is a red cloak,
but as the beast continues to get closer, you realize it's actually the skin from
its back, peeled from the meat and tossed over its head like a veil.

Once again, you find you magically know this creature's name.
""")
	time.sleep(longTime)
	print("The Milk-Starved Beast.")
	time.sleep(longTime)
	print("""
You briefly wonder why that keeps happening, and then try to nope out of the church,
like any sane person would. Sadly, the way is now blocked. And the Milk-Starved
Beast turns out to be surprisingly fast when it sweeps in to strike at you with
its horrible claws.

Good luck in there, kid.
""")
	time.sleep(shortTime)


# Determines whether player should be prompted again for a command.
def milkBeastNext(userInput):
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
def milkBeastOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You open your mouth to speak, and are almost immediately slapped across the church.

For a starving beast, that thing certainly is strong.""",
		"STARE":
"""That's quite possibly the worst thing you could do right now.""",
		"LOOK":
"""You barely have time to look at anything before the Milk-Starved beast is charging
in like a rabid hell beast. It screams and swings its claws at you with enough
force to blow the tails of your coat back as you dodge away. It smashes its paws
into the stone floor in frustration, and the rock cracks beneath it.

Now would be a very good time to fight back.""",
		"LEAVE":
"""You already tried that and it didn't work!

Try using that new hammer of yours or something, at least.""",
		"DREAM":
"""The plushie can't save you here, coward.

Seriously, stop trying to get out of these fights."""}
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
def milkBeastFight(milk, level, won, waitTime):
	bossReward = 12
	print("""
------------------------------

Determined to start acting like the hero you're destined to be, you charge out to
meet the Milk-Starved Beast with the devastating force of your hammer.

Unfortunately, this monster is a hell of a lot faster than your hammer swings.
You do a number on the poor, defenseless floor, but only manage to graze the beast
every so often. You'll need to be tactical here.
""")
	if level >= 6:
		milk = milk + bossReward
		won = True
		print("""You snap the hammer apart to use the sword, hanging the head of the hammer on your
back to keep it out of the way. It's a sacrifice of strength, but it grants you
more dexterity, and the ability to actually hit the stupid monster.

As you learn the attack patterns of the beast, you realize that some of its strikes
give you small windows of potential hammer time. You pounce on these with the vigor
of a born hunter, and gradually beat the Milk-Starved Beast to a pulp.
""")
		time.sleep(waitTime)
		print("""The creature finally falls with a harrowing death rattle, and twelve bottles of
milk roll out from beneath its broken body. It suddenly occurs to you that you just
brutalized a starving cat to death with a hammer.

Good job, hero.

Deflated, but alive, you pick up the bottles of milk and slink out of the church
to proceed to the next area. Maybe if you come across another church, you should
stop in to the confessional for a quick absolution.
""")
		time.sleep(waitTime)
		print("""On your way out, you find an ornately carved greatsword that's as long as you are
tall. It looks like a holy relic from an age gone past. You discard your hammer,
and scoop up the new weapon, expecting it to be somewhat lighter.

It isn't. But it is more balanced and prettier to look at. So you decide it's
worth the exchange after all.
""")
	else:
		milk = 0
		won = False
		print("""You snap the hammer apart to use the sword, hanging the head of the hammer on your
back to keep it out of the way. While you fumble with your fancy trick weapon,
the Milk-Starved Beast seizes the opportunity to zip in and eviscerate you.

You crumple to the ground, and the Milk-Starved Beast shrieks and continues to
slash and maul you as you die. The last thing you see is the monster gleefully
slurping up all the milk you drop.

At least you die knowing you fed a hungry cat.

----------YOU DIED----------
""")
	time.sleep(waitTime)
	return milk, won


##################--PURRGO'S WET NURSE--####################


# Enters Purrgo's Loft.
def loftOpen(waitTime):
	print("""The traversal to the next area in Yhowlnam is decidedly more bizarre than your
prior treks. You notice the buildings around you taking on an almost surrealist
appearance, with strange angles, stairways to nowhere, and even upside-down windows.
Looking up, you see the moon has grown to an unsettling size overhead. That explains
why the streets are so bright now.

Something ominous lies ahead. But at least you find another lantern with the friendly
ghost kitty committee waiting to greet you. They're always a welcome sight. You
can also hear the sound of rats scurrying around nearby, which means a steady
supply of prey. Is your night finally looking up?

Spoiler: No.""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def loftNext(userInput):
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
def loftOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You kneel down by the lantern to hold a soft conversation with the phantom kittens.
They mew and purr, always happy to see you. You softly pat their tiny heads, and
you're surprised to discover that you can feel their fur, despite their ghostly
appearance.

Since petting kittens can lower blood pressure, you spend a while doting on your
little friends. They help you momentarily forget you still don't know how you got
here, or what your ultimate goal is.

Be honest, though; isn't that how you live your life every other day?""",
		"FIGHT":
"""You follow the sound and scent of the hideous giant mousies lurking nearby. It's
milkbath time, baby. So eager for the rewards are you that you don't even care
that your prey-to-be is a whole family of rats.

You put your new greatsword to work by eliminating every member of the rat colony
with no remorse. You're already a well-established butcher, so why care at this point?

Seven bottles of milk serve as your reward. And you hear another group of rats
on its way. Truly, this is the land of milk and honey. But without the honey.""",
		"STARE":
"""You engage in a staring contest with the kittens. They match you for a while,
but then dissolve into adorable kitty giggles. If only you could put them in your
pockets, you would keep them forever.""",
		"LOOK":
"""The strange architecture around you makes you uneasy, and there's an undeniable
sense of impending doom in the air. Perhaps it's the giant moon in the sky, or the
odd geometry, or the... distant sound of a kitten crying?

What is that? You hadn't heard that before. It isn't the ghost kittens, it's something
in the distance, and has an eerie tone to it.""",
		"LEAVE":
"""Once you've had your breather, you pick up your greatsword, pluck up your courage,
and continue your walk through the moonlit streets. The distant sound of a crying
kitten catches your ear, and you follow it out of curiosity.

You realize a bit late that "curiosity killed the cat" is a saying for a reason."""}
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
		milk = milk + 7
	return milk


# Transitions to the Purrgo's Wet Nurse boss arena.
def nurseOpen(longTime, shortTime):
	print("""The melancholy cries of the thus-unseen kitten lead you to an open-air loft at
the top of a tower. Moonlight floods the chamber unhindered, and as you look around,
you realize...

This is definitely a boss arena.

Instinct tells you to run, but a baby carriage at the other end of the room catches
your eye. You find yourself inexplicably drawn to it, but before you get close
enough to peer inside...
""")
	time.sleep(longTime)
	print("""...a nine-foot-tall winged figure in black robes drops down between you and the
buggy. There's no face within the hood, but cat ears poke up through holes at the
top of the fabric, and a skeletal cat tail extends from the back of the figure's robes.

You aren't surprised this time when the figure's name appears in your head.
""")
	time.sleep(longTime)
	print("""Purrgo's Wet Nurse""")
	time.sleep(longTime)
	print("""
The thought of this monstrosity nursing anything is too harrowing for your frail
mind to handle, so you pretend you never saw that.

You lift your greatsword to show you're not to be trifled with.

The Nurse responds by whipping out six arms gripping six jagged blades.

...oh.
""")
	time.sleep(shortTime)


# Determines whether player should be prompted again for a command.
def nurseNext(userInput):
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
def nurseOptions(userInput, dream, milk, level, hasWpn, weapon):
	sceneOptions = {"TALK":
"""You attempt to strike up a conversation with the Nurse about the baby for whom
she's providing. Maybe complimenting her baby will endear you to her.

It doesn't. And we should have a serious discussion about your assumption that you
can simply flatter your way out of a confrontation with a female. It's this narrator's
opinion that you deserve all the flesh wounds you suffer when she charges you with
a whirlwind of blade slashes.

Just kidding. Lighten up. You probably tried this with the other major foes you
faced, which means it isn't that you're sexist; you just don't learn.""",
		"STARE":
"""You're given no time to stare by the Nurse, who has begun using her wings to
swoop across the room in a single motion, shaving off your fur and bits of clothes
with every near-miss.""",
		"LOOK":
"""The kitten you presume is in the baby carriage continues to cry as you dart to
and fro out of the Nurse's reach. The chamber is otherwise unremarkable, and you
have the passing thought that it looks as though it's been cleared out for some
sort of ritual.

Why you think that, you aren't certain.""",
		"LEAVE":
"""You run for the exit, but the Nurse intercepts you and knocks you back into the
center of the room. She's not done with you yet. You'll need to fight to earn your
way out of this nursery of horrors.""",
		"DREAM": "The plushie can't save you here, coward. You're in this for the long haul."}
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
def nurseFight(milk, level, won, waitTime):
	bossReward = 18
	print("""
------------------------------

It takes some time for you to become accustomed to the sheer weight of your
greatsword, but the Nurse provides plenty of incentive for you to learn quickly.
She swoops and twirls with the grace of a deadly ballerina as she attacks you
with unrelenting ferocity.

It takes everything you have to keep up with the Nurse, but you gradually develop
your ability to read her moves and discover openings in her sextupled attacks.
She strikes, you dodge and zip in beneath her arms to slash at her. Over and over,
you repeat this dance, weakening the Nurse with every blow.

You feel good about your progress. Everything is going well! All of your hard work
in this hellscape has paid off!
""")
	time.sleep(waitTime)
	print("""And then the Nurse summons a clone of herself to join in the onslaught.

You have to actively resist the urge to throw your greatsword on the ground so you
can stomp off to the sidelines to sulk. Why is everything so awful all the time?
""")
	time.sleep(waitTime)
	if level >= 9:
		milk = milk + bossReward
		won = True
		print("""Little do those Nurses realize you've been training for this all night.

So what if there's two? Child's play! You'll kill them AND raise that crying kitten
on your own! You don't care! You're the Mouser! You'll turn this into a Feline
Single Parent Simulator and not bat an eyelash!

It takes a second for you to realize you actually said all of that aloud.

Oh, well, it probably sounded cooler to others than it did in your own ears, don't
worry.
""")
		time.sleep(waitTime)
		print("""Your persistence ultimately pays off, and you handily defeat both Nurses. You give
a triumphant howl at the moon as they both fall, lifting your greatsword over your
head. Finally! You are truly the chosen one!

The cries of the kitten ebb away into soft, contented purring, reassuring you of
your righteousness in this gruesome situation.

With your enemies slain, you walk over to the baby carriage, only to find it empty.
Was the kitten ever really there?

You turn to leave, but the moonlight around you intensifies until the world around
you goes completely white. You feel yourself being transported back to the familiar
comfort of the Catnap Dream.
""")
	else:
		milk = 0
		won = False
		print("""Your frustration with the situation quickly takes its toll.

The two nurses are simply too much for you to handle in your current state. You
give it your all for a while, but are soon reduced to shredded cat meat by the
twelve cold blades of the Nurses. The first Nurse scoops up your dropped milk as
you die, and you bitterly hope she gets poisoned by it.

Can nightmarish creatures get food poisoning?

Who cares, it's a nice last fantasy for you to entertain.

----------YOU DIED----------
""")
	time.sleep(waitTime)
	return milk, won


################--DREAM RETURN--####################


# Returns to the Catnap Dream.
def dreamReturnOpen(waitTime):
	print("""You open your eyes back in the Catnap Dream to find the plushie and ghost kittens
awaiting as usual. Everything is as it should be.

Except for the fact the chapel at the top of the hill is on fire.

...wait, what?

Why the hell doesn't the plushie look concerned by this?""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def dreamReturnNext(userInput):
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
def dreamReturnOptions(userInput, dream, milk, level, hasWpn, weapon, cord):
	sceneOptions = {"TALK":
"""You approach the plushie and ask her what happened. She tilts her head.

"You have slain the Nightmare, good Mouser," she replies. "This Night will end.
And the Hunt will begin again. You have done well."

That... explains nothing, but you're not surprised at this point.""",
		"FIGHT":
"""You feel no urge to fight anything. In fact, you contemplate having a nice nap
next to the spectral kittens at the lantern.""",
		"STARE":
"""You stare at the plushie, and she stares back at you in return.

Ah, how you have missed this. No one stares like your beloved plushie.""",
		"LOOK":
"""You look around the garden for any sign of who or what could have started the
fire up on the hill. It's unthinkable the plushie could have done such a thing.
She is best girl, after all.

You never discover the cause of the fire, but you do discover a strange cord in
a patch of dead grass behind a headstone. You pick it up to inspect it, then put
it in your pocket for later. One never knows when mysterious things may come in
handy later.""",
		"LEAVE":
"""You walk over to the Yhowlnam headstone to return to the city, but find yourself
unable to transport the way you have in the past. Is it broken? You approach the
plushie and ask her about it, and she smiles at you.

"Beloved Mouser," she says, "you may return. But only to the beginning. First, we
must end."

You panic a little. Are you about to fight this plushie as the final boss? Please,
not her! Your only friend! Besides the kittens, of course; they're also cool with you.""",
		"DREAM": "You are already dreaming and you can't go deeper."}
	print("""
------------------------------
""")
	if str.upper(userInput) == "CHECK":
		statusCheck(milk, level, hasWpn, weapon)
	elif str.upper(userInput) == "HELP":
		commandList(dream)
	else:
		print(sceneOptions.get(str.upper(userInput)))
	if str.upper(userInput) == "LOOK":
		cord = True
	return cord


#################--ENDINGS--###################


def endNoCord(waitTime):
	print(""" "You have fought well, good Mouser," the plushie says sweetly as she takes your paws.
"Please. Rest now. And then awaken to begin this night again."

The plushie sits you down on the grass, and tenderly holds you as you drift off
to sleep. You wonder if you'll have a grand epiphany about what everything meant,
and finally understand why you came here, and why you fought such foul creatures.
""")
	time.sleep(waitTime)
	print("""You don't. And you won't. You simply slip away, just as you will one day in the
real world. No respawn. No explanation of what it all meant.
""")
	time.sleep(waitTime)
	print("""It only means what you decide it does.
""")
	time.sleep(waitTime)
	print("""Even if it means nothing at all.
""")
	time.sleep(waitTime)
	print("""Goodnight, Mouser.
""")
	time.sleep(waitTime)



def endCord(waitTime):
	print(""" "You have fought well, good Mouser," the plushie says sweetly. "Please. Bring out
the umbilical cord you discovered behind the grave."

Oh, dear God, that's what that was?! And you touched it with your bare paws?!

You quickly dig the cord out of your pocket and toss it to the plushie while making
as little contact with it as possible. She catches it deftly, and holds it to her
heart.

"This is a very special thing," the plushie says. "It will make everything right
again." She bows to you gratefully. "Rest now, sweet Mouser."

Slightly disturbed, you settle down next to the kittens and curl up to go to sleep.
You wonder if you'll have a grand epiphany about what everything meant, and finally
understand why you came here, and why you fought such foul creatures.
""")
	time.sleep(waitTime)
	print("""You do. But it comes as a flood of maddening Eldritch knowledge. Madness consumes
you, and you slip away in the terrifying grip of wisdom you never wanted. Too
insane to make sense of what you've gained.
""")
	time.sleep(waitTime)
	print("""Just as you likely never will in the real world.""")
	time.sleep(waitTime)
	print("""You will simply cease to be, with no respawn, and no chance to put the terrible
truth to any tangible use.
""")
	time.sleep(waitTime)
	print("""Goodnight, Mouser.
""")
	time.sleep(waitTime)


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

bossDead = False

entryTime = 1
cinematicTime = 4

died = False
umbilicalCord = False

# time is used to create pauses between text.
import time

# Display title of game and commands.
titlePage(entryTime)
entry = input("Enter your choice: ")
entry = tryAgainStart(entry)

# Opening "cinematic".
opener(entryTime)
entry = input("Enter your choice: ")
entry = tryAgain(entry)

# Loops command prompts until player selects one that progresses the story.
while nextScene == False:
	nextScene = sceneOneNext(entry)
	sceneOne(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
	print("")
	if nextScene == False:
		time.sleep(entryTime)
		entry = input("Enter your choice: ")
		entry = tryAgain(entry)
	else:
		time.sleep(cinematicTime)

# If player chose to talk to the old cat, arm player.
if str.upper(entry) == "TALK":
	hasWeapon = True
	oldSword = True
	heldWeapon = "1"

# Reset the nextScene check before proceeding.
nextScene = False
# Alone after old cat leaves.
afterOldCat(entryTime)
entry = input("Enter your choice: ")
entry = tryAgain(entry)

# Branches story according to whether or not the player is armed with the sword.
if hasWeapon:
	while nextScene == False:
		nextScene = sceneTwoNext(entry)
		sceneTwoTalk(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			time.sleep(entryTime)
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			time.sleep(cinematicTime)
else:
	while nextScene == False:
		nextScene = sceneTwoNext(entry)
		sceneTwoStare(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			time.sleep(entryTime)
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			time.sleep(cinematicTime)

nextScene = False
# Transitions to the clinic entrance.
clinicEntrance(entryTime)
entry = input("Enter your choice: ")
entry = tryAgain(entry)

if hasWeapon:
	while nextScene == False:
		nextScene = sceneThreeTalkNext(entry)
		collectedMilk = sceneThreeTalk(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			time.sleep(entryTime)
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			time.sleep(cinematicTime)
else:
	while nextScene == False:
		nextScene = sceneThreeStareNext(entry)
		sceneThreeStare(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			time.sleep(entryTime)
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			died = True
			time.sleep(cinematicTime)

# Branches the game according to whether or not the player was armed in scene three.
if hasWeapon:
	nextScene = False
	sceneFourOpen(entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = sceneFourNext(entry)
		sceneFour(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
		print("")
		if nextScene == False:
			time.sleep(entryTime)
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			time.sleep(cinematicTime)
			dreamTransition(cinematicTime)
else:
	nextScene = False
	print("""----------YOU DIED----------
""")
	time.sleep(cinematicTime)

nextScene = False
sceneFiveOpen(entryTime)
entry = input("Enter your choice: ")
entry = tryAgain(entry)

while nextScene == False:
	nextScene = sceneFiveNext(entry)
	sceneFive(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
	print("")
	if nextScene == False:
		time.sleep(entryTime)
		entry = input("Enter your choice: ")
		entry = tryAgain(entry)
	else:
		time.sleep(cinematicTime)

if collectedMilk != 0:
	dreamLeaveLevel(cinematicTime)
	milkLevel = milkLevel + 1
	collectedMilk = 0
	hasDream = True
else:
	hasWeapon, oldSword, heldWeapon = dreamLeaveNoLevel(cinematicTime, hasWeapon, oldSword, heldWeapon)
	hasDream = True

	# If player died in the first fight, return them to the clinic so they can
	# kill the mouse there.
	if died == True:
		nextScene = False
		clinicReturn(cinematicTime, entryTime)

		entry = input("Enter your choice: ")
		entry = tryAgain(entry)

		while nextScene == False:
			nextScene = sceneThreeTalkNext(entry)
			collectedMilk = sceneThreeTalk(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

		nextScene = False
		sceneFourOpen(entryTime)
		entry = input("Enter your choice: ")
		entry = tryAgain(entry)

		while nextScene == False:
			nextScene = sceneFourNext(entry)
			sceneFour(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)
		died = False

# Bring branches back to the main storyline.
# Loops area until Gasclaw has been beaten by the player.
while bossDead == False:
	nextScene = False
	gilpurrtOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = gilpurrtNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			gilpurrtOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk = gilpurrtOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

	nextScene = False
	gasclawOpen(cinematicTime, entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = gasclawNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = gasclawFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			gasclawOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Changes weapon type held by player after Gasclaw defeat.
oldSword = False
hammer = True
heldWeapon = "2"

# Resets the check to see if the boss is dead for the next area.
bossDead = False

# Loops area until Milk-Starved Beast has been beaten by the player.
while bossDead == False:
	nextScene = False
	chapelOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = chapelNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			chapelOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk = chapelOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

	nextScene = False
	milkBeastOpen(cinematicTime, entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = milkBeastNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = milkBeastFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			milkBeastOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Resets the check to see if the boss is dead for the next area.
bossDead = False

# Changes the weapon to the great sword after Milk-Starved Beast defeat.
hammer = False
greatSword = True
heldWeapon = "3"

# Loops area until Purrgo's Wet Nurse has been beaten by the player.
while bossDead == False:
	nextScene = False
	loftOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = loftNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			loftOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk = loftOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

	nextScene = False
	nurseOpen(cinematicTime, entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = nurseNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = nurseFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			nurseOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Resets the check to see if the boss is dead for the next area.
bossDead = False
nextScene = False

# Return to the Catnap Dream for the final sequence.
dreamReturnOpen(entryTime)
print("")
entry = input("Enter your choice: ")
entry = tryAgain(entry)

while nextScene == False:
	nextScene = dreamReturnNext(entry)
	umbilicalCord = dreamReturnOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon, umbilicalCord)
	print("")
	if nextScene == False:
		time.sleep(entryTime)
		entry = input("Enter your choice: ")
		entry = tryAgain(entry)
	else:
		time.sleep(cinematicTime)

if umbilicalCord:
	endCord(cinematicTime)
else:
	endNoCord(cinematicTime)

# Prompts player for last time before exiting.
print("Play again?")
print("")
entry = input("Enter YES or NO: ")
entry = tryAgainEnd(entry)
goodbye(entry)
