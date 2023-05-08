deg = 0
shape = [[[1, 1, 1], [0, 1, 0]], [[0, 1,0], [0, 1, 1], [0, 1, 0]], [[0, 1,0], [1, 1, 0], [0, 1, 0]]]
#shape = [[1, 1, 1], [0, 1, 0]], shape2 = [[0, 1, 0], [0, 1, 1], [0, 1, 0]], shape3 = [[0, 1,0], [1, 1, 0], [0, 1, 0]]
shape2 = [[0, 1,0], [0, 1, 1], [0, 1, 0]]
shape3 = [[0, 1,0], [1, 1, 0], [0, 1, 0]]
        #if the shape is rotated 4 times, it goes back to its original shape
deg = (deg + 1) % 4
print(shape)