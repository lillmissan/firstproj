# Requirements: Server Adress, Port, Username, Password, Sending function
from ftplib import FTP

username = "files.000webhost.com"
password = "rebeck"

ftp = FTP(username, password)
ftp.connect('files.000webhost.com', 21)

ftp.login(username, password)
ftp.cwd("CSS")
filename = "blabla.css"
ftp.storbinary('STOR' + filename, open(filename, 'rb'))

ftp.quit()
