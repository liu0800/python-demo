import smtplib
from email.mime.text import MIMEText

class Sendmail(object):
    
    def __init__(self, host, username, passwd):
        self.host = host
        self.username = username
        self.passwd = passwd
        

    def setmailinfo(self, sendlist, subject, content):
        self.sendlist = sendlist
        self.subject = subject
        self.content = content
        self.msg = MIMEText(self.content)
        self.msg['From'] = self.username
        self.msg['Subject'] = self.subject
        self.msg['To'] = ";".join(self.sendlist)
    
    def run(self):
        try:
            self.send = smtplib.SMTP()
            self.send.connect(self.host)
            self.send.login(self.username, self.passwd)
            self.send.sendmail(self.username, self.sendlist, self.msg.as_string())
            print('[*]-----send mail---to ' + str(self.sendlist) + ' success-----[*]')
        except smtplib.SMTPException as e:
            print(e)

#调用方法
# p = Sendmail('SMTP地址', '发件人邮箱地址', '发件人密码')
# p.setmailinfo(['收件人邮箱地址'],'邮件主题','邮件内容')
# p.run()
