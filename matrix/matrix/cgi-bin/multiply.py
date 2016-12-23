#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
size = form.getfirst("size",1)
res11 = []
res22 = []
for i in range(int(size)):
    res1 = []
    res2 = []
    for j in range(int(size)):
        name1 = '(1,' + str(i) + ',' + str(j) + ')'
        name2 = '(2,' + str(i) + ',' + str(j) + ')'
        state1 = form.getfirst(name1, "off")
        state2 = form.getfirst(name2, "off")
        if state1 == 'on':
            res1.append(1)
        else:
            res1.append(0)
        
        if state2 == 'on':
            res2.append(1)
        else:
            res2.append(0)
    res11.append(res1)
    res22.append(res2)
    
# func(res11, res22) -> list(list(int))

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
        print('<td width=\'50\'>{}</td>'.format(res11[i][j]))
    print('<td>|</td></tr>')
print('</table></div>')
print("""</body>
        </html>""")