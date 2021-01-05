from GapiSetup import GapiSetup

gs = GapiSetup()
message_body = """Hello there!

You are getting this email because you are subscribed to Brandon Werbel's Israel Blog. There has just been a new post, check it out!

If you would like to unsubscribe from this site, respond to this email saying so. There is not currently an automated way to do so, but it should be coming soon!"""

emails = gs.get_emails()

# for email in emails:
message = gs.create_message('me', 'brandon@werbel.org', 'New Post in Brandon\'s Blog!', message_body)
gs.send_message('me', message)