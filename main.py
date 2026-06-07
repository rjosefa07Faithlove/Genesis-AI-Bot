from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import random

from genesis_knowledge import ABOUT_ALEJANDRO
from genesis_knowledge import FOUNDER
from genesis_knowledge import SECOND_CHANCE
from genesis_knowledge import TRUSTPAY
from genesis_knowledge import WITH_CONFIDENCE
from genesis_knowledge import BUSINESS_CREDIT
from genesis_knowledge import RACIN_1804
from genesis_knowledge import TAX_DEEDS
from genesis_knowledge import MONALISA
from genesis_knowledge import GENERATIONAL_WEALTH
from genesis_knowledge import LEADERSHIP
from genesis_knowledge import PERSONAL_CREDIT 
from genesis_knowledge import BUSINESS_DEVELOPMENT
from genesis_knowledge import GENESIS
from genesis_knowledge import UNKNOWN_RESPONSES
from genesis_knowledge import FINANCIAL_LITERACY
from genesis_knowledge import INVESTING_BASICS
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello. I am Genesis AI Assistant.")


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


async def business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Business begins with solving a problem. Focus on value first, money second."
    )


async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Credit is a financial reputation. Protect it and build it consistently."
    )


async def mindset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Discipline beats motivation when motivation disappears."
    )


async def leadership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "A leader serves first. Influence comes from trust, consistency, and example."
    )


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

    elif any(word in text for word in ["business credit", "net 30", "net-30", "paynet"]):
        await update.message.reply_text(BUSINESS_CREDIT)

    elif "1804" in text or "racin ayisyen" in text:
        await update.message.reply_text(RACIN_1804)

    elif "monalisa" in text or "joesie's kitchen" in text:
        await update.message.reply_text(MONALISA)

    elif "generational wealth" in text or "legacy" in text:
        await update.message.reply_text(GENERATIONAL_WEALTH)

    elif any(word in text for word in [
    "tax deed",
    "tax deeds",
    "real estate",
    "property investing",
    "auction property" 
]):
        await update.message.reply_text(TAX_DEEDS)

    elif any(word in text for word in [
    "leadership",
    "leader",
    "lead",
    "accountability",
    "ownership",
    "vision"
]):
        await update.message.reply_text(LEADERSHIP) 

    elif any(word in text for word in [
    "credit score",
    "personal credit",
    "fico",
    "equifax",
    "experian",
    "transunion"
]):
        await update.message.reply_text(PERSONAL_CREDIT)

    elif any(word in text for word in [
    "business development",
    "entrepreneurship",
    "business growth",
    "scaling",
    "startup",
    "business"
]):
        await update.message.reply_text(BUSINESS_DEVELOPMENT)

    elif "what is genesis" in text:
        await update.message.reply_text(GENESIS)

    elif "genesis" in text:
        await update.message.reply_text(
        "Genesis AI is a knowledge assistant. Ask me about leadership, business credit, personal credit, wealth building, tax deeds, TrustPay, Second Chance, MonaLisa, or Racin Ayisyen 1804."
    )

    elif any(word in text for word in [
    "financial literacy",
    "money management",
    "budgeting",
    "saving money",
    "debt management"
]):
        await update.message.reply_text(FINANCIAL_LITERACY)

    else:
        await update.message.reply_text(
        random.choice(UNKNOWN_RESPONSES)
        )
   
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("business", business))
app.add_handler(CommandHandler("credit", credit))
app.add_handler(CommandHandler("mindset", mindset))
app.add_handler(CommandHandler("leadership", leadership))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, group_reply))

app.run_polling()