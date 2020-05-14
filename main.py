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


# Transitions to clinic entrance.
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
	print(""""You have collected milk which can be used to increase your strength,"
the plushie says. "I will channel them, and your power will grow."

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
	print("""
------------------------------
""")
	if level > 3:
		print("""Here is the winning text.
""")
		milk = milk + 6
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


####################--MILK-STARVED BEAST--#########################


# Enters the Cathedral.
def cathedralOpen(waitTime):
	print("""Something""")
	time.sleep(waitTime)


# Determines whether player should be prompted again for a command.
def cathedralNext(userInput):
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
def cathedralOptions(userInput, dream, milk, level, hasWpn, weapon):
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


# Transitions to the Milk-Starved Beast boss arena.
def milkBeastOpen(waitTime):
	print("""Here is the opening text for the Milk-Starved Beast.
""")
	time.sleep(waitTime)


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
def milkBeastFight(milk, level, won, waitTime):
	print("""
------------------------------
""")
	if level >= 7:
		print("""Here is the winning text.
""")
		milk = milk + 14
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


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
	if level >= 12:
		print("""Here is the winning text.
""")
		milk = milk + 24
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


##################--PURRGO'S WET NURSE--####################


# Enters Purrgo's Loft.
def loftOpen(waitTime):
	print("""Something""")
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
		milk = milk + 7
	return milk


# Transitions to the Purrgo's Wet Nurse boss arena.
def nurseOpen(waitTime):
	print("""Here is the opening text for Purrgo's Wet Nurse.
""")
	time.sleep(waitTime)


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
def nurseFight(milk, level, won, waitTime):
	print("""
------------------------------
""")
	if level >= 15:
		print("""Here is the winning text.
""")
		milk = milk + 30
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


################--MOON PRESENCE--###############


# Returns to the Catnap Dream.
def dreamReturnOpen(waitTime):
	print("""Something""")
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
"""Talk something""",
		"FIGHT":
"""Fight something""",
		"STARE":
"""Stare something""",
		"LOOK":
"""Look at something and find the umbilical cord."""}
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
	if str.upper(userInput) == "FIGHT":
		milk = milk + 10
	return milk, cord


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
	if level >= 17:
		print("""Here is the winning text.
""")
		won = True
	else:
		print("""Here is the losing text.
""")
		milk = 0
	time.sleep(waitTime)
	return milk, won


#################--ENDINGS--###################


def endNoCord(waitTime):
	print("""Here is the ending with no umbilical cord.""")
	time.sleep(waitTime)



def endCord(waitTime):
	print("""Here is the ending with the umbilical cord.""")
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
		nextScene = sceneThreeNext(entry)
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
		nextScene = sceneThreeNext(entry)
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
			dreamTransition(entryTime)
else:
	nextScene = False
	print("""----------YOU DIED----------
""")

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
			nextScene = sceneThreeNext(entry)
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
			collectedMilk = gasclawOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Resets the check to see if the boss is dead for the next area.
bossDead = False

# Loops area until Milk-Starved Beast has been beaten by the player.
while bossDead == False:
	nextScene = False
	cathedralOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = cathedralNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			cathedralOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk = cathedralOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

	nextScene = False
	milkBeastOpen(entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = milkBeastNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = milkBeastFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			collectedMilk = milkBeastOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Resets the check to see if the boss is dead for the next area.
bossDead = False

# Loops area until Amelia has been beaten by the player.
while bossDead == False:
	nextScene = False
	churchOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = churchNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			churchOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk = churchOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

	nextScene = False
	ameliaOpen(entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = ameliaNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = ameliaFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			collectedMilk = ameliaOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

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

# Resets the check to see if the boss is dead for the next area.
bossDead = False

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
	nurseOpen(entryTime)
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = nurseNext(entry)
		if str.upper(entry) == "FIGHT":
			collectedMilk, bossDead = nurseFight(collectedMilk, milkLevel, bossDead, cinematicTime)
		else:
			collectedMilk = nurseOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

# Resets the check to see if the boss is dead for the next area.
bossDead = False

# Loops area until Moon Presence has been beaten by the player.
while bossDead == False:
	nextScene = False
	dreamReturnOpen(entryTime)
	print("")
	entry = input("Enter your choice: ")
	entry = tryAgain(entry)

	while nextScene == False:
		nextScene = dreamReturnNext(entry)
		if str.upper(entry) == "DREAM":
			collectedMilk, milkLevel = dream(collectedMilk, milkLevel, cinematicTime)
			print("")
			dreamReturnOpen(entryTime)
			print("")
			entry = input("Enter your choice: ")
			entry = tryAgain(entry)
		else:
			collectedMilk, umbilicalCord = dreamReturnOptions(entry, hasDream, collectedMilk, milkLevel, hasWeapon, heldWeapon, umbilicalCord)
			print("")
			if nextScene == False:
				time.sleep(entryTime)
				entry = input("Enter your choice: ")
				entry = tryAgain(entry)
			else:
				time.sleep(cinematicTime)

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

if umbilicalCord:
	endCord(entryTime)
else:
	endNoCord(entryTime)

# Prompts player for last time before exiting.
print("Play again?")
print("")
entry = input("Enter YES or NO: ")
entry = tryAgainEnd(entry)
goodbye(entry)
