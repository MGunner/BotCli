from pyrogram import Client, filters, raw
from plugins import r, admin

import time


@Client.on_message(filters.private & filters.user(admin) & filters.command("status"))
def get_info(c, m):
    c.send(
        raw.functions.messages.StartBot(
            bot=c.resolve_peer('SpamBot'),
            peer=c.resolve_peer('SpamBot'),
            random_id=c.rnd_id(),
            start_param='start'
        )
    )


@Client.on_message(filters.user('SpamBot'))
def status(c, m):
    c.send_chat_action(chat_id=admin, action='typing')
    time.sleep(0.15)

    c.send_message(chat_id=admin, text=m.text)


@Client.on_message(filters.private & filters.user(admin) & filters.command("info"))
def show_info(c, m):
    chat_id = m.chat.id
    counter = 0

    for dialog in c.iter_dialogs():
        if dialog.chat.type in ["supergroup", "group"]:
            counter += 1

    message = f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
〽️اطلاعات ربات〽️

🔘• تعداد گروه ها : {counter}
🔘• تعداد کاربران : pass
🔘• مدیران :  <a href="tg://user?id={admin}">admin</a> 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    """

    c.send_chat_action(chat_id, 'typing')
    time.sleep(0.15)

    c.send_message(chat_id=chat_id, text=message)
