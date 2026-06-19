import os
import time
import requests
import pytchat

VIDEO_ID = "q82xD7znICw"
TARGET_CHANNEL_ID = "UCQEqMSX5YYpQ9-4pdMip-vg"

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

chat = pytchat.create(video_id=VIDEO_ID)

seen = set()

while chat.is_alive():
    try:
        for c in chat.get().sync_items():
            if c.author.channelId == TARGET_CHANNEL_ID:

                key = f"{c.datetime}-{c.message}"

                if key not in seen:
                    seen.add(key)

                    requests.post(
                        WEBHOOK_URL,
                        json={
                            "content":
                            f"🧸 ベアさんがコメントしました！\n\n"
                            f"💬 {c.message}"
                        },
                        timeout=10
                    )

        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(5)
