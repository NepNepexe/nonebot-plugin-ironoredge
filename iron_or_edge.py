from nonebot import on_message
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.rule import to_me, regex
from nonebot.typing import T_State
from pathlib import Path
import random

iron_or_edge = on_message(rule=regex(r"铁|崩溃边缘"), priority=5)# 关键词

@iron_or_edge.handle()
async def handle_iron_or_edge(state: T_State):
    if random.random() > 0.5:
        return  # 50%概率触发回复
    # 图片路径data
    img_path = Path("data/images/iron.jpg")
    if not img_path.exists():
        await iron_or_edge.finish("图片未找到，请检查图片路径是否正确！")
    msg = MessageSegment.image(f"file:///{img_path.absolute()}")
    await iron_or_edge.send(msg)