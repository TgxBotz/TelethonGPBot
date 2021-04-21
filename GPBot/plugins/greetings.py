from GPBot import Stark
from telethon import events, Button
from telethon.tl.functions.users import GetFullUserRequest
from datetime import timedelta
from Configs import Config

@Stark.on(events.CallbackQuery(pattern=r"check-bot-(\d+)"))
async def check(event):

    user_id = int(event.pattern_match.group(1))
    chat_id = event.chat_id
    if not event.sender_id == user_id:
        await event.answer("You can already speak freely!", alert=True)
        return
    if event.sender_id == user_id:
            await Stark.edit_permissions(chat_id, event.sender_id, send_messages=True)
            await event.answer("You are succesfully unmuted!")
            await event.edit(Config.WELCOME_TEXT, buttons=[
            [Button.url("Chat Rules!", "t.me/{}?start=rules".format(Config.BOT_US))]
            ], parse_mode="HTML", link_preview=False)


@Stark.on(events.ChatAction)
async def join(event):

    if event.user_joined:
        await Stark.edit_permissions(event.chat_id, event.user_id, send_messages=False)
        await event.reply(Config.WELCOME_TEXT, parse_mode="HTML", link_preview=False, buttons=[
        [Button.inline("Click Here to unmute yourslef!", data=f"check-bot-{event.user_id}")]
        ])
