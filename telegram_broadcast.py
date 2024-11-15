import requests
import cv2

class telegram_bot:
    def __init__(self,bot_token,channel_chat_id):
        self.bot_token = bot_token
        self.channel_chat_id = channel_chat_id

    def send_message(self,message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            'chat_id': self.channel_chat_id,
            'text': message
        }
        response = requests.post(url, json=payload)
        return response.json()
        
    def send_image(self,image):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendPhoto"
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Encode the image as JPEG in memory
        success, img_encoded = cv2.imencode('.jpg', image)
        if not success:
            print("Could not encode image")
            return
        files = {
            'photo': ('image.jpg', img_encoded.tobytes())
        }
        data = {
            'chat_id': self.channel_chat_id
        }

        response = requests.post(url, data=data, files=files)
        return response.json()
