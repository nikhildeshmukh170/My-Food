import smtplib
class Mail:
    sender_email = "iFoodddieee@gmail.com"
    rec_email = input(str("Enter Email id"))
    password ="bobxsqfjuydpuhlk"
    subject = "Your Food order"
    body = "Hello, Dear Customer"
    message = "subject:{}\n\n{}".format(subject,body)
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,password)
    print("login success")
    server.sendmail(sender_email,rec_email,message)
    print("Email has been sent to ",rec_email)

