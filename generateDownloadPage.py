import png
import pyqrcode
import datetime
now = datetime.datetime.now()

accessURL = input('Please enter the url you want to get file \n')

big_code = pyqrcode.create(accessURL)
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 0], background=[0xff, 0xff, 0xff])

year = now.year
month = now.month
day = now.day
yymmdd = str(year) + '-' + str(month) + '-' + str(day)

head = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Print This Page</title>
</head>'''

body1 = '''<body><center><h2>Pickup Your File</h2>
			<img src='shopcart.png' width = 100 heigh = 100>
			<h3>Generate Date </h3><h2>'''

body2 = '''
			</h2><h3>go to link <br></h3>'''
body3 = '''<br><br><bold>Or scan the QR code</bold><br>
			<img src = 'code.png' width = 150 heigh = 150><br>'''

end = '''	By using file pickup service, 
			you agree the privacy statement and term of service. 
			Unsure, visit amyisthebest.com/privacy <br>
			<img src = 'stsqr.jpg' width = 150 heigh = 150><br>
			A service my Stutechsupport.
			</center></body></html>'''

contents = head + body1 + yymmdd + body2 + accessURL + body3 + end

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()