# import yagmail and its packages
import yagmail
import traceback
from dataclasses import dataclass, field
from typing import List, NoReturn, Union


class SendError(Exception):
    pass


@dataclass
class SendRecipients:
    recipients:  Union[str,List] = field(default=None)
    cc: Union[str,List] = field(default=None)
    bcc: Union[str,List] = field(default=None)


@dataclass
class EmailContent:
    subject: Union[str,List] = field(default=None)
    contents: Union[str,List] = field(default=None)
    attachments: Union[str,List] = field(default=None)


@dataclass
class Email:
    yag_connection: yagmail.sender.SMTP
    recipients_obj: SendRecipients = field(default=SendRecipients())
    email_content: EmailContent = field(default=EmailContent())

    def send(self) -> NoReturn:
        try:
            yag.send(to = self.recipients_obj.recipients, cc = self.recipients_obj.cc, bcc = self.recipients_obj.bcc,
            subject = self.email_content.subject, contents = self.email_content.contents, 
            attachments = self.email_content.attachments)
            print("Email sent successfully!")

        except:
            print(traceback)
            raise SendError("Error, email not sent.")


if __name__ == "__main__":
    
    yag = yagmail.SMTP("limavibrandao@gmail.com", "Your password goes here")

    receipts = SendRecipients(
    recipients = "persontosendemail@gmail.com", 
    cc = 'persontosendemail+user@gmail.com', 
    bcc = 'persontosendemail+user2@gmail.com'
    )

    content = EmailContent(
        subject = "Excel Automated Attachment File", 
        contents = "<h2>Here's the automated excel file you asked for...<h2>", 
        attachments = r'.\automations\excel-automation\pandas.xlsx'
    )

    send_mail = Email(
        yag_connection = yag, 
        recipients_obj = receipts, 
        email_content = content
                            ).send()
