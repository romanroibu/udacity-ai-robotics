colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

def move(p, motion, p_move):

    q = []

    rows = len(p)
    for i in range(rows):
        q.append([])
        cols = len(p[i])
        for j in range(cols):

            i_did_move = (i - motion[0]) % rows
            j_did_move = (j - motion[1]) % cols

            i_did_stay = i
            j_did_stay = j

            p_did_move = p[i_did_move][j_did_move] *      p_move
            p_did_stay = p[i_did_stay][j_did_stay] * (1 - p_move)
            q[-1].append(p_did_move + p_did_stay)

    return q


def sense(p, world, measurement, p_true):
    q = []

    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            is_hit = world[i][j] == measurement
            coeff = p_true if is_hit else (1 - p_true)
            q[-1].append(p[i][j] * coeff)

    # normalize

    total_sum = sum([ sum(row) for row in q])

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= total_sum

    return q

def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT

    rows = len(colors)
    cols = len(colors[0])
    size = rows * cols

    #initialize with uniform distribution
    p = [ [ 1. / size for col in range(cols) ] for row in range(rows) ]

    for (motion, measurement) in zip(motions, measurements):
        p = move(p, motion, p_move)
        p = sense(p, colors, measurement, sensor_right)

    #Your probability array must be printed 
    #with the following code.

    show(p)
    return p

