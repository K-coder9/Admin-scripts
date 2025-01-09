import win32com.client as win32
import pandas as pd
name = pd.read_csv('old_volunteers.csv',header=None)
olAPP = win32.Dispatch('Outlook.Application')
olNS = olAPP.GetNameSpace('MAPI') #Messaging Application Programming interface

for first_name, email_address in zip(name['Name'],name['email']): #iterates through both lists
    mail_item = olAPP.CreateItem(0)

    mail_item.Subject = "Email Subject"
    mail_item.BodyFormat = 1 #email format

    mail_item.Body = f"Hello {first_name}. Last year you were participated in EWB's Outreach. We are planning more sessions this term and would like your help! Would you be interested in continuing?"
    mail_item.Sender = "Your email"
    mail_item.To = str(email_address) #test for error

    mail_item.Display() #display on Outlook
    mail_item.Save()
    try:
        mail_item.Send() #send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

