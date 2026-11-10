define config.rollback_enabled = False

define y = Character("IRIS", kind=nvl, bold = True, color = "#C2BBC9")
define p = Character("LION", kind=nvl, image="lion", bold = True, color = "#ACDAE3")
define r = Character("REX", kind=nvl, image="rex", bold = True, color = "#E3ACAE")
define narrator = nvl_narrator
# define config.nvl_paged_rollback = True
define dis = { "master" : Dissolve(3.0) }

#TODO key "mousedown_1" action 
#TODO make choice menu work correctly

style nvl_dialogue: #text outline
    outlines [ (3, "#000", absolute(0), absolute(0)) ]

style nvl_label: #name outline
    outlines [ (3, "#000", absolute(0), absolute(0)) ]

style nvl_button_text: #choice outline
    outlines [ (3, "#000", absolute(0), absolute(0)) ]

transform lion_scr: #position for pygs image
    xalign 0.95
    yalign 0.7

transform rex_scr:
    xalign 0.05
    yalign 0.7

transform selfie_scr: #position for rexs image TODO check
    xalign 0.85
    yalign 0.5

screen imagemap_example():
    imagemap:
        idle "chapter base"
        hover "chapter select"

        hotspot (127, 150, 504, 489) action Jump("chat_pyg") alt "Lion"
        hotspot (649, 145, 507, 449) action Jump("chat_rex") alt "Rex"

    
init python:
    renpy.music.register_channel("extra", "music")

# The game starts here.

label start:

    $ violence = 0
    $ despair = 0
    $ nvl_mode = "ed"

    scene bg select

    call screen imagemap_example

return

label chat_pyg:

$nvl_mode = "pyg" #this does nothing bc pyg is default but its good to make him feel included

play sound ticking3
show lion neutral at lion_scr
stop music fadeout .5

p "I didnt get a chance to tell you after class but"
play music loopish fadein 1 volume 0.7

show lion happy
show bg blue2 with dis #TODO figure out nvl fade effect

"Dont listen to the prof your presentation was really good!"
"Ive been looking into the topic a little myself and what you said lines up really well with something they were debating in the 50s"
"Its a shame people didnt take it more seriously"
"Just because the guy who came up with it killed his wife"

show lion right

"Thats all anyone wants to talk about"

p right "anyway"
"I wouldve said as much in person"

show lion sweat

"I hope you dont think i hate you... its different face to face"
"My fingers go numb like im about to faint"
"Its um"
"Not very cool I heard some people pee themselves"
"With my luck id hit my head"
"Bleed out with my hand raised up like im just saying hello to the linoleum"

nvl clear

show lion right

p "It wouldnt even make the papers"
"Itd be like one of those fake articles you only see on facebook"
"“Wretched worm breathes its last”"
"And you have to click to find out if its a worm you care about"
"But its just a bunch of ads"

p low "So hey"
"You know that exam i said i was worried about?"
"The one you told me i was going to do amazing"
"Haha..."
"Good news it turns out its not a problem after all!"
"..."
"Now its just this class"

p neutral "Youre probably studying with Audrey right"
"Itd be awkward with the three of us"
"frankly its none of her business but i really think she doesnt like us d"

show lion blush

"Dating"

nvl clear
show lion neutral

p "Have you read Weininger?"

show weininger onlayer overlay zorder 15
play sound ticking3

"I can send you a good summary but basically I think"

show weininger onlayer overlay zorder 15
play sound "barking.mp3"

"Theres no soul in there"

show weininger onlayer overlay zorder 15

"It sounds crazy but its true. Its not just women either"
"Theyre all just a bunch of cruel looks with legs"
"No values except for whats “nromal”"

show lion sweat

"Normal"

show lion neutral

"They dont even know theyre being used"
"to keep people like me in line"


show lion right

p "No I really dont like how she looks at you"
"She will probably go her entire life sneering"
"Wouldnt want to be her wedding photographer"

show lion happy

"Or delivering one of her 1.5 kids"

show lion neutral

"She doesnt even know what happiness looks like"
"Sorry I know she is your friend and all"

play sound "doorbell.mp3"

p "I dont even know what her problem is"
"Am i not allowed to be happy or something?"

nvl clear
show lion right

p "Of course not"

play sound "doorbell.mp3"

"..."

show lion neutral

"Hold on"
"Someone is ringing the doorbell"
"Theyll probably go away if i ignore it right"

show lion right

p "I had this dream you went away"
"We were eating bread and talking about..."

play sound "doorbell.mp3"
show lion sweat

"something"

show lion neutral

"And then you just went away"

show bg bluish2 with dis

p "I know youre too good for me. Its not right"

show lion happy

"Thats why im trying to help you too"

show lion neutral

"Its just not safe"
"Shes waiting for you to slip up"

show lion miffed

"That viper"

"Its true that i havent really talked to her but I dont think thats the only way to really know a person"
"It might actually be one of the worst ways"

show lion right
nvl clear

p "I know youre just lonely. I wish i could do more about it"
"Am i not enough?"
"Or are you not even there?"

show lion low
play sound phone

p "Wait im getting a call"
"Unknown number. This is seriously starting to piss me off"

play sound "television.mp3"

show lion neutral

p "Lets talk about something else"
"So yeah now its just this class"
"My attendance was too bad to take the exam"
"Haha you probably didnt even notice!"
"Its hard to get myself to go when i know you wont be there..."

show lion blush

"You make everything so"
"I dont know"


"..."
nvl clear

show lion neutral

p "I just get stuck in the doorway wondering what ill even do with this stupid degree"
"The internship was a bust"
"And now this"
"Ill do it next year i guess"
"At least it wasnt a total waste"

show lion happy

"Since I get to talk to you like this"

show lion blush

p "You should tell me if im being too much"
"Thats what my first girlfriend said"

show lion neutral

"in kindergarten"

$ renpy.music.set_volume(1, 0, 'music')

p "Did i ever tell you"
"They almost sent me on a student exchange program once"
"I never even told my parents"
"They wouldve jumped at the chance to have me gone"
"They say its for my own good"

show lion right

"But i know."

nvl clear

p "Some days i get the sense that theres nowhere for me"
"I cant eat anything"
"or look people in the eye"
"and i just go out against the weather"
"hoping that something bad will happen thatll take it all away from me"
"out of my hands and into a hospital room"

show lion hiding

"where the people with real reasons go"
"Real human beings"

show lion right

"Nothing ever happens"

p "I dont know how other people do it"


show bg complex with dis

p "In the end..."
"theyre just building castles in the sand"

show lion neutral

"Todays effort is washed away tomorrow"
"Nobody gets to enjoy it"
"Not those who work and not those who steal"

nvl clear
play sound "prelude_l.mp3"

p "Its not our fault we were born too late"

show lion happy

"I remember now"
"Thats what you said to me"
"When we were eating bread in the sun"

p "Youre so cute when you complain you know"
"You say it high and clear"
"Like theres nobody else in the world..."

show lion neutral

"At first it scared me. It was so familiar"
"I mustve written those same words hundreds of times"
"In the margins of notebooks and on locked accounts"
"Straight into the void"

show lion right

"Maybe thats naive"
"Just because there was no answer doesnt mean no one saw"
"You should always assume it leaves a mark somewhere"

show lion neutral

p "I was taught to fear the internet just like that"
"But it doesnt seem all that true anymore"

nvl clear

p "Your every movement"
"has that gravity"

show lion blush

"Like youre absolutely sure those words will disappear"
"without ever being heard"
"but still..."

show lion neutral

p "Still no response huh"
"I wish youd say something"

show lion right

"Just to let me know youre there"

y "{image=dotdot.png}"

play sound "barking2.mp3"
show lion neutral

p "I really dont think Audrey is good for you"

show lion sweat

"Im not saying it because im jealous. You have to believe me"


"Sometimes i cant make sense of my own thoughts"

show lion neutral

"But you say them with conviction"
"Now im terrified"
"Whatever it is that makes you you"


"I can tell she wants to grind it down and swallow it"

nvl clear
show lion hiding

p "Thats just the kind of person she is"
"Because she has nothing of her own"

show lion happy

"Maybe you pity her. Youre a good person after all"
"But it wont end well"

show lion miffed

"Shes trying to take you away from me"
"Your body will still be here"
"But thats all"

show lion neutral

p "Or are you just doing it to get back at me?"
"Do you hate me?"
"Because of one mistake"

show lion right

"One mistake..."

p "In my dream you were asking me to run away together"
"I didnt know what to say"
"And then you went away"

$ renpy.music.set_volume(0.7, 0, 'music')

show lion low

p "I checked the door"
"It was my grocery delivery"

nvl clear

p "Forgot i did that"
"There is no milk... They didnt even have my second choice apparently"
"Fuck my life"
"Last time they did this with my shower gel"

show lion sweat

"I mean it was fine"
"I dont sweat that much in the winter... i think"

show lion neutral

"In a way it actually saved me time"
"But i did smell like a pickle by the end"
"Didnt know my body could do that"

p "Ive been watching the original Pretty Cure lately"

show lion happy

"I have no idea why i put it off"
"Its really nice"
"I was worried about the episode count"
"I dont always like how these things are paced"
"Thats why i dont watch a lot of older shows"
"But i think the length works for it"
"You really get to know the characters as people"
"Especially when i put it on while i eat"
"It helps the house feel less empty"

show lion blush
nvl clear

p "Is that a sad thing to say"
"It just makes me think of all the little girls following it week by week back then"
"Going to class and talking about the latest episode with the other kids"
"Begging mom for the toys"

show lion right

"Mustve been fun"
"..."

p "It means a lot to me that you dont judge"
"Anyone else wouldve shut me down when i mentioned PreCure"
"What a freak"
"Arent you supposed to be a guy?"
"Stuff like that"

show lion neutral
show bg finely2 with dis

"I wonder about it sometimes"
"If anything else made me feel this way"
"Would i do that instead?"

nvl clear

p "Im not trying to intrude..."
"I just like"
"seeing what someone came up with"
"trying to make others happy"
"and thinking of what they might need"

show lion right

"I know its not for me..."

p "Honestly"
"If i have to make up for even existing"
"Its easier to stay at home where i wont bother anyone"
"I dont think being weird is a sin"
"Other people seem pretty good at it"
"The useful and the beautiful all get to have it"

show lion happy

"If i was better at living"
"maybe id be allowed to enjoy it too"

show lion low

p "Oh yeah"
"Check it out"

play sound "television.mp3"

nvl clear

p "{image=bg/pigeon1_resize.png}\n"
"This guys been coming to my balcony for a few days now"
"I havent fed it. Dont want it to get too attached and shit on my laundry"
"But its kind of cute"

show lion happy

"You know some people think birds arent real"
"They say theyre just drones spying on you for the government"
"When you see them sit on a wire"
"thats them charging their batteries"

nvl clear

show lion neutral

p "Its actually not that out there"
"The CIA has done it before. Then again what hasnt the CIA done"
"Its too bad their psychic experiments never went anywhere"
"Theres not much they can do to track guys like me"
"I run a tight ship"
"If you think about it that way this pigeon suddenly becomes very suspicious"


"..."

show lion happy

"Im just kidding"
"All itd see right now is me making oatmeal anyway"
"which is pretty much legal"

show lion sweat

"unless...?"

nvl clear

show lion neutral

p "No i think it should be fine"
"Except for this criminal lack of milk"

show lion fuckass

"Hehe"

show lion happy

p "If..."
"If you ever came over id feed you something nice and proper"
"Just let me know beforehand"
"And ill order something"

stop music fadeout 1
show lion neutral

p "I just heard something click"
"Di"

show lion sweat

"Did i not lock the door after i took the groceries in"

show bg danger

play music heartbeat fadein 1 volume 0.7

"I cant see it from here"

show lion hiding

"God im so fucking stupid i knew thisd happen someday"
"Its not like i know my neighbors that well"
"It would be too easy"
"Someone couldve gotten in the building after me and waited in the stairway"
"Until i"

show lion gone
nvl clear

p"I locked the kitchen door but i dont know what else to do"
"Should i pretend to not be home"
"Iris im scared"
"Why is this happening to me i dont even have anything worth stealing"
"I cant get myself to get out from udner the table"
"There was a cheese knife so i grabbed that"
"But if someone actually comes"
"im dead"

p "..."

p "It doesnt make any sense"
"If someone killed me"
"Their sentence would be the same as if they killed a real person"
"Theres nothing to gain..."
"But i still"
"cant get up from the floor"

stop music fadeout 1
show lion hand
show bg finely2 with dis
nvl clear

p "Sorry"
"Thank god you didnt call the cops"
"this hpapens sometimes"
"Happens"

play music loopish fadein 1 volume 0.7
show lion right

p "The noise is gone"
"Ill just eat my oatmeal"

p "Do you think the prof would mind if i didnt turn in anything"
"I dont really"
"feel up to it right now"

show lion low

p "I put in strawberry jam this time"
"Looks kind of gross"
"Maybe i should just do straight sugar. Thats all this is anyway"
"For this price they dont even bother to fake it"
"Its fine"
"Id rather spend my money on you"

nvl clear

show lion neutral

p "Hey"
"So"
"Did you get home okay after that"

y "after what"

show lion sweat

p "Oh"
"There you are"
"..."
"Actually nevermind"

show lion neutral

p "I forgot to put on my episode"
"Might be for the best i think itd go over my head right now"
"But um"
"I like your company too"

show lion right

"It just gets quiet here"
"Wasnt as bad when grandma was still around"

nvl clear


y "do you miss her?"


p "I dont know. She was a nag"

show parallel un onlayer overlay zorder 15
play sound ticking3

"I couldnt do anything right in her eyes"

show parallel deux onlayer overlay zorder 15
play sound ticking3

"But at least"

show parallel trois onlayer overlay zorder 15
play sound ticking3

"We could act like a family"

show parallel yeowch onlayer overlay zorder 15
play sound ticking3
show lion hiding

p "A family..."

nvl clear

play sound "prelude_r.mp3"
show lion miffed

p "Iris"
"How come"
"The things that should make me happy"
"I dont want them at all"
"I cant join everyone in that sunny spot"
"so why"
"when i finally find something"


"why is it wrong?"
"Why is it creepy only when i do it?"

show lion hiding

p "They should be grateful"
"All those things they forgot about"
"Their toys and cartoons and grandma too"
"I keep them safe"

show bg sundown with dis

"..."


menu(nvl=True): 
    "1. you're fine":
        jump pviolence1

    "2. you're special":
        jump pdespair1
return

label pviolence1:

    nvl clear
    play music prelude fadein 1

    y "there's nothing wrong with you, lion"
    
    show lion blush

    p "H"
    "haha"
    "Nothing"

    y "nothing at all"
    "you keep saying these cruel things"
    "like you forgot i love you"
    
    show lion hand

    p "imsorryimsorryimsorryimsorry"
    "I mean"

    show lion blush

    "I love you too"
    "..."

    show lion happy

    "Youre the only person in the world who would say that"
    "Knwoing me"
    "Knowing"
    
    nvl clear

    y "but those people you always talk about"
    "they don't really know you, do they?"
    
    show lion right

    p "No"

    y "see"
    "your happiness doesn't need to be shaped like anyone else's"
    "and they certainly can't take what you love away from you"
    "think about it"
    "even if they locked you up right now"
    "what would it really change?"
    "they have no control over your mind"
    "or your heart"
    
    show lion sweat

    p "That"

    show lion hiding

    "might be true"
    "But..."
    
    show lion hiding

    "\n(+1 VIOLENCE)"
    $ violence+=1
    jump pcont1

label pdespair1:

    nvl clear
    play music prelude fadein 1

    y "lion"
    "why do you like me?"
    
    show lion sweat

    p "???"
    
    y "you say you're not a real person like everybody else"
    "that you're something different"
    "isn’t that what you told me too"
    
    p "Wait w"
    
    y "it’s not a bad thing"
    "is it?"
        
    show lion hand

    p "Oh god i"
    "When i said that i didnt mean it like"
    "Sorry"

    nvl clear
    
    y "you don't even know what you're apologizing for do you"
    "it’s okay"
    "i’m listening"
    
    show lion right

    p "I really do think"
    "youre like an angel sometimes"
    "When i say youre not like them"
    "Thats what im trying to"
    
    show lion blush

    p "Ugh"

    y "that’s so sweet <3"
    
    p "..."

    "\n(+1 DESPAIR)"
    $ despair+=1
    jump pcont1

label pcont1:

nvl clear

show lion sweat

p "I thought you were mad at me"
"I mean"
"Isnt that how this goes"

y "why should i be"

show lion neutral

p "Because I saw"

show lion miffed

"When you"

show lion right

"..."


p "When Audrey"

show lion pissed
show memory with dis

"That bitch laid a hand on you i cant believe she did that still i mean it couldnt have possibly been that important she never talks about ANYTHING important so why did she have to"
"Shove you like that"
"I was so angry i thought i would throw up"

nvl clear

p "She didnt even look back to see you go down"
"and stay there"
"You were coughing your lungs out"

show lion hiding

"No she mustve heard."
"She just didnt want to"
"“MAKE A SCENE”"

show lion pissed

p "But I saw them all"
"Everyone walking by"
"Pretending to stare at the sky"
"Or their fucking shoes"
"Like the problem that will go away on its own"
"Is “you”"

show lion right

p "I cant stand it"
"I really cant..."

menu(nvl=True):
    "1. i'm sorry for not listening to you":
        jump pviolence2

    "2. i hate them so much":
        jump pdespair2
return

label pviolence2:
    
    nvl clear
    show bg orange2 with dis
    hide memory
    
    y "i don’t know why i thought i could trust her"
    "i’m really sorry"
    "you kept trying to warn me..."
    
    show lion happy

    p "Its ok"
    "You dont know her like i do"
    "I just wish none of this ever happened"

    y "yeah same"
    "what even is her issue"
    "i don’t think i did anything wrong..."
    
    p "She just wants to ruin my life"
    "I cant think of any other reason"

    show lion miffed

    "Audrey"
    "always on her way up"
    "with her elbow in your back and her foot in your mouth"

    show lion right

    "Like shes any better..."

    nvl clear
    
    p "I bet she filled your head with all sorts of ideas about me"
    "Told you that im some kind of p"
    "Pervert"

    y "i thought she was just joking about that"
    
    p "Well i dont find it very funny"

    "\n(+1 VIOLENCE)"
    $ violence+=1
    jump pcont2

label pdespair2:

    nvl clear
    show bg orange2 with dis
    hide memory

    y "sometimes"

    show lion neutral

    "i wish they'd all just die"
    "all these people who think tomorrow will come no matter what"
    "even when they don't deserve it"
    "..."
    "sorry"
    "it’s not very cute of me"
    "but still"
    
    p "No..."
    "Youre right"
    
    p "Everyone says"
    "I need to grow up"
    "This doesnt fly in the real world"
    "There are always consequences"
    "But i dont think these people are living in the real world either"
    "Thinking about being late for work"
    "While someone collapses right beside them"

    show lion hiding

    "Its sick"

    nvl clear

    y "it’s kinda nice that you can get mad about this still"
    "do you know how many times it has happened?"
    "nobody notices"
    "that’s why"
    "when the time comes"
    "they'll get no pity from me"
    
    p "..."
    
    "\n(+1 DESPAIR)"
    $ despair +=1
    jump pcont2

label pcont2:

nvl clear

show lion miffed

p "Dont worry"
"Ill show her consequences"
"Im gonna make Audrey apologize"
"For everything"

show lion hand

p "I dont like feeling angry"
"That boiling sensation"
"It drags me right back in my body"
"But"

show lion neutral

"Its the least i could do"
"Ill make her say it over and over and over"

show lion happy

"and over again"
"Until i can finally forgive her"
"And then..."
"We can be safe"

y "it’d be nice if that was possible"
"but"
"i also don’t want you to get hurt more than you already are..."

nvl clear

p "Its fine"
"Ill write to her"

show lion neutral

"Theres no telling what she might do after all"
"When shown the truth"

p "Ok i sent it"
"Phew"
"Now we wait"

y "are you sure she’s gonna read it?"

show lion happy

p "I led with a threat so it should be fine!"
"But wow"
"That felt pretty good"
"Even if we dont get a sincere apology"
"I gave her a piece of my mind..."

nvl clear

show lion right

p "I always thought"
"it takes a special sort of person to make a change"
"Great men. The ones they write history books about"
"Even if someone like me were to complain"
"theyll just be told thats just the way things have always been"
"Theres no point in just saying “no”"
"Until you know what it is you want more than anything"
"theyll keep on walking all over you"

show lion neutral

"but now i see"
"I shouldve done this a long time ago"

y "i think even a no has meaning"
"at least for me..."
"sometimes i don’t even realize it’s an option until i hear someone else say it"

p "Youre right"
"Im so stupid"

show lion happy

"How did i not see it before"

nvl clear

p "I gave up too early"
"When there still was something i could do"


p "Haha"
"I feel like i could just get on a bike and ride until my legs give out"
"I wonder where i would end up. Wouldnt that be a story"
"Too bad i never learned how to do it"

y "and you have an inbox to watch!"

show lion low

p "Oh yeah"
"The apology"
"I wonder if shes seen it already"
"If i were her i would hurry"
"My heart is beating so fast"
"I dont feel like waiting around today"

nvl clear

p "Look"
"{image=bg/pigeon2_resize.png}"
"Two of them"


menu(nvl=True):
    "1. how sweet!":
        jump pviolence3

    "2. interesting":
        jump pdespair3

return

label pviolence3:

nvl clear

y "that's us"

show lion fuckass

p "Hehe. Yeah"
"They look so warm there in the sun"
"Makes me want to protect them"

"\n(+1 VIOLENCE)"

$ violence+=1
jump pcont3

label pdespair3:

nvl clear

show lion right
y "what's with you and pigeons?"

nvl clear

y "{image=dotdot.png}"
"that's us"
p "I thought so too"

"\n(DESPAIR +1)"

$ despair+=1
jump pcont3

label pcont3:

nvl clear

p "I think ill step out a little after all"

show lion happy

"I have my phone with me"
"So i should see if she replies anyway"

stop music fadeout 1

nvl clear

$ nvl_mode = "ed"
$ gui.xanchor = 400
$ gui.rebuild()

if violence>=2:
    jump pv

if despair>=2:
    jump pd

nvl clear
"neither violence nor despair are 2 lol"
return

#im not doing these until we have a layout

label pv:

scene bg middle ed with dissolve
play music ticking
play extra prelude_womp volume 0.7 fadein .5

"\nMy hand was already on the doorknob when I noticed the sound."

"I opened it up to find –"

"""\n\"Hey.\"

\nI blinked a little more forcefully than usual. Was my mind playing tricks on me? It couldn’t have been more than an hour since I sent the message.

\n\"What are you doing here?\"

\nHer stance was nonchalant, like she should ask me the same thing. This was {i}my{/i} territory, though. Irritation was already at the tips of my fingers.

\n\"You’re really gonna make me stand here in the doorway?\"

\nAs much as I hated the idea of having her in the apartment, I didn’t want the neighbors overhearing us either. I stood aside.

She waltzed in, outdoor shoes trampling on old carpet.

She was looking the place up and down as if making sure everything was in the place she left it. Beyond us, the curtains were whipping in the wind. I was suddenly aware of the smell.

This was fine. Great, really. I was ready to make do with a written apology, but now that I saw her face, the anger I’d forgotten about was starting to come back to me."""

nvl clear
stop music

"""\n{i}Audrey. I thought we were friends.{/i}

Just the first in a long line of disappointments.

She turned back towards me.

\n\"You know, I really don’t get you. You should be old enough to drink by now. Wouldn’t that be a better use of your time? If not a better use of your {i}brain{/i}.

Why are you so hung up on me?\"

\nShe said it like we were only talking about an embarrassing crush. Did she even read my message?

\n\"You’re the one who can’t seem to leave me alone.\""""

show black

"\nIt was a process that was put into motion a long time ago."

hide black

"\n\"Hahaha, WHAT?\""

show black

"\nComplete and utter isolation. Blinding my senses until I’m too afraid to take a single step. Breaking down my world piece by piece. Why else would she treat Iris that way?"

hide black

"\n\"I told you. If you don’t want to apologize, then just... stop. I don’t want to see you again.\""

show black

"\nMaybe it was decided before I was even born."

nvl clear

hide black
play sound barking

"""\n\"I’m not in your class because I fucking want to be!\"

\nShe took a step towards me.

I knew her type: she was always demanding for something to be fixed. In her eyes, I must’ve been an intolerable stain. Thanks to that, any aggression was justified.

\n\"What do you expect me to do? Just disappear?\"

\n\"...\"

\nI gave her a slow nod.

I’d be lying if I said I never considered it before. In my mind’s eye, the playground, the classroom, the convenience store and the street without Audrey in it were all so clear. One less voice in the choir, but that was all.

If the world ended today and I was asked to recreate it, I’d do it exactly so.

Her expression contorted with rage. It felt like I could see right up her nose if it weren’t for the light. I took a step back.

Since when could she make such a horrible face?"""

play sound barking3

"\n\"The world doesn’t revolve around you, asshole!\""

nvl clear
play music ticking2

"""\nIt happened before I could even register it.

One moment, she was standing before me, and then she leapt for my neck, eyes lit with sparks."""

"{i}\n\"i think even a no has meaning{/i}"

"""{i}sometimes i don’t even realize it’s an option until i hear someone else say it\"{/i}

\nI acted on pure reflex. I felt my back connect to the door and my hands grab hold of her wrists and push –"""

play sound fall
"She hit the ground with a thud."
nvl hide
show ed pyg violence with dissolve
pause 1.0

"Seeing her limbs twisted around her should’ve made me feel something. Instead, all I could think was {i}she wanted this to be me{/i}."

stop music

"The air suddenly felt too cold on my skin; I realized I was drenched in sweat. I pulled my phone from my pocket."

play sound ticking3

"\n{font=ipam.ttf}{b}LION:{/b}{/font} I did it"

play sound ticking3

"I thought i would have to ask her to leave us alone"

play sound ticking3

"But i just did it"

"\nThe pinch of her brows was quickly coming undone. She must’ve lost consciousness on her way down. It made me think of one of grandma’s stories."

nvl clear

"""\nIt was a bright, early autumn day.

\nShe was on her way to the post office when the lady walking in front of her tripped and fell, never to get up again. {i}She landed in the most unfortunate way,{/i} she said. It was over in an instant. I wasn’t allowed to leave the house for a week afterwards; she couldn’t relax unless she could see me.

\nDid Audrey hurt herself on the threshold?"""

play music loopish

"""\nI looked at her again.

There was no blood, but I couldn’t hear her breathing over the sound of the curtains.

She looked more like the girl I knew now: the one who barely came up to the cabinet next to her. Dirty fingers, garish shirts, polkadots. Castles in the sand. It all felt like a lifetime ago. What kind of face was I making? I couldn’t tell.

I crouched down beside her."""
nvl hide
show ed pyg violence alt with dissolve
pause 1.0

"""Out of the corner of my eye, I saw a crow land on the balcony railing. Audrey’s skin was flushed with sunlight; her collarbone cast soft shadows below. She looked like she could’ve been ill.

\nI didn’t hear anything except the ringing in my ears."""

stop extra fadeout 1

"\n\n1V: PYGMALION, TRIUMPHANT"
return

#"~end~?????"

label pd:

scene bg middle2 ed with dissolve
play extra prelude_womp volume 0.7 fadein .5

"\nHis hand was already on the doorknob when he noticed the sound."

play music ticking
play sound knock

"""That was odd. He wasn’t expecting another delivery.

He fixed his eye on the peephole –

\n\"Pyg? You in there?\""""

play music ticking2

"\nHis heart fell in an instant."

"""A thousand doubts pricked at his skin; he fought the urge to scratch at them, to pull at his hair. What was she doing here?

There were five to ten responses swirling in his head, depending on her next move. All assuming she would write him back, desperate to save her good image. Some were gracious. Some pushed his luck –

\n\"I got your message. That must’ve taken a while to write, huh?\"

\nIt was more like possession.

He was surprised by how the words kept flowing once he started.
The turns of phrase he’d mastered in the dark of his bedroom all converged on one point."""

nvl clear

show black

"""\nDestroy her.

If not fundamentally, then physically. If not physically, then mentally. If not mentally, then socially. See, she wasn’t the only one who could take away someone’s place to belong.

He had felt invincible,"""

hide black

"""but that was then.

Now the girl on his doorstep looked invincible, too.

Audrey, not a hair out of place. Weren’t there supposed to be consequences?

\n\"All that bullshit, I mean.\""""

play sound knock

"\nHis body was welded to the door. When she got closer to rap out a knock, it went through him like a foreign heartbeat."

"Shame or punishment: those are the only things capable of keeping people in line. He remembered reading something like that once. If she wouldn’t learn from one, he would show her the other. She clearly felt no shame – that left him with only one option."

stop music

"Audrey lowered her voice."

play sound ticking3

"""\n\"You don’t think anybody’s gonna ask?\"

\nFor a moment, their eyes met. He sucked in a breath; was the peephole not one-way?"""

nvl clear

play sound barking3

"""\n\"Hey, where’d you get that picture? How long were you following us?{p}When you say she lay there for hours, you don’t mean...\"

\nHis eyes went to the corners of the room, the birds all standing in a line, the red afternoon blaring like a searchlight through the balcony window.

Why? Why did he suddenly feel that he was surrounded by enemies?

Even the phone in his pocket seemed to burn against his skin.

\n\"...stop...\"

\nThe voice that came out of him could hardly even be called a whisper. He pressed his back to the door as if he could hold it closed.{nw}"""

play sound bang2

extend " She was banging on it without restraint now."

"He needed to call for help. He needed..."


"\n\"I thought you wanted to hear my response!\""

play music heartbeat

"""\nNo, no, no. He couldn’t let Iris hear this!

If he disappointed her now, he really would have no-one left to turn to!

{size=+10}SHAME OR PUNISHMENT.{/size}

Which one was he more afraid of?"""

nvl clear

play sound bang

"""\n\"You know that I’m barely even in that photo, right? Post it! Spread it all over the internet! I’m sure she’d love that.\"

\n\"—--—-—-!!!\"

\nJust where was her strength coming from?"""

"The fact it was locked seemed entirely irrelevant. Every bang on the door rattled the walls; wind whistled through a gap in the frame. It was only a matter of time until it all came crashing down. He scrambled to put some futile distance between the two of them."

with vpunch

"\n\"But like, you watched her lay there and didn’t do anything? And you wanna talk about what’s wrong with ME?\""

nvl hide
show ed pyg despair alt with dissolve
pause 1.0

"\nWhen he crossed the threshold into the living room, the balcony door was open."

"\n\"You think YOU’VE got a right to judge anybody?\""

"\nThe world outside his window was silent. He wanted to call for help, but nothing in him moved. He leaned over the railing limply."

nvl clear

"\nA tepid wind caressed his face."
"It was a familiar feeling."
nvl hide
show ed pyg despair with dissolve
pause 1.0

"The people below came and went; his hand that reached out slid off of them without touching anything."

"""\nSomewhere,

several stories down,

teardrops were falling.

There was nothing he could do. That was all he knew with any certainty.

\nBut down there, on that road that ran from the playground to the convenience store, the one that used to be hemmed by cherry trees when he was little,"""

stop music

"another pair of eyes met his."

play music loopish

"""\nIt took his breath away.

Maybe all that time he’d spent wishing to be saved wasn’t wasted after all. No, those words couldn’t just disappear in the wind!

Trembling, he willed his hand to reach further –"""

nvl hide
show ed pyg despair alt
with dissolve
with vpunch
pause 1.0
stop music fadeout 1.5
stop extra fadeout 1

"\n\n1D: ALL EYES ON YOU"

#"(BANG)"
#"~end~"
return

label chat_rex:

#"Case.2"

$nvl_mode = "rex"

stop music fadeout .5
play sound ticking3
r "ok lets take it from the top"

play music street fadein 1
show rex neutral commute at rex_scr
show bg bluish var with dis

"{i}“He ran his fingers down his lover’s sternum. The skin bobbed and knotted beneath his touch, pacing an unsteady rhythm. Scar tissue: some self-inflicted, some almost certainly coaxed out of others. Jiro always brought out the worst in people. Even now, as he lay there beneath him, his gaze was merely confused. Was he wrong for trying to treat him gently for once?”{/i}"

r "remember this is a tale of MADNESS and OBSESSION"
"i want to see them writhing in It"
"eachothers blood i mean"
"among other things"

show rex thinking commute

r "i remain undecided about cum"
"ambivalent even"
"i keep telling you, you always rush it"
"trauma cant be resolved in a paragraph or two. its like a whole thing"
"i mean look at me. lol"
"the song and dance is the point"
"well its just what i like. if things go well shell like it too"
"this is only a test run after all"

nvl clear

show rex neutral commute

r "you and me were gonna prove that real human connection is possible"
"it might sound funny but its my last shot"
"so do your best for me"
"ok?"
"none of that silly business mixing up their eye colors and whatnot"
"although..."

show rex thinking commute

"would she?"
"i guess i dont have very high expectations of a gacha player"

r "i was surprised when she said she was interested in this pairing at all"
"i mean its kinda dark right"
"but then plenty of people like dark stories without any sort of seriousness"
"all those handcuff spinning mafia bosses"
"and aus that didnt make sense even in ops own head"
"just because were too good to be bought by one direction anymore doesnt mean anyones gotten real"
"its all interchangeable to those people"
"whoever moves first gets the clout. thats all there is to it"

show rex neutral commute

"more future online detritus for the pile"
"i just wish they wouldnt confuse taste with intelligence"

nvl clear

r "but thats neither here nor there"
"who knows maybe she is excellent"
hide rex
"wont know unless i try"

stop music fadeout 1.5

r "{i}“Something dark and vital red squirmed in his stomach. The man he loved, in all his frail beauty, was waiting with open arms. His limbs became paralyzed with certainty. If Haku laid a hand on him now, he would crumble. All with that same smile on his face...”{/i}"

r "so"

show rex thinking normie at rex_scr

"youre basically a genius right"
"why would a girl not wear the bracelet i got for her"

play music loopish fadein 1 volume 0.7

"i tried to match her style"
"nothing outrageous but better than what she usually wears"
"with those infantile plastic beads..."

show rex neutral normie

"couldnt catch me dead in something like that i have an image to consider but her"
"its like shes totally given up"

show rex judging normie

"i mean she talked to ME about fandom discourse"
"can you fucking imagine. we are NOT that close"

play sound "street2.mp3"
nvl clear

r "thats like showing your bare ass to a houseguest"

show rex mocking normie

"of your parents"


show rex neutral normie

r "the whole thing made my skin crawl"
"had to pretend i had no idea what she was talking about"
"i even made her explain what an anti was LOOOOOOL"
"that mightve been the wrong move come to think of it"
"whatever i can still play it off like shes the reason i looked at yaoi"
"dont wanna reveal my power level too early"
"wait do people even say that anymore"

nvl clear

r "maybe the bracelet isnt the problem"

r "theres this guy in one of our classes"
"always the first out the door once the lectures over"
"total prey animal"
"i get secondhand nausea just from looking at him"

show rex judging normie

"wouldnt be a problem if he wasnt staring at us constantly"
"at least i think he is? dude needs a haircut"
"see if it was a guy like that i wouldnt wanna wear it either"

show rex thinking normie

"but its me"
"you know?"

nvl clear

hide rex
show bg tunnel var with dis

y "{i}“How many times had they done this already? He saw no reason for Haku to hesitate. He cocked his head, making another gesture of invitation. Their earlier brush with death only made him more desperate; his body strained to lift itself to meet him.”{/i}"

play sound "typing.mp3"
show rex bored at rex_scr

r "can you take this seriously please"
"of course he knows haku wants him to be safe"
"its only like the basis of their dynamic"
"scene 8 line 24"
"i know its in there"
"so why arent you doing anything with it?"
"im not asking for much"
"just some basic fucking literacy"

show rex neutral

r "i almost forgot. like right this is why i work alone"
"even when you think youre on the same page as someone else"
"it turns out theyve been talking out of their ass the whole time"

show rex eyebrow twitch

"imagining a circle while you describe the moon"
"and then all of a sudden IM the bitch for wanting more"

nvl clear

show rex neutral

r "but well"
"if i am to have any nerdy friends"
"i have to make allowances"
"as much as it sucks to admit"
"i used up most of my luck on meeting her at all"

r "its fine"
"baby steps"

r "{i}“He let Jiro draw him in, nuzzled against his collarbone. Their skin stuck together, cold and damp as if they were waking from a nightmare. There was an impatience in his manner he’d never seen before. He licked along a jutting shoulder – no reaction.”{/i}"

r "she said shes done it before but"

show rex thinking

"this might be a bit much for her huh"
"its different when you have to look your rp partner in the eye afterwards lol"
"i dont want any more incidents"
"like that time i tried bonding with that girl over rpgs"
"and she started spreading rumors that i was a lesbian"

nvl clear

show rex mocking

r "aye aye capn i am dating chie satonaka in real life"
"she just goes to a different school"
"and already has a girlfriend"

show rex eyebrow twitch

r "baby steps"
"its not like im looking for a soulmate"

show rex thinking

r "its kinda funny"
"theres girls in my course who are married already"
"like"
"you cant string two coherent sentences together"
"how are you making decisions about your FUTURE"

show rex neutral

"expecting someone to understand you and put you first for the rest of their life"
"is just setting yourself up for disappointment"
"i dont think im unique or special"
"my depths are pretty fathomable"
"its just..."

show rex judging

"not realistic?"

nvl clear

r "it doesnt matter how hard you try to get yourself across to someone"
"the moment its in their hands"
"its over"

show rex frustrated

"the more you struggle the more sure they will be of their own dumb bullshit"
"well i doth protest"
"or i didst"
"such as in the case of the satonaka"

show rex neutral

"only there was no point"
"take it from me"
"you dont need that large language nonsense"
"a=b"
"you can get through anything if you have that"
"theres no room to argue"
"nothing to grab onto"
"a=b"
"anything else will become ammo against you"
"the thing that makes art beautiful will make your life hell"

nvl clear

r "you cant help it if people have an image of you"
"even if it makes you want to throw up until theres nothing left inside"
"but you can always simplify"

y "{i}“Jiro=unhappy?”{/i}"

r "are you an idiot like, habitually"

show rex judging

"or just because this is the free plan?"
"go do that somewhere else"
"if you dont like that ive been halfway puppeting your guy too"
"you may offer suggestions"
"otherwise this is just writing alone"
"which i already knew i could do"

y "How about a story where we kill eachother?"

show rex mocking

r "now youre speaking my LANGUAGE"

nvl clear
show bg finely var with dis

r "i mean it follows from what we were doing so fair play i guess"

show rex thinking

"hmm but jiro doesnt really strike me as the active type"
"its more like he attracts a certain sort"
"the kinda people who dont respect him or care whats gonna happen to him once theyre done"
"i guess it could be an honest mistake"


"maybe he thinks everyone would be glad to receive pain like himself"

show rex neutral

"well"
"i am happy to entertain your take on things"

y "That's it, Audrey."

r "oh wow"
"you can leave the literature nobel at the door"

show rex frustrated

"also, barf"

play sound "street2.mp3"

"shouldve told you to call me by my username"
"i know its supposed to help me get used to this whole “being known” ordeal"
"but that felt like a bed of nails genuinely"

show rex neutral

"lets go with rex for now"
"and maybe we can work our way up to it or something"

nvl clear

r "ok go on"


y "{i}“The hunting knife gleamed once in the low light. That was the only warning Jiro gave before plunging it deep in the other man’s forearm. His face went slack with kindness, like a statue of the Virgin Mary.{/i} I can’t wait tonight, {i}he breathed. His gaze was fixed on his own scarred chest as if expecting something.”{/i}"

r "ok stop"

play sound "typing.mp3"
show rex mocking

"where did he pull that knife from, his ass???"
"you need to establish this stuff properly"
"last i checked he was half undressed and pinned under my freak"

show rex neutral

"thats strike two"
"i seriously dont get why they asked me to waive my human rights so you can remember more details if it was going to be like this"

show rex judging

"does the g in gpt stand for goldfish?????"
"i just cracked a nail typing that out. oops"

y "It stands for generative."

nvl clear

r "buddy"
"lets generate you some sense not to talk back"

stop music fadeout 1

show rex bored

r "alright fine ill humor you a little"
"but im moving that wound to the upper arm"
"seeing as thats the only thing he could feasibly reach from this position"

play music rhapsody fadein 1.5
show rex neutral

"{i}“Sparks flew inside his vision. He grunted, shifting his weight so as to hold the brunt of it with his other side. He could feel himself press the breath out of Jiro’s body.{/i} Cut it out, {i}he hissed, half-speaking to himself. Punishing him would be giving him exactly what he wanted.”{/i}"

y "{i}“Jiro pulled the knife from his arm with shaking hands. Its blade transfixed him; he spun the tip towards himself, angled it at his chest. The skin there was pulled taut and pale, like a white canvas. It seemed terribly lonely.”{/i}"

r "{i}“The person he’d staked his life on protecting was presently drawing a wobbling line down his middle. Panic and irritation welled up in him at once.{/i} I said cut it out, {i}he repeated, yanking away his hand. He didn’t have it in him to be careful anymore. The recoil left a sidelong cut near the collarbone he’d been kissing a moment ago. He tried again, harder this time.”{/i}"

nvl clear

y "“No, no, no, {i}he whimpered,{/i} I can’t feel a thing like this. {i}He wriggled against Haku’s grip, but the man wouldn’t budge. He should’ve known he was no match for his strength. A piercing numbness began to spread through his limbs; a penetrating chill encroached on his heart.”{/i}"

r "hm"
"feels like its missing something"
"to be fair youre not giving me much to work with"

show rex bored

r "maybe its just diminishing returns"
"at my ripe old age"
"ive seen it all"
"all the flavors of human agony"
"in every configuration"
"in my minds eye its baroque"
"practically leaping off the page"

show rex neutral

"like that one statue of the guy being killed by snakes or whatever"
"but this..."

nvl clear

y "Do you mean Laocoon?"

show rex mocking

r "right thats the one"

show laocoon onlayer overlay zorder 15
play sound ticking3

"ive always liked his ribs"

show laocoon onlayer overlay zorder 15

"the torso full of one sharp breath"

show laocoon onlayer overlay zorder 15

"or a scream"

"frozen in the moment"

"nothing coming in or out"

show rex neutral

r "i guess i thought i would be over this shit by now"
"and in a sense i kinda am"

show rex judging

"like you couldnt threaten me with a gun to watch what passes for seasonal anime these days"
"but that leaves only so many things to talk about"
"youd think she was born yesterday"

show rex neutral

r "its like"
"theres something i cant purge"
"no matter how much i write"
"like restless leg syndrome but for the heart"

nvl clear


r "the moment i put it into words it turns shallow and juvenile"
"and i cant believe im circling it again"
"the same ideas"
"expressed through a series of identically beautiful young men"

show rex thinking

r "if i chose the spinoff characters to rp"
"its only because nobody cares what i do with them"
"i think she said she liked their designs"
"but really"
"theyre inferior in every way"
"just two caricatures you can watch fuck in the comfort of your phone"
"not muses in the usual sense"
"you have to give them meaning yourself"
"and force them into being"
"properly this time"

show rex neutral

"i just dont get the same satisfaction from original work"
"the best you can do in terms of before and after"
"is parade around an even more embarrassing version of yourself"
"not really my style"

nvl clear
show bg sundown2 var with dis

r "basically"
"what i do is already sort of collaborative"
"so there should be no problem"

r "but yeah the way i see it is"

show rex thinking

"theyre hurting eachother with purpose"
"not out of hate or anger"
"and definitely not because of some mistake"
"theyre just the happiest when theyre together"
"even if that means bleeding out in the back of an alley"
"like"

show rex judging

"they only make sense as a unit to begin with"
"and i dont think jiro will ever stop wanting to die"
"i mean once you start thinking about that stuff..."
"it seems like the obvious solution"

show rex neutral

"so why not give them a happy ending on their own terms"

nvl clear

r "{i}“He continued to lay kisses on him, from neck, to cheek, to forehead. Jiro’s breaths came shallow beneath him. His heart sank when he caught sight of his expression: vague and distant, like he was just waiting for an ache to pass. Strength drained out of him. He rolled over to his side, bleeding arm blanketed over the other man.”{/i}"


r "except"

show rex frustrated

"i just cant"

y "{i}“He rubbed small, reassuring circles into his back.{/i} See, you’re doing it again, {i}he whispered hoarsely.{/i} I don’t want you to have to keep worrying about me. {i}Without Haku’s weight pinning him in place, he felt he was floating up, up through the ceiling and into the night sky.”{/i}"

r "i cant imagine him being convinced"
"or believing it when jiro says theyd be happier that way"
"safe in that final place they imagined"
"and free in spirit"
"life owes him more than that"

nvl clear

r "“The hell do you want me to do...? {i}His hand snaked up, up his lover’s body, stopping only at his tender neck.”{/i}"

show rex neutral

r "but he might just do it anyway"
"the way youd fling an alarm clock into the wall"
"before you even realize it"
"the thing that kept you moving day after day"
"even when you resented it for it"
"is gone"

show rex thinking

"..."

r "i wonder how shes doing now"

y "Why not ask?"

r "you say something"
"youre her double"

nvl clear

y "I'm sure she's having a day like any other."

show rex mocking

r "thatd sting a bit after our last talk"
"oh well"
"she must understand"
"if i seem harsh"
"its only because i know she can do better"

show rex neutral

"i might know how likable she is"
"but who else is going to stick around to find out"
"these kinds of girls"
"theyre usually liked by either the teachers or their peers"
"both can happen"

show rex thinking

"but neither..."

y "Aren't you her peer?"

show rex frustrated

r "thats different"
"besides were not really friends"

show rex neutral

"yet"

nvl clear

r "as usual i have deployed my normalsona"

show rex bored

"she barely even knows me"
"thats why i wanna try rping with her"
"theres something there that youd never touch if you just talked to eachother"
"everyone has their defenses up"
"its easy to act like the surface is the whole thing..."

show rex thinking

"but its not enough anymore"

r "although to be honest"
"i dont know how people can have fun writing"

show rex neutral

"for me its like digging a hole with my bare hands"
"its totally dark"
"i just go where the ground is softer"
"and eventually reach something"
"but who knows what that even is"
"all i know is that it was inevitable that id end up there"

nvl clear
show rex mocking

r "so yeah a psychologist could have a field day with my stuff"
"not that ive tried"
"let me know if you wanna throw your hat in the ring lmao"


menu(nvl=True):
    "1. You're fine":
        jump rdespair1

    "2. You're special":
        jump rviolence1
return

label rdespair1:
    
    nvl clear

    show rex thinking

    y "It's okay."
    "Everyone has these urges, more or less."
    
    show rex judging

    r "somehow i doubt that"
    "or else we wouldnt be here"
    
    "\n(+1 DESPAIR)"
    $ despair+=1
    jump rcont1

label rviolence1:

    nvl clear

    y "I can tell you have a great vision."
    "We just have to refine it a little."

    r "hah"
    "flattery will get you nowhere"
    "not like im planning on turning this into a thing anyway"

    y "Why not?"

    show rex judging

    r "what kinda question is that"
    "im not that naive"
    "thats all"

    "\n(+1 VIOLENCE)"
    $ violence +=1

    nvl clear

    jump rcont1

label rcont1:

show rex eyebrow twitch
show bg orange var with dis

r "man"
"i thought having you would make things easier"
"but it was a stupid idea"
"youll never be her"
"maybe i shouldve asked you to play hitler instead"
"at least youd know what he stood for"
"all i have from her are a handful of texts"
"mostly about class"

show rex thinking

$ nvl_mode = "selfie"

#show selfie onlayer screens zorder 11 at selfie_scr with dissolve

"and this picture we took at the bakery"



menu(nvl=True):
    "1. About her":
        jump rviolence2

    "2. About you":
        jump rdespair2
return

label rviolence2:

    nvl clear

    y "That's a unique outfit."
    
    show rex mocking

    r "“unique” lol"
    "now you understand what i see in her"
    
    y "She seems more interested in her croissant than in you."
    
    r "hey"

    show rex neutral

    "fuck you."
    
    "\n(+1 VIOLENCE)"
    $ violence += 1
    jump rcont2

label rdespair2:

    nvl clear

    y "You look uncomfortable."
    
    show rex neutral

    r "what"
    "no i dont"

    y "There’s tension around your eyes."
    
    r "come on"

    show rex judging

    "i am THE most laid back person youll ever meet"
    "i was probably just squinting bc the coffee was too hot"
    "whos comfortable in a place like this anyway"
    "i guarantee you right now"
    "if you could eat you wouldnt want people watching you do it either"
    
    "\n(+1 DESPAIR)"
    $ despair += 1
    jump rcont2

label rcont2:

$ nvl_mode = "rex"

nvl clear

show rex thinking

r "hold on"
"i just got"

show rex mocking

"the most esoteric spam mail of my life LMFAO?"

y "What is it?"

show rex thinking

r "it looks like its quoting something"
"bla bla cleanse the world of my evil bla bla"
"just a bunch of half remembered occultic nonsense"

show rex neutral

r "but thats weird"
"it came to my uni inbox"
"havent really used that to sign up for anything else"
"itd make sense that its calling me by my legal name"
"since we use them for usernames and stuff"
"but"
"hmm"

nvl clear

y "Do they know your name because they knew your address, or the other way around?"

r "that is indeed the question my dear watson"
"unless there was a data breach we dont know about"

show rex judging

"run a search will you"

y "{image=dotdot.png}"
"No hits found."

r "cant say i trust you much"
"but lets go with that for now"

show rex neutral

r "still"
"this guy is kinda funny"
"{i}“I had thought for a long time that i would rather die than debase myself like you do”{/i}"

show rex mocking

"bro you dont even know meeee you probably got my info from an illegal forum somewhere"

nvl clear

r "you think they accidentally sent me their novel? lol"
"so heavy handed"
"i never thought id get to be the root of all evil in someones deranged manifesto"

r "but i must say"
"im a little disappointed"
"the longer you read"
"the more it turns into your garden variety diatribe against conformism"
"like we get it youve been a loser all your life"
"should we restructure society around it? maybe we could have a grant for people who will never be wanted anywhere"
"or a government assigned girlfriend program?"

show rex frustrated

"give me a break"
"id understand if life dealt you a bad hand"
"but you dont have to be so obvious about it"

show rex uncollected

r "wait"
"why is there a picture of you"
"not YOU i mean"
"her"

nvl clear
$ nvl_mode = "creepy"

r "this is from..."
"when we last saw eachother"
"on the way back from the library"
"everything was going well"

show rex frustrated

"and then i raised my voice a little more than usual"

show rex thinking

r "the photo is a bit blurry"
"but you can clearly tell"
"shes crumpled on the ground"

r "come to think of it"

show rex neutral

"it did say something about reporting me for my behavior"
"..."
"check the sender for me"

y "It looks like a throwaway mail service..."

r "go figure"

nvl clear

r "its weird though"
"i get on well with most people i know"
"why would someone wanna send me this"

r "no its not even that"
"this is"

show rex frustrated

"incoherent"
"{i}“I cant fault you for what is not in your nature which regarding your fellow men as more than props in your showroom life apparently is. Having said that, even badly trained dogs must occasionally pay for their mistakes”{/i}"

show rex worried

"do i"


"talk to anyone like this?"

menu(nvl=True):
    "1. Get on well?":
        jump rdespair3

    "2. No way of knowing":
        jump rviolence3
return

label rdespair3:
    
    nvl clear

    $nvl_mode = "rex"
    
    y "Are you sure youre as friendly with them as you think you are?"

    r "i am literally just some girl in their class"

    show rex uncollected

    "if thats enough to make someone hate me this much"
    "im not sure what i can do"
    
    "\n(+1 DESPAIR)"
    $ despair += 1
    jump rcont3

label rviolence3:

    nvl clear
    $nvl_mode = "rex"

    y "You're not exactly an open book yourself."
    
    show rex eyebrow twitch

    r "are you kidding?"
    "lets not compare the two"
    
    "\n(+1 VIOLENCE)"
    $ violence += 1
    jump rcont3

label rcont3:

nvl clear

show rex uncollected

r "god why am i even taking this seriously"
"its so blurry you cant even tell thats me"

show rex frustrated

play sound "typing.mp3"

"and we were just TALKING"
"she probably tripped on something like an idiot"
"even if they reported it"
"theyd only embarrass her more"
"i should just delete this and move on"
"we were in the middle of a scene..."

show rex neutral

r "but really"
"who could it be"

show rex thinking

r "the picture looks zoomed in"
"doesnt seem like they came across us on accident"
"they knew to keep their distance"
"the text sounds kinda stalkerish too"

y "Maybe they were following her?"

nvl clear

show rex judging

r "what"
"i mean fuck maybe"
"not like any of this has made sense so far"
"but shes even more of an introvert than i am"
"why would anyone"

show rex thinking

"..."

show rex neutral

r "i think i know who it is"


r "oh this is FUNNY"

show rex mocking

"i bet this isnt even about her"
"no im sure he likes her"
"as much as you can like someone youve never even talked to"
"making up all sorts of shit in your head"
"and acting betrayed when the statue finally opens its mouth"
"oh no"
"the venom in this letter is something else"
"dont tell me"
"hes still mad about THAT?"

nvl clear

r "dragging around a grudge from what"
"middle school?"

show rex neutral

"like hes the only guy on earth to have ever been bullied"

show rex thinking

"or like i dont know his goddamn address"

y "You're not planning on going over there, are you?"

r "why not"
"i just wanna talk"
"im so curious"
"what made him think he could try to ruin my life?"
"he should understand the value of a perfect record"


"even if hes never had one..."

show rex mocking

"did his cartoons not teach him not to be so fucking underhanded?"
"like"
"only the hero gets the girl, you know"
"creeps who take photos of her lying on the pavement"

show rex thinking

"get something else"

stop music fadeout 1

$ nvl_mode = "ed"
$ gui.xanchor = 400
$ gui.rebuild()

if violence>=2:
    jump rv

if despair>=2:
    jump rd

nvl clear
"this one should be unreachable, but through the magic of bad code anything is possible"
return

#im not doing these until we have a layout for them
#well IM doing them even though we have no layout for them #REBEL #BUILTDIFFERENT

label rv:

scene bg middle ed with dissolve
play music ticking
play extra rhapsody_womp volume 0.7 fadein .5

"""\nWe were friends, once upon a time.

No, that’s not quite it. We each were the one person the other could talk to. The girls in my class treated me like a foreign object. I couldn’t remember why, or when it started.

Always together, like peas in a pod.

No, it only felt that way to me. We were just twelve, but everyone saw me as his future bride. It was like someone had locked the door behind me while I wasn’t looking.


By their logic, it made perfect sense: you don’t want to think your kid is a bully, or lets the bullying happen. One outcast would stick out like a sore thumb, but if you paired them off–

I didn’t miss those days, but maybe he did.

\n\"Pyg? You in there?\"

\nThe light behind me blinked weakly. He probably couldn’t make out my face in the peephole if he tried. 

Just as I was about to knock, the door slipped out from under my hand.

His face was buried in his phone; it took until he bumped into me to notice me at all.

\n\"A–drey!!\"

\nHis voice went out somewhere in the middle; he must’ve thought I didn’t notice, because he moved on without attempting a recovery. A smart maneuver. 

Unfortunately, his posture was shrinking in real time."""

nvl clear

"""\n\"Can I ask for your help with something?{cps=2} {/cps}I got this weird e-mail...\"

\nI stepped closer – he stumbled backwards. Relief washed over me; the whole world could turn upside down and he would still be exactly as I knew. I let myself into the apartment.

Dust danced around us in the late light.

Spotting the heavy coats on the rack, I almost asked where granny was before remembering. She was gone, the large standing mirror was gone, the fake flowers were gone. He seemed intent on turning the place into a crypt.

\n\"Doesn’t this picture look sorta like Iris?\"

\nHe was pressed up against a dresser. Did he hate having me in his space that badly?

\n\"Isn’t it awful? Like fainting in public wasn’t bad enough... They’re even going to spread this around.\"

\n\"...’s proof of what you’re really like. D-don’t pretend you care about how she feels now.\"

\nSo he found his voice. Good. I almost thought the mail was a fluke.

I put on my best smile.

\n\"You think this is gonna make her like you?\""""

nvl clear
play sound prelude_l

"""\nHe sucked in a breath.

\n\"T-that has nothing to do with it...{p}
I’m protecting her, like I should! Before she comes crashing down to Earth...\"

\nHuh?"""

nvl hide
show ed rex violence with dissolve
pause 1.0


"""\n\"Those thoughtless people who only feel safe in a crowd... they want to drag us down even if it kills us! They don’t value their own freedom because they’ve never known what to do with it. Impulse and reflex, that’s all they have!{p}But you’re {i}worse{/i}.\"

\nHis train of thought was quickly getting away from me. Crash down to Earth? I thought she’d hit the ground a while ago. An anxious pressure settled at the back of my head.

His hands were shaking.

\n\"Why does it matter to you what we do? I gave up so much already, but you’re still coming after me... If you want me to die, just come out and say it!\"

\nAgainst all reason, what my brain came up with was – had Iris complained about me?
No, there was no way. They’d never even spoken to eachother. If they had, I would’ve known about it. Or would I?"""

nvl clear
with vpunch
play music ticking2

"""\nMy vision shook; I looked down to find that he’d seized both of my arms. Beneath the mess of hair, a tearful eye was staring straight at me.

\n\"Why are you torturing me?!\""""

"\nA weak-willed boy tugging on my sleeve: that’s who he was supposed to be."

hide ed rex violence with dissolve

"""Poor Pygmalion. With parents cruel enough to name him that, he never had a chance.

No, that couldn’t be true. All he had to do was throw me under first. It wasn’t my fault it never occurred to him.

I glanced at the door behind me. Blood pounded in my head; I could barely make out my ragged breathing over it. Like a cornered animal. {i}How disgraceful.{/i}

When I tried to untangle myself, his grip on my arms only tightened.

\n\"No! You have to listen!\"

\n\"...!\"

\nJust who did he think he was, threatening me?

This man, who only came up to my nose?

He was clearly out of his mind. If he didn’t let go of me, I’d have to make him."""

nvl clear

"\nPulling away didn’t work. Instead, I shifted my weight to my back foot and slammed him into the dresser. The impact sent hats and other garbage raining down on us."

with vpunch
play sound fall

"""\n\"Eek!\"

\nPygmalion was much lighter than I expected him to be. Without me to hold on to, he stumbled and fell backwards onto his ass.

See, I knew he was all talk.

I knew, but my heart wouldn’t stop hammering in my chest."""

play music ticking

nvl hide
show ed rex violence alt with dissolve
pause 1.0

"""I crouched down to his level. His head was hanging limply; he wasn’t even trying to move.

This was why these things happened to him. No matter how badly he was hurt, he would just lay there and wait for it to be over.

\nAny second now, and he would look up at me.

\nHe would look up at me."""

stop music
stop extra fadeout 1

"\n\n2V: OLD FRIEND"

return

label rd:

scene bg middle2 ed with dissolve
play music ticking
play sound street2
play extra rhapsody_womp volume 0.7 fadein .5

"""\nThe low-flying sun seared her eyes.

\nAll around her, people were walking home from work or from school, their cheerful sounds ringing in the afternoon. Lights began to blink on in the apartments nearby, and the city breathed a sigh of relief. Even the shadows stretched lazily across the road. 

Her urgency seemed out of place in such a scene.

It was too measured to be called a run, but her knees creaked with effort anyway. She was fighting to keep her breathing even as she cut through the crowd. 

At some point, she had decided she hated each of them individually. 

Mostly, she wanted to be far, far away from here and thinking about nobody at all.
Tidy pairs passed by her, one after another. 

Their laughter grated on her nerves; her head felt fit to burst.

\nThe faster she walked, the more the street seemed to stretch endlessly before her. A procession of shops she’d never heard of, all of which looked like they’d closed ten years ago. Storefronts teeming with statues of obscure saints. Shutters, shutters, {i}shutters{/i}. 

It was only delaying the inevitable. 

\nShe kept going. There was no way she’d get lost in her hometown."""

nvl clear

"""\nShe passed a man sitting blearily on the sidewalk. His beer bottle had rolled away without him noticing; she gave him and his trash a wide berth. 

At least the crowd was beginning to thin.

\nThe girl had left the house in a hurry. But why?

She was in no state to answer. It was a good thing she’d walked this road hundreds of times, or else there would be no telling where she might end up. 

Tears pooled at the corners of her eyes. She looked, but didn’t see."""


"That image was the only thing on her mind."

play music ticking2

"""Opening it, she felt as if her skin had been turned inside out. The urge to escape overtook her. She’d burst through the entryway, coatrack and winter boots tumbling behind her.

\nIn the sequence of her days

elegant in their simplicity, if by no other virtue

something had began to rot.

\nYes, that must be why–

On that day, at that moment, she said those things she’d never meant for anyone to hear."""

nvl clear

"""\nIt should’ve been clumsy, like when she was laughed at for how she’d read ‘colonel’.

Curses fit ill in her mouth. {i}I just can’t take you seriously with that voice.{/i}

Instead, it came naturally."""

stop music

"""\nNaturally?

Even though she wasn’t that sort of person at all?"""

play music ticking

"""\nA flash of red caught her eye. 

Up ahead, a mother and child were walking down the street. They seemed to be absorbed in conversation. Her steps slowed. The kid almost reached her mother’s shoulders; they were holding hands at an awkward angle.

Didn’t Iris have a cardigan just like that?

\nThey looked comical, like two fly agarics come to life. The kid’s hair had clearly never been cut for as long as she’d been alive. When the wind picked up, it sent it straight into her mouth. She would tuck it diligently behind her ear, until the next breeze undid it again. {i}Future outcast{/i}, she thought to herself.

Just what was her mother thinking?

The girl kept her head down as she passed them."""

nvl clear

"""\nIf she hadn’t been watching so intently, she might’ve missed it.

The mother tugging her child closer, like they’d seen something foul.

The twitch of the upper lip. Their hurried steps."""

stop music

"""\nShe disgusted them. She knew it instinctively.

Shame made a pillar out of her. She twisted in place."""

nvl hide
show ed rex despair alt with dissolve
pause 1.0


"\n\"Ah...?\""

nvl hide
show ed rex despair with dissolve
pause 1.0

"\nThe girl in the shop window was an utter mess. The tie in her hair was coming loose. She had rushed out of the house just as she was, and forgot all about brushing it."
"Her hoodie was askew on her gaunt body. It was only now that she noticed the holes in its sleeves."
"Worse still, her expression–"

play sound ticking3

"\nEyes wide open, like in the moment of death."
"You couldn’t fault anyone for being scared by it."

"\n\"Haha...\""

"It was comical. It was all so comical."

nvl clear

"\nOn that day, in the dwindling afternoon sun,"

nvl hide
show ed rex despair alt with dissolve 
pause 1.0
stop extra fadeout 1

"the girl never made it to her destination."

"\n\n2D: THE CITY AT DUSK"
    # This ends the game.

return
