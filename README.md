# WhatsApp Auto-Reply Bot

An automated WhatsApp Web bot that monitors incoming messages and sends customized auto-replies based on keywords detected in the messages.

## Features

- **Keyword-based Auto-Replies**: Responds to different keywords with appropriate messages
- **OCR Text Recognition**: Uses Tesseract OCR to read messages from WhatsApp Web
- **Customizable Responses**: Easy to modify responses for different keywords
- **Safe Operation**: Built-in failsafe and proper error handling
- **Real-time Monitoring**: Continuously monitors for new messages

## Prerequisites

### Required Python Packages
```bash
pip install pyautogui pytesseract pillow opencv-python numpy
```

### System Requirements
- **Tesseract OCR**: Download and install from [GitHub](https://github.com/tesseract-ocr/tesseract)
- **Browser**: Chrome, Firefox, Safari, or any modern browser
- **Operating System**: Windows, macOS, or Linux

## Important Setup Requirements

### 1. WhatsApp Web Theme
**CRITICAL**: WhatsApp Web must be set to **WHITE THEME** for OCR to work properly.

To change theme:
1. Open WhatsApp Web
2. Click on the three dots menu (⋮) in the top-left
3. Go to Settings → Theme
4. Select **Light** theme

### 2. Screen Resolution & Browser Setup
- Use a **maximized browser window**
- Ensure WhatsApp Web chat is **fully visible**
- Keep the chat window **unobstructed** by other applications

## Installation & Setup

### Step 1: Clone/Download the Code
git clone

### Step 2: Get Coordinates
You need to get the correct coordinates for your screen setup.

#### For Chat Area Coordinates:
1. Run the coordinate helper script.


### For Input Box Coordinates:
Run the input box coordinate helper:
```bash
python chat-msg-box-coordinates.py
```

### Step 3: Update Coordinates in Code
1. Update `select_region()` function with your chat area coordinates
2. Update `pyautogui.click(x, y)` in the main script with your input box coordinates

## Usage Instructions

### Step 1: Prepare WhatsApp Web
1. Open WhatsApp Web in your browser
2. **Set theme to WHITE/Light**
3. Open the chat you want to monitor
4. **Maximize the browser window**
5. Ensure the chat is fully visible

### Step 2: Run the Bot
1. Open terminal/command prompt
2. Navigate to the script directory
3. Run: `python whatsapp_bot.py`
4. **You have 10 seconds to switch to WhatsApp Web tab**
5. The bot will start monitoring automatically

### Step 3: Monitor Operation
- Watch the console for message detection logs
- The bot will automatically reply to detected keywords
- Press `Ctrl+C` to stop the bot

## Auto-Reply Keywords & Responses

| Keywords | Response |
|----------|----------|
| **order, buy, purchase** | "To place an order, please provide details about what you'd like to purchase. We'll get back to you with confirmation and payment details." |
| **price, cost, how much** | "Our prices start from $10. Please let us know what specific product you're interested in for detailed pricing." |
| **hello, hi, hey** | "Hello! How may I help you?" |
| **help, support** | "I'm here to help! Please let me know what you need assistance with." |
| **contact, phone, address** | "You can reach us at: Phone: +1-234-567-8900, Email: contact@company.com" |
| **service, services** | "We offer a wide range of services including product sales, customer support, and consultation. How can we serve you today?" |
| **timing, hours, open** | "Our business hours are Monday to Friday: 9:00 AM - 6:00 PM, Saturday: 10:00 AM - 4:00 PM. We're closed on Sundays." |
| **thanks, thank you** | "You're welcome! Is there anything else I can help you with?" |


## Troubleshooting

1. **OCR Not Working**
   - Ensure WhatsApp Web is in **WHITE theme**
   - Check if Tesseract is properly installed
   - Verify chat area coordinates are correct

2. **Bot Not Clicking Input Box**
   - Update input box coordinates using the helper script
   - Ensure browser window is maximized
   - Check if input box is visible and not covered


**⚠️ Important**: This bot is for educational and personal use only. Ensure compliance with WhatsApp's terms of service and applicable laws in your jurisdiction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
