import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "fortesting85977@gmail.com"
password = "SamwitAdhikary"

class sendEmail:
    def __init__(self, user_name, user_email, user_phone=None, user_msg=None):
        self.user_name = user_name
        self.user_email = user_email
        self.user_msg = user_msg
        self.user_phone = user_phone
        
        # Create message container - the correct MIME type is multipart/alternative.
        self.msg = MIMEMultipart('alternative')
        self.today = date.today().strftime("%B %d, %Y")

    def register_msgBody(self):
        self.msg['Subject'] = "Contact from College"
        # Create the body of the message (a plain-text and an HTML version).
        self.html = f"""\
        <html>
            <body style="background-color: #ebecf0;">
                <div style="background-color:#ebecf0; padding:10px 20px;">
                    <div style="text-align: center;">
                        <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color:#2f2187;">
                            {self.user_name} Want to say something 
                        </h2>
                        <p>{self.user_msg}</p> <br><br>
                        <h4> Sender Details </h4>
                        <p>Name - <em style="color: #6609df;">{self.user_name}</em>.</p>
                        <p>Email - <em style="color: #6609df;">{self.user_email}</em>.</p>
                        <p>Contact Number - <em style="color: #6609df;">{self.user_phone}</em>.</p>
                </div>
                    <code>
                        - <a href="/admin">Goto Admin Panel</a> <br>
                        - {self.today}
                    </code>
                </div>
            </body>
        </html>
        """
        self.config_msg()
        
    def registerOtpBody(self, otp):
        self.msg['Subject'] = f"{self.user_name} Verify Email for Registration"
        self.html = f"""\
        <html>
          <body style="background-color: #ebecf0;">
            <div style="background-color:#ebecf0; padding:10px 20px;">
                <div style="text-align: center;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color:#2f2187;">
                        Welcome to <a href="#"><Site Name></a>
                    </h2>
                    <img style="height: 250px;width:400px" src="https://i.ibb.co/G9c0S63/header-img.png"
                alt="welcome-image">
                    <p>To complete the process of Registration, you need to active your account.</p>
                    <h3>Your OTP is <a href="#"><em style="color: #6609df;">{otp}</em></a>.</h3> <br><br>
                    <p>If you didn't intend this, just ignore this message</p>
                </div>
                <code>
                    - Site Name <br>
                    - <a href="#">Visit Site</a> <br>
                    - {self.today}
                </code>
            </div>
        </body>
        </html>
        """
        self.config_msg()

    def config_msg(self):
        self.part2 = MIMEText(self.html, 'html')

        self.msg.attach(self.part2)

    def send_MSG(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs={self.user_email},
                                msg=self.msg.as_string())

    def send(self):
        self.register_msgBody()
        self.send_MSG()

    def sendOtp(self, otp):
        self.registerOtpBody(otp)
        self.send_MSG()
