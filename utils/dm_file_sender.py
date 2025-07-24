from pyrogram import Client, errors
from pyrogram.types import Message
from config import OWNER_ID

async def send_dm(client: Client, user_id: int, content=None, file_path=None, caption: str = ""):
    try:
        if file_path:
            await client.send_document(
                chat_id=user_id,
                document=file_path,
                caption=caption or "Here is your file!",
            )
        elif content:
            await client.send_message(chat_id=user_id, text=content)
        return True
    except errors.UserIsBlocked:
        return "User has blocked the bot."
    except errors.PeerIdInvalid:
        return "Invalid user ID or the user has never started the bot."
    except errors.ChatWriteForbidden:
        return "Bot cannot message this user due to privacy settings."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage in command:
# await send_dm(client, user_id=123456789, content="Here's the thing you asked.")
# await send_dm(client, user_id=123456789, file_path="example.zip", caption="Your ZIP file")
