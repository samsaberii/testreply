from pyrogram import *
from pyrogram.types import Message


import asyncio
userchatid = []
api_id = 29291952
api_hash = "302c9d00020783a215d86eaf7feea07c"

# bot_tok = "5473981523:AAFMWsNjHIGSw1uwdqVLmugZfqFs8C9aqpw"







app = Client('userbot', api_id, api_hash)



@app.on_message()
async def hello(client,Message):
    usertext = Message.text
    userchatid = Message.from_user.id
    print(userchatid)
    await   Message.reply("kjhg")

#
#
 #
# # await Message("kjh")


print("app run")
app.run()
