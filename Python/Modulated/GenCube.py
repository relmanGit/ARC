import webbrowser

w = '#FFFFFF'
r = '#FF0000'
g = '#00FF00'
b = '#0000FF'
o = '#FFA500'
y = '#FFFF55'
cube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
solvedCube = [[[w,w,w],[w,w,w],[w,w,w]],[[r,r,r],[r,r,r],[r,r,r]],[[y,y,y],[y,y,y],[y,y,y]],[[g,g,g],[g,g,g],[g,g,g]],[[b,b,b],[b,b,b],[b,b,b]],[[o,o,o],[o,o,o],[o,o,o]]]
face = {'U':0, 'F':1, 'D':2, 'L':3, 'R':4, 'B': 5}
ARC_REFRESH = 1
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
