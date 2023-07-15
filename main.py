pseudo = "@" + input("TikTok username : @")

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, FollowEvent, LikeEvent, GiftEvent


client: TikTokLiveClient = TikTokLiveClient(unique_id=pseudo)

@client.on("connect")
async def on_connect(event: ConnectEvent):
    print("[Connected to the Live.]")
@client.on("comment")
async def on_comment(event: CommentEvent):
    print(f"[comment] {event.user.nickname}: {event.comment}")
@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"[follow] {event.user.nickname} has followed !")
@client.on("like")
async def on_like(event: LikeEvent):
    print(f"[like] {event.user.nickname} has liked the Live.")
@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.info.type == 1:
        print(f"[gift] {event.user.unique_id} sent {event.gift.count}x \"{event.gift.info.name}\"")
    elif event.gift.info.type != 1:
        print(f"[gift] {event.user.unique_id} sent \"{event.gift.info.name}\"")

if __name__ == '__main__':
    try:
        client.run()
    except:
        print(f"{pseudo} is not currently in Live.")
