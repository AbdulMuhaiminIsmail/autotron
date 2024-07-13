import pywhatkit as wk
from contacts import contacts

message = "test message (please ignore)"
recipient_name = 'jazz sim'
phone_no = contacts[recipient_name]
wk.sendwhatmsg(phone_no, message, 17, 47, 8, False)