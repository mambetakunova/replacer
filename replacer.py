#this code helps to find and replace string in a file
import os
#dic is a dictionary, containing 'find and replace' pairs, where a key is a string to find and a value is a string to replace by
dic = {'&#x000A;':'\n', '&quot;':'"', "&amp;":"&", "&lt;":"<", "&gt;":">", "console.log":"", "CC.printed":" ", "return":"", "undefined":"", ".length":"", "var ":" ", "return ":" ", "{":" ", "}":" ", "=":"", ":":"", ",":" ", "`":" ", "!":" ", "ReferenceError":" ", "catch":" ", "try":" ", "i++":" ", "typeof":" ", "phoneNumber":" ", "CC.calls":" ", "this.add":" ", "break":" ", "this.":".", "instanceof":" ", "CC.methods":" ", "code.indexOf":" ", "code.match":" ", "CC.prints":" ", "parseInt":" ", "moduloAnswers":" ", "instanceof":" ", ".substring":" ", ".toString":"", "alert":"", ".indexOf":"", "SyntaxError":"", "TypeError":"", "null":""}
#here comes an input file (the file should be stored in the same folder as this tiny program)
with open('input.txt', 'r') as f33:
    page = f33.read()
#here goes the magic: http://stackoverflow.com/questions/1140958/whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
for i,j in dic.iteritems():
    page = page.replace(i,j)
page = os.linesep.join([s for s in page.splitlines() if s])
#here comes an output file (can be found in the same folder as this tiny program)
with open('ouput.txt', 'w') as f22:
    f22.write(page)
