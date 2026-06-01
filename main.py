from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

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

    if "genesis" in text:
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
