#Kevin Patel
#105177854

# created function empty
def empty(a):
	x = 0
#loop start
	for i in range(len(a)):
		for j in range(len(a[i])):
			if (a[i][j] != 0):
				x = 1
	return x == 0
#created function find
def find(a, b):
    list1 = []
    list2 = [-1, -1]
#loop start
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == b):
                list1.append(i)
                list1.append(j)
#condition to check
    if len(list1) == 2:
        return list1
    else:
        return list2


grid = [[23, 34, 67], [44, 5, 3], [7, 8, 9]]
#grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] 
print('empty(grid) ->',empty(grid)) 
print('find(grid,69) ->',find(grid,8)) 
