import httpx
import json

url_single = "https://api.live.bilibili.com/room/v1/Room/room_init"
url_multi = "https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids"


async def get_status_single(room_id):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url_single, params={"id": room_id})
        return resp.json()


async def get_status_multi(uids):
    async with httpx.AsyncClient() as client:
        resp = await client.post(url_multi, data=json.dumps({"uids": uids}))
        return resp.json()
