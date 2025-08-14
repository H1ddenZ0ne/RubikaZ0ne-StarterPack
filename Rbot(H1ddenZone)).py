
from rubpy import Client
import random
    #Any copyright of hiddenlink is prohibited.
a = "Enter Your API key"
DISCORD_URL = "https://discord.gg/cMGd4DRu"
    #Any copyright of hiddenlink is prohibited.
bot = Client(a)
    #Any copyright of hiddenlink is prohibited.
@bot.on_message_updates()
def handle_start(message):
    #Any copyright of hiddenlink is prohibited.
    if message.text == "/start":
    #Any copyright of hiddenlink is prohibited.
        message.reply(f"سلام! برای پیوستن به دیسکورد، از لینک زیر استفاده کنید:\n{DISCORD_URL}")
    #Any copyright of hiddenlink is prohibited.
        message.reply("بدو بینم دیگه")
@bot.on_message_updates()
def handle_game(message):
    """مدیریت انتخاب‌های کاربر"""
    user_input = message.text
    choices = {"1": "🪨 سنگ", "2": "✂️ قیچی", "3": "📄 کاغذ"}
    if user_input in choices:
        user_choice = choices[user_input]
        bot_choice = random.choice(list(choices.values()))
        if (user_choice == "🪨 سنگ" and bot_choice == "✂️ قیچی") or \
           (user_choice == "📄 کاغذ" and bot_choice == "🪨 سنگ") or \
           (user_choice == "✂️ قیچی" and bot_choice == "📄 کاغذ"):
            outcome = "✅ بردی!"
        elif user_choice == bot_choice:
            outcome = "🤝 مساوی شد!"
        else:
            outcome = "😢 باختی!"
        message.reply(f"تو: {user_choice}\nربات: {bot_choice}\nنتیجه: {outcome}")
    else:
        message.reply("لطفاً عدد ۱ برای سنگ، ۲ برای قیچی یا ۳ برای کاغذ را ارسال کن.")
    #Any copyright of hiddenlink is prohibited.
if __name__ == "__main__":
    print("🤖 ربات در حال اجراست…")
    bot.run()
    #Any copyright of hiddenlink is prohibited.