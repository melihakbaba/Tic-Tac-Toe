import tkinter

player_x = "X"
player_o = "O"
current_player = player_x

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#00c9ff"
color_orange = "#ff9b00"
background_color = "#3a3b3c"
color_light_grey = "#646464"
color_yellow= "#e0de07"

X_score = 0
O_score = 0
tie_score = 0

turns = 0
game_over = False

def set_tile(row,column):
    global current_player
    
    if game_over:
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = current_player
    
    if current_player == player_o:
        current_player = player_x
    else:
        current_player = player_o
        
    label["text"] = current_player+"'s turn"
    
    check_winner()
        
def check_winner():
    global turns,game_over,X_score,O_score,tie_score
    turns += 1
    
    #horizontal check
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text = board[row][0]["text"]+" is the winner!" ,foreground=color_orange)
            if board[row][0]["text"] == "X":
                X_score+=1
            else:
                O_score+=1
            score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
            for column in range(3):
                board[row][column].config(foreground=color_orange,background=color_light_grey)
            game_over=True
            return
                
    #vertical check
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!",foreground=color_orange)
            if board[0][column]["text"] == "X":
                X_score+=1
            else:
                O_score+=1
            score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
            for row in range(3):
                board[row][column].config(foreground=color_orange,background=color_light_grey)
            game_over=True
            return
        
    #diagonal check
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!",foreground=color_orange)
        if board[0][0]["text"] == "X":
            X_score+=1
        else:
            O_score+=1
        score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
        for i in range(3):
            board[i][i].config(foreground=color_orange,background=color_light_grey)
        game_over=True
        return
    
    #anti-diagonal check
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_orange)
        if board[0][2]["text"] == "X":
            X_score+=1
        else:
            O_score+=1
        score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
        board[0][2].config(foreground=color_orange, background=color_light_grey)
        board[1][1].config(foreground=color_orange, background=color_light_grey)
        board[2][0].config(foreground=color_orange, background=color_light_grey)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)
        tie_score +=1
        score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
        for row in range(3):
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_grey)
        
def new_game():
    global turns,game_over
    
    turns = 0
    game_over = False

    label.config(text=current_player+"'s turn",foreground="white")
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=color_blue,background=background_color)

def clear_score():
    global X_score,O_score,tie_score
    X_score = 0
    O_score = 0
    tie_score = 0
    score_label.config(text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""")
        
# WINDOW

window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False,False)
window.iconbitmap("C:\\Users\\melih\\Desktop\\PROJE DOSYALARI\\TIC-TAC-TOE\\favicon.ico")
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = current_player + "'s turn", font = ("Consolas",20),
                      background=background_color,foreground="white")
label.grid(row=0, column=0 , columnspan=4 ,sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="",font = ("Consolas",50,"bold"),
                                          background=background_color,foreground=color_blue,
                                          width=4,height=1,command = lambda row=row,column=column : set_tile(row,column))
        board[row][column].grid(row=row+1 , column=column)

restart_button = tkinter.Button(frame, text="Restart", font=("Consolas",20) ,background=background_color,
                        foreground="white" ,command=new_game)
restart_button.grid(row=4,column=0,columnspan=3,sticky="we")


clear_button = tkinter.Button(frame,text="Clear Scoreboard",font=("Consolas",20) ,background=background_color,
                        foreground="white" ,command=clear_score)
clear_button.grid(row=4,column=3)


score_label = tkinter.Label(frame,text=f"""Scoreboard\n\nPlayer X = {str(X_score)}\nPlayer O = {str(O_score)}\nTie = {str(tie_score)}""",font = ("Consolas",20),
                      background=background_color,foreground="white")
score_label.grid(row=1,column=3,rowspan=2,sticky="wens")

blank_label = tkinter.Label(frame,text="",background=background_color)
blank_label.grid(row=3,column=3,rowspan=1,sticky="wens")


frame.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()