#!C:\Python\python.exe

import cgi
import mysql.connector
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Welcome to MyPage</h1>")


Form=cgi.FieldStorage()
FName=Form.getvalue("name")
FPassword=Form.getvalue("password")


#print("<h1>",FName,FPassword,"</h1>")

print("record stored......thank you for register mr/ms",FName);
mydb=mysql.connector.connect(
    host="localhost",
    user="root"
    password=""
    database="Amazon"
    )
mycursor=mydb.cursor();
sql="insert into user(name,password)VALUES(%S%S)";
val=(FName,FPassword);

mycursor.execute(sql,val)
mydb.commit()
print("</body>")
print("</html>")

print("</body>")
print("</html>")
