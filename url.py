#
# read the data from the URL and print it
#
import email
import urllib.request
import json
import smtplib
def api(number , message , destination):
    # open a connection to a URL using urllib
    apiurl = "http://13.127.124.149:8080/registration_no/"
    vehicle = number
    finalurl = apiurl + vehicle
    webUrl  = urllib.request.urlopen(finalurl)

    #get the result code and print it

    # read the data from the URL and print it
    data = webUrl.read()
    print (data)



    # some JSON:


    # parse x:
    y = json.loads(data)

    # the result is a Python dictionary:
    email = (y["Email"])

    print(email)

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders


    fromaddr = ""
    password = ""
    toaddr = email

    mess = message
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'RTO Automation'

    # string to store the body of the mail
    body = mess

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = destination
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())


    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    server.send_message(msg)

    server.quit()