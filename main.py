from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from genesis_knowledge import ABOUT_ALEJANDRO
from genesis_knowledge import FOUNDER
from genesis_knowledge import SECOND_CHANCE
from genesis_knowledge import TRUSTPAY
from genesis_knowledge import WITH_CONFIDENCE
from genesis_knowledge import BUSINESS_CREDIT
TOKEN = os.getenv("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello. I am Genesis AI Assistant."
    )

# HELP COMMAND
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Genesis Commands

/start - Start Genesis
/help - Show commands
/business - Business guidance
/credit - Credit guidance
/mindset - Personal development
/leadership - Leadership lesson
"""
    )

# BUSINESS
async def business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Business begins with solving a problem. Focus on value first, money second."
    )

# CREDIT
async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Credit is a financial reputation. Protect it and build it consistently."
    )

# MINDSET
async def mindset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Discipline beats motivation when motivation disappears."
    )

# LEADERSHIP
async def leadership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "A leader serves first. Influence comes from trust, consistency, and example."
    )

# GROUP RESPONSE
async def group_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "who is alejandro" in text or "alejandro fowler" in text:
        await update.message.reply_text(ABOUT_ALEJANDRO)

    elif "who created genesis" in text or "founder of genesis" in text:
        await update.message.reply_text(
            f"Genesis was created by {FOUNDER['name']}, {FOUNDER['role']}. "
            f"His mission is {FOUNDER['mission']}"
        )

elif "second chance" in text:
    await update.message.reply_text(SECOND_CHANCE)

elif "trustpay" in text:
    await update.message.reply_text(TRUSTPAY)

elif "with confidence" in text:
    await update.message.reply_text(WITH_CONFIDENCE)

elif "business credit" in text or "net 30" in text or "net-30" in text or "paynet" in text:
    await update.message.reply_text(BUSINESS_CREDIT)

elif "genesis" in text:
    await update.message.reply_text(
        "I'm here. How can I help?"
    )
        

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("business", business))
app.add_handler(CommandHandler("credit", credit))
app.add_handler(CommandHandler("mindset", mindset))
app.add_handler(CommandHandler("leadership", leadership))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, group_reply)
)

app.run_polling()
