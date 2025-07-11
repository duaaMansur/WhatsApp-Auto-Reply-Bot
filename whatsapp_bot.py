import time
import pyautogui
import pytesseract
from PIL import Image
import cv2
import numpy as np
import re
import os

def select_region():
   
    x1, y1 = 574,741 #570, 571  for larger chat area   # top-left corner
    x2, y2 = 1085,861 #1251, 866     # bottom-right corner
    width = x2 - x1       
    height = y2 - y1       
    print(f"Using hardcoded region: ({x1}, {y1}, {width}, {height})")
    return (x1, y1, width, height)

def normalize(text):
    return re.sub(r'[^a-z]', '', text.lower())

def get_auto_reply(message):
    """Get appropriate auto-reply based on message content"""
    normalized_message = normalize(message)
    
    keyword_responses = [
        # Order-related keywords
        (['order', 'buy', 'purchase', 'want'], 
         "To place an order, please provide details about what you'd like to purchase. We'll get back to you with confirmation and payment details."),
        
        # Price-related keywords
        (['price', 'cost', 'howmuch', 'rates', 'pricing'], 
         "Our prices start from $10. Please let us know what specific product you're interested in for detailed pricing."),
        
        # Greeting keywords
        (['hello', 'hi', 'hey', 'goodmorning', 'goodafternoon', 'goodevening'], 
         "How may I help you?"),
        
        # Help/Support keywords
        (['help', 'support', 'assist', 'assistance'], 
         "I'm here for you! Please let me know what you need assistance with."),
        
        # Contact/Info keywords
        (['contact', 'phone', 'address', 'location', 'info'], 
         "You can reach us at: +1-234-567-8900, Email: contact@company.com"),
        
        # Service keywords
        (['service', 'services', 'whatdoyoudo'], 
         "We offer a wide range of services including product sales, customer support, and consultation. How can we serve you today?"),
        
        # Business hours keywords
        (['timing', 'hours', 'open', 'closed', 'time'], 
         "Our business hours are Monday to Friday: 9:00 AM - 6:00 PM, Saturday: 10:00 AM - 4:00 PM. We're closed on Sundays."),
        
        # Thank you keywords
        (['thanks', 'thankyou'], 
         "You're welcome! Is there anything else I can help you with?"),
    ]
    
    # Check for keyword matches in priority order
    for keywords, response in keyword_responses:
        if any(normalize(kw) in normalized_message for kw in keywords):
            return response, keywords[0]  # Return first keyword as matched
    
    return "Thank you for your message! We'll get back to you soon.", "general"

def main():

    print("Open WhatsApp Web, open the chat you want to monitor, and make sure it's visible.")
    print("The bot will start monitoring after a 10-second countdown.")
    
    for i in range(10, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)
   
    region = select_region()
    last_message = ""
    print("Monitoring started. Press Ctrl+C to stop.")
    print("================================\n")
    
    while True:
        try:
            screenshot = pyautogui.screenshot(region=region)
            # screenshot.save('debug_wa_region.png')  # Screenshot of chat region saved for debugging
            img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            print(f"OCR output: {lines}")
            
            if lines:
                latest_message = lines[-1]
                if latest_message != last_message:
                    print(f"New message: {latest_message}")
                    
                    reply_text, matched_keyword = get_auto_reply(latest_message)
                    
                    if reply_text != "Thank you for your message! We'll get back to you soon." or matched_keyword != "general":
                        print(f"Keyword '{matched_keyword}' detected! Sending customized reply...")
                        print(f"Reply: {reply_text}")
                        
                        # Take screenshot of the input chatbox area
                        input_box_x1, input_box_y1 = 700, 900 
                        input_box_x2, input_box_y2 = 1100, 950  
                        input_box_width = input_box_x2 - input_box_x1
                        input_box_height = input_box_y2 - input_box_y1
                        
                        print("Bringing browser to front...")
                        os.system("open -a 'Google Chrome'") 
                        time.sleep(0.5)
                        
                        print("Clicking input box...")
                        pyautogui.click(743, 920)
                        time.sleep(0.5)
                    
                        pyautogui.typewrite(reply_text)
                        pyautogui.press('enter')
                        print("✅ Customized reply sent!")
                    else:
                        print("No specific keywords detected, no reply sent.")
                    
                    last_message = latest_message
                    
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()