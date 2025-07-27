from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

flow = InstalledAppFlow.from_client_secrets_file(
    '/Users/parthsingh/Downloads/client_secret_340001619074-bq4eml9c001iom15dhisa97p9bllr4ra.apps.googleusercontent.com.json',
    SCOPES
)

creds = flow.run_local_server(port=8080)

service = build('gmail', 'v1', credentials=creds)

results = service.users().messages().list(userId='me', maxResults=5).execute()
messages = results.get('messages', [])

def get_html_part(payload):
    """Recursive function to find the html part of the email"""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/html':
                return part['body'].get('data')
            elif 'parts' in part:
                html = get_html_part(part)
                if html:
                    return html
    elif payload.get('mimeType') == 'text/html':
        return payload['body'].get('data')
    return None

html_output = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Latest 5 Gmail Messages</title>
<style>
  body { font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }
  .email { border: 1px solid #ccc; background: white; padding: 15px; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
  h2 { font-size: 1.2em; color: #333; }
  hr { border: none; border-top: 1px solid #eee; margin: 20px 0; }
</style>
</head>
<body>
<h1>Latest 5 Gmail Messages</h1>
"""

for i, msg in enumerate(messages, start=1):
    msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
    payload = msg_data['payload']
    
    html_data = get_html_part(payload)
    
    if html_data:
        decoded_html = base64.urlsafe_b64decode(html_data).decode('utf-8', errors='ignore')
        html_output += f'<div class="email"><h2>Email #{i} (ID: {msg["id"]})</h2>{decoded_html}</div><hr>'
    else:
        html_output += f'<div class="email"><h2>Email #{i} (ID: {msg["id"]})</h2><p><i>No HTML content found.</i></p></div><hr>'

html_output += """
</body>
</html>
"""

# Write to index.html file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Saved latest 5 emails as HTML in 'index.html'. Open this file in your browser to view.")
