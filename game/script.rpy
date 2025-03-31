# CHARACTERS -------------------------------------------------------------------
define char_name = "Player"
define char = Character(char_name, color="#FFFFFF")

define james = Character("James", color="#FF0000", callback=name_callback, cb_name="james") 
define daniel = Character("Daniel", color="#0080FF", callback=name_callback, cb_name="daniel") 
define wendy = Character("Wendy", color="#FFB6C1", callback=name_callback, cb_name="wendy")  
define phoebe = Character("Phoebe", color="#800080", callback=name_callback, cb_name="phoebe") 

# Define Character Images ------------------------------------------------------
image daniel normal = At("images/portraits/doctor-portrait.png", sprite_highlight("daniel"))
image wendy normal = At("images/portraits/doctors-wife-portrait.png", sprite_highlight("wendy"))
image james normal = At("images/portraits/journalist-portrait.png", sprite_highlight("james"))
image phoebe normal = At("images/portraits/ps-portrait.png", sprite_highlight("phoebe"))

# LIGHTS OUT Character Images Using Auto-Highlight -----------------------------
image daniel dark = At("images/portraits/doctor-portrait-dark.png", sprite_highlight("daniel"))
image wendy dark = At("images/portraits/doctors-wife-portrait-dark.png", sprite_highlight("wendy"))
image james dark = At("images/portraits/journalist-portrait-dark.png", sprite_highlight("james"))
image phoebe dark = At("images/portraits/ps-portrait-dark.png", sprite_highlight("phoebe"))

# Blurred Character ------------------------------------------------------------

image phoebe blur = At("images/portraits/ps-portrait-blur.png", sprite_highlight("phoebe"))

# Backgrounds ------------------------------------------------------------------
image bg mansion = "images/bg/mansion-bg.png"
image bg mansion dark = "images/bg/mansion-bg-dark.png"
image bg black = "images/bg/black-bg.png"
image bg bedroom = "images/bg/bedroom-bg.png"
image bg bathroom = "images/bg/bathroom-bg.png"
image bg dining = "images/bg/dining-bg.png"
image bg dining dark =  "images/bg/dining-bg-dark.png"

# Custom Menu ------------------------------------------------------------------
screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.75 
        spacing 10 

        for i in items:
            textbutton i.caption action i.action

# Inventory --------------------------------------------------------------------
default inventory = []

# Character and Event Trackers -------------------------------------------------
default talked_to_daniel_before_death = False
default talked_to_wendy_before_death = False
default talked_to_james_before_death = False
default talked_to_phoebe_before_death = False

default lights_out = False
default hide_char_dark = False

default dining_hall_first_entry = True

default phoebe_death = False

default visited_bathroom_door_one = False
default visited_bathroom_door_two = False

default investigate_phoebe_death = False

default required_clues = 3

# investigation to trigger options during accusation phase
default daniel_clue = False
default wendy_clue = False
default james_clue = False
# check inventory for wax, unlabeled vial, plant extracts, and threat letter

# getting clues
# default wax_clue = False
# default vial_clue = False

default gather_clue_screen = None

# EFFECTS CONFIG ---------------------------------------------------------------
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

# START OF THE GAME LABEL ------------------------------------------------------

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

# IMAGE MAPS FOR DIFFERENT SCENES ----------------------------------------------

#--------------------------------MAIN-HALL-MAP----------------------------------

screen main_hall():
    frame:
        background Solid("#000000") 
        xfill True
        yfill True

    if lights_out:
        add "images/bg/floor-one-main-dark.png" fit "contain" xalign 0.5

        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("dining_hall", transition=fade)]
            xpos 1125
            ypos 550
            at Transform(zoom=0.25)

        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("bedroom_dark", transition=fade)]
            xpos 460
            ypos 150
            at Transform(zoom=0.25, rotate=-90)

        if investigate_phoebe_death:
            imagebutton:
                idle "images/walks/wife-doctor-walk/doctor-wife-stand-dark.png"
                hover "images/walks/wife-doctor-walk/doctor-wife-stand-hover-dark.png"
                action [Hide("main_hall"), Jump("investigate_wendy")]
                xpos 948
                ypos 155
                at Transform(zoom=0.35, rotate=-0.3)

    # BEFORE LIGHTS OUT --------------------------------------------------------
    else:
        add "images/bg/floor-one-main.png" fit "contain" xalign 0.5

        # WENDY (WIFE), ALR TALKED TO AS WELL 
        imagebutton:
            idle "images/walks/wife-doctor-walk/doctor-wife-stand.png"
            hover "images/walks/wife-doctor-walk/doctor-wife-stand-hover.png"
            xpos 623
            ypos 578
            at Transform(zoom=0.35, rotate=-2.3)

        # DANIEL (DOCTOR), ALR TALKED TO
        imagebutton:
            idle "images/walks/doctor-walk/doctor-stand.png"
            hover "images/walks/doctor-walk/doctor-stand-hover.png"
            xpos 680
            ypos 750
            at Transform(zoom=0.35, rotate=-1.3)

        # GREET JAMES
        imagebutton:
            idle "images/walks/journalist-walk/james-stand.png"
            hover "images/walks/journalist-walk/james-stand-hover.png"
            action [Hide("main_hall"), Jump("james_greeting")]
            xpos 460
            ypos 250
            at Transform(zoom=0.35, rotate=0.4)

        # GREET PHOEBE
        imagebutton:
            idle "images/walks/phoebe-walk/phoebe-stand.png"
            hover "images/walks/phoebe-walk/phoebe-stand-hover.png"
            action [Hide("main_hall"), Jump("phoebe_greeting")]
            xpos 1100
            ypos 150
            at Transform(zoom=0.35, rotate=-1.7)

        # GO TO DINING HALL
        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("main_hall"), Show("dining_hall", transition=fade)]
            xpos 1125
            ypos 550
            at Transform(zoom=0.25)

#-------------------------------DINING-HALL-MAP---------------------------------

screen dining_hall():
    frame:
        background Solid("#000000") 
        xfill True
        yfill True

    add "images/bg/floor-one-dining-dark.png" fit "contain" xalign 0.5

    # find new way

    if dining_hall_first_entry:
        timer 0.1 action [Hide("dining_hall"), Jump("dining_room_cutscene")]

    # Vial Pickup
    if not "Spilled Vial (No Label)" in inventory and phoebe_death and not "Poisoned Spilled Vial" in inventory:
        imagebutton:
            idle "images/items/dark-unlabeled-vial.png"
            hover "images/items/dark-unlabeled-vial-hover.png"
            if investigate_phoebe_death:
                action [Hide("dining_hall"), Jump("obtain_spilled_vial")]
            xpos 1308
            ypos 287
            at Transform(zoom=0.15, rotate=-23)
    
    if not "Phoebe's Plant Extracts Kit" in inventory and phoebe_death:
        imagebutton:
            idle "images/items/plant-extracts-dark.png"
            hover "images/items/plant-extracts-dark-hover.png"
            if investigate_phoebe_death:
                action [Hide("dining_hall"), Jump("obtain_plant_extracts")]
            xpos 987
            ypos 277
            at Transform(zoom=0.2, rotate=2)

    # Investigate Phoebe Body
    if investigate_phoebe_death:
        imagebutton:
            idle "images/walks/doctor-walk/doctor-stand-dark.png"
            hover "images/walks/doctor-walk/doctor-stand-dark-hover.png"
            action [Hide("dining_hall"), Jump("investigate_daniel")]
            xpos 587
            ypos 224
            at Transform(zoom=0.45, rotate=0.7)

    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("dining_hall"), Show("main_hall", transition=fade)]
        xpos 250
        ypos 400
        at Transform(zoom=0.25, rotate=180)

    # Phoebe (Dining Hall)
    if not phoebe_death:
        imagebutton:
            idle "images/walks/phoebe-walk/phoebe-stand-dark.png"
            hover "images/walks/phoebe-walk/phoebe-stand-hover-dark.png"
            action [Hide("dining_hall"), Jump("phoebe_dining_scene")]
            xpos 300
            ypos 150
            at Transform(zoom=0.42, rotate=-.4)

    else:    
        imagebutton:
            idle "images/deaths/phoebe-death-dark.png"
            hover "images/deaths/phoebe-death-dark-hover.png"

            # Don't allow cutscene again if 
            if not investigate_phoebe_death: 
                action [Hide("dining_hall"), Call("phoebe_death_scene")]
            else:
                action [Hide("dining_hall"), Call("investigate_phoebe_death")]
            xpos 1183
            ypos 284
            at Transform(zoom=0.62, rotate=15)

#----------------------------------BEDROOM-MAP----------------------------------

screen bedroom_dark():
    frame:
        background Solid("#000000") 
        xfill True
        yfill True

    add "images/bg/bedroom-dark.png" fit "contain" xalign 0.5

    if lights_out:
        # Wendy (bedroom) - during lights out before death
        if not investigate_phoebe_death:
            imagebutton:
                idle "images/walks/wife-doctor-walk/doctor-wife-stand-dark.png"
                hover "images/walks/wife-doctor-walk/doctor-wife-stand-hover-dark.png"
                action [Hide("bedroom_dark"), Jump("wendy_bedroom_scene")]
                xpos 1125
                ypos 155
                at Transform(zoom=0.55, rotate=0.2)

        # James (bedroom) - lights out but after phoebe death
        if investigate_phoebe_death:
            imagebutton:
                idle "images/walks/journalist-walk/dark-james-stand.png"
                hover "images/walks/journalist-walk/dark-james-stand-hover.png"
                action [Hide("bedroom_dark"), Jump("investigate_james")]
                xpos 1157
                ypos 340
                at Transform(zoom=0.55, rotate=.3)
            
            if "Hardened Wax Drop" not in inventory or "Hardened Wax Poison" and not "Hardened Wax With Poison":
                imagebutton:
                    idle "images/items/wax-drop-dark.png"
                    hover "images/items/wax-drop-dark-hover.png"
                    action [Hide("bedroom_dark"), Jump("obtain_wax_drop")]
                    xpos 424
                    ypos 857
                    at Transform(zoom=0.2)

    # Go to bathroom
    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("bedroom_dark"), Show("bathroom_dark", transition=fade)]
        xpos 870
        ypos 0
        at Transform(zoom=0.4, rotate=-90)

    # Go to main hall 
    imagebutton:
        idle "images/ui/arrow.png"
        hover "images/ui/arrow-hover.png"
        action [Hide("bedroom_dark"), Show("main_hall", transition=fade)]
        xpos 1175
        ypos 750
        at Transform(zoom=0.4, rotate=90)

#--------------------------------BATHROOM-MAP-----------------------------------

screen bathroom_dark():
    frame:
        background Solid("#000000")
        xfill True
        yfill True
    
    if lights_out:
        add "images/bg/bathroom-dark.png" fit "contain" xalign 0.5

        # Back to bedroom
        imagebutton:
            idle "images/ui/arrow.png"
            hover "images/ui/arrow-hover.png"
            action [Hide("bathroom_dark"), Show("bedroom_dark", transition=fade)]
            xpos 800
            ypos 750
            at Transform(zoom=0.45, rotate=90)  

        # Investigate First Bathroom Door
        imagebutton:
            idle "images/bg/bathroom-doors/dark-door-one.png"
            hover "images/bg/bathroom-doors/dark-door-one-hover.png"
            if lights_out and not investigate_phoebe_death:
                action [Hide("bathroom_dark"), Jump("bathroom_door_one_locked")]
            # xpos 650
            # ypos 350
            xpos 600
            ypos 240
            at Transform(zoom=2)

        # Investigate Second Bathroom Door
        imagebutton:
            idle "images/bg/bathroom-doors/dark-door-two.png"
            hover "images/bg/bathroom-doors/dark-door-two-hover.png"
            if lights_out and not investigate_phoebe_death:
                action [Hide("bathroom_dark"), Jump("bathroom_door_two_locked")]
            xpos 550
            ypos 700
            at Transform(zoom=2)
    # else: 
    #     add "images/bg/bathroom.png" fit "contain" xalign 0.5

#---------------------------INTRO-GREET-THE-COUPLE------------------------------

label daniel_greeting:

    play voice "audio/sfx/doorclose2.mp3" 
    $ renpy.sound.set_volume(0.2, channel="voice")

    play sound "audio/sfx/rain_inside.ogg" fadein 1.0 loop

    scene bg mansion with fade

    show daniel normal at character_center with dissolve

    daniel "Finally! I was beginning to think you couldn’t make it."

    daniel "The weather is not the best today. They say that the chances of a heavy snowstorm are very high tonight."

    daniel "But no worries! Now that you have arrived in my mansion, our safety is guaranteed. I can promise you that!"

    hide daniel normal 
    jump mansion_intro_before_death

label mansion_intro_before_death:

    # scene bg mansion with fade

    show wendy normal at character_center with dissolve

    wendy "So nice to see you again, [char_name]! It has been too long!"

    wendy "My husband and I were just talking about you!"

    hide wendy normal
    show daniel normal at character_center with dissolve

    daniel "Oh, so you two were talking about me? Hopefully, only good things!"

    hide daniel normal
    show daniel normal at character_left with dissolve
    show wendy normal at character_right with dissolve

    wendy "I have heard that you are working for the city now. I wonder how your work environment may compare to our own?"

    menu:
        "Ask about their work": 
            jump ask_work_before_death
        "Tell them about your work":
            hide daniel normal
            jump tell_work_before_death

label ask_work_before_death:

    daniel "Well, as you may have seen on TV, I’m endorsing a new product for nutrition supplements."

    daniel "You know, it is good for preventing cardiovascular disease and boosting your immune system."

    daniel "You should totally give it a try! In fact, I can send some of it directly to you at a later date!"

    wendy "Daniel has been really busy lately trying to balance between his hospital work and these commercial deals."

    wendy "I often have to step in to take care of the hospital side for him."

    daniel "I told you countless times not to do my work for me!"

    daniel "You are going to mess things up!"

    hide wendy normal
    hide daniel normal
    call screen main_hall

label tell_work_before_death:

    show wendy normal at character_center with dissolve

    wendy "I have always known that you have a righteous mind."

    wendy "To think you became a forensic pathologist to help bring justice to society."

    hide wendy normal
    show daniel normal at character_center with dissolve

    daniel "Don’t say that! You know very well that patients depend heavily on us."

    hide daniel normal
    show wendy normal at character_center with dissolve

    wendy "In spite of my fears, I always do my best to save everyone!"

    hide wendy normal
    call screen main_hall

#--------------------------------GREET-JAMES------------------------------------

label james_greeting:

    scene bg mansion 

    show james normal at character_center with dissolve

    james "[char_name]! I never expected to see you of all people!"
    "How long has it been? Two years?"

    "So, how is this murder case you're working on?"
    "Did you manage to figure out how the victim was killed?"

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

    hide james normal with fade

    call screen main_hall

#-------------------------------GREET-PHOEBE------------------------------------

label phoebe_greeting:

    scene bg mansion 

    show phoebe normal at character_center with dissolve

    phoebe "…….."

    menu:
        "Leave her alone":
            jump phoebe_leave
        "Try saying 'Hi'":
            jump phoebe_hi

label phoebe_leave:

    show phoebe normal at character_center with dissolve

    phoebe "That smell… I recognize it."
    phoebe "The citrus scent is likely coming from limonene or linalool."
    phoebe "Mixing that with aldehydes can further enrich its profile."

    # Swap to the blurred Phoebe portrait before showing the vial
    hide phoebe normal
    show phoebe blur at character_center

    # Show the vial in focus
    show bag_of_chemicals at chem_position with fade
    pause 1.5

    # Hide both the vial and the blurred Phoebe, then restore normal Phoebe
    hide bag_of_chemicals with fade
    hide phoebe blur with dissolve
    show phoebe normal at character_center with dissolve

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

    hide phoebe normal
    call screen main_hall

label phoebe_bad_chemistry:

    phoebe "That can’t be true."
    phoebe "I am aware of your job as a forensic pathologist."
    phoebe "You need to use the correct chemicals and precise doses to produce accurate results."

    phoebe "In fact, I have been trying to develop new formulas for testing various types of rare poison."
    phoebe "It may come in handy in your work one day."

    # Display a message about obtaining research papers
    if "Poison Detection Research Papers" not in inventory:
        
        phoebe "Here, I will send you some files."

        $ inventory.append("Poison Detection Research Papers")
        $ renpy.notify("Obtained research papers on poison detection.")

        phoebe "(These documents discuss developing new reagents for poison detection.)"
        phoebe "(It involves using organic extracts from plants such as red cabbage, turmeric, and hibiscus.)"
    
    else:
        
        phoebe "WIP"

    phoebe "You must let me know your thoughts when you finish reading!"

    hide phoebe normal
    call screen main_hall

label phoebe_hi:

    phoebe "……"
    
    # Phoebe appears absorbed in her thoughts
    "She looks absorbed in her thoughts, staring at her notes."

    hide phoebe normal
    call screen main_hall

#------------------------------DINING-ROOM-CUTSCENE-----------------------------

label dining_room_cutscene:

    if not dining_hall_first_entry:
        call screen dining_hall
        return

    $ dining_hall_first_entry = False
    $ lights_out = True

    scene bg dining 

    show wendy normal at character_center with dissolve
    wendy "Everyone, dinner is ready! Let’s gather around the table."

    hide wendy normal
    show daniel normal at character_left with dissolve
    show james normal at character_right with dissolve

    daniel "Took you long enough! I am starving!"
    james "Ohhh! All the dishes look so good! I can’t wait to dig in."

    hide daniel normal
    hide james normal
    show phoebe normal at character_center with dissolve

    phoebe "Ah yes! 375 degrees, the perfect temperature for baked chicken."
    phoebe "The golden brown color of the skin comes from the Maillard reaction between amino acids and reduced sugar."
    phoebe "The proteins, including collagen and myosin, break down to create its new texture."
    phoebe "The fat melts to keep the meat moist and lock in flavors. Truly marvelous!"

    hide phoebe normal
    show james normal at character_center with dissolve
    james "Come on, Phoebe! Stop reminding me of these terminologies I had to learn in class!"
    james "The nightmares are coming back to me!"

    hide james normal
    show daniel normal at character_center with dissolve
    daniel "I can see she's still a walking textbook!"
    daniel "Surely her intellect makes dinner conversations much more amusing than simple small talk."

    hide daniel normal
    show wendy normal at character_center with dissolve
    wendy "No matter what, having this long-awaited reunion is something to cherish!"
    wendy "I especially want to hear more from [char_name]."
    wendy "We haven't seen you in nearly a decade!"

    hide wendy normal

    scene bg black with Fade(0.3, 0.3, 0.5)
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

#----------------------------------LIGHTS-OUT-----------------------------------

#-------------------------------PHOEBE-IN-DINING--------------------------------

label phoebe_dining_scene:

    scene bg dining dark
    show phoebe dark at character_center with dissolve

    phoebe "Don’t mind me. I am just doing my work here, and I really need to concentrate."
    
    phoebe "If you feel bored, maybe you can go around and check on the others?"

    hide phoebe dark

    call screen dining_hall

#-------------------------------WENDY-IN-BEDROOM--------------------------------

label wendy_bedroom_scene:

    scene bg bedroom
    show wendy dark at character_center with dissolve

    wendy "I could have sworn I put some candles around here. The lighter too… Where could it be?"
    
    wendy "It’s so difficult trying to find these things in total darkness!"

    wendy "Oh, [char_name]! Did you come here looking for Daniel or James? They both went into the bathroom. You can check on them if you want."
    
    wendy "It must be difficult trying to use the bathroom in this total darkness."

    hide wendy dark
    call screen bedroom_dark


#----------------------------INVESTIGATE-BATHROOMS------------------------------

label bathroom_door_one_locked:

    scene bg bathroom

    "(The door is locked)."
    
    james "Hey! Occupied!"
    james "I know you may also be holding it in, but wait just a little longer, ok?"
    
    call screen bathroom_dark

label bathroom_door_two_locked:

    scene bg bathroom

    "(The door is locked.)"
    "(Complete silence...)"

    # Checking on this bathroom door will trigger first death (TK song is tuff)
    $ phoebe_death = True
    
    call screen bathroom_dark

#---------------------------PHOEBE-DEATH-SCENE!!!!------------------------------

label phoebe_death_scene:

    scene bg dining

    show james dark at character_far_left with dissolve
    show daniel dark at character_far_right with dissolve
    show wendy dark at character_center with dissolve

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
 
    hide james dark
    hide daniel dark
    hide wendy dark

    $ investigate_phoebe_death = True

    call screen dining_hall  

#-------------------------INVESTIGATE-PHOEBE-DEATH!!----------------------------
label investigate_phoebe_death:

    scene bg dining dark

    "(Her body is as stiff as a rock.)"
    "(There is no visible wound anywhere on the body. Her pupils are completely dilated.)"

    "Have you gathered enough clues to enter the trial?"

    hide window

    menu:
        "Yes, I'm ready.":  
            if len(inventory) >= required_clues:  
                jump enter_trial
            else:
                "(You haven't gathered enough evidence yet.)"
                call screen dining_hall
        "Not yet.":  
            call screen dining_hall

# CUTSCENE AFTER OBTAINING EVIDENCE --------------------------------------------

label obtain_spilled_vial:

    scene bg dining dark

    "(You carefully pick up the spilled vial.)"
    "(Its contents remain a mystery..)"

    $ renpy.notify("Obtained: Spilled Vial (No Label)")

    if "Spilled Vial (No Label)" not in inventory:
        $ inventory.append("Spilled Vial (No Label)")

    # Jump straight into inventory
    if "Hardened Wax Drop" in inventory and "Phoebe's Plant Extracts Kit" in inventory:
        # gather_clue_screen = "dining_hall"
        call screen inventory_screen

    call screen dining_hall

label obtain_plant_extracts:

    scene bg dining dark

    "(You pick up Phoebe's Plant Extracts Kit.)"
    "(This might help identify unknown substances.)"

    $ renpy.notify("Obtained: Phoebe's Plant Extracts Kit")

    if "Phoebe's Plant Extracts Kit" not in inventory:
        $ inventory.append("Phoebe's Plant Extracts Kit")

    # Jump straight into inventory if both required clues are already collected
    if "Spilled Vial (No Label)" in inventory and "Hardened Wax Drop" in inventory: 
        # gather_clue_screen = "dining_hall"
        call screen inventory_screen

    call screen dining_hall

label obtain_wax_drop:

    scene bg bedroom 

    "(You spot a small drop of hardened wax on top of the cabinet.)"
    "(It seems out of place—who left it here?)"

    $ renpy.notify("Obtained: Hardened Wax Drop")

    if "Hardened Wax Drop" not in inventory:
        $ inventory.append("Hardened Wax Drop")

    if "Spilled Vial (No Label)" in inventory and "Phoebe's Plant Extracts Kit" in inventory:

        # gather_clue_screen = "bedroom_dark"
        call screen inventory_screen

    call screen bedroom_dark

screen inventory_screen():

    draggroup:
        # Plant Extracts (Always visible, droppable target)
        drag:
            drag_name "Plant Extracts"
            idle_child "images/items/plant-extracts.png"
            hover_child "images/items/plant-extracts-hover.png"
            xpos 0.1
            ypos 0.25
            draggable False
            droppable True

        # Wax (only if not processed yet)
        if "Hardened Wax With Poison" not in inventory:
            drag:
                drag_name "Wax"
                child "images/items/wax-drop.png"
                xpos 0.6
                ypos 0.15
                draggable True
                droppable False
                drag_offscreen (200,200)
                dragged drag_placed
                drag_raise True 

        # Vial (only if not processed yet)
        if "Poisoned Spilled Vial" not in inventory:
            drag:
                drag_name "Vial"
                child "images/items/unlabeled-vial.png"
                xpos 0.56
                ypos 0.55
                draggable True
                droppable False
                drag_offscreen (200,200)
                dragged drag_placed
                drag_raise True
                
init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        dragged_name = drags[0].drag_name

        if dragged_name == "Wax" and drop.drag_name == "Plant Extracts":
            renpy.call_in_new_context("wax_cutscene")

        elif dragged_name == "Vial" and drop.drag_name == "Plant Extracts":
            renpy.call_in_new_context("vial_cutscene")

label wax_cutscene:

    image wax_normal = "images/items/wax-drop.png"
    image wax_poisoned = "images/items/wax-drop-poison.png"

    "You combine the wax and the extract..." with fade

    show wax_normal at truecenter
    with dissolve

    pause 1.0

    show wax_poisoned at truecenter
    with Dissolve(1.0)

    "There appears to be green spots on the surface."

    if "Hardened Wax Drop" in inventory and "Hardened Wax With Poison" not in inventory:
        $ inventory[inventory.index("Hardened Wax Drop")] = "Hardened Wax With Poison"

    $ renpy.notify("Obtained: Hardened Wax With Poison")

    pause 1.0

    hide wax_normal
    hide wax_poisoned with fade

    if "Poisoned Spilled Vial" in inventory:
        call screen main_hall 

    call screen inventory_screen

label vial_cutscene:

    image vial_normal = "images/items/unlabeled-vial.png"
    image vial_poisoned = "images/items/unlabeled-vial-poison.png"

    "You pour the plant extract into the vial..." with fade

    show vial_normal at truecenter
    with dissolve

    pause 1.0

    show vial_poisoned at truecenter
    with Dissolve(1.0)

    "The contents turn a cloudy green as something reacts inside."

    if "Spilled Vial (No Label)" in inventory and "Poisoned Spilled Vial" not in inventory:
        $ inventory[inventory.index("Spilled Vial (No Label)")] = "Poisoned Spilled Vial"

        $ renpy.notify("Obtained: Poisoned Spilled Vial")

    pause 1.0

    hide vial_normal
    hide vial_poisoned with fade

    if "Hardened Wax With Poison" in inventory:
        call screen main_hall 

    call screen inventory_screen
    
# INVESTIGATING DANIEL ---------------------------------------------------------

label investigate_daniel:

    scene bg dining 
    show daniel dark at center with dissolve

    daniel "It was supposed to be a day of cheers and laughter! Not only did the power go out, there is now even a dead body inside my mansion! If the media catches wind of it, it will be a huge scandal!"
    daniel "Ahhh! James might just be a tattletale and bring this news to them! I will need to make sure he is on my side, same as always!"

    menu:
        "Were you in the bathroom? I didn’t get any response when I checked on you.":
            jump daniel_bathroom

        "Is there something between you and James?":
            jump daniel_james

label daniel_bathroom:

    daniel "What do you mean? I was using the urinal the whole time! Well… it may have taken longer than normal..."
    daniel "But that’s because I was trying to clean the room. It’s embarrassing for me to admit, but it’s not easy to aim well in the dark."
    daniel "I was probably so focused on my task that I didn’t even notice someone knocking on my door."

    hide daniel dark

    call screen dining_hall

label daniel_james:

    daniel "You probably heard from James that he is covering health-related topics as a journalist, right?"
    daniel "Well, he just won’t stop bugging me! He contacts me all the time, asking for my comments and putting them in his articles."
    daniel "He is also awfully curious about my endorsement deals and business connections."
    daniel "I bet more than half of his article outputs were somehow related to me."
    daniel "On top of dealing with my wife, James is also poking his nose into my business."
    daniel "Thankfully he always speaks highly of me in his articles. I suppose I do owe some of my fame to him too."
    daniel "Ahhh!!! That just makes it more difficult for me to confront him."

    menu:
        "Why are you so bothered by them anyway? They only want to help.":
            jump daniel_bothered_by_james

        "It does seem strange that James would do things to such an extent.":
            jump daniel_suspicious_of_james

label daniel_bothered_by_james:

    daniel "You just had to say that to me, without knowing how much more stressed I have become!"
    daniel "I didn’t care for fame in the beginning. It’s only when my wife heavily encouraged me that I became a public figure."
    daniel "Since then, my wife helps me secure more business deals, and James would end up promoting me through his media coverage."
    daniel "I can no longer enjoy any peace and quiet, all the while having to worry about my reputation as a doctor!"
    daniel "Everything I do is under public scrutiny, and I have no room to breathe!"
    daniel "My good friend, you must understand the harsh reality behind all the surface-level glory!"

    hide daniel dark

    call screen dining_hall

label daniel_suspicious_of_james:

    daniel "Exactly! The way he acts around me is just unnatural. He is too eager."
    daniel "Well, since it is only the two of us in this darkness, this could be my chance."
    daniel "I wish to speak to you about an urgent matter. Promise me that you will not leak this information to anyone else, not anyone here!"

    menu:
        "You have my word!":
            jump daniel_secret

        "Rest assured! My lips are sealed.":
            jump daniel_secret

label daniel_secret:

    daniel "The other day, I received this anonymous letter. It threatens to expose me."

    # Display notification for obtaining the letter
    $ renpy.notify("Obtained: Anonymous Threatening Letter to Daniel")

    # Add item to inventory
    if "Anonymous Threatening Letter" not in inventory:
        $ inventory.append("Anonymous Threatening Letter")

    daniel "It reads: 'Your secrets are no longer hidden. You must answer for your crimes! There may still be redemption for you, however."
    daniel "If you wish not to be exposed, wait in your hospital office at midnight on the day of the full moon.'"

    daniel "Quite frankly, I have no clue what kind of secret the letter is referring to."
    daniel "But I can’t risk having someone out there spreading rumors and tarnishing my reputation!"
    daniel "Wendy and James are both poking their nose into my business."
    daniel "They may have spoken too much to some third party trying to frame me, or worse, they could be intentionally trying to sabotage me, being the real sender behind this letter!"
    daniel "You may not be an attorney, but you are still working closely with the law."
    daniel "I really need your support right now to help me sort out this tricky situation!"

    # Obtain flag for daniel
    $ daniel_clue = True 

    hide daniel dark

    call screen dining_hall

# INVESTIGATING WENDY ----------------------------------------------------------

label investigate_wendy:

    scene bg mansion dark 
    show wendy dark at center

    wendy "I cannot believe this! Phoebe was always looking out for me back then."
    wendy "She helped me go through so many school materials so that I could pass my exams."
    wendy "Even now, I often ask her for support whenever I am struggling at work."
    
    pause 0.5

    wendy "And now…"
    wendy "she is gone…"
    wendy "forever… *sob*"

    window hide

    menu:
        "Did you find anything strange before getting here?":
            jump wendy_strange_noises

        "Cheer up! We will solve this case for her sake too.":
            jump wendy_cheer_up

label wendy_strange_noises:

    wendy "I am sorry, but all three of us were around the bedroom and bathroom at the time."
    wendy "If anything happened in the dining hall, I don’t believe any of us would have heard it."
    
    wendy "But if we are talking about something strange, I think I heard some kind of ghostly scream!"
    
    pause 0.5
    
    wendy "Eek!!" # ADD text effects later and shake
    wendy "Recalling that still sends shivers down my spine!"
    
    wendy "But the sound can’t be from the dining room. It was much closer... within the walls."
    
    wendy "Could it be the spirit of poor Phoebe crying for help before she reaches the afterlife?"

    char "Were you the only one who heard this noise?"

    wendy "I was too scared and just ran away as soon as I got the candles, so I didn’t have the chance to ask James or my husband about this."

    wendy "Honestly, this is not the first time I have heard strange noises from the bedroom walls."

    wendy "When I mentioned this to my husband, his face turned completely pale."
    
    wendy "Yet afterward, he just called me paranoid and pushed my concerns aside."

    char "Are you saying that you find your husband suspicious?"

    wendy "Frankly, I wanted to trust him wholeheartedly, but he has been acting really strange lately."

    wendy "I hardly find him at home, despite having a pretty good grasp on his schedule."

    wendy "Even when I try calling him, there is no answer."

    wendy "It makes me doubt that he is having an affair outside!"

    hide wendy dark

    call screen main_hall

label wendy_cheer_up:

    wendy "You are right! I shouldn’t be whining."

    wendy "We should try to figure out what happened to her."

    wendy "But I don’t even know where to begin…"

    menu:
        "Let’s try to figure out how she took the poison in her body.":
            jump wendy_poison_method

        "Let’s try to determine what kind of poison this is.":
            jump wendy_poison_type

label wendy_poison_method:

    wendy "She probably just drank it by accident, no?"

    wendy "But there doesn’t appear to be any traces of her drinking it on her lips."

    wendy "The situation just gets more and more puzzling…"

    hide wendy dark

    call screen main_hall

label wendy_poison_type:

    wendy "But there is no label on it."

    wendy "Without any professional equipment at hand, how can we possibly identify the chemicals inside?"

    wendy "If only Phoebe was still alive, she could tell us about it."

    wendy "She was a walking encyclopedia for chemicals like this."

    # Wendy realizes what she just said
    pause 0.7
    wendy "Oh no! Whatever nonsense am I saying? I may have just disrespected her death…"

    $ wendy_clue = True

    hide wendy dark

    call screen main_hall

# INVESTIGATING JAMES ----------------------------------------------------------

label investigate_james:

    scene bg bedroom 
    show james dark at center

    james "…… Sorry…… I am at a loss for words."
    james "It shouldn’t have come to this!"
    
    # Slow text effect for emotional weight
    window hide
    pause 0.5
    window show
    james "If only I didn’t go to the bathroom, or if I came back to the dining room sooner……"
    james "I could have prevented this from happening!"

    char "It is not your fault at all."

    james "Thanks for trying to cheer me up, [char]."
    james "I can’t believe how calm you can be despite witnessing something so horrible."
    james "Guess that is part of being a forensic pathologist."

    james "I will help out with your investigation in any way I can!"
    james "Just like how you helped me back then."

    window hide

    menu:
        "Were you in the bathroom the whole time before getting back here?":
            jump james_bathroom

        "I am so sorry I was unable to save you then.":
            jump james_past

label james_bathroom:

    james "Yeah… I had to take a dump, so I was in the toilet room the whole time."
    james "You know, it’s especially difficult trying to clean yourself in pitch darkness."

    james "After hearing you call for us, I came out of the bathroom and noticed Wendy just by the bedroom door."
    james "She was holding the lit candles in her hand, and she looked really devastated."
    
    james "As she rushed toward the dining room, I hurriedly followed behind her."
    james "And the rest is history."

    hide james dark

    call screen bedroom_dark 

label james_past:

    james "Don’t be. You did everything you could to prove my innocence."
    james "It was ultimately my decision anyway."

    james "When the drug samples in the lab went missing, the school was ready to accuse Phoebe of stealing them."
    james "You know, since she always carries around vials of chemicals and extracts with her."

    james "You have probably figured out by now that I had feelings for her."

    # Emotional pause before revealing the truth
    pause 0.7

    james "To ensure her bright future, I willingly took the blame."
    james "I still remember you yelling at me for being an idiot, admitting to crimes I did not commit."

    james "I am glad you didn’t give up and fought till the very end."
    james "But when I inevitably got my expulsion letter, I just couldn’t find the courage to face you all."

    james "I was ready to put all this in the past, but not this time!"

    pause 0.5

    james "Phoebe is dead now, and I am certain that someone is responsible for it."
    james "This could potentially be the doing of the same person from two years ago."

    james "You want to know my thoughts?"

    pause 0.5

    james "I think Daniel is a big fraud."
    james "He always thinks himself the best, and he was jealous of Phoebe’s talent."

    james "He is the only one who could possibly have the motives to hurt her, this time taking her life!"
    
    james "I have been watching his every move."
    james "He seems anxious whenever I try to bring up social problems like drug theft or drug trafficking."

    james "I know he is still hiding something!"

    james "In fact, I came to his house for the first time hoping to gather more evidence, and Phoebe’s death could be the key to all of this!"

    $ james_clue = True

    hide james dark

    call screen bedroom_dark

#--------------------------------ENTER TRIAL!!----------------------------------

label enter_trial:
    scene bg dining dark with fade

    show daniel dark at left
    show wendy dark at center
    show james dark at right

    daniel "So…"                
    daniel "Did you figure out anything about Phoebe’s death?"

    wendy "Oh please! We must know the truth!"
    wendy "It’s the least we can do for her soul!"

    james "What do you think happened to her?"

    call trial_choices
    return

label trial_choices:
    menu:
        "It was an accident":
            call accident_route
        "It was suicide":
            call suicide_route
        "This is a serious murder case":
            call serious_case_route
    return

label accident_route:

    daniel "Most tragic! They say curiosity kills the cat." 
    daniel "How ironic it is that the heavens have taken the life of a person of great intellect through such an idiotic approach."

    james "Hold on just a second! You can’t be serious!"
    james "How dare you just stand there shedding fake tears?"
    james "Phoebe was clearly murdered, and the culprit could be none other than you, Daniel!"

    call accusation_phase

label suicide_route:

    wendy "I can hardly believe that! She was so into her research. You can see her eyes sparkle when she speaks of it."
    wendy "No one that hopeful would ever commit suicide!"

    james "I am very disappointed, [char]."
    james "Your judgment of the situation is clearly mistaken!"
    james "Phoebe was clearly murdered, and the culprit could be none other than you, Daniel!"
    
    call accusation_phase

label serious_case_route:

    james "Exactly! I am sure you are thinking the same as I do, [char]."
    james "The culprit could be none other than you, Daniel!"

    call accusation_phase

label accusation_phase:
    
    daniel "What?! Outrageous! You are making the most baseless claims."
    daniel "What could my motives possibly be for killing Phoebe?"

    james  "Don’t think you can escape this time, you sly fox! I have been keeping tabs on you. I am aware of your dirty doings!"

    daniel "Ha! So you finally admit it! You came close to me once more to try to spy on me! You were the one who threatened to ruin my career!" 
    daniel "This is defamation! Your claims are completely bogus!"

    james "None of that matters anymore! You have made your move. I wish I had gathered more evidence beforehand, but I have to strike you down now!" 
    james "Admit it! You killed Phoebe this time, just like how you had intention to frame her during the drug stealing incident 2 years ago!"

    daniel "So this is the reasoning behind your claims? I have nothing to do with that incident!"

    james "I know there is no proof left for that incident, but I have great intuition! My suspicions were confirmed when your wife approached me for help!"

    daniel "Wendy! What did you do this time?"

    wendy "I am sorry! I really didn’t mean to! But you have been acting so strange lately."
    wendy "I had to ask James to get close to you to find out if you are having an affair!"

    james "And guess what I have found out! I know Phoebe and you have been in close contact, unknown to the rest of us."

    daniel "Impossible! How did you manage to get that info? Furthermore, if the two of us are very close, why would that lead to me killing her?"

    james "To manipulate her of course! You were ready to use her talent somehow. I am sure of it!"

    daniel "What a load of nonsense! You cannot possibly believe this too, [char]?"

    call suspicion_choice

label suspicion_choice:
    menu:
        "You are clearly hiding something, Daniel. Spill the truth at once!":
            call daniel_accused
        "James, your story doesn’t add up. Daniel can’t be the killer.":
            call james_suspicion

label daniel_accused:

    daniel "You would turn against me as well, [char]? I had the wrong idea about you!"

    james "Quick, tie him up! We have to wait until the police can get here tomorrow. He’s too dangerous to be kept free!"

    daniel "No!!! I am innocent! You are all gathered here today to set me up!"

    pause 3.0

    "(The next morning, the police took Daniel away, and he was put on trial.)"

    return "game_over"

label james_suspicion:

    james "What are you saying, [char]? Who else could possibly be responsible for such a murder?"

    menu:
        "It’s James" if required_clues >= 2:
            call accuse_james
        "It’s James" (disabled):
            "I don't have enough evidence to accuse James."
        "It’s Wendy" if required_clues >= 2:
            call accuse_wendy
        "It’s Wendy" (disabled):
            "I don't have enough evidence to accuse Wendy."
    return

label accuse_james:

    wendy "James? That’s quite a bold claim! What evidence makes you think that?"

    # "Present any evidence and none of them would work."

    james "I can’t believe you would try to frame me instead without any evidence."
    james "Are you trying to cover up for Daniel? Don’t think I didn’t notice when you and Daniel were speaking in private."
    james "Now that I think about it, you were the first person to find Phoebe dead!"
    james "You should be the most suspicious one of us all! Spill it out! Did Daniel order you to kill Phoebe in his stead?"

    "Both [char] and Daniel were prosecuted as suspects of murder."

    return "game_over"


label accuse_wendy:
    james "Wendy? You must have gone mad! What makes you suggest her as the culprit?"

    "(Present piece of wax with green spots.)"

    wendy "You are accusing me of murder? How could you say such a heartless thing!"

    james "Explain yourself, [char]."

    char "The poison could be identified with the plant extracts in Phoebe’s kit, which turns green upon contact. The green spot you see on the wax is evidence of the poison!"

    james "But what does it have to do with Wendy?"

    char "The color of this wax is the same as the candle, which means it must have fallen off from the candle at some point. The only person carrying candles around is Wendy!"

    wendy "What? This story doesn’t add up. The piece of wax could just have been there the whole time and got splashed with poison for all we know."

    char "If that is the case, surely you wouldn’t mind presenting the candles that you were holding before? Let’s see if any one of them has parts missing, which matches with the shape of the piece of wax!"

    wendy "No!!!!!!!!"

    "When [char] examines the candles, he finds one of them that matches perfectly with the small piece of wax. Moreover, the candle itself has traces of being lit before."

    "Player melts the candle wax off to reveal its content."

    james "Unbelievable! This is where the poison was hidden the whole time?"

    char "She purposely replaced the content of the vials that Phoebe carries with this poison to make it look like an accident. She probably planned to dispose of the candles before the police arrive!"

    pause 3.0

    return "wendy_arrested"




