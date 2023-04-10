"""
File: katosa_by_noah_nielsen.py
Title: KATOSA
Description: A computerized choose-your-own-fantasy-adventure novel
Author: Noah Nielsen
Purpose: Handle user input with if statements to make an interactive story

"""

import sys # sys.exit() is used to end the game.

# THE DECISION VARIABLE SYSTEM:
# Decisions are stored in variables and then checked using if statements.
# The variable naming system is very peculiar. The game is a giant decision tree,
# and giving unique variable names to each node on the tree helps me navigate.
# I used flowchart software to plan out the story, as I wanted to grant the player
# up to five decisions per run. That ended up being quite an order to fill
# with only if statements, as you can see by how long this file is.


# The story is intentionally inconsistent at times, but there is an underlying story
# which needs to be gathered through hints. Read into it, and see what you'll find!
# Try out multiple different paths each time, and who knows? Maybe you'll enjoy it :)


# Warn the user that story elements might seem inconsistent.
# Hopefully they'll get the hint and interpret discontinuity as normal.
print("Welcome to KATOSA, the choice-based fantasy adventure novel where the future is not the only thing shaped by your choices.")
print("Acceptable choices are presented in CAPITAL LETTERS. Choices do not also have to be entered in capitals.")
print()

# Let's get this story started!
print("Your name is Joshua, a human who normally lives on Earth.")
print("You wake up and find yourself beside a small lake in a dense forest. It must be the middle of the night,")
print("but the water seems to glow and you can see it clearly in the darkness.")
print("The lake is almost surrounded by high cliffs. You are lying on its rocky shore,")
print("between two such hills.")
print("All you have is an adventurer's pack, with a few things inside.")
print()

# FIRST DECISION: PANIC, SLEEP, STONES
# These are the three major story branches, so they are visually separated using this big ol' hash divider

###########################################################################################################################################
#######          PANIC          ###########################################################################################################
###########################################################################################################################################


while True:
    z = input("Do you PANIC, go back to SLEEP, or skip STONES? (You can also QUIT or ASK) >> ")
    print()

    if z.lower() == "panic":
        print("\"What's going on? Where am I?!\" you wonder to yourself. You've never seen this place before.")
        print("You're also rather cold. You don't know if you are in danger. You become so afraid you can hardly stand it!")
        print()

        while True:
            a = input("Do you SCREAM or remain SILENT? >> ")
            print()

            if a.lower() == "scream":
                print("\nYou can't contain your fear. You let out a whimper, and you start breathing faster. Soon this whimper grows louder,")
                print("and you let out a shrill, desperate cry. Very quickly, you realize that now is not the time to be attracting attention to yourself.")
                print("You've stopped screaming, but it is too late. You hear a few footsteps, and turn around to find a monster towering over your cowering self.")
                print("He does not look happy to see you.")
                print()

                while True:
                    aa = input("Do you FIGHT, flee to the FOREST, or flee to the LAKE? >> ")
                    print()

                    if aa.lower() == "fight":
                        print("Despite your current cowardly intentions, a sudden rush of anger surges through you, and you grab hold of a sliver of confidence.")
                        print("You decide now is the time to fight this beast. It is the only way to ensure your safety.")
                        print("The monster isn't moving. You take this small window of time granted you to discretely search for a weapon.")
                        print("You spot a good-sized sharp log nearby, and remember the rocks you were lying on when you woke up here. Those will have to do.")
                        print()

                        while True:
                            aaa = input("You only have time for one. Do you use the LOG or the ROCKS? >> ")
                            print()

                            if aaa.lower() == "log":
                                print("With not a moment to spare, you break into a sprint. The log is farther away than you thought.")
                                print("The monster grunts, and you can hear him following you. He's faster than he looks!")
                                print("It catches up to you right as you lay hold on your weapon. With precision, you hoist it up")
                                print("and rotate to point it towards him. Already in the motion of reaching for you, the monster puts forth his hand")
                                print("but gets a sharp log through it instead! You impaled the monster's hand!")
                                print("Flashing lights issue forth from the wound you inflicted. The monster roars, now enraged.")
                                print("Shocked and defenseless, you have barely enough time to almost feel bad for the creature.")
                                print("Before you are able to come to, the monster flails at you with his stricken hand.")
                                print("The log you used to incapacitate the monster falls hard onto you.")
                                
                                print("\n\nYOU DIED.")
                                sys.exit()

                            elif aaa.lower() == "rocks" :
                                print("You stoop down slowly and start picking up rocks and placing them into your sack. You manage to collect five")
                                print("before the monster suddenly takes a step backward, startling you. You start to run in the opposite direction.")
                                print()

                                while True:
                                    aab = input("Do you use the rocks against the beast NOW or find some COVER first? >> ")
                                    print()

                                    if aab.lower() == "now":
                                        print("You reach into your pack and discover... a sling! Still running, you pull it out along with one of the rocks.")
                                        print("You are unsure if this will be your only shot, but you draw the sling with confidence, and let a stone fly.")
                                        print("The monster was moving very quickly, you find out, but the stone effortlessly traverses the distance between you")
                                        print("and strikes the monster clean in the eye. The monster stumbles and falls, both hands covring his face.")
                                        print("He lets out a harsh, pained groan. You keep running, and find your way up one of the steep banks.")
                                        print("Looking back, the creature appears to have stopped breathing. You are safe now.")

                                        print("\n\nBut are you missing something?")
                                        sys.exit()

                                    elif aab.lower() == "cover":
                                        print("You decide to find some cover before attacking. You run as fast as your legs can carry you,")
                                        print("But it quickly becomes apparent that you couldn't run fast enough, because this creature")
                                        print("is much faster than you assumed. He quickly catches up to you, jumps ten feet into the air,")
                                        print("and slams directly atop you.")
                                        
                                        print("\n\nYOU DIED.")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
                                
                            else:
                                print("Invalid input.")
                                continue
                    
                    elif aa.lower() == "forest":
                        print("Confident you can outrun the monster, you dart towards the forest on your left. You can hear only the sounds")
                        print("of your own footsteps. Is he even following you? This is not the time to look back and see.")
                        print("You hear a moan echo from behind you. He seems sad and confused. Then the footsteps start. He's coming fast!")
                        print("You take a few turns to avoid leaving a simple trail to follow.")
                        print()

                        while True:
                            aab = input("You need to hide. You spot a BUSH and several TREES. Which do you use? >> ")
                            print()

                            if aab.lower() == "bush":
                                print("You dive into a thick bush. You didn't expect it to be so painful, but the twigs pierce and scrape your skin.")
                                print("Filled with adrenaline, you manage to restrain a whimper that would surely give you away. Breathing easy,")
                                print("you start to calm down. Listening like a helpless deer, you hear sparse footsteps interspersed with the sounds")
                                print("of rummaging leaves and trees being uprooted. \"Good thing I didn't go for the tree,\" you think to yourself.")
                                print("You are safe.")

                                print("\n\nBut are you missing something?")
                                sys.exit()

                            elif aab.lower() in ("tree", "trees"):
                                print("You notice the many low-hanging branches in the trees. Sounds like the footsteps are far away now.")
                                print("You steal a brief moment to look back. You spot the beast a ways off, searching curiously for you.")
                                print("If you make a sound, he'll surely hear you. However, you figure he'll find you even if you sit still.")
                                print("You decide to climb a nearby tree. You're not as clumsy as you thought. It's an easy climb almost straight to the top.")
                                print("Now above the thick canopy, you look around. It's a beautiful view. A distant, majestic mountain range stretches for miles.")
                                print("Suddenly, a flying tree obscures your view. It shoots straight into the air, and another follows it")
                                print("before it even touches the ground. The flying trees start tracing a path that's coming straight for you.")
                                print("\"The thing's pulling up the trees!\" You whisper, astounded. A terrible feeling overcomes you.")
                                print("Before long, the uprootings get closer, and your own tree heaves upward into the air. Left without much of a choice,")
                                print("you fly up with it, and come plummeting down with it too. You black out but don't wake up.")
                                print("The monster got you.")

                                print("\n\nYOU DIED")
                                sys.exit()

                            else:
                                print("Invalid input.")
                                continue

                    elif aa.lower() == "lake":
                        print("The lake is only some twenty feet away from you, but you may be able to outrun the beast and find some cover.")
                        print("Just as you are about to make a run for it, a loud rumbling shakes the earth beneath you and almost knocks you over.")
                        print("You hear the sound of crashing waters and turn back toward the lake. A large creature emerges from the deep,")
                        print("then spreads its reptilian wings and utters a terrible roar. You cover your ears at the deafening sound of it.")
                        print("Looking upward, you see a fantastic dragon some two hundred feet above you, flapping loudly and looking energized.")
                        print("You hear a voice behind you. \"Ahlakhaz has awoken.\" You turn to see the beast that once intimidated you")
                        print("mumbling in an unknown language. You can't just stand here caught betwen two things that may want to eat you.")
                        print()

                        while True:
                            aac = input("Do you STARE regardless, or do you RIDE the dragon? >> ")
                            print()
                            
                            if aac.lower() == "stare":
                                print("It may be unwise, but this is a sight to behold. You can't help but stand there, motionless, and gawk.")
                                print("The monster behind you has stopped mumbling, and looking at him you see his gaze is also locked on the dragon.")
                                print("It moves its feet into a square stance, and then leaps straight into the air toward the dragon.")
                                print("It lands atop the dragon, seemingly ready to pilot it. \"I wonder...\" you say, on the brink of realizing something.")
                                print()
                                
                                while True:
                                    aaca = input("Do you THROW ROCKS at the dragon, or continue to STARE? >> ")
                                    print()

                                    if aaca.lower() == "throw rocks":
                                        print("Filled with almost childish energy, you pick up a rock at your feet, grimace upward at the pair of enemies, and catapult it")
                                        print("straight up into the night air. Unable to control yourself, you pick up three more and hurl them in like manner, screaming.")
                                        print("You've had enough of this murderous fantasy world and its unfair surprises.")
                                        print("To your astonishment, as the final stone slides out of your hand, you see it burst into flame and gather tremendous speed.")
                                        print("Leaving behind a trail of fire and smoke, the stone shoots straight through the dragon's heart.")
                                        print("The dragon's wings begin to flap out of sync and it careens downward, crashing into the lake's surface. The monster")
                                        print("is nowhere to be seen. You are thoroughly confused, but you appear to be safe.")

                                        print("\n\nYou may be safe, but are you missing something?")
                                        sys.exit()

                                    elif aaca.lower() == "stare":
                                        print("You don't feel there's anything you can do at this point. You're cold, confused, and outnumbered.")
                                        print("The monster atop the dragon shrieks excitedly, and the dragon reels its head back, fire filling its maw.")
                                        print("Whipping its scaly head back in your direction, he lets loose a wide, burning beam of fire and gas,")
                                        print("which strikes you directly. You are unable to withstand it.")

                                        print("\n\nYOU DIED.")
                                        sys.exit()

                                    elif aaca.lower() == "wonder": # THIS IS A SECRET OPTION!!!
                                        print("After a brief moment of pondering, something clicks. \"I must be dreaming!\" you shout, \"And if I'm dreaming...\"")
                                        print("You snap your fingers, and a second large dragon comes and hovers between you and Ahlakhaz.")
                                        print("Finding unreasonable strength in your legs, you jump onto its back. Immediately, Ahlakhaz dashes away")
                                        print("toward a tall, crooked mountain peak far off to your right. Seizing your opportunity to further ensure your safety,")
                                        print("you charge after them. You quickly catch up and are soon flying directly adjacent to Ahlakhaz and the monster.")
                                        print("They both seem now to be unconcerned by your appearance. Instead, you notice they are enjoying themselves.")
                                        print("Your adrenaline recedes as your curiosity increases. \"Are they... having fun?\" You hold back slightly to put")
                                        print("more distance between you and them. They couldn't possibly still be trying to get away, with all the tricks")
                                        print("they were doing in the air. The beautiful nature of this world finally starts to feel safe and enjoyable.")
                                        print("You're glad you didn't attack either of these creatures. The dream dissolves and you wake up.")

                                        print("\n\n\"What a fantastic dream!\" you say, ready for a new day.")
                                        sys.exit()

                                    else: # ROCKS, STARE, WONDER
                                        print("Invalid input.")
                                        continue
                            
                            elif aac.lower() == "ride":
                                print("Spotting a safe path to run up the steep hill to your right, you take off and begin climbing, almost with boundless energy.")
                                print("Having reached the top astonishingly quickly, you recklessly jump straight off the peak toward the dragon.")
                                print("You catch hold of his wing as it moves back upward, and manage to cling to it despite its incredible speed.")
                                print("You spot a large saddle strapped to the dragon's neck, and without hesitation you clamor towards it.")
                                print("Instinctively, the dragon begins to move, flying away from the lake as fast as it can. But you reached the saddle faster.")
                                print("Unsure how to control the dragon, you decide to simply see where it will take you. You feel pure euphoria as the chilly wind")
                                print("rushes under your arms and through your hair. The scenery is absolutely gorgeous.")

                                print("\n\nYou have found your true calling, Dragonrider.")
                                sys.exit()

                            else:
                                print("Invalid input.")
                                continue
                    
                    else: # FIGHT, FOREST, LAKE
                        print("Invalid input.")
                        continue
            
            elif a.lower() == "silent":
                print("Although you are scared out of your mind, you let nary a peep escape your mouth.")
                print("You hear a noise not too far off. Perhaps this is the noise that woke you up.")
                print()

                while True:
                    ab = input("Do you RUN from the noise or INVESTIGATE it? >> ")
                    print()

                    if ab.lower() == "run":
                        print("You run off into the forest, and after several minutes of wandering, you encounter a hill.")
                        print("You climb it for a while, and find shelter in a shallow cave. You feel very tired and carelessly drift off into sleep.")
                        print("\"The end,\" Grandpa says, closing the story book. \"That was kind of a disappointing story, grandpa,\" you admit frankly.")
                        print("His eyes full of love and wisdom, he candidly smiles. \"Have you ever considered writing your own?\"")
                        print("He pats you on the shoulder, wishes you a good night, and switches off the lights as he exits the room. All you can do is stare at the ceiling.")

                        print("\n\n\"Write my own story?\"")
                        sys.exit()

                    elif ab.lower() == "investigate":
                        print("Carefully, you make your way around the base of the tall bank.")
                        print("On the other side, you spot a large creature with gargantuan hands. Light is emanating from him")
                        print("and he is mumbling incoherently, but rhythmically.")
                        print()

                        while True:
                            abb = input("Do you RUN or LISTEN? >> ")
                            print()

                            if abb.lower() == "run":
                                print("You practically fly off in the opposite direction as far as the woods will take you.")
                                print("Suddenly, the trees give way, and you sharply inhale. There's a massive cliff in front of you now.")
                                print("You feel somewhat safe, confident you ran a good distance, so you walk farther out, curious to look down into the chasm.")
                                print("You find a portion of the cliff face jutting out, and walk across it. But before you can get")
                                print("a good look at the expanse below, a bolt of energy strikes the rock platform behind you,")
                                print("causing a rumbling that sends a spike of fear straight through your heart. The rock begins to be")
                                print("extremely unstable. In fact, it is definitely falling.")
                                print()

                                while True:
                                    abba = input("Do you JUMP into the chasm, or RETREAT to the forest? >> ")
                                    print()

                                    if abba.lower() == "jump":
                                        print("Foolishly, you jump into the chasm. Now you've got a perfect view of what's down there.")
                                        print("What luck! A river! You pray it is deep enough to break your fall. You take a minute")
                                        print("to figure out a proper diving position given the circumstances. Several minutes pass.")
                                        print("You start to wonder if you'll ever reach the bottom. It feels like an hour has passed now.")
                                        print("It dawns on you: this is nothing more than a bottomless pit. And you're right.")

                                        print("\n\nGAME OVER")
                                        sys.exit()

                                    elif abba.lower() == "retreat":
                                        print("Your feet miraculously carry you back to the forest. You watch as the rock you once stood on")
                                        print("finally breaks loose of the cliff face and quickly disappears from view. You have no desire to look down after it.")
                                        print("You return your gaze to the forest, but your gaze is met by at least twenty large creatures,")
                                        print("exactly resembling the one performing magic back at the lake. Characteristically, they stand still and silent")
                                        print("for far too long, giving you plenty of time to make a run for it. But it's no use. They are faster")
                                        print("than they appear. They capture you and take you back to their den. After a laborious process spanning over")
                                        print("several years, they have transformed you into one of them.")

                                        print("\n\nGAME OVER")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
                            
                            elif abb.lower() == "listen":
                                print("You put your ear into the air, hoping to get a better sonic appreciation of the situation. Carefully, you move in closer.")
                                print("Each stride makes the chanting louder and only makes you more curious.")
                                print("An unexpected leaf finds it way underneath your next step, and makes a loud crunching sound.")
                                print("To your horror, the creature stops mumbling and turns around. Before you can think to escape, he spots you.")
                                print("You expect him to swiftly end you, but instead you hear his soft voice over the night breeze.")
                                print("\"Come,\" he beckons.")
                                print()

                                while True:
                                    abbb = input("Do you GO or RUN? >> ")
                                    print()

                                    if abbb.lower() == "go":
                                        print("More leaves crunch as you make careful steps toward the wizard creature. You can't tell if you feel safe or in danger.")
                                        print("You stop ten paces from where he stands. He must be terribly patient if he was able to endure your painfully slow movement.")
                                        print("Seemingly understanding of your unwillingness to come closer, he takes three long steps and is suddenly right in front of you.")
                                        print("He lowers his arm to place his hand gently on your shoulder. He draws in a great big breath and begins to speak.")
                                        print("\"Your destiny is to wield the power I now hold.\" After a long, awkward pause, he removes his hand and turns to face the hill adjacent him.")
                                        print("With one dramatic upward swoop of his hands, large fractures form at the base of the hill, sending violent shock waves through the air")
                                        print("and nearly causing you to soil your pants. The entire hill is now weightlessly floating just a few feet above where it once stood.")
                                        print("\"Some need to be broken,\" he says, agitation trembling in his voice.")
                                        print("He puts his arms down, and the mount lowers in tandem, dropping back to where it was before, large, uneven seams still visible.")
                                        print("He stares at what he has done for a moment, and eventually speaks up again, this time much calmer. He gently lifts his hands")
                                        print("and moves them in a careful swirling motion in front of him. \"Others... need to be healed.\"")
                                        print("Shimmering strands of angelic light begin to grow and maneuver around the rough edges of the broken base of the hill.")
                                        print("Within seconds, the entire thing looks as if it was never disturbed. It is completely restored.")
                                        print("\n\"Take my blessing with you. There are many who ache to see a brighter day.\" He turns away from you and faces the lake.")
                                        print("He says, \"I'm counting on you to end the human race.\"")
                                        print("The statement barely registers in your brain before he swiftly turns around and whips his arm upward.")
                                        print("An unknown force launches you hard and fast, sending you off into space. You feel a rush of power enter your being.")
                                        print("\"Is this the power he was talking about?\" you wonder aloud. \"I... I think I can feel it!\"")
                                        print("You are far outside the atmosphere of that strange planet. You feel the air start to disappear.")
                                        print("The wizard forgot to protect you from the lack of oxygen you would soon experience. You promptly asphyxiate.")

                                        print("\n\nYOU DIED")
                                        sys.exit()

                                    elif abbb.lower() == "run":
                                        print("In an instant, you feel the cold autumn air whipping past you as you vacate the premises.")
                                        print("As you run, you feel strength fill your legs and arms. You feel you could keep running, forever.")
                                        print("Suddenly, a booming voice hits your ears. You keep running, quite exhilarated. The voice speaks your name.")
                                        print("\"Joshua. You must learn that you cannot outrun your destiny.\" The voice echoes in your mind")
                                        print("as if it had uttered the cryptic phrase a thousand times. As your speed increases, the world around you begins to dissolve.")
                                        print("You feel the ground disappear from beneath your feet. You slow to a halt, unable to move.")
                                        print("You remain floating in the air. You are surrounded by thick blackness, punctured by a mosaic of scattered stars.")
                                        print("\nYou wake up in a cold sweat, breathing heavily. The familiar sight of your bedroom floods your senses")
                                        print("and you find yourself beginning to calm down.")
                                        print("You look over to your nightstand and spot a picture of a familiar girl on a familiar flight of stairs.")
                                        print("You breathe a loud sigh of relief and lay back down, smiling. It's still there.")
                                        print("\"Maybe I can't outrun my destiny,\" you say to yourself,")
                                        print("\"But maybe I can let my destiny outrun me!\"")

                                        print("\n\nTHE END")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
    





###########################################################################################################################################
#########################################################          SLEEP          #########################################################
###########################################################################################################################################

    elif z.lower() == "sleep":
        print("\"Can\'t a guy get some shut-eye around here?\" you mutter to yourself.")
        print("Disgruntled, you stretch, exhale, and feel much more relaxed now as you drift off back to sleep.")
        print("Before you float too far down dream river, the same sound returns. You flinch and wake up again, irritated.")
        print()

        while True:
            b = input("Do you SEARCH for the source of the noise, or go back to SLEEP? >> ")
            print()

            if b.lower() == "search":
                print("You decide to gain a higher vantage point to discover the annoyance.")
                print("With one powerful downward swoop of your wings, you leap up to the top of the cliff beside you.")
                print("Casting your eyes about, you quickly realize that the forest looks like it's infested with red and purple flames.")
                print("\"Oh no...\" you say to yourself. Garganza the Demon Lord and his armies have you surrounded.")
                print("You curse yourself for having so foolishly taken a nap in such an obvious place with little to protect yourself.")
                print("They look like they have a plan and are about ready to execute it. In any case, they know you're here,")
                print("and they can track you.")
                print()

                while True:
                    ba = input("Do you ATTACK or NEGOTIATE? >> ")
                    print()

                    if ba.lower() == "attack":
                        while True:
                            baa = input("Attack with KNIVES or with WATER? >> ")
                            print()

                            if baa.lower() == "knives":
                                print("Without missing a beat, you reach for the knives in your holsters and prepare to duplicate them.")
                                print("\n.-* You are now Garganza, Chief Lord of the Demons. *-.\n")
                                print("You've finally located him. \"What a fool!\" you whisper, a triumphant grin forming on your devilish face.")
                                print("\"He knows he's surrounded. Perhaps this time we will come off victorious.\"")
                                print()

                                while True:
                                    baaa = input("Do you, Garganza, Chief Lord of all Demons, CHARGE immediately or WAIT a moment first?")
                                    print()

                                    if baaa.lower() == "charge":
                                        print("You take in a deep breath, and the words erupt from your lips as magma from a hellish volcano,")
                                        print("\"CHAAARGE!!\"")
                                        print("Immediately, fifty knives pour into your chest like a stream of frozen death.")
                                        print("You let out a fiery screech. You hear a similar sound echoing around you. Your captains...")
                                        print("You feel the power of your army draining as your own life force dwindles. A horrid, dreadful")
                                        print("pang of failure strikes your empty heart. \"Superna... You must... forgive me...\"")
                                        print("A vivid image prints onto the back of your closing eyelids.")
                                        print("\"THERE IS NO FORGIVENESS FOR A FAILURE OF THIS ORDER. THAT WAS THE DEAL.\"")
                                        print("You are on the ground now, the fire in your bones shooting out and leaving you but a pile of old bones.")
                                        
                                        print("\nYOU DIED")
                                        sys.exit()
                                    
                                    elif baaa.lower() == "wait":
                                        print("\"What is he doing...?\" you wonder aloud, gazing up at your winged prey.")
                                        print("Suddenly, a gleam of reflected moonlight hits your eye. Something is flying directly towards you.")
                                        print("You yell out and put up your shield, indicating to the others to follow suit.")
                                        print("Just as the shield rises to cover your face, something strikes it repeatedly and with great force.")
                                        print("You see small holes appearing in the impenetrable material. \"Impossible...\" you think, eyes wide with surprise.")
                                        print("A new idea ignites your adrenaline. Sensing the pounding has stopped, you quickly reach for the front")
                                        print("of your shield and begin pulling the knives out. As you touch each one, you feel its magic")
                                        print("enter your being. What once was connected to your foe is now yours.")
                                        print("\"THANKS, COMRADE!!\" you taunt. Joshua is not moving. Your entire army now wields the weapon used against you.")
                                        print("With precision, you lift your arm and hurl the weapon back toward its sender. Your soldiers do the same.")
                                        print("A flurry of magical knives hone in on their target. You see Joshua lift his arms, and the lake rises,")
                                        print("seemingly at his command. \"Who is this man?\" But before you ponder long, the knives reach their destination.")
                                        print("Whatever Joshua was attempting failed horrendously. Lifeless, he falls to the lake.")
                                        print("The lake ceases glowing. It seems there is no more life here. Master will be quite pleased.")

                                        print("\nYOU WIN")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
                            
                            elif baa.lower() == "water":
                                print("You feel the water beneath you is ready to be utilized. Now positioned in the air above the lake, flapping to stay up,")
                                print("you lift your arms upward, and the crashing waves begin ascending to meet you in the air.")
                                print("You hear the noise of a great army charging and the flames close in on you. Within seconds,")
                                print("you are enclosed in a bubble of air, shielded by a thick barrier of water.")
                                print("Seizing your opportunity, you begin twisting the water around you. It moves increasingly quickly")
                                print("until a raging tornado now shakes the air with a thunderous, watery voice. You see bones flying past you now.")
                                print("The intensity of the swirling blue lake water only grows as more and more dismembered demons swim helplessly around you.")
                                print()

                                # There was a while True statement here, but I realized we don't need it!
                                baab = input("It is time. Shout the victory cry and put this pathetic army to shame. >> ")
                                baab = baab.replace("!","") # Removes exclamation marks. I will handle the punctuation, thank you very much!
                                print()

                                if baab.lower() == "reach":
                                    print("All the air in your tornado's heart draws into your lungs. For a moment, everything is calm.")
                                    print("You can sense him. He is flying directly toward you. You reach out your hand and grab hold")
                                    print("of none other than Garganza himself. The deafening cry of the storm reaches neither of you.")
                                    print("\"Send my greetings to Superna,\" you say to him, his face now flushed with rage.")
                                    print("The lake is empty. Now is the perfect time. You throw Garganza straight down toward the dry lakebed.")
                                    print("As expected, you hear not the clatter of bones, but the sound of the portal closing far beneath you,")
                                    print("evidently having swallowed your new most recent success.")
                                    print("\"That should send an unquestionable message,\" you say to yourself, highly satisfied.")

                                    print("\nYOU WIN")
                                    sys.exit()
                                    
                                else:
                                    print("All the air in your tornado's heart draws into your lungs. For a moment, everything is calm.")
                                    print("Then, with a voice like a mountain splitting asunder, you let loose the cry of victory in the tongue of the ancients:")
                                    print(f"\"{baab.upper()}!!!\"")
                                    print("The sound penetrates the thrashing of the tornado and echoes across all of Katosa. You hear the ancients")
                                    print(f"return the same cry back to you: \"{baab.upper()}!!! {baab.upper()}!!!!\"")
                                    print("It fills your heart with burning pride. With an evil grin, you thrust your hand upward as if heaving a heavy object at the moon.")
                                    print("The tornado flies upward at your gesture, dissipating into the air and strewing a massive cloud of bones in all directions.")
                                    print(f"\"{baab.title()}. You weaklings.\"")

                                    print("\nYOU WIN")
                                    sys.exit()

                            else:
                                print("Invalid input.")
                                continue
                    
                    elif ba.lower() == "negotiate":
                        print("Magically amplifying your voice, you speak up. \"I AM WILLING TO NEGOTIATE!!\" you say, calmly.")
                        print("The demonic army is not moving. Perhaps they will be willing as well.")

                        while True:
                            bab = input("Play INNOCENT or COCKY? >> ")
                            print()

                            if bab.lower() == "innocent":
                                print("You make the first move. \"What do you want of me?\" Your tempered voice causes the trees to sway.")
                                print("After a moment, you hear a voice emanating from a large, flaming skeleton. Garganza.")
                                print("\"YOU KNOW WHAT WE WANT!!\" His anger is followed by a loud cheer from the army.")
                                print("You need to think.")

                                while True:
                                    baba = input("Do you continue to play INNOCENT, or do you FLEE? >> ")
                                    print()

                                    if baba.lower() == "innocent":
                                        print("\"I\'m afraid I don't, my good sir,\" you lie. You hear an avalanche off in the distance.")
                                        print("With tenacity, Garganza responds, \"THEN LET US REMIND YOU!!!\"")
                                        print("The army begins screaming again, and it resounds and clatters in the cavity of your skull.")
                                        print("You try to flee, but you hear a voice echoing from an unknown source,")
                                        print("\"FIVE MOVES...\"")
                                        print("You feel your strength draining. Now in a panic, you look for somewhere to hide.")
                                        print("It's no use. Your energy is feeling too rapidly. You plummet straight down toward the lake surface.")
                                        print("The glow of the water shifts from its royal blue to a neutral white. Quickly, hundres of demonic")
                                        print("arms and feet enter the shallow lake, and the white turns to a ghastly purple and red. You begin to sink.")
                                        print("You feel your wings dissolving. Alarmed but listless, you cannot speak a word of surprise.")
                                        print("You are now bound to Katosa Lake for eternity, though it is yours no longer. The water burns.")

                                        print("\nGAME OVER")

                                    elif baba.lower() == "flee":
                                        print("Though he's far away, you stare straight into what are probably Garganza's eyes.")
                                        print("\"And I know...\" you retort, your earth-shaking voice like fierce wind,")
                                        print("\"...that you shall never obtain it!\"")
                                        print("You let out a loud, melodic screech that could curdle the demon army's blood if they had any.")
                                        print("A loud whooshing sound soon follows. A large, rocky, humanoid creature is barreling straight for you in mid-air.")
                                        print("It opens its arms wide. You brace for impact. Without even the slightest thud, it gracefully")
                                        print("grabs hold of you and glides straight over the soldiers' heads. Despite a rough landing, the two of you")
                                        print("manage to outrun the streaks of purple flame behind you.")
                                        print("You're safe, for now. Maybe you can finally get some sleep.")

                                        print("\nBut are you missing something?")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
                            
                            elif bab.lower() == "cocky":
                                print("You speak first. \"You cannot obtain what you seek, you know.\"")
                                print("Garganza's hoarse, hellish voice echoes back, \"NOT IF YOU KEEP INTERFERING, BOY!!\"")
                                print("You detect a hint of shame behind Garganza's arrogance. You wonder if that was fabricated or sincere.")
                                print("Either way, you recognize that this army is made of puppets, being controlled by something they don't understand.")
                                print("Though previously you may have desired to wipe them out and ensure your safety,")
                                print("you're not so sure you want to fight anymore. It might yield nothing but dismembered bones")
                                print("and wasted energy.")
                                print()

                                while True:
                                    babb = input("Do you FIGHT anyway, or RELENT? >> ")
                                    print()

                                    if babb.lower() == "fight":
                                        print("You could run, but you would eventually have to fight them anyway. You decide to fight them now.")
                                        print("Thinking quickly, the only option you have is to take out the leaders and gain control of the soldiers.")
                                        print("You must keep up the negotiation act for just a few seconds while you draw power from the lake.")
                                        print("Discretely, you lift your hands in front of you, and use one to trace a circle in the air around the other.")
                                        print("Now is the time to speak. \"I must interfere...\" you begin.")
                                        print("Blades of water stretch forth like tentacles from the surface of the lake toward the shore.")
                                        print("Their points could cut straight through rock. You hear the army start to get antsy.")
                                        print("You pause and hold everything still. Your spirit exits your body and descends to the shore as if down a flight of stairs.")
                                        print("Your projection strides up to Garganza and looks straight into his rage-filled eyes.")
                                        print("\"...or you will never learn your lesson.\"")
                                        print("Your apparition vanishes. The army lets out a cry of excitement and charges.")
                                        print("Thrusting your arms outward, the waters slither through the air and pierce the hearts of the army leaders.")
                                        print("The waters explode and send sharp, liquid spears through every captain and officer you can see.")
                                        print("They all fall to the ground, leaving nothing but scattered bones on the forest floor,")
                                        print("no more magic to hold them together. Though powerless, the soldiers continue their charge")
                                        print("and make their way into the glowing lake. They converge to the center, forming a mass tower")
                                        print("out of their own skeletal bodies just to reach your height. You see the final one step in.")
                                        print("There are thousands of them clamoring atop each other now.")
                                        print("You snap your fingers and send a ball of burning stardust straight through the lake's surface.")
                                        print("Instantly, the lake appears to have caught fire. The soldier's bones dissolve, leaving only their dark matter souls.")
                                        print("The water loses its sapphire shimmer and turns a condemning shade of red.")
                                        print("It worked. These souls will be bound to Katosa Lake as long as time shall stand.")
                                        print("Victorious, but alone, you wander off into the forest, eventually losing your strength entirely")
                                        print("and collapsing. Right as your head hits the hard, alien soil, you wake up somewhere else.")
                                        print("Panicked, you realize where you are and quickly calm down.")
                                        print("Your friend Jeff rushes over to you and puts his hand on your shoulder.")
                                        print("\"Josh! What happened?\" he asks, clearly alarmed yet maintaining a calm, smooth tone.")
                                        print("\"This is one point for Superna. They got the lake. I had no choice.\"")

                                        print("\nOr did you?")
                                        sys.exit()

                                    elif babb.lower() == "relent":
                                        print("Voice still deafeningly loud, you respond.")
                                        print("\"Then I shall step out of the way.\"")
                                        print("You stop flapping your wings and plunge through the lake's surface. You have entirely vanished from sight.")
                                        print("The glow of the lake's waters slowly lifts from the rocks and sand beneath, and floats toward you")
                                        print("like a cloud of shimmering dust. It meets you, sits for a second, and then shoots across to the shore")
                                        print("and collides with the land with a loud boom. Slowly, it starts seeping through the soil,")
                                        print("sending beams of light through the cracks. It stops at the feet of Garganza, looking surprised but satisfied,")
                                        print("and spits out a dark blue crystal, which floats in the air as Garganza stares into it.")
                                        print("\"What do you see?\" one of the captains asks him.")
                                        print("Garganza continues staring, faking a studious squint, then turns to him and laughs.")
                                        print("\"I see a foolish boy who just gave me the power to make this world our own!\"")
                                        print("The entire army laughs with him as he callously snatches the crystal from the air and walks off, cackling with pride.")
                                        print("Little does he know you have made your way inside the very crystal he holds.")
                                        print("Before long, you should have enough information on this group to slowly bring them to their demise.")

                                        print("\nYOU WIN")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue
                            
                            else:
                                print("Invalid input.")
                                continue

                    else:
                        print("Invalid input.")
                        continue

            elif b.lower() == "sleep": # second sleep
                print("Trying your hardest to let your frustration simply leave you, you hurry back to sleep.")
                print("You hear the same noise as before, waking you up a third time.")
                print()

                while True:
                    bb = input("Do you INVESTIGATE, RUN, or go back to SLEEP again? >> ")
                    print()

                    if bb.lower() == "investigate":
                        print("You get up, stretch once more, and take a look around. In scanning the other side of the lake,")
                        print("you notice something gleaming in the moonlight. It's shiny! Could it be treasure? You need to get over there.")
                        print()

                        while True:
                            bba = input("Do you WALK across, or SWIM across? >> ")
                            print()

                            if bba.lower() == "walk":
                                print("Feeling like taking a nice moonlit stroll along the beach, you decide to make your way over on foot.")
                                print("You reach the place you scoped out, but find nothing shiny whatsoever. Confused, you look around")
                                print("and spot someting on the side of the lake where you were sleeping earlier. \"What the...?\"")
                                print("It has the same gleam that you spotted before. It looks to be the same object. The same treasure!")
                                print("Confused but complacent, you stroll back over to your resting place, a walk of several minutes.")
                                print("You've arrived back where you started, and the treasure is gone. You dare a glance back over")
                                print("to the other side, and a familiar glimmer catches your eye. Feeling disoriented, you sit down, fingers pressed to your temples.")
                                print("After a moment, you decide to walk back over, but you go along the bank opposite from before, keeping your eye")
                                print("on the coveted shiny object. You arrive but, as expected, the treasure has vanished again.")
                                print("Your uneasiness and confusion drains your energy completely, and you feel an alien force")
                                print("slip your strength away from you completely. You collapse, completely lifeless.")

                                print("\nYOU DIED")
                                sys.exit()

                            elif bba.lower() == "swim":
                                print("You're dying to get into the water anyway. You swim straight across and climb out on the other shore.")
                                print("Now that you have a better look at the thing, you discover it is in fact a treasure chest!")
                                print("Looks like you could open it with relative ease.")

                                while True:
                                    bbab = input("Do you SEARCH it now, or CHECK to see if the coast is clear?")
                                    print()

                                    if bbab.lower() == "search":
                                        print("You lift the heavy lid to reveal the treasure inside.")
                                        print("You see a mirror. Four words come suddenly, ringing loudly in your ears:")
                                        print("\"Y O U   A R E   T H E   T R E A S U R E .\"")
                                        print("\"Oh, that's nice of you!\" you say, reaching into your pack.")
                                        print("You pull out a metallic sphere, twist it in half, and toss it into the lake.")
                                        print("As you run away, you hear the expected explosion. It's louder than you remember.")
                                        print("That or you are a much slower runner than you thought.")

                                        print("\nYOU WIN ...?")
                                        sys.exit()

                                    elif bbab.lower() == "check":
                                        print("Before being foolishly lured into what could easily be a simple trap,")
                                        print("you decide to pace around the area, checking for signs of life.")
                                        print("You're about to return to the treasure and claim your prize, but you decide")
                                        print("to turn one last corner behind a large rock. Your eyes almost fly out of their sockets.")
                                        print("Standing before you is a ginormous butterfly. It speaks.")
                                        print("\"AAAAAAAAAAAAAAAAAAAAAAAAA,\" it says, looking bugged.")
                                        print("You scramble to get away, but it buzzes over to you and grabs you with its... butterfly... claws?")
                                        print("It carries you away, lifting you over a mountain and revealing to your tired eyes")
                                        print("a hidden valley of surprising beauty. You've definitely never seen this part of the country before!")
                                        print("Your head is filled with music as you gaze upon the landscape, starstruck and inspired.")
                                        print("The monster drops you and you plummet to your death.")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            else:
                                print("Invalid input.")
                                continue

                    elif bb.lower() == "run":
                        print("You turn around to get out of there before something bad happens,")
                        print("but you see a sword on the ground twenty feet in front of you and stop.")
                        print("\"Uhh... Well,\" you ponder, \"so that's there... Okay. Umm...\" you say, stunned. \"Yeah. So, like...\"")
                        print("Interrupting your musing, the sword begins to shake increasingly violently.")
                        print("\"Huh,\" you continue. \"Let's see then, hmm... now it's shaking. I think that-- no... Or maybe-- Well, probably not...\"")
                        print("You hear a scuffle taking place in the forest. It sounds like two adventurers are fighting and yelling.")
                        print("You look up but see no one. Hopefully they will finish each other off before they get too close.")
                        print("The sword is having a real conniption now. It might flail up and strike you.")
                        print()

                        while True:
                            bbb = input("Do you TAKE the sword, continue to OBSERVE, or RUN away? >> ")
                            print()

                            if bbb.lower() == "take":
                                print("You stare at the sword, waiting for a moment to take it by the hilt like nature intended.")
                                print("The sword flings up, crashes back down, and rests. You might only have a split second.")
                                print("You dive and successfully grab the sword. It starts to shake again, but this time you can feel it.")
                                print("The hilt explodes, leaving ashes of everything within two hundred feet. Yet you stand, holding tight.")
                                print("The sword is still shaking, though not trying to free itself. You can't help but stare at the blade.")
                                print("It's definitely reflecting more light than is coming from the moon. This might be the end for you.")
                                print("Your fondest memories flick past your eyes, alarmingly carelessly. A single tear drops down your cheek.")
                                print("The blade opens and reveals a single eye. It is staring right at you and seems to be speaking.")
                                print("\"Si tu veux, dis le mot et mets fin à cette tyrannie! DIS LE MOT!!\"")
                                print("Before you catch a moment to attempt to understand the voice, a blinding sphere of light")
                                print("emerges from the center of the eye and entirely engulfs you.")
                                print("The light disappears. You are now the sword.")
                                print()

                                bbba = input(">> ")

                                if ("what","happened","why","who") in bbba.lower():
                                    print("Oh right, sorry.\n\nGAME OVER.")
                                    print("\n...but I mean, you couldn't have figured that out yourself?")
                                    sys.exit()

                                elif bbba.lower() == "break":
                                    print("You are not entirely gone, however. There remains just enough of you in this world for one more move.")
                                    print("You channel all of what you have left, everything you ever lived for and hoped to see again,")
                                    print("and you release it all from within the sword, shattering it to pieces")
                                    print("and sending a terrible, metallic shriek into the night air.")
                                    print("You did it. The reign of tyranny is over.")
                                    print("\n\"That was sick, man! You totally destroyed my most clever monster with only five moves from the lake!\"")
                                    print("\"Well,\" you say humbly, \"I couldn't have done it without her...\" you absent-mindedly tap the board,")
                                    print("chin resting in your left palm. John gives you a bewildered stare for a second, then seems to connect the dots.")
                                    print("\"Oh, you mean without your Dark Charger Elf?\" You look up at him as if arising from a deep slumber.")
                                    print("\"Huh? Oh... yeah, my Charger.\" You scratch the back of your neck, pretending to pay attention. \"Yeah,")
                                    print("would have been wrecked without the... Charger.\"")
                                    print("Though suspicious of it, John seems to let your odd behavior slide. He's invested in the game, anyway.")
                                    print("He continues, \"No one's ever bested my Steel Trap in the Five-Move Frenzy. I'm impressed, Josh. Let's check out your loot.\"")
                                    print("\"I wish she were here,\" you mumble.")
                                    print("John stops rolling the die. \"Okay, you can tell me. What's going on, man?\"")

                                    print("\n\"Oh, nothing.\" You're smiling like an idiot.")
                                    sys.exit()

                                else:
                                    sys.exit()

                            elif bbb.lower() == "observe":
                                print("You take a few steps back and continue to observe the sword. You can still hear the adventurers fighting in the woods.")
                                print("After a moment, it suddenly stops, and is now hovering five feet above the ground. It is pointing straight downward.")
                                print("The sword isn't moving. You wonder what would happen if you grabbed it. You take a few steps toward it.")
                                print("The sword shoots down and sticks straight into the rocky ground. The sudden sound frightens you, and you fall over.")
                                print("Astonishingly, the ground begins to rumble, and a stone formation begins to rise up where the sword stuck.")
                                print("It is clearly some sort of pedestal that holds the sword. Just as it starts rising, the yelling draws near")
                                print("and a man dressed in ridiculous yellow clothing comes striding out of the woods, walking forward but looking behind him.")
                                print("\"Look, Darche, I am exactly the right person to make this happen. Think of it! I'll just do the thing, do the other thing, and we'll be rich!\"")
                                print("\"You're nuts, Pel! I'm telling you, neither of us know what we're up against!\"")
                                print("\"Pel\" is walking toward the sword, probably intent on retrieving it. The sword is YOUR destiny,")
                                print("not that of this \"Pel\" character!")
                                print()

                                while True:
                                    bbbb = input("GRAB the sword. >> ")
                                    print()

                                    if ("grab","take","yes","y","ye","yeah") in bbbb.lower():
                                        print("You place your hands carefully around the hilt of the coveted sword. You lift upward,")
                                        print("but it doesn't budge. You try to pull again, harder this time. Not even a particle of dirt is disturbed.")
                                        print("It feels like the sword has become part of the stone, permanently.")
                                        print("\"Pel\" is now standing on the other side of the pedestal, staring greedily at the sword.")
                                        print("\"I've got you now!\" he says, smacking his lips and rubbing his hands together.")
                                        print("\"Pel! Pel! What are you doing? Aren't you listening to me? You'll die if you touch it! Grandmother said--\"")
                                        print("\"Oh, nuts to her! How will she ever find out about this? The whole village would love to just forget all about us, anyway!\"")
                                        print("Pel continues, \"Look, it's as easy as one, two, three. One! Left, right, up, down! Right, left, down, up!\"")
                                        print("Pel has begun dancing. You can't help but giggle, amazed how he seems to be completely ignoring you.")
                                        print("\"Two! Sing a little song, lalala! Okay, that's done... Three! Offer up an honest, well-to-do heart, yada yada...\"")
                                        print("Pel reaches for the sword and slides it cleanly out of its pedestal. You're gawking. He now looks at you and glares maliciously.")
                                        print("Sword in hand, he slices you across the chest from across the pedestal. He left a very deep cut.")
                                        print("The blow kills you instantly.")
                                        print("\"...I can't believe it.\" Pel turns to face Darche, clearly confused on whether to smile or be utterly disgusted.")
                                        print("\"You actually got it out... The actual Sword of Katosa... Wielded by Lady Jessica herself...\"")
                                        print("\"Is that really what the Scoatica Verse meant by \'an heart, honest and well-to-do\'?\"")
                                        print("Realizing something, Darche points at your lifeless body and looks up at Pel.")
                                        print("\"And what were you planning to do if this considerate lad hadn't come along?!\"")
                                        print("\"Oh, I don't know, maybe shown you around the place, introduced you to a few nice gals, got you something to drink? I'm a courteous man, Darche!\"")
                                        print("\"Come on,\" Pel continues. \"Let's go get rich!\"")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    else:
                                        print("So, you have decided to let your destiny outrun you, have you?")
                                        print("I don't care how many dimensions you cross to get me. You will never find me.")
                                        print("But I have found you. And you will never escape.")
                                        print("                                                      - S")
                                        sys.exit()

                            elif bbb.lower() == "run":
                                print("You turn to make a break for it. This thing is NOT going to kill you. That is a LAME way to go.")
                                print("Before you can put any real distance between it and yourself, it starts flying straight toward you.")
                                print()

                                while True:
                                    bbbc = input("Do you DUCK, or GRAB? >> ")
                                    print()

                                    if bbbc.lower() == "duck":
                                        print("You wait until the last possible moment, which only takes half a second, and you duck.")
                                        print("You're lying flat on the ground now. You hear the sword stick into something behind you.")
                                        print("Everything is quiet. You roll over to steal a glance at what the sword stuck into.")
                                        print("To your great dismay, there is a tall, slender, fiery being standing over you, with the sword stuck firmly in his chest.")
                                        print("He speaks, though you know now from whence the voice comes. \"Look at you, lying there! I knew you were a lyer!")
                                        print("But one would assume otherwise, judging by how well-grounded you initially appear!\"")
                                        print("Bewildered and incredibly alarmed, you reach for the sword and pull it out of him.")
                                        print("\"HEY!!\" The thing has stopped being... punny, and is now beside itself with anger.")
                                        print("He starts running at you, screaming. \"GIVE THAT BACK!!\" You just might have the advantage, however.")
                                        print("He takes a swing at your head. You duck and slice his magma legs clean off, sending him tumbling down.")
                                        print("\"YOU CAN'T DO THAT! THAT'S NOT FAIR! I'M LITERALLY MADE OF VOLCANO JUICE!!\"")
                                        print("\"Okay, who on earth brought this guy here?\" you think to yourself before realizing something important.")
                                        print("\"Right. Nobody, I guess.\"")
                                        print("The fire man rolls over and looks up at you. This situation seems familiar.")
                                        print("\"You WILL regret this, foolish human!!\" He rapidly sinks into the ground,")
                                        print("leaving a curved, S-shaped incision in the ground and inspiring a look of disgust on your face.")

                                        print("\"Okay.\"")
                                        print("\nYOU WIN, FOR NOW")
                                        sys.exit()

                                    elif bbbc.lower() == "grab":
                                        print("You wait until the last possible moment, which only takes half a second, and you quickly sidestep,")
                                        print("reach out your hand, and successfully latch onto the hilt of this crazy thing.")
                                        print("As you do, you hear a loud booming sound as a sudden gust of wind dramatically shapes a bowl of dust")
                                        print("with you at its center. Anything nearby had to have heard that.")
                                        print("Sure enough, a parade of different elemental races emerge from their homes to stand before you.")
                                        print("Everything from water people to rock people to cloud people... everyone is now standing in front of you.")
                                        print("One of them, an elderly looking woman, emerges from the crowd, staring you in the eye.")
                                        print("She nods at you, then turns back toward the crowd and proclaims, \"The prophecy... is fulfilled!\"")
                                        print("Loud acclamations fill the air. It's like a symphony of cheer.")
                                        print("The sword, however, seems permanently affixed to your hand. Bummer.")

                                        print("\nYOU WIN")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            else:
                                print("Invalid input.")
                                continue

                    elif bb.lower() == "sleep": # third sleep
                        print("You are determined to get your beauty rest, and fall asleep a third time.")
                        print("You dream a magnificent dream. You're floating down a chocolate river on a graham cracker boat.")
                        print("You have a crazy straw in your hand, which you can use to take sips and slurps from the river at your pleasure.")
                        print("Beautiful birds are flying over you. The marshmallow queen sees you sailing by and says hi. She's pretty hot.")
                        print("You follow the river into a gorgeous autumn forest, brilliant tawny and vermillion leaves breaking the sunlight")
                        print("into shimmering beams that dance on the rich forest floor.")
                        print("Suddenly, you hear a strange sound getting louder. You look up and see a lizard man with a gorilla's head,")
                        print("screaming \"TAH! TAH! TAH! TAH!\" over and over again. Your ears start twitching, and you wake with a start.")
                        print("There's a bird right near your head making that exact noise you heard in the dream. Eyes bloodshot and mood soured,")
                        print("you feel anger bubbling up inside you. All you want is some escape! Can't you just take a nap by a lake?")
                        print()

                        while True:
                            bbc = input("Do you YELL, or go back to SLEEP? Careful, now. >> ")
                            print()

                            if bbc.lower() == "yell":
                                print("Absolutely frustrated, you let off some steam in the form of hoarse yelling.")
                                print("But I mean, not like a horse, you know, like the animal? I mean \'hoarse\' with an \'a\'...")
                                print("\"I get it, okay? I know the word \'hoarse\'! You literally said it earlier, too. You don't need")
                                print("to clarify every little detail whenever there's a slight chance that I might misunderstand you!\"")
                                print("\"Did I say you could speak?! TIGHTEN THOSE BANDS!! A servant pulls on the ropes. They're nearly breaking the skin now.\"")
                                print("\"Anyway... where was I... oh, yes!\"")
                                print("To your surprise, a person with a grand, flowing blue robe emerges from the water.")
                                print("His face is mostly obscured by his garb, but he seems unhappy. Perhaps you awoke him with your fit of hysteria.")
                                print()

                                while True:
                                    bbca = input("Do you APOLOGIZE to him, or do you INTERROGATE him? >> ")
                                    print()

                                    if bbca.lower() == "apologize":
                                        print("You find the words to show you're sincerely sorry for having disturbed him.")
                                        print("But before you can even get them out, you hear a whooshing sound behind you, alarmingly close.")
                                        print("You jump, turn around, and see a group of cloud people, riding their poofy clouds like flying carpets.")
                                        print("Your yell disturbed them, too. One of the cloud men moves up to you, but then looks over your shoulder")
                                        print("and spots the water man behind you. Immediately his focus shifts, and he moves right on past you and says,")
                                        print("\"I thought I told you to never let me see your face around here, water scum.\"")
                                        print("\"Well, I didn't expect to be an encyclopedia tonight, but funny thing about us water scum,")
                                        print("usually where there's water, we kinda live there, so you'll probably find one of us nearby.\"")
                                        print("You haven't turned around. The cloud man starts yelling. You hope you've somehow become invisible.")
                                        print("\"You think you're so funny, huh?! So funny you could just snatch up one of my cloud girls for yourself?")
                                        print("Someone oughta wipe the floors with you. Teach you something about respect!!")
                                        print("You hear the water man retort, \"Respect this, nimbus pants!\" A loud cracking sound splits the air in your ears.")
                                        print("You instinctively turn around, only to find a massive rock falling directly above where you're standing.")
                                        print("With no time to react, you end up crushed.")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    elif bbca.lower() == "interrogate":
                                        print("You pick up a rock by your foot and lug it directly into the water man's face.")
                                        print("You hear the flesh squelch upon impact and almost flinch at the strangeness of the sound.")
                                        print("\"What was that for?!\" he cries. He seems passive-aggressive. You take the upper hand.")
                                        print("\"Don't play dumb with me!\" you shout, walking sternly up to him and grabbing him by the arms.")
                                        print("You pin him against the sheer cliff wall. \"You know something!\"")
                                        print("\"What do you mean I \'know something\'?? Who are you?\" he replies, struggling to get free.")
                                        print("\"I'm the guy you were about to kidnap, aren't I? Well why don't you go ahead and kidnap me?\"")
                                        print("Really struggling now, he confesses. \"I would... if you... would LET... GO!!\"")
                                        print("He breaks free and you engage in a magic duel. \"Ah, so you WOULD kidnap me? Interesting, tell me more!\"")
                                        print("You dodge a bolt of ice. \"You don't have to know anything about me if I kill you first!\" he shoots a frost cloud at you.")
                                        print("You duck beneath it. \"You're new to this then, huh? Normally you AVOID killing your leads!\" You throw another rock, a direct hit.")
                                        print("\"I have--\" he dodged that one. \"...YEARS of experience! I am--\" he shoots two more ice shards. \"...a MASTER of my craft!\"")
                                        print("He continues. \"And you, why not use some of that magic you've got? I can feel it! Stop throwing those stupid-- ouch!\"")
                                        print("He levitates ten large stones and sends them hurtling toward you. You run up to them and ascend them like a staircase.")
                                        print("Now high in the air above him, you summon a magical two-pronged spear, kick him over, and land,")
                                        print("placing the prongs just around his neck and sinking the points into the soil, pinning him to the ground.")
                                        print("\"Use some of that what?\" you taunt, \"Didn't catch that last part. Oh well, not important.\"")
                                        print("You move so that you are standing atop his legs. \"Where is he?!\" you demand.")
                                        print("\"Who? I know lots of \"he\'s\"\". I'm afraid you'll have to specify.\"")
                                        print("Sick of his style of humor, you threateningly sink the points lower, nearing the sharp middle blade to his throat.")
                                        print("\"Do you think I'm looking for a boyfriend? The person you SENT you, of course! Spill or you lose that big, funny brain of yours.\"")
                                        print("Whimpering, he spills the beans.")
                                        
                                        print("\n\"STONES STONES HIDE ATTACK AGREE\"")
                                        print("\"Excellent.\" You free him, and he scampers back into the lake.")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            elif bbc.lower() == "sleep":
                                print("Nothing matters to you anymore except taking this nap here and taking it now!")
                                print("After 30 minutes of unsuccessful snoozing, eventually your nerves calm and your dedication prevails.")
                                print("The hypnogogia dance on the inner side of your eyelids. Mesmerized, you start to dream...")
                                print("You open your eyes, and you're back in your bed. You are right in the middle of a searing hot volcano.")
                                print("\"What a stupid dream!\" you say to yourself, \"I could have done anything,")
                                print("\"but I chose to just sleep? Man!\"")
                                print("Slightly annoyed, you put your hands behind your back in an effort to calm down.")
                                print("You notice a painting high up on the wall is slightly misaligned. You groan at the mundane")
                                print("necessitudes of the waking world.")

                                print("\nTHE END")
                                sys.exit()

                            else:
                                print("Invalid input.")
                                continue

                    else:
                        print("Invalid input.")
                        continue

            else:
                print("Invalid input.")
                continue

    



##########################################################################################################################################
#################################################################################################         STONES         #################
##########################################################################################################################################


    elif z.lower() == "stones":
        print("\"That was a well-needed nap,\" you say, stretching out on the ground.")
        print("You sit up and look across the lake. This is her favorite place to relax and to meditate. You're hoping")
        print("you can find the same solace she always finds here. You're pretty terrible at meditating, though. \"Jessica...\" you ruminate.")
        print("\"What am I supposed to do...\"")
        print("You pick up a stone and instinctively toss it hard toward the lake. That seemed to relieve a bit of stress.")
        print("You stare out after it, still deep in thought. Suddenly, you perk up. The stone traveled all the way across the lake!")
        print("\"What...! But that's not even... Heh??\"")
        print()

        while True:
            c = input("Do you throw more STONES or return to thinking about JESSICA? >> ")
            print()

            if c.lower() == "stones":
                print("Skeptical but curious and excited, you pick up more rocks and start skipping them.")
                print("The first few only get a few skips, but you throw another and, sure enough, it traverses")
                print("the length of the lake, striking the cliff face on the opposite side.")
                print("\"Well this explains why she doesn't like skipping stones with me. Or... wait, does it?\"")
                print("You toss another rock. This time, however, it turns mid-skip and is now making its way over")
                print("to the shore on your left. There is a small hill between you and the stone's target.")
                print("You hear a loud smacking sound, and a monstrous, confused roar follows. \"Oh no...\"")
                print()

                while True:
                    ca = input("That thing's sure to come looking for you. Do you SEARCH your pack or HIDE? >> ")
                    print()

                    if ca.lower() == "search":
                        print("You reach into your pack and feel... a wad of grass? You take it out and sure enough, it's a wad of grass.")
                        print("You recognize the strong scent. \"Pali!\" There's no doubt the monster would love to have some.")
                        print()

                        while True:
                            caa = input("Do you throw the pali into the FOREST, throw it into the LAKE, or EAT it? >> ")
                            print()

                            if caa.lower() == "forest":
                                print("Thinking fast, you hurl the pali over the hill and into the woods.")
                                print("Though sounding desperately confused and angry before, the monster now gives a great, audible sniff, apparently abated.")
                                print("You hear swift footsteps trot away. You clutch your chest and breathe a sigh of relief.")
                                print("You are safe now. The thought calms your nerves. Weren't you doing something earlier?")
                                print("\"Right...\"")
                                print()

                                while True:
                                    caaa = input("Do you REMEMBER or go back to skipping STONES? >> ")
                                    print()

                                    if caaa.lower() == "remember":
                                        print("\"...Jessica.\" You realize you should probably get back to your meditating.")
                                        print("You close your eyes and focus on thinking clearly... but it just isn't working.")
                                        print("For hours you sit there, brow furrowed, trying to avoid giving in to discouragement.")
                                        print("It's no use. \"I just can't even think... Oh, I don't know what to do!\"")
                                        print("You fall backward, now lying flat on the ground, tears welling in your eyes.")
                                        print("You scream, and the intensity of your emotions wakes you up. You're sitting cross-legged on a yoga mat.")
                                        print("\"Did everyone have some lovely dreams? All right, glad to hear it.\"")
                                        print("\"The total for this session will be $134.75. Please pay it as you leave.\"")
                                        print("\"We accept MasterCard. See you next week!\" You really didn't get anything out of that.")
                                        print("You spot Jessica across the room. As much as you'd like to, you couldn't talk to her in your current state.")

                                        print("\nGAME OVER")
                                        sys.exit()

                                    elif caaa.lower() == "stones":
                                        print("\"...I was skipping stones.\" You pick up a rock and give it a good toss.")
                                        print("The important thing is that you really make the movement with your wrist. That's how you guide the stone... probably.")
                                        print("This stone, just like the previous ones, goes far out, nearly to the lake's center.")
                                        print("You stoop to pick up another, searching for a nice, smooth one.")
                                        print("You find one, stand upright, and face the lake. There is a rock directly in front of your face.")
                                        print("The rock you just threw had turned straight back around. It knocks into your head with unreal force.")
                                        
                                        print("\nYOU DIED")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            elif caa.lower() == "lake":
                                print("Unsure what to do, you throw the pali onto the surface of the lake, not too far out.")
                                print("The pained, angry noises of the monster have stopped. You can hear him sniffing loudly.")
                                print("The sound of wind hits your ears, and you see a large creature leaping high into the air, toward the lake.")
                                print("He appears to be a large man made of mossy stone. Apparently he can jump fifty feet high. You're secretly jealous.")
                                print("Looking over at the lake, you see the pali grabbed by an underwater hand and pulled downward.")
                                print("Before you can even process what just happened, the stone beast slams into the calm waters and phases straight through")
                                print("as if surface tension didn't exist. You almost hear what sounds like an... underwater scuffle?")
                                print("Two lifeless bodies float to the surface. One gray and green, one blue. That can't be good.")
                                print("Within seconds, you hear a flurry of heavy footsteps emerging from the forest.")
                                print("A hundred or so similar-looking stone man-beasts emerge and are charging straight for the lake.")
                                print("You're trampled underfoot very quickly. No human could survive that, winged or not!")
                                print("A hundred water people emerge from the bottom of the lake, and the two races engage in an epic battle.")
                                print("Too bad you couldn't live to see who won the war you just started.")

                                print("\nYOU DIED")
                                sys.exit()

                            elif caa.lower() == "eat":
                                print("You've always been curious as to what this stuff tastes like. You shove the entire thing in your mouth.")
                                print("You don't know what you expected. It feels like you're chewing on a big wad of grass.")
                                print("You manage to swallow it, somehow. You feel a new strength surge through your bones.")
                                print("You turn around to the sound of sniffing and see a monstrous stone creature twenty paces away.")
                                print("He's not moving. Maybe he's blind? Or... it's blind?")
                                print("It sniffs a few more times, grunts, and walks briskly toward you.")
                                print("You can't sense any danger about it anymore. It sticks out its hand, palm up, seemingly")
                                print("expecting you to give it something. It stands in silence for a moment. Maybe it wants the pali you ate?")
                                print()

                                while True:
                                    caac = input("Do you FIGHT it, or GIVE it something? >> ")
                                    print()

                                    if caac.lower() == "fight":
                                        print("You take courage in the unnatural strength you still feel within you.")
                                        print("Unsure of whether or not you're actually safe with this thing around, you leap into the air,")
                                        print("and land a kick precisely into the bottom of its chin.")
                                        print("\"OOWW!! HOLY CRAP!!\" you scream, realizing how terrible that idea was. This thing is solid rock.")
                                        print("That seemed to have hurt the golem as much as it hurt you. It falls over backward, hands covering its wounded chin.")
                                        print("It feels like your entire foot is broken. \"What was I thinking??\" you say through gritted teeth.")
                                        print("Quickly, the golem gets back up and rushes toward you. He picks you up and walks straight into the lake.")
                                        print("He leaps up into the air, then slams you into the water.")
                                        print("You are completely out of breath. Not a good time to be underwater.")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    elif caac.lower() == "give":
                                        print("Under the assumption that it wants some of your pali, you try your hand at making some.")
                                        print("How hard could it be? You walk around the area, plucking every blade of grass you can find.")
                                        print("You stroll over to the forest and pick some leaves for good measure. You crumple all your loot up into a ball")
                                        print("and place it proudly into the beast's hand.")
                                        print("\"Thanks,\" the golem says, his voice astonishingly human. He strolls off, contently munching on some delicious pali.")
                                        print("Congrats, chef.")

                                        print("\nYOU WIN")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            else:
                                print("Invalid input.")
                                continue

                    elif ca.lower() == "hide":
                        print("Panicked and unsafe, you leave your pack on the ground and rush into a nearby bush to hide.")
                        print("You're very close to the lake now, and you can hear a strange pulsing sound.")
                        print("You listen harder. Could it be... laughter? You push some leaves out of the way and peer into the water.")
                        print("You see what appears to be a man dressed in a blue robe. He's hunched over, hands on his knees, clearly laughing.")
                        print("You felt your life was about to end. Seeing laughter coming from the apparent cause of your fear angers you.")
                        print()

                        while True:
                            cab = input("Do you ATTACK, or LEAVE? >> ")
                            print()

                            if cab.lower() == "attack":
                                print("You snap a solid, sharp stick off from the bush and get ready to jump into the lake.")
                                print("Suddenly, you feel a hand grab your shoulder rather forcefully. You nearly yelp.")
                                print("You turn your head to see what appears to be a woman made entirely of a homogeny of rocks and dirt.")
                                print("Before you have a change to question who she is or how she found you, her shrill voice speaks,")
                                print("\"Don't be an idiot. You can't breathe underwater. You know that, right?\" You're dumbfounded.")
                                print("\"Why do you care what I know?\" you protest, eager to put an end to the water man's continuous laughter.")
                                print("\"She was right. You are a dunce,\" she says coolly. \"Look. Don't worry about me. You need to leave.\"")
                                print()

                                while True:
                                    caba = input("Do you AGREE or ATTACK anyway? >> ")
                                    print()

                                    if caba.lower() == "agree":
                                        print("Realizing your foolishness in wanting to leave your element to murder someone who didn't actually harm you, you relent.")
                                        print("\"I suppose you're right. But... who are you? And who is this \'she\'?\" She doesn't respond.")
                                        print("Instead, her grip tightens, and she lifts you up out of the bush and throws you hard into the air.")
                                        print("At least a minute has passed, and you're still flying. \"I guess that's why you don't skip arm day,\" you think.")
                                        print("finally, you feel yourself start to pitch downward. You didn't realize the forest was this expansive.")
                                        print("You come across a rocky clearing. Large boulders are scattered everywhere. Seems like a cozy place to live.")
                                        print("You spot an orange speck on the ground. You're headed directly towards it. It grows bigger as you near it.")
                                        print("Before you can figure out what it is, you crash straight into it. He must be made of fire. You now have")
                                        print("a terribly burned face. He is lying on the ground as well, probably unconscious. You grab a stick and poke him,")
                                        print("hoping to wake him up. Eventually, he seems to regain consciousness, and stands himself back up.")
                                        print("He turns to you. The only facial feature he has is one eye, which is now giving you a piercing stare.")
                                        print("He carves an \"S\" into the ground with his pointy arm, then looks back at you and speaks.")
                                        print("\"See that?\" he gestures to his most recent masterpiece.")
                                        print("Apparently he's expecting a response. You close your burned, swollen eyes and respond, \"Nope, can't see a thing!\"")
                                        print("The fire person responds, \"You just got on the wrong man's bad side.\"")
                                        print("\"Okay,\" you say sarcastically. Eyes still closed, you walk away to find some water for your burn.")
                                        print("You can't find any. You feel the magic remnants of the mysterious injury seeping deeper into your body.")
                                        print("Suddenly, you drop dead.")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    elif caba.lower() == "attack":
                                        print("You can't let this one slide. You grip your weapon tighter, loose yourself from her grip, and dive into the water.")
                                        print("Unable to keep your eyes open, you have to remember where he was. You thrust your arm foward in a stabbing motion.")
                                        print("You feel nothing there.")
                                        print("An arm grabs your shoulder. You really wish people would stop doing that. It pulls you down, and you run out of air.")
                                        
                                        print("\nYOU DIED")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            elif cab.lower() == "leave":
                                print("You decide it would be best to just forget this whole lake and find somewhere else to be.")
                                print("You make your way through the forest. After a long journey, the trees give way to desert.")
                                print("These trees evidently have less life, being so far away from water. You remember you're not feeling so hydrated yourself.")
                                print("Miraculously, you spot a castle about ten miles to the east. They may be able to give you something to keep you alive for a while.")
                                print("To your surprise, you also sense a malicious presence. It might be nearby, but it is most likely farther away in... a cave?")
                                print()

                                while True:
                                    cabb = input("Do you travel to the CASTLE, or HUNT for food yourself? >> ")
                                    print()

                                    if cabb.lower() == "castle":
                                        print("Your hunting skills are getting rusty, and now is not the time to put yourself to that test. Walking is safer.")
                                        print("You make a path directly toward what appears to be the front of the castle. It is perched on the side of a mountain")
                                        print("that overlooks the empty expanse of the desert on one side, and a breathtaking gorge on the other. Quite a unique location")
                                        print("for a castle. You discover a bridge that crosses over the gorge and into the castle. The crashing waterfall")
                                        print("mocks you as you start to struggle to walk. You nearly collapse at the front entry. A comically small door constitutes")
                                        print("what seems to be the only way in. You knock on it desperately. To your relief, someone answers.")
                                        print("He seems to be a large fox-looking man, wearing a gleaming crown on his head and boasting a splendid, purple robe.")
                                        print("He takes one look at you and says, \"My, you look exhausted. Please, come in!\" He gestures for you to walk in past him.")
                                        print("You enter a grand hall with tables that are filled with strange-looking food. Apparently this kingdom is having a feast.")
                                        print("Please do help yourself, and feel free to leave once you're feeling better.")
                                        print("You thank him, and he leaves you alone. The food is strange but it will have to do. You feel much better now.")
                                        
                                        print("\nBut aren't you missing something?")
                                        sys.exit()

                                    elif cabb.lower() == "hunt":
                                        print("You seriously doubt anyone could be living in that castle who would want to help you. Now is the time to hunt.")
                                        print("You walk in the opposite direction of the castle, along the border between the forest and the desert,")
                                        print("hoping to find some kind of animal to kill and cook.")
                                        print("After walking a good ten or so miles, you're startled by the sound of an elephant. You look to your left")
                                        print("and sure enough, you spot the big, gray beast not a hundred paces from where you stand.")
                                        print("You're unsure if you're ready to take on such a beast, but it looks rather small, and it clearly has been separated from the herd.")
                                        print("You locate a makeshift spear in the forest and tie a sharp rock to it. You make a second, and charge the beast.")
                                        print("It charges at you, too. You retreat toward a large rock and quickly sidestep just before you run into it.")
                                        print("The elephant was not as lucky. It runs straight into the rock, stunned. You run back up to it, planning how to finish the job.")
                                        print("The elephant topples over and falls on top of you.")

                                        print("\nYOU DIED")
                                        sys.exit()

                                    elif cabb.lower() == "teleport": # THIS IS A SECRET OPTION!
                                        print("Ignoring your growing hunger pains, you latch on to the sensation of this presence. This seems familiar... can it be?")
                                        print("You haven't felt this way in a long time. The conduit is opening. If you don't act fast, you'll miss it!")
                                        print("You begin to focus on teleporting to the location of the evil presence. Within seconds, you open your eyes, in an entirely new place.")
                                        print("It appears to be a dark, musty cave, just as you suspected. The only light here is coming from a few torches, one of which")
                                        print("is in the hand of a woman on the other side of this room. Unsure what to do, you crouch down to hide. You hear her speak,")
                                        print("apparently to some shady figure you can't see. You recognize the voice. You realize what's going on.")
                                        
                                        print("\n.-* You are now Jessica, Runner of Dimensions *-.\n")

                                        print("You feel someone else has come into the room. You brush it off and continue speaking. \"He doesn't have to know about this.\"")
                                        print("The hooded man responds, \"But he will find out! That is why we need to come to an agreement! There is much to discuss;")
                                        print("we couldn't hope to get it to you tonight!\" Frustrated, you turn away from him and notice something in the corner.")
                                        print("You remember the feeling you had just a moment ago. Alert, you stride carefully up to the far wall and discover...")
                                        print("\"What, you're just going to walk away?\" the hooded man follows behind you, trying to get your attention back.")
                                        print("You try to pretend nothing happened, but you look back at him and see he's staring at the wall as well. This is bad.")
                                        print("\"You! You can't be here! How did you find us? Oh no, this is awful...\" the hooded man is panicking now.")
                                        print("\"Get out of here now! Both of you! I can't be seen with you!\" He shoos you away, but it is too late.")
                                        print("Three large men come sprinting into the room dressed in tight-fitting clothes and orange bandanas. \"Skaias...\" you observe.")
                                        print("Leaving no time for you to react, they take Joshua into their hands and rush out of the room. You run after them")
                                        print("into the main sacrificial room. You're suddenly surrounded by ten Skaias, who grab you and tie you up, turning you to face Joshua.")
                                        print("Superna is standing in the middle of the room, looking both irritated and pleased at the same time.")
                                        print("\"So, you've found us!\" he screeches. You can't cover your ears.")
                                        print("\"Marvelous. You're just in time. I've finished writing my story!\"")
                                        print("\"Your story? I didn't know you were the creative type, Supes!\" Joshua taunts. Superna slices a shallow, vertical wound into Joshua's face.")
                                        
                                        print("\n\"Yeah... my story. Been planning it for ages. Let's run through it now, shall we?\"")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            else:
                                print("Invalid input.")
                                continue

                    else:
                        print("Invalid input.")
                        continue

            elif c.lower() == "jessica":
                print("You turn away from the lake. You must be hallucinating.")
                print("After a long silence, you let out a sigh and desperately say aloud, \"I just don't know what to do!\"")
                print("As you speak these words, another voice becomes audible. It's not yours, but it's saying exactly what you're saying.")
                print("Startled, you assume a defensive position and turn to the source of the voice. There's just a hill there.")
                print("Thinking it must be on the other side, you walk around it and spot a woman kneeling on the shore, looking forlorn. Clearly a cloud-dweller.")
                print()

                while True:
                    cb = input("Do you draw your SWORD or TALK to her? >> ")
                    print()

                    if cb.lower() == "sword":
                        print("This person, though not presently threatening, could be dangerous. You decide to draw your sword.")
                        print("The sound of steel slithers through the air, startling her. She looks to you in shock and flies away on her cloud.")
                        print("A voice suddenly shouts directly in your ear, knocking you to the ground. You are crouched on the ground,")
                        print("eyes closed and hands over the back of your neck. You feel the ground slip away from under your feet, and you fall.")
                        print("You land feet-first on a cloud. You're in a grand courtroom, standing directly in the center.")
                        print("\"Joshua...\" you turn and see a large man sitting in an elegant throne. He is wearing an exquisite white robe")
                        print("and has hair as pure and white as the clouds that make up much of this place.")
                        print("\"What don't you understand?\" he says, clearly exasperated. \"You are not meant to KILL the people of this land!!\"")
                        print("His voice echoes in the room and in your heart. He's right. You beg to be given a second chance.")
                        print("\"I recognize that I have done wrong. I was afraid and made a bad decision. Please forgive me.\"")
                        print("The Zeus-like man stares you down, stroking his chin, considering his options.")
                        print("Finally, he seems to have come to a decision. \"I can let you through one more time,\" he admits,")
                        print("\"But I cannot guarantee that you will come back here the same person. You may end up entirely different,")
                        print("in a way that may cause you great dysphoria, or worse. It's a dangerous thing. The choice is yours.\"")
                        
                        print("\nA glimmering portal opens up to your left. You take one last look at everyone in the room, and jump in.")
                        sys.exit()

                    elif cb.lower() == "talk":
                        print("\"Hey, Alira,\" you say, startling her. You apologize and sit down next to her.")
                        print("Alira says nothing in response.")
                        print()

                        while True:
                            cbb = input("Do you continue to TALK, or stay SILENT? >> ")
                            print()

                            if cbb.lower() == "talk":
                                print("Breaking the silence, you speak up about what's troubling you.")
                                print("\"I'm glad you're here. I need someone to talk to,\" you start.")
                                print("You look to Alira. \"I don't know what to do about Jessica. It's all I can think about.\"")

                                print("\n.-* You are now Alira, Princess of the Cloud Kingdom *-.\n")

                                print("Joshua goes on, recounting some recent experiences he's had. You're not entirely sure you understand")
                                print("what the problem is. \"So, what is it that you're unsure about?\" you inquire.")
                                print("He stares out over the lake and gathers his thoughts. \"She's been really sick recently. We've talked about it,")
                                print("but there's no one anywhere who can help her. I feel like, at this point, I'm too dangerous of a person")
                                print("for her to be spending time with. People are looking for me, and I don't think she'd survive another confrontation.\"")
                                print("He goes silent for another moment. \"And...\" he stops himself. Perhaps he's unsure if he should admit something to you.")
                                print()

                                while True:
                                    cbba = input("Do you SMILE at Joshua, or do you FLY to a special place? >> ")
                                    print()

                                    if cbba.lower() == "smile":
                                        print("You place your hand on Joshua's shoulder. He looks at you, and you smile.")
                                        print("Josh's contemplating face turns into an irritated one. He clearly didn't like that.")
                                        print("He brushes your hand off his shoulder. \"Don't smile at me like that. Can't you take anything seriously?\"")
                                        print("Frustrated, Josh stands up and walks away. You hope he just needs to get some air.")
                                        print("You may have just lost a friend. Will you ever see him again?")

                                        print("\nGAME OVER")
                                        sys.exit()

                                    elif cbba.lower() == "fly":
                                        print("You consider it unnecessary for Josh to say what he's got stuck in his throat. You say to him,")
                                        print("\"Whenever I'm unsure about what to do, the flowers always help me out. We can go there now, if you'd like.\"")
                                        print("Apparently relieved of a difficult decision, Joshua nods his head. You bring him onto your cloud")
                                        print("and fly away. It's been a while since you've gone where you intend to go, but the memory is clear.")
                                        print("Gliding over the forest at a medium pace, both of you remain silent. Joshua seems to be pondering something again.")
                                        print("Finally, the place draws near. You can see it in the distance. You arrive at a clearing in the woods.")
                                        print("Approaching it from above, you come just close enough to see a lavish display of every kind of flower imaginable.")
                                        print("They are surrounded by a thick, magical fog pierced by the light of fireflies.")
                                        print("Just the sight of it places a new thought into your heart. Before you enter the clearing, you stop the cloud.")
                                        print("\"This is as far as we need to go, isn't it?\" You look back at Josh. His eyes are wide open. You're a bit startled.")
                                        print("\"Umm, Josh? Is something wrong?\" He looks at you with an energized smile and says, \"Thank you, Alira. Thank you!\"")
                                        print("He embraces you, then closes his eyes, clasps his hands together, and vanishes into thin air. You're quite surprised.")
                                        print("Hopefully you were able to help him out?")

                                        print("\n.-* You are now Joshua, King of Katosa. *-.\n")

                                        print("The sight of flowers and magical forests folds away from your eyes. The cloud and trees flee downward, and a familiar")
                                        print("room comes over you from above. You're standing in the kitchen. It's raining outside.")
                                        print("A crash of thunder awakens you fully to your new surroundings. This is where you intended to be.")
                                        print("You're supremely satisfied that it worked. You say a final thank-you to Alira and look out the window to your right.")
                                        print("Through the rain-splattered glass, you can see a grove of trees. Your heart starts beating fast.")
                                        print("You make your way to the back door and fling it open. The rain is pouring down, but you can make it to the grove quickly.")
                                        print("You run across the muddy field and take shelter under the first tree you find. The sound of laughter floats past you.")
                                        print("\"Still afraid of the rain, are we?\" You look over and see Jessica, gracefully perched on a bench")
                                        print("without even the slightest protection from the present downpour. She's crazy.")
                                        print("Your heart is pounding now. You would have liked to spend more time meditating at the lake, but now is the time to decide.")
                                        print("What is it you were so uncertain about? Or is it really just the rain?")
                                        print("\nYou come out from under the tree and sit down next to Jessica. \"Fancy meeting you here,\" you tease.")
                                        print("\"I thought you would never arrive. I've been sitting here in the rain all alone! Glad to see you're finally conquering your fears.\"")
                                        print("\"Jess, I came here because I have something I need to tell you. And I'll say it in the rain if I have to, and I do hate the rain.\"")
                                        print("She places her hand on your leg. \"I'm listening,\" she says.")
                                        print("\"Jess, do you remember when we were kids? Our fathers gave us the most magnificent toys, and we wouldn't share them")
                                        print("with the other kids. We only wanted to share them with each other.\"")
                                        print("She looks off into the distance. \"Yes, those are some of my fondest memories,\" she smiles.")
                                        print("You continue, \"Well, our fathers also gave us these magnificent lives. And, Jess...\"")
                                        print("You pause a moment, take her hands in yours, and look into her eyes.")
                                        print("\"...You're the only person I want to share mine with.\"")
                                        print("It looks like her heart is beating fast now as well. She starts breathing excitedly, and she embraces you.")
                                        print("\"And I wouldn't want to share mine with anyone else either!\" she confesses. You couldn't be happier.")

                                        print("\nSeems you didn't need to spend that much time by the lake, after all. Congrats, Josh.")
                                        print("THE END")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            elif cbb.lower() == "silent":
                                print("You sense Alira may be under quite a bit of stress right now. It may be best to stay silent.")
                                print("After a minute, she speaks up. \"You have no idea how hard it is being Princess.\" She starts crying.")
                                print("\"Every boy in the kingdom wants to be with you, but you can never tell how sincere they really are!")
                                print("I know my dad has a lot of money, but I don't want to pressure guys into going on expensive dates with me.")
                                print("All I really want to do right now is sell my bouquets and decorate my clients' weddings;")
                                print("it's the most satisfying thing in the world to me to beautify their lives with my flowers.")
                                print("I want to get married eventually, but I just don't think now is the right time for me.")
                                print("Despite this, my mother is constantly setting me up with losers!!\"")
                                print("You're shocked. You did not expect it all to come out at once. The only thing you can think to do")
                                print("is put your hand on her shoulder.")
                                print()

                                while True:
                                    cbbb = input("Do you give her some ADVICE, or continue to stay SILENT? >> ")
                                    print()

                                    if cbbb.lower() == "advice":
                                        print("You figure now would be the right time to speak up. Searching the depths of your heart, you find something")
                                        print("that she might find useful. \"You know, Alira, I don't know what it's like to be princess,")
                                        print("but I totally get why would feel that way. It makes perfect sense, and I can't figure out")
                                        print("why your mother can't see that you just don't want to date right now. My father always told me")
                                        print("that if you're unsure about something, just stick to what you know, and go ahead and take that step")
                                        print("into the darkness. That advice has always helped me. What do you think?\" She ponders for a moment.")
                                        print("\"I think you're right. Maybe these dates aren't so bad. I can be pretty harsh on others.")
                                        print("I appreciate that, Josh. Thank you.\" She smiles. You're just relieved you were able to help.")
                                        print("Suddenly, she looks concerned. \"Oh, I've got to go now. It was nice seeing you!\"")
                                        print("\"Oh, uhh, okay! See you around then!\" She gives you a friendly hug, and flies off into the stars.")
                                        print("You had forgotten about that old advice your father always told you ad nauseum.")
                                        print("Remembering him brings a smile to your face. Maybe he isn't so far away after all.")

                                        print("\nTHE END")
                                        sys.exit()

                                    elif cbbb.lower() == "silent":
                                        print("You know Alira too well to speak up now. She expressed herself, now she has to process things again.")
                                        print("You remain silent out of respect for her feelings.")
                                        print("An even longer silence prevails. You start to wonder why she isn't saying anything.")
                                        print("Suddenly, she looks over at you, eyes red with tears. \"Josh?\" she says,")
                                        print("\"Thank you for listening to me. Sometimes I feel like no one is really there for me. But I know you are.\"")
                                        print("Tears start to well up in your eyes now. \"At this point, that's the only thing I can offer anyone.")
                                        print("I never wanted to run away. To this day I still don't understand why they did it. Father had such")
                                        print("a kind heart, but I guess they wanted both of us out. It's lonely in my little wanderer's world, so it always")
                                        print("makes me happy to listen to you.\"")
                                        print("She puts her head on your shoulder. A nice, easy conversation follows. You see things in Alira")
                                        print("that you've never seen before. You agree to see each other again soon.")

                                        print("\nMaybe Jessica isn't the one for you after all.")
                                        print("THE END")
                                        sys.exit()

                                    else:
                                        print("Invalid input.")
                                        continue

                            else:
                                print("Invalid input.")
                                continue

                    else:
                        print("Invalid input.")
                        continue

            else:
                print("Invalid input.")
                continue

    





##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

# Here are the options "QUIT" and "ASK"


    elif z.lower() == "quit":
        print("\n\nGoodbye.")
        break

    elif z.lower() == "ask":
        question = input("Ask a question: ")
        if "missing" in question.lower() and "?" in question.lower():
            print("\nWONDER WHAT BREAK REACH TELEPORT\n♥ Jessica")
            sys.exit()
        elif ("what","am","i","something") in question.lower():
            print("I don't know how to answer that question, but you're close.\n-Jessica")
            print()
            continue
        else:
            print("I don't know how to answer that question.\n-Jessica")
            print()
            continue

    else:
        print("Invalid input.")
        continue
