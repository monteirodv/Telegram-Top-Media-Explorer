import asyncio
import logging
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerChannel, MessageMediaDocument, MessageMediaPhoto
from telethon.errors import SessionPasswordNeededError, FloodWaitError

# 📝 Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 🔐 Telegram client secret settings (don't share!)
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
PHONE_NUMBER = 'your_phone_number'
GROUP_USERNAME = 'target_group_name'

# ⏱️ Wait time between attempts if something goes wrong (in seconds)
WAIT_TIME = 5

async def main():
    client = None
    try:
        # 🚀 Starting our Telegram adventure!
        logger.info("🌟 Beginning our Telegram journey!")
        client = TelegramClient('session', API_ID, API_HASH)
        await client.start(phone=PHONE_NUMBER)
        logger.info("✅ Phew! We've successfully logged into Telegram. Ready for action!")

        # 🚪 Trying to join the desired group
        try:
            await client(JoinChannelRequest(GROUP_USERNAME))
            logger.info(f"🎉 Yay! We've successfully joined the group: {GROUP_USERNAME}")
        except Exception as e:
            logger.error(f"😢 Oops! We couldn't join the group. What happened: {e}")
            return

        # 🕵️ Collecting secret group information
        logger.info("🔍 Investigating the group...")
        entity = await client.get_entity(GROUP_USERNAME)
        peer = InputPeerChannel(entity.id, entity.access_hash)

        # 📚 Time to fetch all messages from the group!
        logger.info("📥 Starting to download messages. This might take a little while...")
        messages = []
        offset_id = 0
        limit = 100

        while True:
            try:
                # 🎣 Fishing for messages in small batches
                history = await client(GetHistoryRequest(
                    peer=peer,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
                if not history.messages:
                    break
                messages.extend(history.messages)
                offset_id = messages[-1].id
                if len(history.messages) < limit:
                    break
            except FloodWaitError as e:
                logger.warning(f"🚦 Oops! Telegram asked us to take a break. Let's wait {e.seconds} seconds.")
                await asyncio.sleep(e.seconds)

        logger.info(f"📊 Wow! We've collected a total of {len(messages)} messages!")

        # 🖼️ Filtering only messages with files or images
        media_messages = [m for m in messages if isinstance(m.media, (MessageMediaDocument, MessageMediaPhoto))]
        logger.info(f"🖼️ We found {len(media_messages)} messages with files or images!")

        # 🏆 Time to discover the champion messages with the most reactions!
        logger.info("🥇 Let's see which media messages are the most popular...")
        sorted_messages = sorted(media_messages, key=lambda m: sum(r.count for r in m.reactions.results) if m.reactions else 0, reverse=True)

        # 📝 Saving the 30 most incredible messages to a file
        logger.info("💾 Preparing to save the 30 most loved media messages to a file...")
        with open("top_30_media_messages.txt", "w", encoding="utf-8") as file:
            file.write(f"🌟 Top 30 most reacted media messages from the group {GROUP_USERNAME} 🌟\n\n")
            for i, message in enumerate(sorted_messages[:30], 1):
                reaction_count = sum(r.count for r in message.reactions.results) if message.reactions else 0
                message_text = message.message if len(message.message) <= 100 else message.message[:97] + "
