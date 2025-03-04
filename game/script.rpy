# CHARACTERS
define char_name = "Player"
define char = Character(char_name, color="#FFFFFF")

define daniel = Character("Daniel", color="#FF5733")
define wendy = Character("Wendy", color="#FFB6C1")
define james = Character("James", color="#87CEEB")
define phoebe = Character("Phoebe", color="#9370DB")


# Define Character Images
image daniel_portrait = "images/portraits/doctor-portrait.png"
image wendy_portrait = "images/portraits/doctors_wife_portrait.png"
image james_portrait = "images/portraits/journalist_portrait.png"
image phoebe_portrait = "images/portraits/ps_portrait.png"

# Backgrounds
image bg mansion = "images/bg/mansion_bg.png"
image bg black = "images/bg/black_bg.png"


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

# EFFECTS CONFIG
transform blur_effect:
    blur 2 

transform chem_position:
    xalign 0.5  
    yalign 0.3

transform character_center:
    xalign 0.5  
    yalign 1.0 

transform character_left:
    xalign 0.1  # Moves character to the left
    yalign 1.0

transform character_right:
    xalign 0.9  # Moves character to the right
    yalign 1.0

# START OF THE GAME
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


screen image_map():
    frame:
        background Solid("#000000")  # Keep it dark
        xfill True
        yfill True

    add "images/bg/floor-one-main.png" fit "contain" xalign 0.5 at blur_effect

    # Image Buttons (Characters)
    imagebutton:
        idle "images/walks/doctor-walk/doctor-stand.png"
        hover "images/walks/doctor-walk/doctor-stand-hover.png"
        # action [Hide("image_map"), Jump("daniel_greeting")]
        xpos 680
        ypos 750
        at Transform(zoom=0.3, rotate=-0.3)

    imagebutton:
        idle "images/walks/journalist-walk/james-stand.png"
        hover "images/walks/journalist-walk/james-stand-hover.png"
        action [Hide("image_map"), Jump("james_greeting")]
        xpos 460
        ypos 250
        at Transform(zoom=0.3, rotate=.3)

    imagebutton:
        idle "images/walks/phoebe-walk/phoebe-stand.png"
        hover "images/walks/phoebe-walk/phoebe-stand-hover.png"
        action [Hide("image_map"), Jump("phoebe_greeting")]
        xpos 1100
        ypos 150
        at Transform(zoom=0.3, rotate=-.4)

    # Arrow Button (Return to the image_map screen with fade)
    imagebutton:
        idle "images/ui/arrow-right.png"
        hover "images/ui/arrow-right-hover.png"
        action [Hide("image_map"), Show("image_map", transition=fade)]
        xpos 1100
        ypos 550
        at Transform(zoom=0.25)

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
    call screen image_map

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
    call screen image_map



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

    call screen image_map


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
    call screen image_map

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
    call screen image_map

label phoebe_hi:

    phoebe "……"
    
    # Phoebe appears absorbed in her thoughts
    "She looks absorbed in her thoughts, staring at her notes."

    hide phoebe_portrait
    call screen image_map


# label dining_room_cutscene:

#     scene bg dining_room with fade

#     show wendy_portrait at character_center with dissolve

#     wendy "Everyone, dinner is ready! Let’s gather around the table."

#     hide wendy_portrait
#     show daniel_portrait at character_left with dissolve
#     show james_portrait at character_right with dissolve

#     daniel "Took you long enough! I am starving!"

#     james "Ohhh! All the dishes look so good! I can’t wait to dig in."

#     hide daniel_portrait
#     hide james_portrait
#     return

# label mansion_exploration:

#     scene bg dark_mansion with fade

#     "You can freely explore the mansion with limited sight using your flashlight."

#     menu:
#         "Go to the dining room":
#             jump dining_room_explore
#         "Go to the bedroom":
#             jump bedroom_explore
#         "Go to the bathroom":
#             jump bathroom_explore
#         "End exploration":
#             jump advance_story

# label dining_room_explore:

#     scene bg dining_room_dark with fade

#     show phoebe_portrait at character_center with dissolve

#     phoebe "Don’t mind me. I am just doing my work here, and I really need to concentrate."

#     phoebe "If you feel bored, maybe you can go around and check on the others?"

#     hide phoebe_portrait
#     jump mansion_exploration

label advance_story:

    "Having talked to everyone, you feel a strange sense of unease..."

    return