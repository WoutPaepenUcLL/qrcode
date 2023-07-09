
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
##############################################################
from email.mime.application import MIMEApplication
##############################################################
## The pandas library is only for generating the current date, which is not necessary for sending emails

class Email:
    def __init__(self,naam_jg,email,loc_file) -> None:
        self.email = email
        self.naam_jg = naam_jg
        self.loc_file = loc_file
    def send_email(self):
        # Define the HTML document
        html = f'''
            <html>
                <body>
                    <h1>Jong-Giver TicketMaster</h1>
                    <p>Hey {self.naam_jg}, proficiat dit is je officiele ticket voor het festival!</p>
                    <br>
                    <p> In de bijlage vind je een pdf met je ticket.</p>
                    <p> Vergeet deze niet mee te nemen naar het festival! Bij de inkom zal je ticket gescand worden.</p>
                    <br>
                    <p> Veel plezier!</p>
                    <p> Groetjes, </p>
                    <p> De leiding </p>
                    <br>
                    <p> PS: Dit is een automatisch gegenereerd bericht, als er fouten in het ticket staan, gelieve contact op te nemen met Wout.</p>                    
                </body>
            </html>
            '''

        # Define a function to attach files as MIMEApplication to the email
        ##############################################################
        def attach_file_to_email(email_message, filename):
            # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
            with open(filename, "rb") as f:
                file_attachment = MIMEApplication(f.read())
            # Add header/name to the attachments    
            file_attachment.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            # Attach the file to the message
            email_message.attach(file_attachment)
        ##############################################################    

        # Set up the email addresses and password. Please replace below with your email address and password
        email_from = 'paepen.wout@gmail.com'
        password = 'xxx'
        email_to = self.email
        


        # Create a MIMEMultipart class, and set up the From, To, Subject fields
        email_message = MIMEMultipart()
        email_message['From'] = email_from
        email_message['To'] = email_to
        email_message['Subject'] = f'Ticket voor {self.naam_jg}'

        # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
        email_message.attach(MIMEText(html, "html"))

        # Attach more (documents)
        ##############################################################
        attach_file_to_email(email_message, self.loc_file)
        ##############################################################
        # Convert it as a string
        email_string = email_message.as_string()

        # Connect to the Gmail SMTP server and Send Email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_from, password)
            server.sendmail(email_from, email_to, email_string)