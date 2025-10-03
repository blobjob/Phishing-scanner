from imap_tools import MailBox #Importing imap_tools
from colorama import Fore, Back, Style #Allows for coloured text
from phishinglist import common_phrases_list

MAIL_PASSWORD = "yoie rzie kbyh jyqf" #APP PASSWORD NOT ACCOUNT PASSWORD
MAIL_USERNAME = "phishingtesteremail@gmail.com"#EMAIL ADDRESS

with MailBox("imap.gmail.com").login(MAIL_USERNAME, MAIL_PASSWORD, "Inbox") as mb: #conecting to the gmail account using imap-tools
    #print(mb.folder.get()) checks which folder you're currently in
    for msg in mb.fetch(limit=2, reverse=True, mark_seen=True): #for each email, gets the subject, date, flags and text.
        print(msg.subject, msg.date, msg.flags, msg.text)
        
        msg_lower = (msg.text or "").lower()#get the message in lowercase
        flagged = False#set the flag to false
        for phrase in common_phrases_list:#for each phrase in the phrase list
            if phrase.lower() in msg_lower:#check if phrase is in the email text
                print(Fore.RED + 'flagged: ',phrase.lower())#if phrase is correct, print phrase in red
                flagged = True#set flag to true

        if not flagged:#if no phrases match
            print(Fore.GREEN + "no flags")#print no flags in green text