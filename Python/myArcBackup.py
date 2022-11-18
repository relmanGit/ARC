import webbrowser

w = '#FFFFFF'
r = '#FF0000'
g = '#00FF00'
b = '#0000FF'
o = '#FFA500'
y = '#FFFF55'
cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
face = {'U':0, 'F':1, 'D':2, 'L':3, 'R':4, 'B': 5}
i = 0
##print('***CUBE STATE***')
##print(cube)
##print()

rubiks_html='''
<!DOCTYPE html>
<html>
<!-- <meta http-equiv="refresh" content="10" > -->
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
    
def main():
    for face_index in range(6):
        print('***face_index***', face_index)
        print(cube[face_index])
        print()
        for row in range(3):
            for col in range(3):
                print(cube[face_index][row][col], end=' ')
            print()
        print()
#    U()
#    R()
#    L()
#    F()
#    D()
#    B()
    save_HTML()
    open_HTML()
    

main()
