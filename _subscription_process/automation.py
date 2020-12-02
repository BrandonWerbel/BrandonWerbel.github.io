from SendEmail import SendEmail

em = SendEmail()
message = em.create_message('me', 'brandon@werbel.org', 'I hope this works', 'Hello, Brandon. I hope you get this!')
em.send_message('me', message)