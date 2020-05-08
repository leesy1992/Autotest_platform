import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

user = '790844153@qq.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
password = 'nrzwklhaietbbfdb'  # 邮箱密码
host = "smtp.qq.com"
port = 465
class SendEMail(object):
    """封装发送邮件类"""

    def __init__(self):
        # 第一步：连接到smtp服务器
        self.smtp_s = smtplib.SMTP_SSL(host=host,
                                       port=port)
        # 第二步：登陆smtp服务器
        self.smtp_s.login(user,
                          password)

    def send_text(self, to_user, content, subject):
        """
        发送文本邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :return:
        """
        # 第三步：准备邮件
        # 使用email构造邮件
        msg = MIMEText(content, _subtype='plain', _charset="utf8")
        # 添加发件人
        msg["From"] = user
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        self.smtp_s.send_message(msg, from_addr=user, to_addrs=to_user)

    def send_file(self, to_user, content, subject, reports_path, file_name):
        """
        发送测试报告邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param reports_path: 测试报告路径
        :param file_name: 发送时测试报告名称
        """
        # 读取报告文件中的内容
        file_content = open(reports_path, "rb").read()
        # 2.使用email构造邮件
        # （1）构造一封多组件的邮件
        msg = MIMEMultipart()
        # (2)往多组件邮件中加入文本内容
        text_msg = MIMEText(content, _subtype='plain', _charset="utf8")
        msg.attach(text_msg)
        # (3)往多组件邮件中加入文件附件
        file_msg = MIMEApplication(file_content)
        file_msg.add_header('content-disposition', 'attachment', filename=file_name)
        msg.attach(file_msg)
        # 添加发件人
        msg["From"] = [user]
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        self.smtp_s.send_message(msg, from_addr=[user], to_addrs=to_user)

if __name__=="__main__":

    mail=SendEMail()
    mail.send_text("790844153@qq.com","tester","tester")
