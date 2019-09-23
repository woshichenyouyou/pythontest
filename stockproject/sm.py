import smtplib
HOST = 'smtp.163.com'
PORT = '25'
FROM = 'woshiyouyouchen@163.com'
TO = 'woshichenyouyou@163.com'

SUBJECT = 'testsubject'
CONTENT = "this is the mail content"

smtp_obj = smtplib.SMTP()

smtp_obj.connect(host=HOST, port=PORT)

res = smtp_obj.login(user=FROM, password='cyy07110313')
print('logon result:', res)

msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(SUBJECT), '', CONTENT])
smtp_obj.sendmail(from_addr=FROM, to_addrs=TO, msg=msg.encode('utf-8'))

