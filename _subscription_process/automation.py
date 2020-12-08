from SendEmail import SendEmail

em = SendEmail()
message_body = """Hello there!

You are getting this email because you are subscribed to Brandon Werbel's Israel Blog. There has just been a new post, check it out!

If you would like to unsubscribe from this site, respond to this email saying so. There is not currently an automated way to do so, but it should be coming soon!"""


with open('../subscriber_list.txt', 'r') as subscribers:
    subsArray = subscribers.readlines()
    for line in subsArray[:len(subsArray) - 1]:
        line = line[0: len(line) - 1]
        message = em.create_message('me', line, 'New Post in Brandon\'s Blog!', message_body)
        em.send_message('me', message)
    line = subsArray[len(subsArray) - 1]
    message = em.create_message('me', line, 'New Post in Brandon\'s Blog!', message_body)
    em.send_message('me', message)