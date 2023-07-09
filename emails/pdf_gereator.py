import os
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

class TicketGenerator:
    def __init__(self, ticket_data, qr_path):
        self.ticket_data = ticket_data
        self.qr_path = qr_path

    def generate_ticket(self, pdf_path):
        # Create a PDF canvas
        pdf = canvas.Canvas(pdf_path, pagesize=letter)

        # Define the layout of the ticket
        pdf.setFont('Helvetica', 14)
        pdf.drawString(1 * inch, 10 * inch, f"Name: {self.ticket_data['name']}")
        pdf.drawString(1 * inch, 9.5 * inch, f"Date: {self.ticket_data['date']}")
        pdf.drawString(1 * inch, 9 * inch, f"Time: {self.ticket_data['time']}")
        pdf.drawString(1 * inch, 8.5 * inch, f"Location: {self.ticket_data['location']}")
        pdf.drawImage(self.qr_path, 4 * inch, 6 * inch, width=2*inch, height=2*inch)

        # Save the PDF
        pdf.save()

if __name__ == '__main__':
    # Define the data to include in the ticket
    ticket_data = {
        'name': 'John Doe',
        'date': '2022-09-01',
        'time': '8:00 PM',
        'location': 'Main Stage',
    }

    # Create a QR code image
    qr = qrcode.make(ticket_data['qr_code'])
    qr_path = 'qr.png'
    qr.save(qr_path)

    # Generate the ticket
    ticket_generator = TicketGenerator(ticket_data, qr_path)
    ticket_generator.generate_ticket('ticket.pdf')