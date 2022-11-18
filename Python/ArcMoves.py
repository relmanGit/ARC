w = '#FFFFFF'
r = '#FF0000'
g = '#00FF00'
b = '#0000FF'
o = '#FFA500'
y = '#FFFF55'
default_cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
face = {'U':0, 'F':1, 'D':2, 'L':3, 'R':4, 'B': 5}
def U():
    global cube #required to MODIFY global cube
    row = 0
    col = 0
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = temp

    col = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = temp

    col = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = temp

    temp = cube[face['U']][0][0]
    cube[face['U']][0][0] = cube[face['U']][2][0]
    cube[face['U']][2][0] = cube[face['U']][2][2]
    cube[face['U']][2][2] = cube[face['U']][0][2]
    cube[face['U']][0][2] = temp

    temp = cube[face['U']][0][1]
    cube[face['U']][0][1] = cube[face['U']][1][0]
    cube[face['U']][1][0] = cube[face['U']][2][1]
    cube[face['U']][2][1] = cube[face['U']][1][2]
    cube[face['U']][1][2] =

def F():
    global cube #required to MODIFY global cube
    temp = cube[face['U']][2][0]
    cube[face['U']][2][0] = cube[face['L']][2][2]
    cube[face['L']][2][2] = cube[face['D']][0][2]
    cube[face['D']][0][2] = cube[face['R']][0][0]
    cube[face['R']][0][0] = temp

    temp = cube[face['U']][2][1]
    cube[face['U']][2][1] = cube[face['L']][1][2]
    cube[face['L']][1][2] = cube[face['D']][0][1]
    cube[face['D']][0][1] = cube[face['R']][1][0]
    cube[face['R']][1][0] = temp

    temp = cube[face['U']][2][2]
    cube[face['U']][2][2] = cube[face['L']][0][2]
    cube[face['L']][0][2] = cube[face['D']][0][0]
    cube[face['D']][0][0] = cube[face['R']][2][0]
    cube[face['R']][2][0] = temp

    temp = cube[face['F']][0][0]
    cube[face['F']][0][0] = cube[face['F']][2][0]
    cube[face['F']][2][0] = cube[face['F']][2][2]
    cube[face['F']][2][2] = cube[face['F']][0][2]
    cube[face['F']][0][2] = temp

    temp = cube[face['F']][0][1]
    cube[face['F']][0][1] = cube[face['F']][1][0]
    cube[face['F']][1][0] = cube[face['F']][2][1]
    cube[face['F']][2][1] = cube[face['F']][1][2]
    cube[face['F']][1][2] = temp

def D():
    global cube #required to MODIFY global cube
    row = 2
    col = 0
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = temp

    col = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = temp

    col = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['L']][row][col]
    cube[face['L']][row][col] = cube[face['B']][row][col]
    cube[face['B']][row][col] = cube[face['R']][row][col]
    cube[face['R']][row][col] = temp

    temp = cube[face['D']][0][0]
    cube[face['D']][0][0] = cube[face['D']][2][0]
    cube[face['D']][2][0] = cube[face['D']][2][2]
    cube[face['D']][2][2] = cube[face['D']][0][2]
    cube[face['D']][0][2] = temp

    temp = cube[face['D']][0][1]
    cube[face['D']][0][1] = cube[face['D']][1][0]
    cube[face['D']][1][0] = cube[face['D']][2][1]
    cube[face['D']][2][1] = cube[face['D']][1][2]
    cube[face['D']][1][2] = temp

def L():
    global cube #required to MODIFY global cube
    row = 0
    col = 0
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][2][2]
    cube[face['B']][2][2] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

    row = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][row][2]
    cube[face['B']][row][2] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

    row = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][0][2]
    cube[face['B']][0][2] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

    temp = cube[face['L']][0][0]
    cube[face['L']][0][0] = cube[face['L']][2][0]
    cube[face['L']][2][0] = cube[face['L']][2][2]
    cube[face['L']][2][2] = cube[face['L']][0][2]
    cube[face['L']][0][2] = temp

    temp = cube[face['L']][0][1]
    cube[face['L']][0][1] = cube[face['L']][1][0]
    cube[face['L']][1][0] = cube[face['L']][2][1]
    cube[face['L']][2][1] = cube[face['L']][1][2]
    cube[face['L']][1][2] = temp

def R():
    global cube #required to MODIFY global cube
    row = 0
    col = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][2][0]
    cube[face['B']][2][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][1][0]
    cube[face['B']][1][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][0][0]
    cube[face['B']][0][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    temp = cube[face['R']][0][0]
    cube[face['R']][0][0] = cube[face['R']][2][0]
    cube[face['R']][2][0] = cube[face['R']][2][2]
    cube[face['R']][2][2] = cube[face['R']][0][2]
    cube[face['R']][0][2] = temp

    temp = cube[face['R']][0][1]
    cube[face['R']][0][1] = cube[face['R']][1][0]
    cube[face['R']][1][0] = cube[face['R']][2][1]
    cube[face['R']][2][1] = cube[face['R']][1][2]
    cube[face['R']][1][2] = temp

def B():
    global cube #required to MODIFY global cube
    temp = cube[face['U']][0][0]
    cube[face['U']][0][0] = cube[face['R']][0][2]
    cube[face['R']][0][2] = cube[face['D']][2][2]
    cube[face['D']][2][2] = cube[face['L']][2][0]
    cube[face['L']][2][0] = temp

    temp = cube[face['U']][0][1]
    cube[face['U']][0][1] = cube[face['R']][1][2]
    cube[face['R']][1][2] = cube[face['D']][2][1]
    cube[face['D']][2][1] = cube[face['L']][1][0]
    cube[face['L']][1][0] = temp

    temp = cube[face['U']][0][2]
    cube[face['U']][0][2] = cube[face['R']][2][2]
    cube[face['R']][2][2] = cube[face['D']][2][0]
    cube[face['D']][2][0] = cube[face['L']][0][0]
    cube[face['L']][0][0] = temp

    temp = cube[face['B']][0][0]
    cube[face['B']][0][0] = cube[face['B']][2][0]
    cube[face['B']][2][0] = cube[face['B']][2][2]
    cube[face['B']][2][2] = cube[face['B']][0][2]
    cube[face['B']][0][2] = temp

    temp = cube[face['B']][0][1]
    cube[face['B']][0][1] = cube[face['B']][1][0]
    cube[face['B']][1][0] = cube[face['B']][2][1]
    cube[face['B']][2][1] = cube[face['B']][1][2]
    cube[face['B']][1][2] = temp

def U2():
    U()
    U()

def F2():
    F()
    F()

def D2():
    D()
    D()

def L2():
    L()
    L()

def R2():
    R()
    R()

def B2():
    B()
    B()

def Uprime():
    U()
    U2()

def Fprime():
    F()
    F2()

def Dprime():
    D()
    D2()

def Lprime():
    L()
    L2()

def Rprime():
    R()
    R2()

def Bprime():
    B()
    B2()

def r():
    global cube #required to MODIFY global cube
    R()
    row = 0
    col = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][2][0]
    cube[face['B']][2][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][1][0]
    cube[face['B']][1][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][0][0]
    cube[face['B']][0][0] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp
