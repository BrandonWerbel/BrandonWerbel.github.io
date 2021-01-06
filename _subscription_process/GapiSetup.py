from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pybase64 import urlsafe_b64encode
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/spreadsheets.readonly']
spreadsheet_id = '1pPd2Xws3oO0v3EfAB7ToX9x7yxw6nUHUUQW5zRkIKVo'

class GapiSetup:

    def __init__(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.gmailService = build('gmail', 'v1', credentials=creds)
        self.sheetsService = build('sheets', 'v4', credentials=creds)

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

    def create_message_html(self, sender, to, subject, message_text, html_message_text):
        message = MIMEMultipart("alternative")
        message["To"] = to
        message["From"] = sender
        message["Subject"] = subject

        plainText = MIMEText(message_text, "plain")
        htmlText = MIMEText(html_message_text, "html")
        
        message.attach(plainText)
        message.attach(htmlText)

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
            message = (self.gmailService.users().messages()
                .send(userId=user_id, body=message)
                .execute())
            print('Message Id: %s' % message['id'])
            return message
        except HttpError as error:
            print('An error occurred: %s' % error)

    def get_emails(self):
        return self.sheetsService.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='B2:B1000', majorDimension='COLUMNS').execute()['values'][0]