from telethon import TelegramClient
import schedule
import time

api_id = 23729016
api_hash = "fdd914d1be8d30e6aed32dc98cf79f5b"

channel = "rajeevmehtacoursez"

client = TelegramClient("session", api_id, api_hash)

async def repost():
    messages = []

    async for msg in client.iter_messages(channel, limit=24):
        messages.append(msg)

    messages.reverse()

    for msg in messages:
        await client.forward_messages(channel, msg)
        await asyncio.sleep(2)

def job():
    with client:
        client.loop.run_until_complete(repost())

schedule.every().day.at("09:00").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(20)
