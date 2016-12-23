#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
size = form.getfirst("size",1)
res = []

for i in range(int(size)):
    res1 = []
    for j in range(int(size)):
        name = '(' + str(i) + ',' + str(j) + ')'
        state = form.getfirst(name, "off")
        if state == 'on':
            res1.append(1)
        else:
            res1.append(0)
    res.append(res1)
    
# func(res) -> list(list(int))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Matrix.com</title>
        </head>
        <body style="background:url(../pic/matrix.png) no-repeat;background-size: 100%;color:white;">""")
print("<div style='height:150px;text-align:center;'><br><br><a href='/'><img src='/pic/logo.png'></a></div>")
print('<div style=\'font-size:25pt;background:rgba(20,40,15,0.4);margin:0px auto;width:300px;\'><table style=\'text-align:center;margin:0px auto;\' cellspacing=\'5\' cellpadding=\'5\'>')
for i in range(int(size)):
    print('<tr><td>|</td>')
    for j in range(int(size)):
        print('<td width=\'50\'>{}</td>'.format(res[i][j]))
    print('<td>|</td></tr>')
print('</table></div>')
print("""</body>
        </html>""")