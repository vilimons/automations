# import yagmail and its packages
import yagmail

# initiating connection with SMTP Server
# SMPT = Simples Mail Transfer Protocol, the standard for the transmission of email on a computer network
yag = yagmail.SMPT("limavibrandao@gmail.com", "Your password goes here")

# wrap the remaining code in a try-except block to handle errors, such as wrong password

try:
    yag.send(to = "persontosendemail@gmail.com", cc = 'persontosendemail+user@gmail.com', bcc = 'persontosendemail+user2@gmail.com',
    subject = "Excel Automated Attachment File", contents = "<h2>Here's the automated excel file you asked for...<h2>", 
    attachments = r'C:\Users\Administrator\Desktop\projects\automations\excel-automation\pandas.xlsx')
    print("Email sent successfuly!")

except:
    print("Error, email not sent.")