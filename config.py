"""
Configuration file.
"""
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
IP = str(os.getenv("IP"))

admins = [
    520809126
]

# ================================ REDIS ================================

aiogram_redis = {
    'host': IP,
}

redis = {
    'address': (IP, 6379),
    'encoding': 'utf8'
}
