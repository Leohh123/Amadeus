import nonebot
from nonebot.plugin import plugins
from .config import Config
from .data_source import get_status_single, get_status_multi

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

scheduler = nonebot.require("nonebot_plugin_apscheduler").scheduler

uid_dict = {}
status = {}


async def live_push(sta):
    message = f"{sta['uname']}开播啦！{sta['title']}"
    for qq_number in plugin_config.subscribers:
        await nonebot.get_bot().call_api(
            "send_msg", **{"user_id": qq_number, "message": message})


@scheduler.scheduled_job("interval", seconds=plugin_config.live_check_interval, id="live")
async def live():
    for rid in plugin_config.room_ids:
        if rid not in uid_dict:
            res = await get_status_single(rid)
            uid_dict[rid] = res["data"]["uid"]
    res = await get_status_multi(list(uid_dict.values()))
    res = res["data"]
    for uid in uid_dict.values():
        if str(uid) in res:
            cur_sta = res[str(uid)]
            if uid in status:
                old_sta = status[uid]
                if old_sta["live_status"] != 1 and cur_sta["live_status"] == 1:
                    await live_push(cur_sta)
            status[uid] = cur_sta
