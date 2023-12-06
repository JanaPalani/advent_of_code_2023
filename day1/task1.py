file = open("task1.txt","r")

data = file.read()

data = data.split()

list_of_num = []
for i in data:
    each_num = ""
    for j in i:
        if j.isnumeric():
            each_num += j
            break
    for j in i[::-1]:
        if j.isnumeric():
            each_num+= j 
            break
    list_of_num.append(int(each_num))

print(sum(list_of_num))  
