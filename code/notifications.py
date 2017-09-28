#!/usr/bin/python
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

def send_email(recivers, message):

    auten_file = "../../private/authentication.csv"
    with open(auten_file, 'r') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        # creating a list
        for account in reader:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(account[0], account[1])

            for reciver in recivers:
                print reciver[0]
                mail.sendmail(account[0], reciver[0], message)

            mail.close()
    f.close()

    return;

def send_email_notification(file_name):

    emails_list = "../../private/emails.csv"
    chart = file_name.replace(" ", "").rstrip(file_name[-4:]) + '.png'
    content = '\n'

    num_items = 0

    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            num_items += 1
            price    = row[0]
            area     = row[1]
            msquare  = row[2]
            location = row[3]
            link     = row[5]
            if int(price) <= 30000:
                #print 'todo: implement email notification!'
                content += '<br>' + 'cena: ' + price +' <b>('+msquare+')</b>' + '\t\t' + \
                           '<br>kvadrati: ' + area + '\t\t' + \
                           '<br>lokacija: ' + location + \
                           '<br>' + link + '<br>'
                #content += '<br>' + '<a href="' + link + '">' + 'cena: ' + price + '\t\t' + 'kvadrati: ' + area + '\t\t' + 'lokacija: ' + location + '</a> </br>'
    f.close()

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'notification - solun stanovi'
    #msgRoot['From'] = strFrom
    #msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('Dneven report/analiza na oglasi (izvor www.spitogatos.gr).<br> '
                       '<b>Analiza bazirana na %d oglasi.</b><br>'
                       '<img src="cid:image1"><br>'
                       '<b>Lista na filtrirani oglasi:</b> <br>'
                       '%s <br>'
                       '<b>note: Ako imate nekoja idea kako moze nesto podobro da se napravi..pisi te mi..</b>'
                       % (num_items,content),
                       'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(chart, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    with open(emails_list, 'rb') as f:
        email = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        send_email(email, msgRoot.as_string())

    return;
