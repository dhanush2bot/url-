import pyrogram
import requests
import urllib.parse

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = ''

# Initialize the bot
app = pyrogram.Client("my_bot", bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(pyrogram.filters.command("start"))
def start_command(client, message):
    message.reply_text("Welcome to the URL shortener bot! Send me a URL and I will shorten it for you.")

# URL shortening command handler
@app.on_message(pyrogram.filters.text & ~pyrogram.filters.command)
def shorten_url(client, message):
    url = message.text.strip()
    if not url.startswith("http"):
        message.reply_text("Please send a valid URL starting with http:// or https://.")
        return

    # Shorten the URL using your own URL shortening service
    shortened_url = shorten_url_with_service(url)

    # Send the shortened URL back to the user
    message.reply_text(f"Here is your shortened URL: {shortened_url}")

def shorten_url_with_service(url):
    # Replace 'YOUR_API_ENDPOINT' with your actual API endpoint for URL shortening
    api_url = "https://instantearn.in/api/cb4c61dbfb6bc7b23011c6bb84fbc79e5a3fb105"
    payload = {
        "url": url,
    }
    response = requests.post(api_url, data=payload)
    if response.status_code == 200:
        return response.text  # Assuming the API returns the shortened URL directly
    else:
        return "Error: Unable to shorten URL."

# Error handling
@app.on_message(pyrogram.filters.private & pyrogram.filters.text)
def handle_errors(client, message):
    message.reply_text("Sorry, I can only process URLs in private chats.")

# Run the bot
if __name__ == "__main__":
    app.run()
