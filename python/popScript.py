# pop3 protocol client script to
# automate process of signing in and reading
# most recent email received

import poplib

host = "jmail.cvent.com"
user = "mkochubeevsky@j.mail"
pass_ = "123123"

mail = poplib.POP3(host=host, port=110, timeout=5)
mail.user(user)
mail.pass_(pass_)

most_recent_index = len(mail.list()[1])

print(mail.retr(most_recent_index)[1])
