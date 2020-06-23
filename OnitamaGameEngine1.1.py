#    Project: OnitamaGameEngine
#    Name: Samuel Tran
#    File Created: 06/13/2020
from tkinter import *
from PIL import ImageTk,Image
import random, math

Tiger = ((-2, 0), (1, 0))
Crab = ((0, 2), (0, -2), (-1, 0))
Monkey = ((1, -1), (1, 1), (-1, -1), (-1, 1))
Crane = ((1, -1), (1, 1), (-1, 0))
Goose = ((0, 1), (0, -1), (-1, -1), (1, 1))
Eel = ((1, -1), (-1, -1), (0, 1))
Rabbit = ((-1, 1), (1, -1), (0, 2))
Ox = ((1, 0), (-1, 0), (0, 1))
Dragon = ((-1, 2), (-1, -2), (1, 1), (1, -1))
Elephant = ((-1, -1), (0, 1), (0, -1), (-1, 1))
Mantis = ((-1, 1), (1, 0), (-1, -1))
Boar = ((-1, 0), (0, 1), (0, -1))
Frog = ((-1, -1), (0, -2), (1, 1))
Horse = ((1, 0), (-1, 0), (0, -1))
Rooster = ((0, 1), (-1, 1), (0, -1), (1, -1))
Cobra = ((0, -1), (-1, 1), (1, 1))

card_moves = [Tiger, Crab, Monkey, Crane, Goose, Eel, Rabbit, Ox, 
             Dragon, Elephant, Mantis, Boar, Frog, Horse, Rooster, 
             Cobra]

pawn_type_index = [0, 0, 1, 0, 0]
SIDE = 104

deck = list(range(0,15))
random.shuffle(deck)
red_cards = [deck[0], deck[1]]
blue_cards = [deck[2], deck[3]]

WHITE = '#fdfefe'
DARK_GREEN = '#599974'
LIGHT_GREEN = '#c1ff86'

#GameState: 
# 0 : Non-Active, Not-Start
# 1 : Active, Start
# 2 : Active, Not-Start
game_state = 0


start_game = 0
is_red_turn = 1
rotate_cards = 0

s_row = -1
s_col = -1

e_row = -1
e_col = -1

first_click = 1

root = Tk()
root.title('Onitama Game Engine')
root.iconbitmap('assets/Logo.ico')

width_of_window = 1100
height_of_window = 900

canvas = Canvas(root, width=width_of_window, height=height_of_window)
board_img = ImageTk.PhotoImage(Image.open("assets/Board.bmp"))

canvas.create_image(0, 0, anchor=NW, image=board_img)
canvas.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coord = (screen_width/2) - (width_of_window/2)
y_coord = (screen_height/2) - (height_of_window/2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coord, y_coord))

root.resizable(False, False)

start_img = ImageTk.PhotoImage(Image.open("assets/StartButton.png"))

red_student_img = ImageTk.PhotoImage(Image.open("assets/StudentRed.png"))
red_master_img = ImageTk.PhotoImage(Image.open("assets/MasterRed.png"))
blue_student_img = ImageTk.PhotoImage(Image.open("assets/StudentBlue.png"))
blue_master_img = ImageTk.PhotoImage(Image.open("assets/MasterBlue.png"))

tiger_img = Image.open("assets/TigerCard.png")
crab_img = Image.open("assets/CrabCard.png")
monkey_img = Image.open("assets/MonkeyCard.png")
crane_img = Image.open("assets/CraneCard.png")
goose_img = Image.open("assets/GooseCard.png")
eel_img = Image.open("assets/EelCard.png")
rabbit_img = Image.open("assets/RabbitCard.png")
ox_img = Image.open("assets/OxCard.png")

dragon_img = Image.open("assets/DragonCard.png")
elephant_img = Image.open("assets/ElephantCard.png")
mantis_img = Image.open("assets/MantisCard.png")
boar_img = Image.open("assets/BoarCard.png")
frog_img = Image.open("assets/FrogCard.png")
horse_img = Image.open("assets/HorseCard.png")
rooster_img = Image.open("assets/RoosterCard.png")
cobra_img = Image.open("assets/CobraCard.png")

card_imgs = [tiger_img, crab_img, monkey_img, crane_img, goose_img, 
             eel_img, rabbit_img, ox_img, dragon_img, elephant_img, 
             mantis_img, boar_img, frog_img, horse_img, rooster_img, cobra_img]

#Blue Cards : 0 - 7 index
#Red Cards : 8 - 15 index
card_tk_imgs = []
for c in card_imgs:
    card_tk_imgs.append(ImageTk.PhotoImage(c))

rotated_card_imgs = []
for c in card_imgs:
    rotated_card_imgs.append(ImageTk.PhotoImage(c.rotate(180)))

red_starts_img = ImageTk.PhotoImage(Image.open("assets/RedStarts.png"))
blue_starts_img = ImageTk.PhotoImage(Image.open("assets/BlueStarts.png"))

how_to_play_img = ImageTk.PhotoImage(Image.open("assets/HowToPlay.png"))

green_square_img = ImageTk.PhotoImage(Image.open("assets/GreenSquare.png"))
white_square_img = ImageTk.PhotoImage(Image.open("assets/WhiteSquare.png"))

red_wins_img = ImageTk.PhotoImage(Image.open("assets/RedWins.png"))
blue_wins_img = ImageTk.PhotoImage(Image.open("assets/BlueWins.png"))

class Pawn:
    def __init__(self, index, row, col, type):
        self.index = index
        self.row = row
        self.col = col
        self.type = type

class Move:
    def __init__(self, posit1, posit2, start_row, start_col, end_row, end_col):
        self.posit1 = posit1
        self.posit2 = posit2
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col

def start_button_clicked():
    global start_game, game_state, is_red_turn
    if is_red_turn:
        red_card1.config(state=NORMAL)
        red_card2.config(state=NORMAL)
    elif not is_red_turn:
        blue_card1.config(state=NORMAL)
        blue_card2.config(state=NORMAL)
    start_game = 1
    game_state = 1
    start_button.destroy()
    how_to_play_lbl.destroy()

start_button = Button(root, image=start_img, relief=RAISED)
start_button.config(command=start_button_clicked)
start_button.place(x=SIDE*7.7, y=SIDE*3.8)

best_move = None

Board = []
for i in range(5):
    tiles = [0, 0, 0, 0, 0]
    Board.append(tiles)

#-1,-2,-4,-5 : Blue Student
#-3 : Blue Master
#1,2,4,5 : Red Student
#3 : Red Master
for j in range(5):
    Board[0][j] =- (j+1)
for j in range(5):
    Board[4][j] = (j+1)

blue_pawns = []
for col in range(5):
    BlueTemp = Pawn(Board[0][col], 0, col,0)
    blue_pawns.append(BlueTemp)

red_pawns = []
for col in range(5):
    RedTemp = Pawn(Board[4][col], 4, col,0)
    red_pawns.append(RedTemp)

color_pawns=[blue_pawns, red_pawns]
for row in range(2):
    for col in range(5):
        color_pawns[row][col].type = pawn_type_index[col]

color_alive = []
red_alive = list(range(5))
blue_alive = list(range(5))
color_alive = [red_alive, blue_alive]

blue_pawn_lbls = []
red_pawn_lbls = []

blue_pawn_lbls.append(Label(root, image=blue_student_img, bd=0))
blue_pawn_lbls.append(Label(root, image=blue_student_img, bd=0))
blue_pawn_lbls.append(Label(root, image=blue_master_img, bd=0))
blue_pawn_lbls.append(Label(root, image=blue_student_img, bd=0))
blue_pawn_lbls.append(Label(root, image=blue_student_img, bd=0))
for j in range(5):
    blue_pawn_lbls[j].config(bg=WHITE)
    blue_pawn_lbls[j].place(x=SIDE*(j+2.81), y=SIDE*1.85)

red_pawn_lbls.append(Label(root, image=red_student_img, bd=0))
red_pawn_lbls.append(Label(root, image=red_student_img, bd=0))
red_pawn_lbls.append(Label(root, image=red_master_img, bd=0))
red_pawn_lbls.append(Label(root, image=red_student_img, bd=0))
red_pawn_lbls.append(Label(root, image=red_student_img, bd=0))
for j in range(5):
    red_pawn_lbls[j].config(bg=WHITE)
    red_pawn_lbls[j].place(x=SIDE*(j+2.81), y=SIDE*5.85)

color_pawn_lbls=[blue_pawn_lbls, red_pawn_lbls]

red_clicked = None
blue_clicked = None
current_card = None
color_starts = 0

def red_card_clicked(widget, card_type):
    global red_clicked, current_card
    
    if is_red_turn:
        widget['state'] = NORMAL
        if red_clicked:
            red_clicked['relief'] = widget['relief']
            red_clicked['bg'] = widget['bg']
    
        widget['relief'] = SUNKEN
        widget['bg'] = '#4dff00'
    
        red_clicked = widget
        current_card = card_type

def blue_card_clicked(widget, card_type):
    global blue_clicked, current_card
    
    if (not is_red_turn):
        widget['state'] = NORMAL
        if blue_clicked:
            blue_clicked['relief'] = widget['relief']
            blue_clicked['bg'] = widget['bg']
    
        widget['relief'] = SUNKEN
        widget['bg'] = '#4dff00'
    
        blue_clicked = widget
        current_card = card_type

red_card1=Button(root, image=card_tk_imgs[deck[0]], relief=RAISED, 
                 bd=3, bg='black', state=DISABLED)
red_card1.config(command=lambda arg=red_card1:red_card_clicked(arg, deck[0]))
red_card1.place(x=SIDE*2.70, y=SIDE*6.85)

red_card2=Button(root, image=card_tk_imgs[deck[1]], relief=RAISED, 
                 bd=3, bg='black', state=DISABLED)
red_card2.config(command=lambda arg=red_card2:red_card_clicked(arg, deck[1]))
red_card2.place(x=SIDE*5.77, y=SIDE*6.85)

blue_card1=Button(root, image=rotated_card_imgs[deck[2]], relief=RAISED, 
                  bd=3, bg='black', state=DISABLED)
blue_card1.config(command=lambda arg=blue_card1:blue_card_clicked(arg, deck[2]))
blue_card1.place(x=SIDE*2.70, y=SIDE*0.02)

blue_card2=Button(root, image=rotated_card_imgs[deck[3]], relief=RAISED, 
                  bd=3, bg='black', state=DISABLED)
blue_card2.config(command=lambda arg=blue_card2:blue_card_clicked(arg, deck[3]))
blue_card2.place(x=SIDE*5.77, y=SIDE*0.02)

neutral_card=Label(root, image=card_tk_imgs[deck[4]], bd=0)
neutral_card.place(x=SIDE*0.35, y=SIDE*3.5)

if deck[4] in range(8):
    is_red_turn = 0
    blue_card1.config(state=NORMAL)
    blue_card2.config(state=NORMAL)
    
    blue_starts_lbl = Label(root, image=blue_starts_img, bd=0)
    blue_starts_lbl.place(x=SIDE*0.35, y=SIDE*2)
    color_starts = 1
    
else:
    is_red_turn = 1
    red_card1.config(state=NORMAL)
    red_card2.config(state=NORMAL)
    
    red_starts_lbl = Label(root, image=red_starts_img, bd=0)
    red_starts_lbl.place(x=SIDE*0.35, y=SIDE*6)
    color_starts = 2

def switch_players_turn():
    global rotate_cards, color_starts, current_card
    
    rotate_cards += 1
    
    current_card = None
    
    red_card1.config(bg='black')
    red_card2.config(bg='black')
    
    blue_card1.config(bg='black')
    blue_card2.config(bg='black')
    
    if rotate_cards == 2:
        red_card1.config(image=card_tk_imgs[deck[1]], command=lambda arg=red_card1:red_card_clicked(arg, deck[1]))
        red_card2.config(image=card_tk_imgs[deck[3]], command=lambda arg=red_card2:red_card_clicked(arg, deck[3]))
        
        blue_card1.config(image=rotated_card_imgs[deck[4]], command=lambda arg=blue_card1:blue_card_clicked(arg, deck[4]))
        blue_card2.config(image=rotated_card_imgs[deck[2]], command=lambda arg=blue_card2:blue_card_clicked(arg, deck[2]))
        
        neutral_card.config(image=card_tk_imgs[deck[0]])
        
        if color_starts == 2:
            red_starts_lbl.destroy()
        if color_starts == 1:
            blue_starts_lbl.destroy()
    if rotate_cards == 4:
        red_card1.config(image=card_tk_imgs[deck[3]], command=lambda arg=red_card1:red_card_clicked(arg, deck[3]))
        red_card2.config(image=card_tk_imgs[deck[2]], command=lambda arg=red_card2:red_card_clicked(arg, deck[2]))
        
        blue_card1.config(image=rotated_card_imgs[deck[0]], command=lambda arg=blue_card1:blue_card_clicked(arg, deck[0]))
        blue_card2.config(image=rotated_card_imgs[deck[4]], command=lambda arg=blue_card2:blue_card_clicked(arg, deck[4]))
        
        neutral_card.config(image=card_tk_imgs[deck[1]])
    if rotate_cards == 6:
        red_card1.config(image=card_tk_imgs[deck[2]], command=lambda arg=red_card1:red_card_clicked(arg, deck[2]))
        red_card2.config(image=card_tk_imgs[deck[4]], command=lambda arg=red_card2:red_card_clicked(arg, deck[4]))
        
        blue_card1.config(image=rotated_card_imgs[deck[1]], command=lambda arg=blue_card1:blue_card_clicked(arg, deck[1]))
        blue_card2.config(image=rotated_card_imgs[deck[0]], command=lambda arg=blue_card2:blue_card_clicked(arg, deck[0]))
        
        neutral_card.config(image=card_tk_imgs[deck[3]])
    if rotate_cards == 8:
        rotate_cards = 0
        red_card1.config(image=card_tk_imgs[deck[4]], command=lambda arg=red_card1:red_card_clicked(arg, deck[4]))
        red_card2.config(image=card_tk_imgs[deck[0]], command=lambda arg=red_card2:red_card_clicked(arg, deck[0]))
        
        blue_card1.config(image=rotated_card_imgs[deck[3]], command=lambda arg=blue_card1:blue_card_clicked(arg, deck[3]))
        blue_card2.config(image=rotated_card_imgs[deck[1]], command=lambda arg=blue_card2:blue_card_clicked(arg, deck[1]))
        
        neutral_card.config(image=card_tk_imgs[deck[2]])
        
    if is_red_turn:
        red_card1.config(state=NORMAL)
        red_card2.config(state=NORMAL)
        
        blue_card1.config(state=DISABLED)
        blue_card2.config(state=DISABLED)
    if (not is_red_turn):
        blue_card1.config(state=NORMAL)
        blue_card2.config(state=NORMAL)
        
        red_card1.config(state=DISABLED)
        red_card2.config(state=DISABLED)

def found_moves(P, card_type):
    global card_moves, color_pawns, Board, is_red_turn
    
    if card_type == None:
        return
    
    FoundMoves = []
    index = P.index
    for c in card_moves[card_type]:
        y = c[0]
        x = c[1]
        r = P.row + y
        c = P.col + x
        
        if (not is_red_turn):
            r = P.row - y
            c = P.col - x
        if (r >= 0 and r <= 4 and c >= 0 and c <= 4):
            if(Board[r][c] == 0):
                next_move = Move(index, 0, P.row, P.col, r, c)
                FoundMoves.append(next_move)
            elif (Board[r][c]*index < 0):
                next_move = Move(index, Board[r][c], P.row, P.col, r, c)
                FoundMoves.append(next_move)
    return FoundMoves

show_move_lbls = []

def show_valid_moves(image_index, card_type):
    global color_pawns, is_red_turn, color_alive, show_move_lbls
    
    if card_type == None:
        return
    
    for i in range(len(show_move_lbls)):
        if show_move_lbls[i].cget('text') == "G":
            show_move_lbls[i].destroy()
    show_move_lbls.clear()
    
    turn = 1
    if (not is_red_turn):
        turn = 0
    all_moves = found_moves(color_pawns[turn][image_index], card_type)
    
    all_end_cols = []
    all_end_rows = []
    
    for m in all_moves:
        if turn == 1:
            if Board[m.end_row][m.end_col] == 0:
                all_end_cols.append(m.end_col)
                all_end_rows.append(m.end_row)
            elif Board[m.end_row][m.end_col] < 0:
                index = (Board[m.end_row][m.end_col] * -1) - 1
                color_pawn_lbls[0][index].config(bg=LIGHT_GREEN)
        elif turn == 0:
            if Board[m.end_row][m.end_col] == 0:
                all_end_cols.append(m.end_col)
                all_end_rows.append(m.end_row)
            elif Board[m.end_row][m.end_col] > 0:
                index = Board[m.end_row][m.end_col] - 1
                color_pawn_lbls[1][index].config(bg=LIGHT_GREEN)
    for k in range(len(all_end_cols)):
        show_move_lbls.append(Label(root, image=green_square_img, bd=0, text="G"))
        show_move_lbls[k].place(x=(SIDE*all_end_cols[k])+292, y=(SIDE*all_end_rows[k])+192)

def is_valid_move(image_index, card_type):
    global color_pawns, is_red_turn, best_move
    
    turn = 1
    
    if (not is_red_turn):
        turn = 0
    
    legal_moves = found_moves(color_pawns[turn][image_index], card_type)
    
    for m in legal_moves:
        if ((m.end_row == best_move.end_row) and (m.end_col == best_move.end_col)):
            best_move = m
            return 1
    return 0

def update_board():
    global color_pawn_lbls, color_pawns, best_move, is_red_turn, current_card, game_state

    moves = best_move
    start_type = 1
    start_index = moves.posit1 - 1

    if (moves.posit1 < 0):
        start_type = 0
        start_index =- moves.posit1 - 1
                        
    end_type = 1
    end_index = moves.posit2 - 1
    
    if (moves.posit2 < 0):
        end_type = 0
        end_index =- moves.posit2 - 1
        
    for i in range(2):
        for j in color_alive[i]:
            if (color_pawns[i][j].index == 0):
                color_alive[i].remove(j)
    
    image_type = 1
    image_index = moves.posit1 - 1
                    
    if (moves.posit1 < 0):
        image_type = 0
        image_index =- moves.posit1 - 1
    
    Board[moves.start_row][moves.start_col] = 0
    Board[moves.end_row][moves.end_col] = moves.posit1
    
    color_pawns[start_type][start_index].row = moves.end_row
    color_pawns[start_type][start_index].col = moves.end_col
    
    if (moves.posit2 != 0):
        color_pawns[end_type][end_index].index = 0
    
    color_pawn_lbls[image_type][image_index].place(x=(SIDE*moves.end_col) + 292, y=(SIDE*moves.end_row) + 192)
    color_pawn_lbls[image_type][image_index].config(bg=WHITE)
                    
    if (moves.posit2 != 0):
        end_type = 1
        end_index = moves.posit2-1
        if(moves.posit2 < 0):
            end_type = 0
            end_index =- moves.posit2-1
        color_pawn_lbls[end_type][end_index].place(x=-2*SIDE, y=-2*SIDE)
    
        win_condition(image_type, end_type, end_index, moves.end_row, moves.end_col)

    win_condition(image_type, end_type, end_index, moves.end_row, moves.end_col)
    is_red_turn = not is_red_turn
    switch_players_turn()

def win_condition(image_type, end_type, end_index, end_row, end_col):
    global game_state, color_pawns, start_game
    
    #THE WAY OF THE STONE: If any pawn captures the enemy's MASTER pawn
    if (color_pawns[end_type][end_index].type == 1):
        if (end_type == 0): 
            show_red_wins=Label(root, image=red_wins_img, bd=0)
            show_red_wins.place(x=SIDE*(3.85), y=SIDE*3.5)
            game_state = 0
            start_game = 0
        elif (end_type == 1):
            show_blue_wins=Label(root, image=blue_wins_img, bd=0)
            show_blue_wins.place(x=SIDE*(3.85), y=SIDE*3.5)
            game_state = 0
            start_game = 0
    
    #THE WAY OF THE STREAM: If any pawn lands on the enemy's shrine
    if ((image_type == 1) and (end_row == 0) and (end_col == 2)):
        show_red_wins=Label(root, image=red_wins_img, bd=0)
        show_red_wins.place(x=SIDE*(3.85), y=SIDE*3.5)
        game_state = 0
        start_game = 0
    elif ((image_type == 0) and (end_row == 4) and (end_col == 2)):
        show_blue_wins=Label(root, image=blue_wins_img, bd=0)
        show_blue_wins.place(x=SIDE*(3.85), y=SIDE*3.5)
        game_state = 0
        start_game = 0

def mouse_position(event):
    global game_state, start_game, red_card1, red_card2, blue_card1, blue_card2
    
    MOUSE_Y = root.winfo_pointery() - root.winfo_rooty()
    MOUSE_X = root.winfo_pointerx() - root.winfo_rootx()
    
    if (game_state):
        click_board(MOUSE_Y, MOUSE_X)
    elif (MOUSE_X >= SIDE*2.769 and MOUSE_X < SIDE*7.807 and MOUSE_Y >= SIDE*1.817 and MOUSE_Y < SIDE*6.836):
        if (start_game == 1):
            game_state = 1
        print("Game State = ", game_state)

def click_board(i, j):
    global is_red_turn, color_pawns, first_click, current_card, Board
    global s_row, s_col, e_row, e_col, r, c
    global best_move, show_move_lbls
    
    if (i >= SIDE*1.817 and i < SIDE*6.836 and j >= SIDE*2.769 and j < SIDE*7.807):
        if i in range (192, 291):
            r = 0
        elif i in range (296, 395):
            r = 1
        elif i in range (400, 499):
            r = 2
        elif i in range (504, 603):
            r = 3
        elif i in range (608, 707):
            r = 4
        
        if j in range (292, 391):
            c = 0
        elif j in range (396, 495):
            c = 1
        elif j in range (500, 599):
            c = 2
        elif j in range (604, 703):
            c = 3
        elif j in range (708, 807):
            c = 4
        
        if (first_click):
            if ((Board[r][c] > 0) and is_red_turn):
                first_click = 0
                
                s_row = r
                s_col = c
                
                image_type = 1 
                image_index = Board[s_row][s_col] - 1
                
                color_pawn_lbls[image_type][image_index].config(bg=DARK_GREEN)
                
                show_valid_moves(image_index, current_card)
                
            elif ((Board[r][c] < 0) and (not is_red_turn)):
                first_click = 0
                
                s_row = r
                s_col = c
                
                image_type = 0
                image_index =- Board[s_row][s_col] - 1
                
                color_pawn_lbls[image_type][image_index].config(bg=DARK_GREEN)
                
                show_valid_moves(image_index, current_card)
                
                
        else:
            for l in range(len(show_move_lbls)):
                if show_move_lbls[l].cget('text') == "G":
                    show_move_lbls[l].destroy()
            show_move_lbls.clear()
            
            for i in range(2):
                for j in range(5):
                    color_pawn_lbls[i][j].config(bg=WHITE)
            
            if (Board[r][c]*Board[s_row][s_col] > 0):
                image_type = 1
                image_index = Board[s_row][s_col] - 1
                
                if (Board[s_row][s_col] < 0):
                    image_type = 0
                    image_index =- Board[s_row][s_col] - 1
                
                color_pawn_lbls[image_type][image_index].config(bg=WHITE)
                
                if (s_row != r or s_col != c):
                    s_row = r
                    s_col = c
                    image_type = 1
                    image_index = Board[s_row][s_col] - 1
                    if (Board[s_row][s_col] < 0):
                        image_type = 0
                        image_index =- Board[s_row][s_col] - 1
                    color_pawn_lbls[image_type][image_index].config(bg=DARK_GREEN)
                    show_valid_moves(image_index, current_card)
                else:
                    first_click = 1
                    s_row = -1
                    s_col = -1
                    
            else:
                first_click = 1
                e_row = r
                e_col = c
                best_move = Move(Board[s_row][s_col], Board[e_row][e_col], s_row, s_col, e_row, e_col)
                
                image_index = Board[s_row][s_col] - 1
                if (not is_red_turn):
                    image_index =- Board[s_row][s_col] - 1
                
                if (is_valid_move(image_index, current_card)):
                    update_board()
                else:
                    image_type = 1
                    image_index = Board[s_row][s_col] - 1
                    if (Board[s_row][s_col]<0):
                        image_type = 0
                        image_index =- Board[s_row][s_col] - 1
                    color_pawn_lbls[image_type][image_index].config(bg=WHITE)

how_to_play_lbl = Label(root, image=how_to_play_img, bd=0)
how_to_play_lbl.place(x=SIDE*2.88, y=SIDE*1.92)

if (game_state == 0):
        red_card1.config(state=DISABLED)
        red_card2.config(state=DISABLED)
            
        blue_card1.config(state=DISABLED)
        blue_card2.config(state=DISABLED)

root.bind('<Button-1>', mouse_position)

root.mainloop()

