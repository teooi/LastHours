init python:
    class ZoomCharacter(object):
        def __init__(self, *args, **kwargs):
            self.chr = renpy.character.Character(*args, **kwargs)
            if not self.chr.image_tag:
                raise Exception('A ZoomCharacter must have an image')

        def __call__(self, *args, **kwargs):
            if not hide_char_dark:
                renpy.show(self.chr.image_tag, at_list=[presayzoom], zorder=10)
            self.chr(*args, **kwargs)
            if not hide_char_dark:
                renpy.show(self.chr.image_tag, at_list=[postsayzoom], zorder=0)

transform presayzoom:
    ease 0.25 zoom 1.02

transform postsayzoom:
    ease 0.25 zoom 1.0

# CHARACTERS
define char_name = "Player"
define char = Character(char_name, color="#FFFFFF")

define james = ZoomCharacter("James", color="#87CEEB", image="james_portrait")
define daniel = ZoomCharacter("Daniel", color="#FF5733", image="daniel_portrait")
define wendy = ZoomCharacter("Wendy", color="#FFB6C1", image="wendy_portrait")
define phoebe = ZoomCharacter("Phoebe", color="#9370DB", image="phoebe_portrait")

# Define Character Images
image daniel_portrait = "images/portraits/doctor-portrait.png"
image wendy_portrait = "images/portraits/doctors_wife_portrait.png"
image james_portrait = "images/portraits/journalist_portrait.png"
image phoebe_portrait = "images/portraits/ps_portrait.png"

# Backgrounds
image bg mansion = "images/bg/mansion_bg.png"
image bg black = "images/bg/black_bg.png"
image bg bedroom = "images/bg/bedroom-bg.png"
image bg bathroom = "images/bg/bathroom-bg.png"
image bg dining = "images/bg/dining-bg.png"


# Custom Menu
screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.75  # Move the choices lower (default is usually 0.5)
        spacing 10  # Space between choices

        for i in items:
            textbutton i.caption action i.action

# Character Trackers
default talked_to_daniel_before_death = False
default talked_to_wendy_before_death = False
default talked_to_james_before_death = False
default talked_to_phoebe_before_death = False

default lights_out = False
default hide_char_dark = False

default dining_hall_first_entry = True

default phoebe_death = False

# EFFECTS CONFIG
transform blur_effect:
    blur 2 

transform chem_position:
    xalign 0.5  
    yalign 0.3

transform character_far_left:
    xalign 0.0
    yalign 1.0

transform character_left:
    xalign 0.2
    yalign 1.0

transform character_center:
    xalign 0.5
    yalign 1.0

transform character_right:
    xalign 0.8
    yalign 1.0

transform character_far_right:
    xalign 1.0
    yalign 1.0

# START OF THE GAME LABEL

label start:

    stop music fadeout 3.0

    play sound "audio/sfx/rain_thunder.mp3" fadein 3.0 loop
    $ renpy.sound.set_volume(0.1, channel="sound")

    scene bg black with fade

    "Before we begin, what is your name?"

    $ char_name = renpy.input("Enter your name:", default="Player")
    $ char_name = char_name.strip() or "Player"
    $ char = Character(char_name, color="#FFFFFF")

    "Welcome, [char_name]. The storm rages as you arrive at the mansion."

    stop sound fadeout 1.0

    window hide

    jump daniel_greeting


# IMAGE MAPS FOR DIFFERENT SCENES

# Main hall scene
screen main_hall():
    frame:
        background Solid("#000000")  # Dark background
        xfill True
        yfill True

    if lights_out:
        add "images/bg/floor-one-main-dark.png" fit "contain" xalign 0.5

        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("dining_hall", transition=fade)]
            xpos 1100
            ypos 550
            at Transform(zoom=0.25)

        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("bedroom_dark", transition=fade)]
            xpos 460
            ypos 150
            at Transform(zoom=0.25, rotate=-90)

    else:
        add "images/bg/floor-one-main.png" fit "contain" xalign 0.5

        # Image Buttons (Characters) during normal lighting
        imagebutton:
            idle "images/walks/doctor-walk/doctor-stand.png"
            hover "images/walks/doctor-walk/doctor-stand-hover.png"
            # action [Hide("main_hall"), Jump("daniel_greeting")]
            xpos 680
            ypos 750
            at Transform(zoom=0.3, rotate=-0.3)

        imagebutton:
            idle "images/walks/journalist-walk/james-stand.png"
            hover "images/walks/journalist-walk/james-stand-hover.png"
            action [Hide("main_hall"), Jump("james_greeting")]
            xpos 460
            ypos 250
            at Transform(zoom=0.3, rotate=.3)

        imagebutton:
            idle "images/walks/phoebe-walk/phoebe-stand.png"
            hover "images/walks/phoebe-walk/phoebe-stand-hover.png"
            action [Hide("main_hall"), Jump("phoebe_greeting")]
            xpos 1100
            ypos 150
            at Transform(zoom=0.3, rotate=-.4)

        # Arrow Button (Return to dining hall screen with fade)
        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("dining_hall", transition=fade)]
            xpos 1100
            ypos 550
            at Transform(zoom=0.25)

screen dining_hall():
    frame:
        background Solid("#000000")  # Keep it dark
        xfill True
        yfill True

    add "images/bg/floor-one-dining-dark.png" fit "contain" xalign 0.5 at blur_effect

    if dining_hall_first_entry:
        timer 0.1 action [Hide("dining_hall"), Jump("dining_room_cutscene")]

    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("dining_hall"), Show("main_hall", transition=fade)]
        xpos 250
        ypos 400
        at Transform(zoom=0.25, rotate=180)

    if not phoebe_death:
        # Phoebe (Dining Hall)
        imagebutton:
            idle "images/walks/phoebe-walk/phoebe-stand-dark.png"
            hover "images/walks/phoebe-walk/phoebe-stand-hover-dark.png"
            action [Hide("dining_hall"), Jump("phoebe_dining_scene")]
            xpos 300
            ypos 150
            at Transform(zoom=0.42, rotate=-.4)

screen bedroom_dark():
    frame:
        background Solid("#000000") 
        xfill True
        yfill True

    add "images/bg/bedroom-dark.png" fit "contain" xalign 0.5

    # Wendy (bedroom)
    imagebutton:
        idle "images/walks/wife-doctor-walk/doctor-wife-stand-dark.png"
        hover "images/walks/wife-doctor-walk/doctor-wife-stand-hover-dark.png"
        action [Hide("bedroom_dark"), Jump("wendy_bedroom_scene")]
        xpos 1125
        ypos 175
        at Transform(zoom=0.55, rotate=0.2)

    # Go to main hall 
    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("bedroom_dark"), Show("main_hall", transition=fade)]
        xpos 1175
        ypos 700
        at Transform(zoom=0.4, rotate=90)

    # Go to bathroom
    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("bedroom_dark"), Show("bathroom_dark", transition=fade)]
        xpos 830
        ypos 0
        at Transform(zoom=0.4, rotate=-90)

screen bathroom_dark():
    frame:
        background Solid("#000000")
        xfill True
        yfill True
    
    add "images/bg/bathroom-dark.png" fit "contain" xalign 0.5

    # Back to bedroom
    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("bathroom_dark"), Show("bedroom_dark", transition=fade)]
        xpos 700
        ypos 650
        at Transform(zoom=0.45, rotate=90)

    # Phoebe (bathroom)
    imagebutton:
        idle "images/deaths/phoebe-death-dark.png"
        hover "images/deaths/phoebe-death-dark-hover.png"
        action [Hide("bathroom_dark"), Jump("phoebe_death")]
        xpos 200
        ypos 100
        at Transform(zoom=0.65, rotate=0.2)

# BEFORE THE FIRST DEATH DIALOGUE AROUND THE MAP

label daniel_greeting:

    play voice "audio/sfx/doorclose2.mp3" 
    $ renpy.sound.set_volume(0.2, channel="voice")

    play sound "audio/sfx/rain_inside.ogg" fadein 1.0 loop

    scene bg mansion with fade

    show daniel_portrait at character_center with dissolve

    daniel "Finally! I was beginning to think you couldn’t make it."

    daniel "The weather is not the best today. They say that the chances of a heavy snowstorm are very high tonight."

    daniel "But no worries! Now that you have arrived in my mansion, our safety is guaranteed. I can promise you that!"

    hide daniel_portrait
    jump mansion_intro_before_death

label mansion_intro_before_death:

    # scene bg mansion with fade

    show wendy_portrait at character_center with dissolve

    wendy "So nice to see you again, [char_name]! It has been too long!"

    wendy "My husband and I were just talking about you!"

    hide wendy_portrait with fade
    show daniel_portrait at character_center with dissolve

    daniel "Oh, so you two were talking about me? Hopefully, only good things!"

    hide daniel_portrait
    show daniel_portrait at character_left with dissolve
    show wendy_portrait at character_right with dissolve

    wendy "I have heard that you are working for the city now. I wonder how your work environment may compare to our own?"

    menu:
        "Ask about their work":
            jump ask_work_before_death
        "Tell them about your work":
            hide daniel_portrait 
            jump tell_work_before_death

label ask_work_before_death:

    show daniel_portrait at character_left with dissolve
    show wendy_portrait at character_right with dissolve

    daniel "Well, as you may have seen on TV, I’m endorsing a new product for nutrition supplements."

    daniel "You know, it is good for preventing cardiovascular disease and boosting your immune system."

    daniel "You should totally give it a try! In fact, I can send some of it directly to you at a later date!"

    wendy "Daniel has been really busy lately trying to balance between his hospital work and these commercial deals."

    wendy "I often have to step in to take care of the hospital side for him."

    daniel "I told you countless times not to do my work for me!"

    daniel "You are going to mess things up!"

    hide wendy_portrait
    hide daniel_portrait
    call screen main_hall

label tell_work_before_death:

    show wendy_portrait at character_center with dissolve

    wendy "I have always known that you have a righteous mind."

    wendy "To think you became a forensic pathologist to help bring justice to society."

    hide wendy_portrait
    show daniel_portrait at character_center with dissolve

    daniel "Don’t say that! You know very well that patients depend heavily on us."

    hide daniel_portrait
    show wendy_portrait at character_center with dissolve

    wendy "In spite of my fears, I always do my best to save everyone!"

    hide wendy_portrait
    call screen main_hall



## JAMES GREETING    


label james_greeting:

    scene bg mansion 

    show james_portrait at character_center with dissolve

    james "[char_name]! I never expected to see you of all people!"
    james "How long has it been? Two years?"

    james "So, how is this murder case you're working on?"
    james "Did you manage to figure out how the victim was killed?"

    james "Hmm... you're wondering how I know about that?"
    james "We haven’t seen each other in so long, after all."

    james "Behold! You stand before the greatest journalist of our generation!"
    james "No secrets can escape my grasp! Hahaha!"

    james "I know for a fact you work in the city coroner's office."
    james "Apparently, you're one of their best forensic experts too!"

    james "I guess it's only fair to tell you what I've been up to."
    james "Running around the city, chasing stories all day—it can be exhausting."

    james "But honestly? I love this job!"
    james "I never realized I had what it takes to be a good journalist."

    james "With my medical background, my boss had me focus on health topics."
    james "I get to speak to experts at their level, and people trust my work."

    james "Readers say my articles are scientific, reliable, and easy to understand."
    james "That’s pretty rewarding, you know?"

    james "Hey! You know what?"
    james "I should definitely interview you at some point!"

    james "I’m not sure if it’s newsworthy..."
    james "But it’s a great excuse to finally reconnect!"

    james "Let me know when you have time, okay?"

    hide james_portrait with fade

    call screen main_hall


## PHOEBE GREETING


label phoebe_greeting:

    scene bg mansion 

    show phoebe_portrait at character_center with dissolve

    phoebe "…….."

    menu:
        "Leave her alone":
            jump phoebe_leave
        "Try saying 'Hi'":
            jump phoebe_hi

label phoebe_leave:

    image bag_of_chemicals = "images/items/unlabeled-vial.png"

    show phoebe_portrait at character_center with dissolve

    phoebe "That smell… I recognize it."
    phoebe "The citrus scent is likely coming from limonene or linalool."
    phoebe "Mixing that with aldehydes can further enrich its profile."

    # Swap to the blurred Phoebe portrait before showing the vial
    hide phoebe_portrait
    show ps_portrait_blur at character_center

    # Show the vial in focus
    show bag_of_chemicals at chem_position with fade
    pause 1.5

    # Hide both the vial and the blurred Phoebe, then restore normal Phoebe
    hide bag_of_chemicals with fade
    hide ps_portrait_blur with dissolve
    show phoebe_portrait at character_center with dissolve

    phoebe "Yes… This is quite nostalgic."
    phoebe "So you are still wearing the same cologne from two years ago."

    phoebe "It reminds me of simpler days, when we all studied chemistry together."

    menu:
        "I remember you were really good at chemistry!":
            jump phoebe_chemistry
        "I am so bad with chemistry though…":
            jump phoebe_bad_chemistry


label phoebe_chemistry:

    phoebe "I find it absolutely fascinating!"
    phoebe "It’s the study of matter and change, which can be observed all around us!"
    phoebe "Think of all the possibilities!"

    phoebe "You can shape reality to your will with just the smallest amount of the right chemicals."
    phoebe "And it couldn’t be more accurate in the case of human biology."

    phoebe "Anything we take into our body can make or break us."
    phoebe "There are still so many unknown aspects."

    phoebe "With my pride as a pharmaceutical scientist, I will unlock the secrets to it all!"
    phoebe "It doesn’t get more exciting than this!"

    phoebe "Having a smell of your cologne and talking about chemistry actually reminded me of something related to my current research."
    phoebe "I need to immediately sort things out before the ideas elude me."
    phoebe "If you’ll excuse me."

    hide phoebe_portrait
    call screen main_hall

label phoebe_bad_chemistry:

    phoebe "That can’t be true."
    phoebe "I am aware of your job as a forensic pathologist."
    phoebe "You need to use the correct chemicals and precise doses to produce accurate results."

    phoebe "In fact, I have been trying to develop new formulas for testing various types of rare poison."
    phoebe "It may come in handy in your work one day."

    phoebe "Here, I will send you some files."

    # Display a message about obtaining research papers
    $ renpy.notify("Obtained research papers on poison detection.")

    phoebe "These documents discuss developing new reagents for poison detection."
    phoebe "It involves using organic extracts from plants such as red cabbage, turmeric, and hibiscus."

    phoebe "You must let me know your thoughts when you finish reading!"

    hide phoebe_portrait
    call screen main_hall

label phoebe_hi:

    phoebe "……"
    
    # Phoebe appears absorbed in her thoughts
    "She looks absorbed in her thoughts, staring at her notes."

    hide phoebe_portrait
    call screen main_hall


label dining_room_cutscene:

    if not dining_hall_first_entry:
        call screen dining_hall
        return

    $ dining_hall_first_entry = False
    $ lights_out = True

    scene bg dining 

    show wendy_portrait at character_center with dissolve
    wendy "Everyone, dinner is ready! Let’s gather around the table."

    hide wendy_portrait
    show daniel_portrait at character_left with dissolve
    show james_portrait at character_right with dissolve

    daniel "Took you long enough! I am starving!"
    james "Ohhh! All the dishes look so good! I can’t wait to dig in."

    hide daniel_portrait
    hide james_portrait
    show phoebe_portrait at character_center with dissolve

    phoebe "Ah yes! 375 degrees, the perfect temperature for baked chicken."
    phoebe "The golden brown color of the skin comes from the Maillard reaction between amino acids and reduced sugar."
    phoebe "The proteins, including collagen and myosin, break down to create its new texture."
    phoebe "The fat melts to keep the meat moist and lock in flavors. Truly marvelous!"

    hide phoebe_portrait
    show james_portrait at character_center with dissolve
    james "Come on, Phoebe! Stop reminding me of these terminologies I had to learn in class!"
    james "The nightmares are coming back to me!"

    hide james_portrait
    show daniel_portrait at character_center with dissolve
    daniel "I can see she's still a walking textbook!"
    daniel "Surely her intellect makes dinner conversations much more amusing than simple small talk."

    hide daniel_portrait
    show wendy_portrait at character_center with dissolve
    wendy "No matter what, having this long-awaited reunion is something to cherish!"
    wendy "I especially want to hear more from [char_name]."
    wendy "We haven't seen you in nearly a decade!"

    hide wendy_portrait

    scene bg black with Fade(0.5, 0.5, 0.5)
    # play sound "audio/sfx/snowstorm.mp3" fadein 2.0 loop

    $ hide_char_dark = True

    james "A sudden blackout? I thought you took pride in this place, Daniel."

    daniel "Oh, shut it! Heavy snow may have destroyed nearby power lines."
    daniel "It has nothing to do with my house!"

    wendy "I'll go find candles to light up the room!"

    phoebe "Can't we just use our phones for light?"
    phoebe "Oh no! Looks like there's no signal."

    wendy "Just our phone lights won't be enough."
    wendy "I'll find candles to properly illuminate the room. Don't worry, I'll be right back."

    james "Hehe, it just so happens I need to use the bathroom."
    james "Could someone guide me?"

    daniel "Alright, James, come with me to the bathroom while Wendy finds candles."

    "(James and Daniel leave off screen)"

    phoebe "I'll just wait here and resume my research until you all return."

    $ hide_char_dark = False

    stop sound fadeout 2.0

    call screen dining_hall

# LIGHTS ARE NOW OFF

label phoebe_dining_scene:

    scene bg dining
    show phoebe_portrait at character_center with dissolve

    phoebe "Don’t mind me. I am just doing my work here, and I really need to concentrate."
    
    phoebe "If you feel bored, maybe you can go around and check on the others?"

    hide phoebe_portrait

    call screen dining_hall

label wendy_bedroom_scene:

    scene bg bedroom
    show wendy_portrait at character_center with dissolve

    wendy "I could have sworn I put some candles around here. The lighter too… Where could it be?"
    
    wendy "It’s so difficult trying to find these things in total darkness!"

    wendy "Oh, [char_name]! Did you come here looking for Daniel or James? They both went into the bathroom. You can check on them if you want."
    
    wendy "It must be difficult trying to use the bathroom in this total darkness."

    hide wendy_portrait
    call screen bedroom_dark

# PHOEBE DEATH
label phoebe_death:

    scene bg bathroom

    show james_portrait at character_far_left with dissolve
    show daniel_portrait at character_far_right with dissolve
    show wendy_portrait at character_center with dissolve

    $ phoebe_death = True

    james "What happened?"

    daniel "No pulse. No breathing."
    daniel "Phoebe... She is... dead..."

    wendy "How could this be?"

    james "We need to contact the police straight away!"
    james "Ah! But there is no signal due to the storm."
    james "It just had to be at a time like this!"

    daniel "There's no visible wound."
    daniel "It could only be poison."
    daniel "Look at the kit she carried with her right over there."
    daniel "One of the vials is spilled all over the table."

    wendy "I can’t wrap my head around this."
    wendy "Did she accidentally kill herself with poison?"
    wendy "But why would she bring something like that?"

    daniel "It’s Phoebe we're talking about."
    daniel "We know her hobbies are gardening and botany."
    daniel "She would extract different substances from plants."
    daniel "It's hard to say if she went beyond and messed with poisonous plants."

    james "I find it unlikely."
    james "Someone brilliant like her wouldn't be so careless."
    james "For all we know, this could be murder disguised as an accident!"

    daniel "You can't be serious."
    daniel "Are you accusing one of us of murder?"

    james "I'm only speaking of possibilities here."
    james "At this point, there’s nothing we can say without further examination."
    james "I believe it’s best to leave this to our forensic expert, [char_name]."

    hide james_portrait
    hide daniel_portrait
    hide wendy_portrait

    call screen main_hall 

