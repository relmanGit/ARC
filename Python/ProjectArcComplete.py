import webbrowser
#color values
w = '#FFFFFF'
r = '#FF0000'
g = '#00FF00'
b = '#0000FF'
o = '#FFA500'
y = '#FFFF55'
#create cube and solved_cube
solved_cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
face = {'U':0, 'F':1, 'D':2, 'L':3, 'R':4, 'B': 5}
ARC_REFRESH = 1 #refresh time variable
#syntactically valid html -> write to file
rubiks_html='''
<!DOCTYPE html>
<html>
<meta http-equiv="refresh" content="arcREFRESH">
<head>
<style>
table, th, td {
    width: 100px;
    height: 25px;
}
</style>
</head>
<body>
<p>Ariel's Rubik's Cube!</p>
<table>
<!-- Top Section -->
  <tr>
    <td><!-- Empty --></td>
    arcUFACE
    <td><!-- Empty --></td>
    <td><!-- Empty --></td>
  </tr>
<!-- Middle Sections -->
  <tr>
    arcLFACE
    arcFFACE
    arcRFACE
    arcBFACE
  </tr>
<!-- Bottom Section -->
  <tr>
    <td><!-- Empty --></td>
    arcDFACE
    <td><!-- Empty --></td>
    <td><!-- Empty --></td>
  </tr>
</table>
<p>© 2017, An Ariel Sharon Production</p>
</body>
</html>
'''
#structure for a face of the cube using a 3x3 table for each face
face_html='''
    <td>
      <table style="border: 1px solid black">
        <tr>
          <td bgcolor="topleft" style="border: 1px solid black"></td>
          <td bgcolor="topmiddle" style="border: 1px solid black"></td>
          <td bgcolor="topright" style="border: 1px solid black"></td>
        </tr>
        <tr>
          <td bgcolor="middleleft" style="border: 1px solid black"></td>
          <td bgcolor="middlemiddle" style="border: 1px solid black"></td>
          <td bgcolor="middleright" style="border: 1px solid black"></td>
        </tr>
        <tr>
          <td bgcolor="bottomleft" style="border: 1px solid black"></td>
          <td bgcolor="bottommiddle" style="border: 1px solid black"></td>
          <td bgcolor="bottomright" style="border: 1px solid black"></td>
        </tr>
      </table>
    </td>
'''

def generate_face_html(face_id):
    arc_string = 'arc'+face_id.upper()+'FACE'
    output = str(face_html) #copy of face_html
    output = output.replace('topleft', cube[face[face_id]][0][0])
    output = output.replace('topmiddle', cube[face[face_id]][0][1])
    output = output.replace('topright', cube[face[face_id]][0][2])
    output = output.replace('middleleft', cube[face[face_id]][1][0])
    output = output.replace('middlemiddle', cube[face[face_id]][1][1])
    output = output.replace('middleright', cube[face[face_id]][1][2])
    output = output.replace('bottomleft', cube[face[face_id]][2][0])
    output = output.replace('bottommiddle', cube[face[face_id]][2][1])
    output = output.replace('bottomright', cube[face[face_id]][2][2])
    return output
    
def HTML_output():
    output = str(rubiks_html) #copy of rubiks_html
    output = output.replace('arcREFRESH', str(ARC_REFRESH))
    string_faces = 'UDFBLR'
    for string_face in string_faces:
        output = output.replace('arc' + string_face + 'FACE', generate_face_html(string_face))
    return output

def save_HTML(filename = 'arc.html'):
    f = open(filename, 'w')
    f.write(HTML_output())
    f.close()

def open_HTML(filename = 'arc.html'):
    webbrowser.open(filename, 1)

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
    cube[face['U']][1][2] = temp

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

#functions: U2 F2 D2 L2 R2 B2
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
#funtions: U' F' D' L' R' B'
def U_prime():
    U2()
    U()
def F_prime():
    F2()
    F()
def D_prime():
    D2()
    D()
def L_prime():
    L2()
    L()
def R_prime():
    R2()
    R()
def B_prime():
    B2()
    B()

#middle column (front face) up
def mcu():
    row = 0
    col = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][2][col]
    cube[face['B']][2][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][1][col]
    cube[face['B']][1][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

    row = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = cube[face['B']][0][col]
    cube[face['B']][0][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = temp

#middle column (front face) down
def mcd():
    row = 0
    col = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][2][col]
    cube[face['B']][2][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

    row = 1
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][1][col]
    cube[face['B']][1][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

    row = 2
    temp = cube[face['F']][row][col]
    cube[face['F']][row][col] = cube[face['U']][row][col]
    cube[face['U']][row][col] = cube[face['B']][0][col]
    cube[face['B']][0][col] = cube[face['D']][row][col]
    cube[face['D']][row][col] = temp

#middle row (front face) right
def mrr():
    row = 1
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

#middle row (front face) left
def mrl():
    row = 1
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

#middle column (left face) up (clockwise)
def mlu():
    temp = cube[face['U']][1][0]
    cube[face['U']][1][0] = cube[face['L']][2][1]
    cube[face['L']][2][1] = cube[face['D']][1][2]
    cube[face['D']][1][2] = cube[face['R']][0][1]
    cube[face['R']][0][1] = temp

    temp = cube[face['U']][1][1]
    cube[face['U']][1][1] = cube[face['L']][1][1]
    cube[face['L']][1][1] = cube[face['D']][1][1]
    cube[face['D']][1][1] = cube[face['R']][1][1]
    cube[face['R']][1][1] = temp

    temp = cube[face['U']][1][2]
    cube[face['U']][1][2] = cube[face['L']][0][1]
    cube[face['L']][0][1] = cube[face['D']][1][0]
    cube[face['D']][1][0] = cube[face['R']][2][1]
    cube[face['R']][2][1] = temp

#middle column (left face) down (counter-clockwise)
def mld():
    temp = cube[face['U']][1][0]
    cube[face['U']][1][0] = cube[face['R']][0][1]
    cube[face['R']][0][1] = cube[face['D']][1][2]
    cube[face['D']][1][2] = cube[face['L']][2][1]
    cube[face['L']][2][1] = temp

    temp = cube[face['U']][1][1]
    cube[face['U']][1][1] = cube[face['R']][1][1]
    cube[face['R']][1][1] = cube[face['D']][1][1]
    cube[face['D']][1][1] = cube[face['L']][1][1]
    cube[face['L']][1][1] = temp

    temp = cube[face['U']][1][2]
    cube[face['U']][1][2] = cube[face['R']][2][1]
    cube[face['R']][2][1] = cube[face['D']][1][0]
    cube[face['D']][1][0] = cube[face['L']][0][1]
    cube[face['L']][0][1] = temp

#functions: u f d l r b x y z
def u():
    U()
    mrl()
def f():
    F()
    mlu()
def d():
    D()
    mrr()
def l():
    L()
    mcd()
def r():
    R()
    mcu()
def b():
    B()
    mld()
def x():
    r()
    L_prime()
def y():
    u()
    D_prime()
def z():
    f()
    B_prime()
#functions: u2 f2 d2 l2 r2 b2 x2 y2 z2
def u2():
    u()
    u()
def f2():
    f()
    f()
def d2():
    d()
    d()
def l2():
    l()
    l()
def r2():
    r()
    r()
def b2():
    b()
    b()
def x2():
    x()
    x()
def y2():
    y()
    y()
def z2():
    z()
    z()
#functions: u' f' d' l' r' b' x' y' z'
def u_prime():
    u2()
    u()
def f_prime():
    f2()
    f()
def d_prime():
    d2()
    d()
def l_prime():
    l2()
    l()
def r_prime():
    r2()
    r()
def b_prime():
    b2()
    b()
def x_prime():
    x2()
    x()
def y_prime():
    y2()
    y()
def z_prime():
    z2()
    z()

def menu():
    print('Welcome to Project ARC - Ariel\'s Rubik\'s Cube')
    print()
    print('Valid inputs: U F D L R B U\' F\' D\' L\' R\' B\' U2 F2 D2 L2 R2 B2 u f d l r b u\' f\' d\' l\' r\' b\' u2 f2 d2 l2 r2 b2 x y z x\' y\' z\' x2 y2 z2 reset exit')
    print()
    
def game():
    global cube
    menu()
    save_HTML()
    open_HTML()
    while True:
        user_input = input('Enter a sequence of moves separated by spaces: ')
        if user_input.upper() == 'EXIT':
            return
        elif user_input.upper() == 'RESET':
            cube = list(solved_cube)
            save_HTML()
            continue
        split_input = user_input.split() #splits on space
        #cmds - for each command entered, call correscponding function
        for cmd in split_input:
            if cmd == 'R':
                R()
            elif cmd == 'R2':
                R2()
            elif cmd == 'R\'':
                R_prime()
            elif cmd == 'L':
                L()
            elif cmd == 'L2':
                L2()
            elif cmd == 'L\'':
                L_prime()
            elif cmd == 'U':
                U()
            elif cmd == 'U2':
                U2()
            elif cmd == 'U\'':
                U_prime()
            elif cmd == 'D':
                D()
            elif cmd == 'D2':
                D2()
            elif cmd == 'D\'':
                D_prime()
            elif cmd == 'B':
                B()
            elif cmd == 'B2':
                B2()
            elif cmd == 'B\'':
                B_prime()
            elif cmd == 'F':
                F()
            elif cmd == 'F2':
                F2()
            elif cmd == 'F\'':
                F_prime()
            elif cmd == 'u':
                u()
            elif cmd == 'u2':
                u2()
            elif cmd == 'u\'':
                u_prime()
            elif cmd == 'f':
                f()
            elif cmd == 'f2':
                f2()
            elif cmd == 'f\'':
                f_prime()
            elif cmd == 'd':
                d()
            elif cmd == 'd2':
                d2()
            elif cmd == 'd\'':
                d_prime()
            elif cmd == 'l':
                l()
            elif cmd == 'l2':
                l2()
            elif cmd == 'l\'':
                l_prime()
            elif cmd == 'r':
                r()
            elif cmd == 'r2':
                r2()
            elif cmd == 'r\'':
                r_prime()
            elif cmd == 'b':
                b()
            elif cmd == 'b2':
                b2()
            elif cmd == 'b\'':
                b_prime()
            elif cmd == 'x':
                x()
            elif cmd == 'x2':
                x2()
            elif cmd == 'x\'':
                x_prime()
            elif cmd == 'y':
                y()
            elif cmd == 'y2':
                y2()
            elif cmd == 'y\'':
                y_prime()
            elif cmd == 'z':
                z()
            elif cmd == 'z2':
                z2()
            elif cmd == 'z\'':
                z_prime()
            else:
                print('Unknown input!', cmd)
        save_HTML()
    
def main():
    game()

main()
