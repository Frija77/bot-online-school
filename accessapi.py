import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]#разрешения

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "elaborate-scope-488115-i1-87b4d3ef1ed9.json", scope
) #объект для авторицзацит паспорт

client = gspread.authorize(creds) #соединение Google Api к Google sheets

sheet = client.open("Schedule").sheet1

data = sheet.get_all_records() #превращает в словари все что есть в самой таблице 

#print(data)