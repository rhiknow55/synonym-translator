#!/usr/bin/python

import cgi, cgitb
import sys
print(sys.path)
sys.path.insert(1, "/Users/Rhino/Projects/synonym-translator")
print(sys.path)

from translator import translate

form = cgi.FieldStorage()

if form.getvalue('beforetext'):
    beforetext = form.getvalue('beforetext')
else:
    beforetext = "N/A"

translatedtext = translate(beforetext)

print("Content-type:text/html\r\n\r\n")
print("<html>")
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Synonym Translator</h2>')
print('<h3>Before text:</h3>')
print('<t>' + beforetext + '</t>')
print('<h3>Translated text:</h3>')
print('<t>' + translatedtext + '</t>')
print('</body>')
print('</html>')
