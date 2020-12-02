from GmailSetUp import GmailSetUp
from email.mime.text import MIMEText
from pybase64 import urlsafe_b64encode
from googleapiclient.errors import HttpError

class SendEmail:

    def __init__(self):
        self.set_up = GmailSetUp()

    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.

        Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

        Returns:
        An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = urlsafe_b64encode(message.as_bytes())
        raw = raw.decode()
        return {'raw': raw}

    def send_message(self, user_id, message):
        """Send an email message.

        Args:
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            message: Message to be sent.

        Returns:
            Sent Message.
        """
        try:
            message = (self.set_up.service.users().messages()
                .send(userId=user_id, body=message)
                .execute())
            print('Message Id: %s' % message['id'])
            return message
        except HttpError as error:
            print('An error occurred: %s' % error)