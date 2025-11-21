#send email
import email.message
msg = email.message.EmailMessage()
msg["Form"] = "khlcvs@gmail.com"
msg["To"]= "khlcvs@stu.edu.tw"
msg["subject"]= "你好 這是測試"
msg.set_content("hello this is test again by mail")
#msg.add_alternative("<h4>hello</h4 買500送100",subtype="html")
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",645)
server.login("khlcvs@gmail.com","密碼")
server.send_message(msg)
server.close