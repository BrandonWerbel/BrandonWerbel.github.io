from GapiSetup import GapiSetup
from datetime import datetime

gs = GapiSetup()

names = []
try:
    f = open("../file_names.txt", "r")
except:
    print('wrong file name')
else:
    for line in f:
        names.append(line)
print(names)

post_names = []
for name in names:
    if name[:12] == "_blog_posts/":
        post_names.append(name[12:22])

highestTimestamp = 0.0
highestDate = ""
for name in post_names:
    date = datetime.strptime(name, '%Y-%m-%d')
    timestamp = datetime.timestamp(date)
    if timestamp > highestTimestamp:
        highestTimestamp = timestamp
        highestDate = name

message_body_plain = open("message_body_plain.txt", "r").read().format(highestDate)

message_body_html = open("message_body_html.txt", "r").read().format(highestDate)

# emails = gs.get_emails()

message = gs.create_message_html('me', 'brandon@werbel.org', 'New Post in Brandon\'s Blog!', message_body_plain, message_body_html)
gs.send_message('me', message)
# for email in emails:
#     message = gs.create_message('me', email, 'New Post in Brandon\'s Blog!', message_body_plain, message_body_html)
#     gs.send_message('me', message)