import win32com.client as win32
import pandas as pd
#must have old version of outlook open when running the script
name = pd.read_csv('Name_email_file.csv',header=None)
olAPP = win32.Dispatch('Outlook.Application')
olNS = olAPP.GetNameSpace('MAPI') #Messaging Application Programming interface

for first_name, email_address in zip(name['Name'],name['email']): #iterates through both lists
    mail_item = olAPP.CreateItem(0)

    mail_item.Subject = "EWB Volunteering"
    mail_item.BodyFormat = 1 #email format

    mail_item.Body = f"Hello {first_name}. Your message"
    mail_item.Sender = "Your Email"
    mail_item.To = str(email_address) #test for error

    mail_item.Display() #display on Outlook
    mail_item.Save()
    try:
        mail_item.Send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

