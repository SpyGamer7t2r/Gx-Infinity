from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def send_message_with_buttons(client, chat_id, text, buttons):
    """
    Send a message with inline keyboard buttons.

    :param client: Pyrogram client instance
    :param chat_id: Target chat ID to send the message
    :param text: Message content
    :param buttons: List of rows, each row is a list of tuples (button_text, callback_data or url)
    """
    keyboard = []
    for row in buttons:
        row_buttons = []
        for btn_text, btn_data in row:
            if isinstance(btn_data, str) and btn_data.startswith("http"):
                row_buttons.append(InlineKeyboardButton(text=btn_text, url=btn_data))
            else:
                row_buttons.append(InlineKeyboardButton(text=btn_text, callback_data=btn_data))
        keyboard.append(row_buttons)

    await client.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )