import pandas as pd
import gspread
import os.path

from google.auth.transport.requests import Request
from google.oauth2.service_account import credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# ID of the Google Sheet
spreadsheet_ID = "1EFGhOjgs8kzGW-2O-ZTjpJyA8hPO41gPMgl0qBF35Gc"
scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


# Google Sheets API credentials
creds = credentials.from_service_account_file('C:\Users\spang\sac_elections\credentials.json',scopes)

gc = gspread.authorize(credentials)
worksheet = gc.open('SAC Elections').sheet1

# Operations on the Sheet
# Make sure emails are logins
email_column = worksheet.col_values(1)
for email in email_column[1:]: