#Kevin Patel
#105177854


#imported random and math libary
import random
import math

tree_planted = 10
size = 30
tree = 'X'
empty_space = '_'

#created a function
def check_distance(backyard, x, y):
#loop start
    for i in range(size):
        for j in range(size):
            if backyard[i][j] == tree:
                dist = math.sqrt((i - x) ** 2 + (j - y) ** 2)
                if dist <= 3:
                    return True
    return False

#created a function
def planted_trees():
    backyard = [[empty_space for i in range(size)] for j in range(size)]
    trees_planted = 0
#loop start
    while trees_planted < tree_planted:
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        if backyard[x][y] == empty_space:
            if not check_distance(backyard, x, y):
                backyard[x][y] = tree
                trees_planted += 1
    for i in range(size):
        print(*backyard[i], sep=' ')


planted_trees()
