define char_name = "Player"
define char = Character(char_name, color="#FFFFFF")

define daniel = Character("Daniel", color="#FF5733")
define wendy = Character("Wendy", color="#FFB6C1")
define james = Character("James", color="#87CEEB")
define phoebe = Character("Phoebe", color="#9370DB")

# START OF THE GAME

label start:

    scene bg black with fade

    "Before we begin, what is your name?"

    $ char_name = renpy.input("Enter your name:", default="Player")
    $ char_name = char_name.strip() or "Player"
    $ char = Character(char_name, color="#FFFFFF")

    "Welcome, [char_name]. You have arrived at the mansion."

    call screen image_map

    return

transform blur_effect:
    # matrixcolor TintMatrix("#eaeaea")  # Slight gray tint
    blur 2  # Increase the blur level

screen image_map():
    # Background map
    add "images/bg/floor-one-main.png" fit "contain" xalign 0.5 at blur_effect

    # Clickable characters
    imagebutton:
        idle "images/walks/doctor-walk/doctor-stand.png"
        hover "images/walks/doctor-walk/doctor-stand-hover.png"
        action Jump("daniel_greeting")
        xpos 680
        ypos 750
        at Transform(zoom=0.3, rotate=-0.3)

    # imagebutton:
    #     idle "images/characters/wendy.png"
    #     hover "images/characters/wendy_hover.png"
    #     action Jump("wendy_greeting")
    #     xpos 700
    #     ypos 500

    imagebutton:
        idle "images/walks/journalist-walk/james-stand.png"
        hover "images/walks/journalist-walk/james-stand-hover.png"
        action Jump("james_greeting")
        xpos 460
        ypos 250
        at Transform(zoom=0.3, rotate=.3)

    imagebutton:
        idle "images/walks/phoebe-walk/phoebe-stand.png"
        hover "images/walks/phoebe-walk/phoebe-stand-hover.png"
        action Jump("phoebe_greeting")
        xpos 1100
        ypos 150
        at Transform(zoom=0.3, rotate=-.4)

# BEFORE THE FIRST DEATH DIALOGUE AROUND THE MAP

label daniel_greeting:

    scene bg mansion with fade

    daniel "Finally! I was beginning to think you couldn’t make it."

    daniel "The weather is not the best today. They say that the chances of a heavy snowstorm are very high tonight."

    daniel "But no worries! Now that you have arrived in my mansion, our safety is guaranteed. I can promise you that!"

    jump mansion_intro_before_death

label mansion_intro_before_death:

    wendy "So nice to see you again, [char_name]! It has been too long!"

    wendy "My husband and I were just talking about you!"

    wendy "I have heard that you are working for the city now. I wonder how your work environment may compare to our own?"

    menu:
        "Ask about their work":
            jump ask_work_before_death
        "Tell them about your work":
            jump tell_work_before_death

label ask_work_before_death:

    daniel "Well, as you may have seen on TV, I’m endorsing a new product for nutrition supplements."

    daniel "You know, it is good for preventing cardiovascular disease and boosting your immune system."

    daniel "You should totally give it a try! In fact, I can send some of it directly to you at a later date!"

    wendy "Daniel has been really busy lately trying to balance between his hospital work and these commercial deals."

    wendy "I often have to step in to take care of the hospital side for him."

    daniel "I told you countless times not to do my work for me!"

    daniel "You are going to mess things up!"

    wendy "But I am only trying to lighten the load for you, my dear!"

    daniel "And I always end up having to check what you have done to make sure everything is in order."

    daniel "It just makes my life even more stressful!"

    wendy "Well, I think you should…"

    daniel "Enough of this topic."

    daniel "If you really want to help me, right now is the best time to go check on our dinner."

    daniel "You don’t want to burn the chicken, do you?"

    wendy "Oh yes! You are right! I will catch up with you all at the dinner table."

    scene bg mansion with fade

    jump after_choice_before_death

label tell_work_before_death:

    wendy "I have always known that you have a righteous mind."

    wendy "To think you became a forensic pathologist to help bring justice to society."

    wendy "I can’t even bear looking at dead corpses. It reminds me of failing to save the patients during their most desperate hour."

    daniel "Don’t say that! You know very well that patients depend heavily on us."

    daniel "If you can’t get over death, might as well quit as a doctor!"

    daniel "I see you going around the hospital every day like a corpse yourself!"

    daniel "How can you instill confidence in the patients if they see you looking as pale as they are!"

    wendy "I know very well that my patients trust me!"

    wendy "In spite of my fears, I always do my best to save everyone!"

    daniel "Enough talk of your ideals."

    daniel "You should go check on our dinner."

    daniel "You don’t want to burn the chicken, do you?"

    wendy "Oh yes! You are right! I will catch up with you all at the dinner table."

    scene bg mansion with fade

    jump after_choice_before_death

label after_choice_before_death:

    daniel "What do you think, my old friend?"

    daniel "I am talking about my wife, of course."

    daniel "She always looks so timid and indecisive."

    daniel "I never believed she could get through the tough workload at school, thinking she might need my help and advice."

    daniel "Yet here she is, standing right next to me, both respected doctors!"

    daniel "Now she tries to get her nose into my business every chance she can, but I don’t need her help!"

    daniel "To be frank, I don’t think she is just trying to help with my work."

    daniel "She is trying to control every aspect of my life!"

    daniel "I can tell from my desk that she always goes through my mails and documents."

    daniel "Even if she is my wife, it is hardly the right thing to just peek at someone else’s privacy without permission."

    daniel "I actually wish to speak with you in private today."

    daniel "It’s good to finally catch up with you."

    daniel "There are many things I want to share too, but we will have to continue our conversation after dinner."

    daniel "I’m sure the others are happy to see you as well. I can’t keep you all to myself."

    return


label talk_james:

    scene bg newsroom with fade

    james "[char_name]! I never expected to see you of all people! How long has it been? Two years?"

    james "So how is this murder case that you are currently working on? Did you manage to figure out how the victim was killed?"

    james "Hmm, you are wondering how I know about that when we haven’t seen each other for so long?"

    james "Behold, for you are in the presence of the greatest journalist of our generation! No secrets can escape from my grasp! Hahaha!"

    james "I know for a fact that you work in the city coroner's office, and apparently, one of their best forensic experts too!"

    james "I guess it is only fair to tell you more of what I have been up to, yeh?"

    james "Going around the city all day trying to dig deep into the latest story, it can be quite exhausting."

    james "But I honestly really like this job! I guess I didn’t realize I had what it takes to be a good journalist."

    james "With my previous medical background, my boss wanted me to focus on health-related topics and speak to these experts at their level."

    james "People would leave comments saying that they find my articles scientific, reliable, and easy to understand."

    james "Hey! You know what, I should definitely interview you at some point!"

    james "While I cannot be certain if it’s news-worthy, I need a good excuse to finally reconnect with you again!"

    james "Let me know when would be a good time later, ok?"

    return

label talk_phoebe:

    scene bg laboratory with fade

    phoebe "…….."

    menu:
        "Leave her alone":
            jump phoebe_leave
        "Try saying 'Hi'":
            jump phoebe_hi

label phoebe_leave:

    phoebe "That smell… I recognize it."

    phoebe "The citrus scent is likely coming from limonene or linalool, and mixing that with aldehydes can further enrich its profile."

    phoebe "In fact, I have some samples right here."

    # Show a bag of chemicals sprite or display text
    show bag_of_chemicals with fade
    pause 1.5
    hide bag_of_chemicals

    phoebe "Yes…This is quite nostalgic… So you are still wearing the same cologne from two years ago."

    phoebe "It reminds me of simpler days, when we all studied together for chemistry."

    menu:
        "I remember you were really good at chemistry!":
            jump phoebe_chemistry
        "I am so bad with chemistry though…":
            jump phoebe_bad_at_chemistry

label phoebe_chemistry:

    phoebe "I find it absolutely fascinating!"

    phoebe "It’s the study of matter and change, which can be observed all around us!"

    phoebe "Think of all the possibilities! You can shape reality to your will with just the smallest amount of the right chemicals."

    phoebe "And it couldn’t be more accurate in the case of our human biology."

    phoebe "Anything we take in our body can make or break us, and there are still so many aspects unknown."

    phoebe "With my pride as a pharmaceutical scientist, I will unlock the secrets to it all. It doesn’t get more exciting than this!"

    phoebe "Having a smell of your cologne and talking about chemistry actually reminded me of something related to my current research."

    phoebe "I need to immediately sort things out before the ideas elude me. If you’ll excuse me."

    return

label phoebe_bad_at_chemistry:

    phoebe "That can’t be true."

    phoebe "I am aware of your job as a forensic pathologist."

    phoebe "You need to use the correct chemicals and precise doses to produce accurate results."

    phoebe "In fact, I have been trying to develop new formulas for testing various types of rare poison."

    phoebe "It may come in handy in your work one day."

    phoebe "Here, I will send you some files."

    # Show message that player obtained research papers
    show text "Obtained research papers on poison detection."
    pause 2.0
    hide text

    show text "Description: A research developing new reagents for poison detection, which involves using organic extracts from plants such as red cabbage, turmeric, and hibiscus."
    pause 3.0
    hide text

    phoebe "You must let me know your thoughts when you finish reading!"

    return

label phoebe_hi:

    phoebe "……"

    "She looks absorbed in her thoughts, staring at her notes."

    return

label dining_room_cutscene:

    scene bg dining_room with fade

    wendy "Everyone, dinner is ready! Let’s gather around the table."

    daniel "Took you long enough! I am starving!"

    james "Ohhh! All the dishes look so good! I can’t wait to dig in."

    phoebe "Ah yes! 375 degrees, the perfect temperature for baked chicken."

    phoebe "The golden brown color of the skin comes from the Maillard reaction between amino acids and reduced sugar."

    phoebe "The proteins, including collagens and myosin, break down to create its new texture."

    phoebe "The fat melts to keep the meat moist and lock in the flavors. Truly marvelous!"

    james "Come on, Phoebe! Stop reminding me of these terminologies I had to learn in class! The nightmares are coming back to me!"

    daniel "I can see that she is still a walking textbook!"

    daniel "Surely her great intellect will make topics at the dinner table much more amusing than simple, uninspiring small talks."

    wendy "No matter the case, having this chance for our long-awaited reunion is something to be cherished!"

    wendy "I especially want to hear more from [char_name]. We all haven’t seen you in close to a decade!"

    scene bg black with fade
    play sound "snowstorm.mp3"

    james "A sudden blackout? I thought you took pride in this place, Daniel."

    daniel "Oh, shut it! Heavy snow may have destroyed nearby power lines, it has nothing to do with my house!"

    wendy "I will go find some candles to light up the room!"

    phoebe "Can’t we just use the light of our phones? Oh no! Looks like there is no signal."

    wendy "Just the light of our phones won’t be enough to illuminate the rooms."

    wendy "But it is a good idea to use them as flashlights to navigate around the mansion."

    wendy "Don’t worry! I will be right back."

    james "Hehe, it just so happens that I need to go to the bathroom. Can you tell me where it is?"

    daniel "Alright, you come with me to the bathroom while Wendy gets the candles."

    scene bg dark_hallway with fade

    "James and Daniel leave off-screen."

    scene bg dining_room_dark with fade

    phoebe "I guess I will just stay here and wait for you all then."

    phoebe "I will take this time and resume work on my latest project."

    return

label mansion_exploration:

    scene bg dark_mansion with fade

    "You can freely explore the mansion with limited sight using your flashlight."

    "Phoebe will stay in the dining hall unless you leave."

    menu:
        "Go to the dining room":
            jump dining_room_explore
        "Go to the bedroom":
            jump bedroom_explore
        "Go to the bathroom":
            jump bathroom_explore
        "End exploration":
            jump advance_story

label dining_room_explore:

    scene bg dining_room_dark with fade

    phoebe "Don’t mind me. I am just doing my work here, and I really need to concentrate."

    phoebe "If you feel bored, maybe you can go around and check on the others?"

    jump mansion_exploration

label bedroom_explore:

    scene bg dark_bedroom with fade

    wendy "I could have sworn I put some candles around here. The lighter too… Where could it be?"

    wendy "It’s so difficult trying to find these things in total darkness!"

    wendy "Oh, [char_name]! Did you come here looking for Daniel or James?"

    wendy "They both went into the bathroom. You can check on them if you want."

    wendy "It must be difficult trying to use the bathroom in this total darkness."

    jump mansion_exploration

label bathroom_explore:

    scene bg dark_bathroom with fade

    menu:
        "Examine first toilet room door":
            jump examine_first_toilet
        "Examine second toilet room door":
            jump examine_second_toilet
        "Go back":
            jump mansion_exploration

label examine_first_toilet:

    "Description: The door is locked."

    james "Hey! Occupied!"

    james "I know you may also be holding it in, but wait just a little longer, ok?"

    jump bathroom_explore

label examine_second_toilet:

    "Description: The door is locked. But there is no sound coming out from it."

    jump bathroom_explore

label advance_story:

    "Having talked to everyone, you feel a strange sense of unease..."

    return


# THE FIRST DEATH (That song by TK is so tuff)


