import schedule
import time
import google.generativeai as genai
import smtplib
from email.message import EmailMessage

# Your existing code (or import your generation function)
def generate_and_send_email():
    # 1. Generate email content with Gemini (your current logic)
    prompt = "Create a summer sale marketing email ..."
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    email_content = response.text

    # 2. Prepare email message (replace placeholders as needed)
    msg = EmailMessage()
    msg['Subject'] = "Sizzle into Summer with Our Unbeatable Sale!"
    msg['From'] = "balajiiiiii24@gmail.com"
    msg['To'] = "customer@example.com"
    msg.set_content(email_content)

    # 3. Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('balajiiiiii24@gmail.com', 'hhju hffk nyoo qjau')
        smtp.send_message(msg)

    print("Email sent!")

# Schedule the job (e.g., every Monday 9AM)
schedule.every(1).monday.at("09:00").do(generate_and_send_email)

print("Scheduler started. Waiting for scheduled tasks...")

while True:
    schedule.run_pending()
    time.sleep(1)
