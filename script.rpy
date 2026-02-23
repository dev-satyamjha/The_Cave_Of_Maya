define santosh = Character("Santosh", who_color="#FFD700", what_color="#FFFFFF")
define sadhu = Character("Sadhu", who_color="#FF8C00", what_color="#FFE4B5")
define vani = Character("Mayavani", who_color="#AAAAAA", what_color="#CCCCCC", what_italic=True)

define flashback = Fade(0.5, 0.5, 0.5, color="#fff")

default current_time = 90
default cipher_time = 300
default punishment_time = 75
default punishment_tries = 7
default level_4_time = 200
default punishment_5_time = 10
default punishment_5_tries = 2
default level_6_time = 12
default playfair_time = 60
default playfair_tries = 3
default choice_time = 15
default void_time = 10
default has_failed_level_7 = False

transform floating_card:
    yoffset 0
    easein 2.5 yoffset -20
    easeout 2.5 yoffset 0
    repeat

screen how_to_play_screen():
    add "#000000cc"

    frame:
        at floating_card
        align (0.5, 0.5)
        xysize (1200, 800)
        
        background Frame(Solid("#F2DD9E"), 10, 10)
        padding (60, 60)

        frame:
            background Frame(Solid("#00000000"), 5, 5)
            
            vbox:
                align (0.5, 0.5)
                spacing 30
                
                text "INSTRUCTIONS BEFORE ENTERING INTO THE CAVE" size 35 color "#8B0000" bold True xalign 0.5 text_align 0.5 xoffset 50
                
                text "✧ ══════════════ ✧" size 30 color "#8B0000" xalign 0.5
                
                text "The only rule is that" size 35 color "#3b2f2f" xalign 0.5 text_align 0.5
                
                text "You must read every dialogue carefully" size 35 color "#3b2f2f" xalign 0.5 text_align 0.5
                
                text "If you rush and miss a single line" size 35 color "#3b2f2f" xalign 0.5 text_align 0.5

                text "You will be trapped in the cave forever!" size 35 color "#3b2f2f" xalign 0.5 text_align 0.5
                
                text "Time is limited. Think carefully." size 35 color "#3b2f2f" xalign 0.5 text_align 0.5
                
                text "✧ ══════════════ ✧" size 30 color "#8B0000" xalign 0.5
                
                null height 40
                
                textbutton "Accept the Journey":
                    xalign 0.5
                    text_size 40
                    text_color "#8B0000"
                    text_hover_color "#FF4500"
                    text_bold True
                    action Return()

screen credits_screen():
    add "#000000cc"

    frame:
        at floating_card
        align (0.5, 0.5)
        xysize (1200, 800)
        
        background Frame(Solid("#F2DD9E"), 10, 10)
        padding (60, 60)

        frame:
            background Frame(Solid("#00000000"), 5, 5)
            
            vbox:
                align (0.5, 0.5)
                spacing 40
                
                text "THE JOURNEY ENDS" size 55 color "#8B0000" bold True xalign 0.5 text_align 0.5 xoffset 250
                
                text "✧ ══════════════ ✧" size 30 color "#8B0000" xalign 0.5 xoffset 250
                
                text "Thank you for playing!" size 40 color "#3b2f2f" bold True xalign 0.5 text_align 0.5 xoffset 250
                
                text "Created & Programmed by" size 30 color "#3b2f2f" xalign 0.5 text_align 0.5 xoffset 250
                text "Satyam Jha" size 45 color "#8B0000" bold True xalign 0.5 text_align 0.5 xoffset 250
                text " Built in Ren'Py" size 30 color "#8B0000" xalign 0.5 xoffset 250
                text "✧ ══════════════ ✧" size 30 color "#8B0000" xalign 0.5 xoffset 250
                
                null height 40
                
                textbutton "Return to Reality":
                    xalign 0.5
                    yalign 0.5  
                    yoffset -80
                    text_size 40
                    text_color "#8B0000"
                    text_hover_color "#FF4500"
                    text_bold True
                    action Return()
                    xoffset 250

screen puzzle_timer(fail_label):
    text "Time Left: [current_time]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000000", 0, 0)]
    timer 1.0 repeat True action If(current_time > 0, SetVariable("current_time", current_time - 1), Jump(fail_label))

screen level_3_cipher_timer(fail_label):
    text "Time Left: [cipher_time]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(cipher_time > 0, SetVariable("cipher_time", cipher_time - 1), Jump(fail_label))

screen level_3_punishment_timer(fail_label):
    vbox xalign 0.9 yalign 0.1 spacing 10:
        text "Time: [punishment_time]s" size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
        text "Tries Left: [punishment_tries]" size 30 color "#cccccc" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(punishment_time > 0, SetVariable("punishment_time", punishment_time - 1), Jump(fail_label))

screen level_4_timer(fail_label):
    text "Time Left: [level_4_time]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(level_4_time > 0, SetVariable("level_4_time", level_4_time - 1), Jump(fail_label))

screen level_5_punishment_timer(fail_label):
    vbox xalign 0.9 yalign 0.1 spacing 10:
        text "Time: [punishment_5_time]s" size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
        text "Tries Left: [punishment_5_tries]" size 30 color "#cccccc" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(punishment_5_time > 0, SetVariable("punishment_5_time", punishment_5_time - 1), Jump(fail_label))

screen level_6_timer(fail_label):
    text "Time Left: [level_6_time]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(level_6_time > 0, SetVariable("level_6_time", level_6_time - 1), Jump(fail_label))

screen playfair_timer(fail_label):
    vbox xalign 0.9 yalign 0.1 spacing 10:
        text "Time: [playfair_time]s" size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
        text "Tries Left: [playfair_tries]" size 30 color "#cccccc" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(playfair_time > 0, SetVariable("playfair_time", playfair_time - 1), Jump(fail_label))

screen choice_timer(fail_label):
    text "Hurry: [choice_time]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action If(choice_time > 0, SetVariable("choice_time", choice_time - 1), Jump(fail_label))

screen void_timer(fail_label):
    text "[void_time]" size 40 color "#ff0000" outlines [(2, "#000", 0, 0)] align (0.5, 0.1)
    timer 1.0 repeat True action If(void_time > 0, SetVariable("void_time", void_time - 1), Jump(fail_label))

screen playfair_grid():
    frame:
        background "#222222cc"
        xalign 0.1
        yalign 0.4
        padding (20, 20)
        vbox:
            spacing 15
            text "M O H A B" size 45 color "#FFD700" bold True align (0.5, 0.5)
            text "C D E F G" size 45 color "#FFD700" bold True align (0.5, 0.5)
            text "I K L N P" size 45 color "#FFD700" bold True align (0.5, 0.5)
            text "Q R S T U" size 45 color "#FFD700" bold True align (0.5, 0.5)
            text "V W X Y Z" size 45 color "#FFD700" bold True align (0.5, 0.5)

label start:
    play music "lv7.ogg"
    call screen how_to_play_screen
    stop music fadeout 1.0
    play music "carstarts.ogg" 
    scene start with fade:
        size (1920, 1080)
    "Car engine starts... {w=2}{nw}"
    
    stop music fadeout 1.0
    scene santosh with fade:
        size (1920, 1080)
    play music "driving.ogg"  fadein 1.0
    
    santosh "(Thinking) My new car... my diamond watch... {w=3}{nw}"
    
    scene wedding with flashback:
        size (1920, 1080)
        
    santosh "Ten years ago, Vikram was begging me for notes. {w=3}{nw}"
    santosh "Now he acts like he owns the world! And his wife... mocking my wife's cotton saree? Humiliating. {w=5}{nw}"
    
    scene santoshsad with hpunch:
        size (1920, 1080)
        
    santosh "(Grips steering wheel) We have a good life. Why does it suddenly feel like I have absolutely nothing? {w=6}{nw}"
    santosh "Just a few more kilometers. I just want to sleep and forget this whole miserable evening. {w=5}{nw}"

    scene driving:
        size (1920, 1080) 
    stop music fadeout 1.0
    play music "forest.ogg" fadeout 1.0
    play sound "brake.ogg" 

    santosh "Hey Oldie! Are you crazy or what?! {w=5}{nw}"
    stop sound 

    scene saint with fade:
        size (1920, 1080) 
    play sound "horn.ogg"
    queue sound ["horn.ogg"]
    santosh "Aye! Babaji.. Move aside! I need to pass! {w=5}{nw}"
    
    scene driving:
        size (1920, 1080) 
    play sound "horn.ogg"
    queue sound ["horn.ogg", "horn.ogg", "horn.ogg"]
    santosh "Are you deaf?! Move! I've had a terrible night, and I am not in the mood for this now! {w=12}{nw}"
    stop sound 
    santosh "Fine. I'll move him myself! {w=5}{nw}"

    scene angry:
        size(1920, 1080)
    santosh "Look, Baba, I respect the saffron robes, but this is a road, not an ashram. Get up! {w=10}{nw}"
    santosh "I said, Get Up!! {w=4}{nw}"

    scene kicks with vpunch:
        size(1920, 1080)
    play sound "kicks.ogg"
    "A sharp kick. A copper pot clatters violently. Water splashes onto the dirt. {w=7}{nw}"

    scene sadhuangry with dissolve:
        size(1920, 1080)
    sadhu "The water only spilled because the pot was struck. But your mind, son... your mind was spilling poison long before you met me. {w=12}{nw}"

    scene sadhuangry: 
        size(1920, 1080)
    santosh "I... I told you to move! {w=3}{nw}"

    scene sadhuangry with dissolve:
        size(1920, 1080)
    sadhu "You look, but do not see. You are blinded by the wealth of others, choked by your own anger, and starved by your hidden greed. {w=12}{nw}"
    sadhu "You believe you are blocked on this physical road? No. You are already trapped in the labyrinth of your own 'Awguns'. {w=12}{nw}"

    scene sadhuangry:
        size(1920, 1080)
    santosh "What nonsense are you talking about? I am turning my car around. {w=12}{nw}"

    scene transition1 with fade:
        size(1920,1080)
    sadhu "(Voice echoing) Since you are lost in the illusion of what you lack, you shall wander in the dark until you see what you have. Welcome to the Cave of Maya. {w=12}{nw}"

    scene cave with vpunch:
        size(1920, 1080)
    play sound "creepy_laugh.ogg"
    "The cave walls are jagged. You hear faint, echoing laughter from the wedding and the clinking of expensive glasses. {w=10}{nw}"
    play music "creepysound.ogg" fadeout 1.0
    "The puzzles ahead force you to organize your chaotic thoughts. {w=5}{nw}"

label phase_1_krodha:
    scene phase1 with pixellate:
        size (1920, 1080)
    $ current_time = 60
    show screen puzzle_timer("punishment_1")
    
label puzzle_1_loop:
    $ answer_1 = renpy.input("Unscramble the letters to find the cure to jealousy: HGEONU", length=15).strip().upper()
    
    if current_time <= 0:
        jump punishment_1
        
    if answer_1 == "ENOUGH":
        hide screen puzzle_timer
        santosh "Enough... I have enough. {w=4}{nw}"
        "The chaotic letters dissolve into glowing dust, revealing a path forward. {w=7}{nw}"
        if has_failed_level_7:
            jump punishment_1
        else:
            jump phase_1_cleared
    else:
        santosh "No, that doesn't make sense... {w=5}{nw}"
        jump puzzle_1_loop

label punishment_1:
    hide screen puzzle_timer
    scene owls with vpunch:
        size (1920, 1080)
    play sound "misc.ogg"   
    "The ground crumbles. You fall into a pitch-black void. {w=5}{nw}"
    $ current_time = 80
    show screen puzzle_timer("punishment_2")
    
label punishment_1_loop:
    $ answer_2 = renpy.input("Unscramble: T O N C E T N N E M T", length=20).replace(" ", "").upper()
    
    if current_time <= 0:
        jump punishment_2
        
    if answer_2 == "CONTENTMENT":
        hide screen puzzle_timer
        "The void shatters like glass. You scramble back up to the cave. {w=5}{nw}"
        if has_failed_level_7:
            jump punishment_2
        else:
            jump phase_1_krodha 
    else:
        vani "Think, Santosh! {w=2}{nw}"
        jump punishment_1_loop

label punishment_2:
    hide screen puzzle_timer
    scene snakes with vpunch:
        size (1920, 1080)
    play sound "misc.ogg"
        
    "You sink deeper into the illusion. The air is heavy. The voices are deafening. {w=8}{nw}"
    
    $ current_time = 50
    show screen puzzle_timer("game_over")
    
label punishment_2_loop:
    $ answer_3 = renpy.input("Unscramble: ORESRME", length=15).strip().upper()
    
    if current_time <= 0:
        jump game_over
        
    if answer_3 == "REMORSE":
        hide screen puzzle_timer
        "A rope of golden light pulls you back to the surface. {w=5}{nw}"
        if has_failed_level_7:
            jump phase_1_cleared
        else:
            jump phase_1_krodha
    else:
        vani "The darkness tightens its grip around you. {w=5}{nw}"
        jump punishment_2_loop

label phase_1_cleared:
    "You take a deep breath. The anger in your chest reduces slightly. {w=57}{nw}"
    jump level_2_start

label level_2_start:
    hide screen wordle_ui
    scene cave with fade:
        size (1920, 1080)
    play sound "spider.ogg"
    "Your way to freedom is a riddle. {w=5}{nw}"
    vani "I am a fire you start to burn your enemy, but I only burn your own hands. What am I? {w=15}{nw}"

    scene phase1 with fade:
        size (1920, 1080)

    if has_failed_level_7:
        $ current_wordle = WordleGame("ANGER", 5, 180, "punishment_1_level2", "punishment_1_level2")
    else:
        $ current_wordle = WordleGame("ANGER", 5, 180, "punishment_1_level2", "level_2_cleared")
    show screen wordle_ui(current_wordle)
    $ ui.interact()

label punishment_1_level2:
    hide screen wordle_ui
    scene river with vpunch:
        size (1920, 1080)
    play sound "shock1.ogg"
    santosh "No! The door is sealing shut! {w=5}{nw}"
    vani "Your anger blinds you. To extinguish the fire, you must find its opposite. Only the letters will guide you. {w=15}{nw}"
    
    if has_failed_level_7:
        $ current_wordle = WordleGame("PEACE", 5, 120, "punishment_2_level2", "punishment_2_level2")
    else:
        $ current_wordle = WordleGame("PEACE", 5, 120, "punishment_2_level2", "level_2_start")
    show screen wordle_ui(current_wordle)
    $ ui.interact()

label punishment_2_level2:
    hide screen wordle_ui
    scene chains with vpunch:
        size (1920, 1080)
    
    santosh "(Gasping) It's so hot... the air is burning my heart! {w=5}{nw}"
    vani "You cling to rage because you fear what comes after. Acknowledge the bitter pill you refuse to swallow. {w=15}{nw}"
    
    if has_failed_level_7:
        $ current_wordle = WordleGame("REGRET", 5, 150, "game_over", "level_2_cleared")
    else:
        $ current_wordle = WordleGame("REGRET", 5, 150, "game_over", "level_2_start")
    show screen wordle_ui(current_wordle)
    $ ui.interact()

label level_2_cleared:
    hide screen wordle_ui
    "The stone door grinds open with a deafening crack. {w=7}{nw}"
    
    santosh "Anger... it wasn't protecting me. It was destroying me. {w=5}{nw}"
    jump level_3_start
    
label level_3_start:
    scene phase1 with fade:
        size (1920, 1080)
    play sound "monster.ogg"
    "You reach the end of the cave. {w=5}{nw}"
    vani "To conquer pride, you must step down. Shift the burden back by 3. You must have basic knowledge of Caesar cipher to solve this (Di = (Ei-3)mod26) {w=15}{nw}"
    vani "You can answer the riddles or ciphers in any case.{w=4}{nw}"
    "An inscription glows on the heavy stone gate: H J R {w=9}{nw}"
    
    $ cipher_time = 300
    show screen level_3_cipher_timer("level_3_punishment")
    
label cipher_input_loop:
    $ cipher_ans = renpy.input("Enter the 3-letter code:").strip().upper()
    
    if cipher_time <= 0:
        jump level_3_punishment
        
    if cipher_ans == "EGO":
        hide screen level_3_cipher_timer
        "The massive stone gate shudders and opens, revealing an inner chamber. {w=5}{nw}"
        jump level_3_statues
    else:
        vani "The gate remains sealed. That is not the word. {w=5}{nw}"
        jump cipher_input_loop

label level_3_statues:
    scene statue with hpunch:
        size(1920, 1080)
    "Three glowing statues materialize, blocking the final exit. They wear the faces of your past. {w=12}{nw}"
    vani "Illusion is built on lies. To break free, find the only truth. {w=9}{nw}"
    
    menu:
        "Statue 1 (The Sadhu's Echo): 'The first voice is lying. Desire has no end. Listen to my code.'":
            santosh "The Sadhu... he speaks the truth. {w=5}{nw}"
            if has_failed_level_7:
                jump level_3_punishment
            else:
                jump level_3_cleared

        "Statue 2 (Vikram's Voice): 'Wealth brings absolute peace.'":
            santosh "Vikram always knew how to succeed... {w=5}{nw}"
            jump level_3_punishment
                
        "Statue 3 (Rahul's Voice): 'Only the first voice speaks the truth.'":
            santosh "Rahul wouldn't lie to me... {w=5}{nw}"
            jump level_3_punishment

label level_3_punishment:
    hide screen level_3_cipher_timer 
    scene pit with vpunch:
        size (1920, 1080)
    
    vani "You let the illusion deceive you. Steady your mind, or start from the beginning. {w=7}{nw}"
    
    $ punishment_time = 75
    $ punishment_tries = 7
    show screen level_3_punishment_timer("level_3_fail_completely")

label punishment_proverb_1:
    if punishment_tries <= 0:
        jump level_3_fail_completely
        
    $ prov_1 = renpy.input("Complete the thought: 'A spoken word, like a flown ____, cannot be recalled.'").strip().upper()
    
    if punishment_time <= 0:
        jump level_3_fail_completely
        
    if prov_1 == "ARROW":
        "The howling wind dies down slightly. One more remains. {w=5}{nw}"
        jump punishment_proverb_2
    else:
        $ punishment_tries -= 1
        vani "Wrong. The winds whip harder. {w=5}{nw}"
        jump punishment_proverb_1

label punishment_proverb_2:
    if punishment_tries <= 0:
        jump level_3_fail_completely
        
    $ prov_2 = renpy.input("Complete the thought: 'You can't unring a ___'").strip().upper()
    
    if punishment_time <= 0:
        jump level_3_fail_completely
        
    if prov_2 == "BELL":
        hide screen level_3_punishment_timer
        "The pit dissolves. A blinding light pulls you upward. {w=6}{nw}"
        if has_failed_level_7:
            jump level_3_cleared
        else:
            jump level_3_start
    else:
        $ punishment_tries -= 1
        vani "Wrong. The darkness closes in. {w=5}{nw}"
        jump punishment_proverb_2

label level_3_fail_completely:
    hide screen level_3_punishment_timer
    scene black with fade:
        size (1920, 1080)
    
    vani "Your pride has consumed you. The cycle begins again. {w=5}{nw}"
    "You are thrown violently back to the entrance of the cave. {w=5}{nw}"
    jump phase_1_krodha

label level_3_cleared:
    scene phase1 with fade:
        size (1920, 1080)
    santosh "Ego... My own ego was making me feel small. {w=5}{nw}"
    
    "The heavy weight of anger and jealousy lifts. You have survived Krodha. {w=8}{nw}"
    jump phase_2_lobha

label phase_2_lobha:
    scene lobha with fade:
        size (1920, 1080)
    play sound "coins.ogg"
    
    vani "Your mind is fractured. You had the option to set yourself frree but you choose the path to greed, now face the consequences! {w=9}{nw}"
    
    scene river with fade:
        size(1920, 1080)
    $ level_4_time = 180
    show screen level_4_timer("level_4_failed")
    
    vani "Listen to the water. Notice how the smallest disturbance ruins the perfect image. {w=9}{nw}"
    
    vani "What comes for a short time but can ruin everything if not controlled? {w=5}{nw}"

label level_4_puzzle_1:
    $ ans1 = renpy.input("Peace is a perfectly still lake; ______ is the stone you throw that shatters your own reflection.").strip().upper()
    
    if level_4_time <= 0:
        jump level_4_failed
        
    if ans1 in ["ANGER", "KRODHA"]:
        "The first riddle is over...Time for the next one {w=5}{nw}"
    else:
        vani "The carving remains dull. That is not the right word. {w=5}{nw}"
        jump level_4_puzzle_1

    vani "A famous qoute for people like you!"
label level_4_puzzle_2:
    $ ans2 = renpy.input("There is enough for every man's need, but not enough for every man's ______.").strip().upper()
    
    if level_4_time <= 0:
        jump level_4_failed
        
    if ans2 in ["GREED", "LOBHA"]:
        "That's it, you got it! . {w=5}{nw}"
    else:
        vani "The stone feels cold. Try again. {w=5}{nw}"
        jump level_4_puzzle_2

    vani "The only that can be earned and can't be demanded! {w=3}{nw}"
label level_4_puzzle_3:
    $ ans3 = renpy.input("You demand _____ from the world outside, but leave the door open for ego on the inside.").strip().upper()
    
    if level_4_time <= 0:
        jump level_4_failed
    if ans3 in ["PEACE", "RESPECT"]:
        "And that's how, you earned it!. {w=5}{nw}"
    else:
        vani "The word echoes empty. Focus, Santosh. {w=5}{nw}"
        jump level_4_puzzle_3

    hide screen level_4_timer
    jump level_4_cleared

label level_4_failed:
    hide screen level_4_timer
    scene black with vpunch:
        size (1920, 1080)
    
    vani "Time has slipped through your fingers. You have learned nothing. {w=8}{nw}"
    jump phase_1_krodha

label level_4_cleared:
    santosh "The answers were inside me all along. I just... refused to look at them. {w=9}{nw}"
    "You step through the archway, journeying deeper into the Cave of Maya. {w=8}{nw}"
    
    jump level_5_start

label level_5_start:
    scene lobha2 with fade:
        size (1920, 1080)
    
    santosh "I found the exit! And... so much gold. Diamonds everywhere... {w=5}{nw}"
    
    vani "To pass through the Door of Lobha, your pockets must match your soul on the day you were born. How much wealth will you take with you to the next life? {w=12}{nw}"

label level_5_input:
    $ renpy.block_rollback() 
    
    $ scale_ans = renpy.input("Type your answer in numbers or words:").strip().upper()
    
    if scale_ans in ["0", "ZERO", "NOTHING"]:
        if has_failed_level_7:
            jump level_5_punishment
        else:
            jump level_5_cleared
    else:
        "The golden scale violently tips. The ground shatters beneath your feet! {w=5}{nw}"
        jump level_5_punishment


label level_5_punishment:
    scene lobha_p:
        size(1920, 1080)
    play sound "heartbeat.ogg" fadein 1.0
        
    vani "The gold is heavy. You are sinking. The only way up is to... {w=5}{nw}"
    vani "P R O D   T I {w=5}{nw}"

    $ punishment_5_time = 12
    $ punishment_5_tries = 2
    show screen level_5_punishment_timer("level_5_failed")

label level_5_punishment_loop:
    $ renpy.block_rollback()
    
    if punishment_5_tries <= 0 or punishment_5_time <= 0:
        jump level_5_failed
        
    $ drop_ans = renpy.input("Unscramble the floating text:").strip().upper()
    
    if punishment_5_time <= 0:
        jump level_5_failed
        
    if drop_ans == "DROP IT":
        hide screen level_5_punishment_timer
        
        santosh "(Gasping for air) I... I let it go! {w=5}{nw}"
        if has_failed_level_7:
            jump level_5_cleared
        else:
            jump level_5_start
    else:
        $ punishment_5_tries -= 1
        if punishment_5_tries > 0:
            vani "You sink deeper into the suffocating gold. Try again! {w=5}{nw}"
            jump level_5_punishment_loop
        else:
            jump level_5_failed


label level_5_failed:
    hide screen level_5_punishment_timer
    stop music fadeout 1.0
    
    scene pit with fade:
        size (1920, 1080)
        
    vani "Crushed by your own desires. Confiscated forever. {w=5}{nw}"
    "You are thrown violently back to the beginning of Lobha. {w=5}{nw}"
    
    jump phase_2_lobha 

label level_5_cleared:
    scene lobha2 with fade:
        size (1920, 1080)
        
    "The golden scale balances perfectly. The massive doors slowly grind open. {w=5}{nw}"
    santosh "We bring nothing into this world, and we take nothing out. {w=5}{nw}"
    
    "You step out of the glittering cave, leaving the heavy burden of Lobha behind. {w=5}{nw}"
    
    jump level_6_start
    
label level_6_start:
    scene lust with fade:
        size (1920, 1080)
    play sound "female_laugh.ogg"
    vani "You choose the wrong path again, now mend it or loose. {w=5}{nw}"
    
    vani "To climb out of the dark, you must undo your steps. You fell DOWN, stepped RIGHT, looked UP, and stepped LEFT. {w=15}{nw}"
    scene phase3_1:
        size(1920, 1080)
    stop music fadeout 1.0
    play music "lv7.ogg"
    $ level_6_time = 25
    show screen level_6_timer("level_6_punishment")

label level_6_input_loop:
    $ renpy.block_rollback()
    
    $ escape_path = renpy.input("Type the exact opposite path to escape with spaces in any case:").strip().upper()
    
    $ clean_path = escape_path.replace(" ", "").replace(",", "")
    
    if level_6_time <= 0:
        jump level_6_punishment
        
    if clean_path == "UPLEFTDOWNRIGHT":
        hide screen level_6_timer
        if has_failed_level_7:
            jump level_6_punishment
        else:
            jump level_6_cleared
    else:
        vani "The room shrinks. That is not the correct path! {w=5}{nw}"
        jump level_6_input_loop


label level_6_punishment:
    hide screen level_6_timer
    
    scene phase3_1 with fade:
        size (1920, 1080)
    play sound "laugh_male.ogg"
    vani "Two words will open the path. One feeds the flesh, the other reveals the truth. {w=12}{nw}"
    vani "To read the secret, find the corners of the rectangle. If they share a line, look to the right or look below. {w=14}{nw}"
    
    "The tablet shows a 5x5 grid using the keyword MOHA. You must have knowledge of the Playfair Cipher to decode the keys. {w=15}{nw}"
    
    show screen playfair_grid

    $ playfair_time = 60
    $ playfair_tries = 3
    show screen playfair_timer("playfair_failed_decipher")

label decipher_key_1:
    $ renpy.block_rollback()
    
    if playfair_time <= 0 or playfair_tries <= 0:
        jump playfair_failed_decipher
        
    $ key1_ans = renpy.input("Decipher Key 1: P S T U").strip().upper()
    
    if playfair_time <= 0:
        jump playfair_failed_decipher
        
    if key1_ans == "LUST":
        "The first lock disengages with a heavy clank. {w=5}{nw}"
        jump setup_key_2
    else:
        $ playfair_tries -= 1
        if playfair_tries > 0:
            vani "Incorrect. The jewel door glows blood red. Try again. {w=5}{nw}"
            jump decipher_key_1
        else:
            jump playfair_failed_decipher

label setup_key_2:
    $ playfair_time = 60
    $ playfair_tries = 3

label decipher_key_2:
    $ renpy.block_rollback()
    
    if playfair_time <= 0 or playfair_tries <= 0:
        jump playfair_failed_decipher
        
    $ key2_ans = renpy.input("Decipher Key 2: K H X C").strip().upper()
    
    if playfair_time <= 0:
        jump playfair_failed_decipher
        
    if key2_ans == "LOVE":
        hide screen playfair_timer
        "The second lock disengages. You have successfully deciphered both keys. {w=5}{nw}"
        jump playfair_final_choice
    else:
        $ playfair_tries -= 1
        if playfair_tries > 0:
            vani "Incorrect. The silken veils tighten around you. Try again. {w=5}{nw}"
            jump decipher_key_2
        else:
            jump playfair_failed_decipher

label playfair_failed_decipher:
    hide screen playfair_timer
    hide screen playfair_grid
    
    scene black with vpunch:
        size (1920, 1080)
        
    vani "You have failed to uncover the hidden truths. Your mind is wiped clean. {w=5}{nw}"
    "You are dragged all the way back to the entrance of the cave. {w=5}{nw}"
    
    jump phase_1_krodha

label playfair_final_choice:
    $ choice_time = 15
    show screen choice_timer("playfair_wrong_choice")
    
    vani "You hold both keys: LUST and LOVE. You must now speak the correct key to open the gate and reveal the ultimate truth of the physical body. {w=12}{nw}"
    
label choice_input_loop:
    $ renpy.block_rollback()
    
    $ final_key = renpy.input("Enter the final key to open the gate:").strip().upper()
    
    if choice_time <= 0:
        jump playfair_wrong_choice
        
    if final_key in ["KHXC", "LOVE"]:
        hide screen choice_timer
        hide screen playfair_grid
        
        "The jewel-encrusted door swings open, shattering the silken illusions into dust. {w=5}{nw}"
        santosh "The physical form is temporary... only Love survives the ashes. {w=5}{nw}"
        
        "You step through, returning to the path you fell from. {w=5}{nw}"
        if has_failed_level_7:
            jump level_6_cleared
        else:
            jump level_6_start 
    else:
        jump playfair_wrong_choice

label playfair_wrong_choice:
    hide screen choice_timer
    hide screen playfair_grid
    
    scene black with hpunch:
        size (1920, 1080)
        
    vani "A fatal choice. The illusions consume your flesh. {w=5}{nw}"
    "You are thrown back to the trials of Ego. {w=5}{nw}"
    
    jump level_3_start

label level_6_cleared:
    scene phase3_1 with fade:
        size (1920, 1080)
        
    "You successfully trace your steps backwards. The oppressive darkness recedes, and a new path opens forward. {w=5}{nw}"
    
    if has_failed_level_7:
        jump level_7_punishment
    else:
        jump level_7_start

label level_7_start:
    scene phase3_2 with fade:
        size (1920, 1080)
    
    "You step into a massive, echoing area. The air is entirely still. {w=5}{nw}"
    "Ancient stone pillars block the final path. They demand a single word of historical or cultural truth to let you pass. {w=5}{nw}"
    
    $ level_7_tries = 3

label pillar_1:
    $ renpy.block_rollback()
    vani "Pillar of Dharma: It is the path of perfect Dharma. The story begins with a broken bow in Mithila and ends with the ashes of Lanka. Name the epic."
    $ ans_p1 = renpy.input("Enter the Epic:").strip().upper()
    
    if ans_p1 in ["RAMAYANA", "RAMAYAN"]:
        "The path is slowly becoming clear. {w=5}{nw}"
        jump pillar_2
    else:
        jump level_7_wrong_answer

label pillar_2:
    $ renpy.block_rollback()
    vani "Pillar of India: I am the mathematical void that ancient India gave the world. I represent nothing, yet I give value to everything."
    $ ans_p2 = renpy.input("Enter the Gift:").strip().upper()
    
    if ans_p2 in ["ZERO", "SHUNYA", "0"]:
        "The path gets more clearer now. {w=5}{nw}"
        jump pillar_3
    else:
        jump level_7_wrong_answer

label pillar_3:
    $ renpy.block_rollback()
    vani "Pillar of Devotion: A single game of dice, fueled by greed and jealousy, stripped a kingdom of its wealth and led millions to war. Name the grand epic."
    $ ans_p3 = renpy.input("Enter the Epic:").strip().upper()
    
    if ans_p3 in ["MAHABHARATA", "MAHABHARAT"]:
        "Just the last answer and then you are free. {w=5}{nw}"
        jump pillar_4
    else:
        jump level_7_wrong_answer

label pillar_4:
    $ renpy.block_rollback()
    vani "Pillar of the Gods: Revered by sages as the language of the gods (Devabhasha), its grammar is as precise as mathematics. Name this ancient tongue."
    $ ans_p4 = renpy.input("Enter the Language:").strip().upper()
    
    if ans_p4 == "SANSKRIT":
        "The path becomes clear and you advances to the end of cave but before that.... {w=5}{nw}"
        jump stage_2_guardian
    else:
        jump level_7_wrong_answer

label level_7_wrong_answer:
    $ level_7_tries -= 1
    if level_7_tries > 0:
        vani "The pillars tremble ominously. You have [level_7_tries] attempt(s) left before they crush you. {w=5}{nw}"
        jump pillar_1 
    else:
        jump level_7_fatal_failure

label stage_2_guardian:
    scene phase3_2 with dissolve:
        size (1920, 1080)
        
    "A glowing, ethereal Guardian steps forward from the shadows. {w=5}{nw}"
    vani "You know the history of the world, but do you know yourself? {w=5}{nw}"
    
label guardian_loop:
    $ renpy.block_rollback()
    vani "Tell me: What is the one thing that belongs entirely to you, yet everyone else uses it more than you do?"
    
    $ ans_guardian = renpy.input("Enter your answer:").strip().upper()
    
    if ans_guardian in ["NAME", "MY NAME"]:
        "The Guardian smiles, bowing its head before fading into the mist. {w=5}{nw}"
        jump stage_3_mirror
    else:
        vani "The Guardian's eyes flare red. 'You do not know yourself.' {w=5}{nw}"
        jump level_7_fatal_failure

label stage_3_mirror:
    scene phase3_2 with fade:
        size (1920, 1080)
    
    vani "You have proven your knowledge. You have proven your wit. Now, prove your truth. {w=5}{nw}"
    
label mirror_loop:
    $ renpy.block_rollback()
    vani "Who is the architect of this prison? Who built the Cave of Maya?"
    
    $ ans_mirror = renpy.input("Speak the truth:").strip().upper()
    
    if ans_mirror in ["SANTOSH", "ME", "MYSELF"]:
        "The truest soul is the one that embraces his own flaws. {w=5}{nw}"
        jump final_resolution
    else:
        vani "Look within yourself; the answer lies there. {w=5}{nw}"
        jump level_7_fatal_failure

label level_7_fatal_failure:
    scene phase1 with hpunch:
        size (1920, 1080)
        
    vani "You have failed the final test. Your arrogance has led you down. {w=5}{nw}"
    "The ground opens beneath you. You are falling.... {w=5}{nw}"
    
    $ has_failed_level_7 = True 
    
    jump level_7_punishment

label level_7_punishment:
    
    scene white with fade:
        size (1920, 1080) 
        
    pause 3.0
    
    show text "{color=#000000}You have fought the cave. You have fought the illusions. You have fought yourself.{/color}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    show text "{color=#000000}Your hands are bleeding. Your mind is exhausted. The timer is ticking.{/color}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve
    
    show text "{color=#000000}To break the cycle of Maya, what is the final action you must take?{/color}" at truecenter with dissolve
    pause 3.0
    hide text 
    
    $ void_time = 10
    show screen void_timer("ultimate_game_over")
    
    $ renpy.block_rollback()
    $ void_ans = renpy.input("...", length=15).strip().upper()
    
    if void_time <= 0:
        jump ultimate_game_over
        
    if void_ans in ["NOTHING", "SURRENDER", "LET GO", "ACCEPTANCE", ""]:
        hide screen void_timer
        jump level_7_start
    else:
        hide screen void_timer
        jump ultimate_game_over


label ultimate_game_over:
    hide screen void_timer
    
    scene black with fade:
        size (1920, 1080)
        
    vani "The struggle consumes you. Confiscated forever."
    
    return 

label final_resolution:
    hide screen void_timer
    
    scene white with fade:
        size (1920, 1080)
        
    "The blinding light fades. The heavy air of the cave vanishes. {w=5}{nw}"
    stop music fadeout 1.0

    play music "ending.ogg" fadein 3.0
    
    scene end with dissolve:
        size (1920, 1080)
        
    santosh "(Breathing heavily, trembling) Baba... the cave... the gold... the voice...{w=4}{nw}"
    sadhu "The cave was always within you, my son. I merely locked the door so you could finally see the walls. {w=5}{nw}"
    santosh "I am so sorry. I was arrogant. I was foolish. I kicked your holy water because I was poisoned by my own jealousy. Please, forgive me.{w=6}{nw}"
    sadhu "There is nothing to forgive. The water returns to the earth, just as your ego has returned to dust.{w=5}{nw}"

    sadhu "This was not a curse, but your destiny. You were given the name Santosh—Contentment. But a man cannot know the true meaning of his name until he has survived the starvation of his own greed.{w=7}{nw}"
    santosh "I thought I needed more to be happy. But i had everything with me. {w=3}{nw}"
    sadhu "Indeed. Do not let the illusions of Maya blind you again. {w=3}{nw}"

    scene santosh:
        size(1920, 1080)
    
    santosh "What a night... Just a few hours ago, I drove down this exact road consumed by a fire I didn't even know I had started.{w=5}{nw}"
    santosh "Well, that was a necessity too as now i have learned the real meaning of my name 'Santosh'. {w=3}{nw}"
    
    scene saintmorning with dissolve:
        size (1920, 1080)
        
    sadhu "So that was Santosh but The Awguns—anger, greed, lust, and pride resides in each one of us, All we have to do is defeat the Cave of Maya to win over it  {w=7}{nw}"
    
scene black with fade:
        size (1920, 1080)
        
call screen credits_screen
return

label game_over:
    hide screen puzzle_timer
    scene black with fade:
        size (1920, 1080)
    "Confiscated by your desires forever. {w=5}{nw}"
    "GAME OVER {w=5}{nw}"
    return