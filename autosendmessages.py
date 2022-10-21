import requests
from datetime import datetime
import pytz

WIB = pytz.timezone('Asia/Jakarta') # Select and adjust timezone
dt = datetime.now(WIB)
curr_date = dt.strftime("%d-%m-%Y") # Convert to string format time
curr_time = dt.strftime("%H:%M:%S") # Convert to string format time

tg_api_token = "5433564123:AAE__TMEk7w9VW2LTV-dSE0UUL8skkpT46E" # Telegram bot token (create /newbot in @botfather and replace this)
tg_userid = "automationbot_test"                                # User ID or username of group/channel

msg = f" Message received on {curr_date} at {curr_time}"

def send_messages(messages):
    telegram_api_url = f"https://api.telegram.org/bot{tg_api_token}/sendMessage?chat_id=@{tg_userid}&text={messages}"
    telegram_response = requests.get(telegram_api_url)
    
    if telegram_response.status_code == 200:
        print("INFO : Notification has been sent on Telegram")
    else:
        print("ERROR : Could not send Message")
        
while True:
    send_messages(msg)