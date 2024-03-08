from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient
from config import MONGO_DB_URI
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import random
import os

# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME", "ll_ts_security_ll_bot")
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5957398316 6352061770").split()))
OWNER_ID = "6352061770"
LOG_ID = int(os.environ.get("LOGGER_ID", "-1001916618183"))

# -------------------------------------------------------------------------------------

API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6985864893:AAHoVglT07dVjOQNNQ6b-G28M4qG_JqNG_c")


# --------------------------------------------------------------------------------------

SUPPORT_GROUP_USERNAME = "three_stars_ki_duniya"
SOURCE_CODE_CHANNEL_USERNAME = "ll_about_ari_ll"

# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------

VIDEO_URLS = [
    "https://telegra.ph/file/1722b8e21ef54ef4fbc23.mp4",
    "https://telegra.ph/file/ac7186fffc5ac5f764fc1.mp4",
    "https://telegra.ph/file/4156557a73657501918c4.mp4",
    "https://telegra.ph/file/0d896710f1f1c02ad2549.mp4",
    "https://telegra.ph/file/03ac4a6e94b5b4401fa5a.mp4",
]

# -------------------------------------------------------------------------------------

@app.on_message(filters.private & filters.command("start"))
async def start_private_chat(client, message):
    # Choose a random video URL
    video_url = random.choice(VIDEO_URLS)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️‍🔥ᴀᴅᴅ ᴍᴇ❤️‍🔥", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
                InlineKeyboardButton("💫ꜱᴜᴘᴘᴏʀᴛ💫", url=f"t.me/{SUPPORT_GROUP_USERNAME}"),
            ],
            [
                InlineKeyboardButton("💖ꜱᴏᴜʀᴄᴇ💖", url=f"t.me/{SOURCE_CODE_CHANNEL_USERNAME}"),
            ]
        ]
    )

    await client.send_video(
        chat_id=message.chat.id,
        video=video_url,
        caption="<b>нυι</b> тнιѕ ιѕ 「🛡 ᴄᴏᴘʏʀɪɢʜᴛ ʜᴀɴᴅʟᴇʀ 🛡」❖ 💖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n"
                "ᴏᴜʀ ᴍɪssɪᴏɴ ɪs ᴛᴏ ᴇɴsᴜʀᴇ ᴀ sᴇᴄᴜʀᴇ ᴀɴᴅ ᴘʟᴇᴀsᴇɴᴛ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ.\n "
                "ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴏ ᴍᴀɴᴛᴀɪɴɪɴɢ ᴅᴇᴄᴏʀᴜᴍ, ᴡᴇ'ᴠᴇ ɢᴏᴛ ɪᴛ ᴄᴏᴠᴇʀᴇᴅ.\n"
                "ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀɴʏ ᴄᴏɴᴄᴇʀɴs, ᴀɴᴅ ʟᴇᴛ's ᴡᴏʀᴋ ᴛᴏɢᴇᴛʜᴇʀ ᴛᴏ ᴍᴀᴋᴇ ᴛʜɪs ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛʜʀɪᴠᴇ\n"
                "❖ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴊᴜꜱᴛ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ ɪѕ ᴀᴜᴛᴏ❖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n\n"
                "ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/lll_notookk_lll\">||ᴀʀɪ||❣️</a>",
        reply_markup=keyboard
    )
    accha = await message.reply_text(
        text="__ᴅιиg ᴅιиg ꨄ︎ ѕтαятιиg..__"
    )
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ sтαятιиg.....__")
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ︎ sтαятιиg..__")
    await asyncio.sleep(0.2)
    await accha.delete()


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links_and_keywords(client, message):
    keywords = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

    if any(keyword.lower() in message.text.lower() for keyword in keywords) or any(link in message.text.lower() for link in ["http", "https", "www."]):
        await message.delete()

# -------------------------------------------------------------------------------------

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    if len(message.text.split()) >= 10:
        await message.delete()

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------

@app.on_message(filters.private)
async def delete_long_messages(client, message):
    if message.text and len(message.text) > 15:
        await message.delete()




mongo_uri = config.MONGO_DB_URI

mongo_client = MongoClient(mongo_uri)
db = mongo_client["your_database_name"]
top_members_collection = db["top_members"]

user_data = {}

async def get_chat_member_safe(chat_id, user_id):
    try:
        chat_member = await app.get_chat_member(chat_id, user_id)
        return chat_member
    except UserNotParticipant:
        return None
    except PeerIdInvalid:
        return None

async def send_response(message, response, reply_markup=None):
    await message.reply_text(response, reply_markup=reply_markup)

@app.on_message(filters.command("ranking"))
async def top_members(_, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🍃ᴛᴏᴅᴀʏ🍃", callback_data="today"),
                InlineKeyboardButton("🍃ᴛᴏᴛᴀʟ🍃", callback_data="total")
            ],
            [
                InlineKeyboardButton("🍃ᴄʜᴀɴɴᴇʟ🍃", callback_data="channel"),
                InlineKeyboardButton("🍃ɢʀᴏᴜᴘ🍃", callback_data="group")
            ]
        ]
    )

    await send_response(message, "❀｡:•.─────  ❁ - ❁  ─────.•:｡❀\n ❤️‍🔥<b>ᴡᴇʟᴄᴏᴍᴇ, ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ᴄᴏᴜɴᴛ ɢʀᴏᴜᴘ ᴍᴇꜱꜱᴀɢᴇꜱ\n ᴄʀᴇᴀᴛᴇ ʀᴀɴᴋɪɴɢꜱ ᴀɴᴅ ɢɪᴠᴇ ᴘʀɪᴢᴇꜱ ᴛᴏ ᴜꜱᴇʀꜱ!\n ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️‍🔥ʙʏ ||ᴀʀɪ||❣️ \n❀｡:•.─────  ❁ - ❁  ─────.•:｡❀", reply_markup)
@app.on_callback_query()
async def callback_handler(_, query):
    if query.data == "today":
        await handle_today_query(query)
    elif query.data == "total":
        await handle_total_query(query)
    elif query.data == "channel":
        await handle_channel_query(query)
    elif query.data == "group":
        await handle_group_query(query)

async def handle_today_query(query):
    top_members = get_top_members("today")

    response = " 𝗧𝗢𝗗𝗔𝗬 𝗟𝗘𝗔𝗗𝗘𝗥𝗕𝗢𝗔𝗥𝗗:\n\n"
    counter = 1
    for member in top_members:
        user_id = member["_id"]
        chat_member = await get_chat_member_safe(query.message.chat.id, user_id)
        
        if chat_member:
            total_messages = member["total_messages"]
            full_name = f"{chat_member.user.first_name} {chat_member.user.last_name}" if chat_member.user.last_name else chat_member.user.first_name
            username = chat_member.user.username
            user_info = f"{counter}. {full_name} , ⏤͟͞{total_messages}\n"
            
            response += user_info
            counter += 1

    await query.message.edit_text(response)

async def handle_total_query(query):
    top_members = get_top_members("overall")

    response = " 𝗚𝗟𝗢𝗕𝗔𝗟 𝗟𝗘𝗔𝗗𝗘𝗥𝗕𝗢𝗔𝗥𝗗 | 🌍\n\n"
    counter = 1
    for member in top_members:
        user_id = member["_id"]
        chat_member = await get_chat_member_safe(query.message.chat.id, user_id)
        
        if chat_member:
            total_messages = member["total_messages"]
            full_name = f"{chat_member.user.first_name} {chat_member.user.last_name}" if chat_member.user.last_name else chat_member.user.first_name
            username = chat_member.user.username
            user_info = f"{counter}. {full_name}, ⏤͟͞{total_messages}\n"
            
            response += user_info
            counter += 1

    await query.message.edit_text(response)

async def handle_channel_query(query):
    
    await query.message.reply_text("𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗼𝗿 𝗺𝗼𝗿𝗲 𝘂𝗽𝗱𝗮𝘁𝗲𝘀: @ll_about_ari_ll")

async def handle_group_query(query):
    
    await query.message.reply_text("𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗳𝗼𝗿 𝗱𝗶𝘀𝗰𝘂𝘀𝘀𝗶𝗼𝗻𝘀: @three_stars_ki_duniya")

def get_top_members(timeframe):
    if timeframe == "overall":
        return top_members_collection.find().sort("total_messages", -1).limit(10)
    elif timeframe == "today":
        today_start = datetime.combine(datetime.today(), datetime.min.time())
        today_end = today_start + timedelta(days=1)
        return top_members_collection.find({
            "last_updated": {"$gte": today_start, "$lt": today_end}
        }).sort("total_messages", -1).limit(10)

@app.on_message()
async def handle_messages(_, message):
    user_id = message.from_user.id
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1

    today_start = datetime.combine(datetime.today(), datetime.min.time())
    top_members_collection.update_one(
        {"_id": user_id},
        {"$inc": {"total_messages": 1}, "$set": {"last_updated": datetime.now()}},
        upsert=True
    )


# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪
║┏━━━━━━➣
║┣⪼ ᴏᴡɴᴇʀ :- @lll_notookk_lll
║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ll_about_ari_ll
║┗━━━━━━➣
║╔═════ஜ۩۞۩ஜ════╗
║   ᴍᴇʀᴇ ʟɪʏᴇ ᴍᴇʀɪ ᴅᴜɴɪʏᴀ ʜᴏ ᴛᴍ..♥️ ᴍᴀɪɴᴇ
║
║ ᴊᴏ ᴍᴀɴɢɪ ᴡᴏ ᴅᴜᴀ ʜᴏ ᴛᴍ💞 ᴍᴇʀɪ ɴᴀᴢᴀʀ
║
║ ᴋɪ ᴛᴀʟᴀꜱʜ ʜᴏ ᴛᴍ🥰 ᴍᴀɪɴᴇ ᴊᴏ ᴄʜᴀʜᴀ ᴡᴏ
║
║ ᴘʏᴀʀ ʜᴏ ᴛᴍ😍 ᴍᴇʀᴇ ɪɴᴛᴇᴢᴀᴀʀ ᴋɪ ʀᴀʜᴀᴛ
║
║ ʜᴏ ᴛᴍ✨ ᴍᴇʀᴇ ᴅɪʟ ᴋɪ ᴄʜᴀʜᴀᴛ ʜᴏ ᴛᴍ💖
║
║ ᴛᴜᴍ ʜᴏ ᴛᴏ ᴍᴜᴊʜᴇ ᴏʀ ᴋᴜᴄʜ ɴʜɪ ᴄʜᴀʜɪʏᴇ❣️ 
║ ᴋᴀɪꜱᴇ ᴋᴀʜᴜɴ ꜱɪʀꜰ  ᴘʏᴀʀ ɴᴀʜɪ 🥀 ᴍᴇʀɪ ᴊᴀᴀɴ ʜᴏ ᴛᴍ💥
║╚═════ஜ۩۞۩ஜ════╝
╚═════════════════❍⊱❁ """)
app.run()
