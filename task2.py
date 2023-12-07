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
    # print(game_new)

    values = {"red":0,"blue":0,"green":0}
    for i in game_new:
        i = i.split(" ")
        i[0]  = int(i[0])
        if i[0] > values[i[1]]:
            values[i[1]] = i[0]
    
    values_list = [values for key, values in values.items()]
    mutiple = 1
    for i in values_list:
        mutiple *= i 
    
    games_possible += mutiple

print(games_possible)
    
