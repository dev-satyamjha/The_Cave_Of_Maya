init python:
    class WordleGame:
        def __init__(self, answer, chances, time_left, on_fail, on_win):
            self.answer = answer.upper()
            self.chances = chances
            self.time_left = time_left
            self.on_fail = on_fail
            self.on_win = on_win
            
            self.history = [] 
            self.keys = {chr(i): "default" for i in range(65, 91)} 
            self.typed = ""
            
        def tick(self):
            self.time_left -= 1
            if self.time_left <= 0: 
                renpy.jump(self.on_fail)
            renpy.restart_interaction()
            
        def type_letter(self, letter):
            if len(self.typed) < len(self.answer):
                self.typed += letter.upper()
                renpy.restart_interaction()
                
        def delete_letter(self):
            if self.typed:
                self.typed = self.typed[:-1]
                renpy.restart_interaction()
                
        def submit(self):
            if len(self.typed) != len(self.answer): 
                return 
            
            colors = ["grey"] * len(self.answer)
            ans_chars = list(self.answer)
            typed_chars = list(self.typed)
            
            for i in range(len(self.answer)):
                if typed_chars[i] == ans_chars[i]:
                    colors[i] = "green"
                    self.keys[typed_chars[i]] = "green"
                    ans_chars[i] = None 
                    typed_chars[i] = None
                    
            for i in range(len(self.answer)):
                if typed_chars[i] is not None:
                    char = typed_chars[i]
                    if char in ans_chars:
                        colors[i] = "yellow"
                        if self.keys[char] != "green":
                            self.keys[char] = "yellow"
                        ans_chars[ans_chars.index(char)] = None
                    elif self.keys[char] == "default":
                        self.keys[char] = "grey"
                            
            self.history.append((self.typed, colors))
            self.typed = ""
            
            if colors.count("green") == len(self.answer):
                renpy.jump(self.on_win)
            elif len(self.history) >= self.chances:
                renpy.jump(self.on_fail)
                
            renpy.restart_interaction()

screen wordle_ui(game):
    text "Time Left: [game.time_left]s" xalign 0.9 yalign 0.1 size 40 color "#ff5555" outlines [(2, "#000", 0, 0)]
    timer 1.0 repeat True action Function(game.tick)
    
    vbox xalign 0.5 yalign 0.3 spacing 10:
        for i in range(game.chances):
            hbox spacing 10:
                if i < len(game.history):
                    $ word, colors = game.history[i]
                    for j in range(len(game.answer)):
                        $ bg = "#538d4e" if colors[j] == "green" else ("#b59f3b" if colors[j] == "yellow" else "#3a3a3c")
                        frame background bg xysize (70, 70):
                            text word[j] align (0.5, 0.5) size 40 color "#fff" bold True
                elif i == len(game.history):
                    for j in range(len(game.answer)):
                        frame background "#818384" xysize (70, 70):
                            if j < len(game.typed):
                                text game.typed[j] align (0.5, 0.5) size 40 color "#fff" bold True
                else:
                    for j in range(len(game.answer)):
                        frame background "#818384" xysize (70, 70)
                            
    vbox xalign 0.5 yalign 0.85 spacing 10:
        for row in ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]:
            hbox xalign 0.5 spacing 8:
                for char in row:
                    $ state = game.keys[char]
                    $ bg = "#538d4e" if state == "green" else ("#b59f3b" if state == "yellow" else ("#3a3a3c" if state == "grey" else "#d3d6da"))
                    $ txt = "#fff" if state != "default" else "#000"
                    
                    button background bg xysize (50, 60) action Function(game.type_letter, char):
                        text char align (0.5, 0.5) size 24 color txt bold True
                        
        hbox xalign 0.5 spacing 20:
            button background "#d3d6da" xysize (120, 60) action Function(game.submit):
                text "ENTER" align (0.5, 0.5) size 20 color "#000" bold True
            button background "#d3d6da" xysize (120, 60) action Function(game.delete_letter):
                text "DELETE" align (0.5, 0.5) size 20 color "#000" bold True
                
    key "K_BACKSPACE" action Function(game.delete_letter)
    key "K_RETURN" action Function(game.submit)
    key "K_KP_ENTER" action Function(game.submit)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        key char.lower() action Function(game.type_letter, char)