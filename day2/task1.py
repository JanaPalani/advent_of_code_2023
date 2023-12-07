file = open("task.txt","r")

file = file.read()

data = file.split("\n")

available = {"red":12,"blue":14,"green":13}

games_possible = 0

for index,game in enumerate(data):
    game = game.split(": ")
    game.pop(0)
    game = game[0].split("; ")
    game_new= ()
    for draws_index,each_draw in enumerate(game):
       each_draw = tuple(each_draw.split(", "))
       game_new += each_draw 
    game_new = list(game_new)

    game = []
    
    for i in game_new:
        i = i.split(" ")
        i[0]  = int(i[0])
        if i[0] <= available[i[1]] :pass     
        else :break 
    
    else:
        games_possible += index + 1
    
print(games_possible)