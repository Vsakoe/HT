# ---------------------------------------------------------------------------------
#  /\_/\  ūüĆź This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  ūüĒď Not licensed.
#  > ^ <   ‚ö†ÔłŹ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: inlinetimer
# Author: sqlmerr
# Commands:
# .timer
# ---------------------------------------------------------------------------------

"""
‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚Ėą‚Ėą‚ēó‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ
‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚ēź‚ēź‚ēĚ‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚ēź‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚ēź‚ēź‚ēĚ‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚Ėą‚Ėą‚ēó
‚ēö‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚ēĒ‚Ėą‚Ėą‚Ėą‚Ėą‚ēĒ‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēĒ‚ēĚ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēĒ‚ēĚ
‚ĖĎ‚ēö‚ēź‚ēź‚ēź‚Ėą‚Ėą‚ēó‚ēö‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēĒ‚ēĚ‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚ēĎ‚ēö‚Ėą‚Ėą‚ēĒ‚ēĚ‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĒ‚ēź‚ēź‚Ėą‚Ėą‚ēó
‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēĒ‚ēĚ‚ĖĎ‚ēö‚ēź‚Ėą‚Ėą‚ēĒ‚ēź‚ēĚ‚ĖĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ēö‚ēź‚ēĚ‚ĖĎ‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚Ėą‚ēó‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚ēĎ‚Ėą‚Ėą‚ēĎ‚ĖĎ‚ĖĎ‚Ėą‚Ėą‚ēĎ
‚ēö‚ēź‚ēź‚ēź‚ēź‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ēö‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚ĖĎ‚ēö‚ēź‚ēź‚ēź‚ēź‚ēź‚ēź‚ēĚ‚ēö‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ĖĎ‚ēö‚ēź‚ēĚ‚ēö‚ēź‚ēź‚ēź‚ēź‚ēź‚ēź‚ēĚ‚ēö‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚ēö‚ēź‚ēĚ‚ēö‚ēź‚ēĚ‚ĖĎ‚ĖĎ‚ēö‚ēź‚ēĚ
"""
# meta developer: @sqlmerr_m
# meta banner: https://github.com/sqlmerr/sqlmerr/blob/main/assets/hikka_mods/sqlmerrmodules_inlinetimer.png?raw=true

import asyncio

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall, InlineQuery


@loader.tds
class InlineTimer(loader.Module):
    """–ě–Ņ–ł—Ā–į–Ĺ–ł–Ķ –Ĺ–į—ą–Ķ–≥–ĺ –ľ–ĺ–ī—É–Ľ—Ź"""

    strings = {
        "name": "InlineTimer",
        "text": "‚Ź≤ <b>Inline timer</b>\n‚Źį <i>Current time</i>: {} seconds",
        "successful": (
            "Great, in {} seconds the inline bot will send you a message via PM"
        ),
        "timer_created": "<b>Timer created!</b>",
        "text_cfg": "The text that your inline bot will send when the timer expires",
        "below_zero": "Time cannot be below zero",
    }
    strings_ru = {
        "text": "‚Ź≤ <b>Inline timer</b>\n‚Źį <i>–Ę–Ķ–ļ—É—Č–Ķ–Ķ –≤—Ä–Ķ–ľ—Ź</i>: {} —Ā–Ķ–ļ—É–Ĺ–ī",
        "successful": "–ě—ā–Ľ–ł—á–Ĺ–ĺ, —á–Ķ—Ä–Ķ–∑ {} —Ā–Ķ–ļ—É–Ĺ–ī –ł–Ĺ–Ľ–į–Ļ–Ĺ –Ī–ĺ—ā –ĺ—ā–Ņ—Ä–į–≤–ł—ā –≤–į–ľ —Ā–ĺ–ĺ–Ī—Č–Ķ–Ĺ–ł–Ķ –≤ –Ľ—Ā",
        "timer_created": "<b>–Ę–į–Ļ–ľ–Ķ—Ä —Ā–ĺ–∑–ī–į–Ĺ!</b>",
        "text_cfg": (
            "–Ę–Ķ–ļ—Ā—ā, –ļ–ĺ—ā–ĺ—Ä—č–Ļ –Ī—É–ī–Ķ—ā –Ņ–ł—Ā–į—ā—Ć –≤–į—ą –ł–Ĺ–Ľ–į–Ļ–Ĺ –Ī–ĺ—ā –Ņ–ĺ –ł—Ā—ā–Ķ—á–Ķ–Ĺ–ł—é –≤—Ä–Ķ–ľ–Ķ–Ĺ–ł —ā–į–Ļ–ľ–Ķ—Ä–į"
        ),
        "below_zero": "–í—Ä–Ķ–ľ—Ź –Ĺ–Ķ –ľ–ĺ–∂–Ķ—ā –Ī—č—ā—Ć –ľ–Ķ–Ĺ—Ć—ą–Ķ –Ĺ—É–Ľ—Ź",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "text",
                "‚ö†ÔłŹ",
                lambda: self.strings("text_cfg"),
                validator=loader.validators.String(),
            )
        )

    @loader.command(ru_doc="–ĺ—ā–Ņ—Ä–į–≤–ł—ā—Ć —ā–į–Ļ–ľ–Ķ—Ä")
    async def timer(self, message):
        """Send timer"""
        timer = self.get("timer", 0)
        await self.inline.form(
            text=self.strings("text").format(timer),
            message=message,
            reply_markup=[
                [
                    {
                        "text": "-1 sec",
                        "callback": self.decrement,
                    },
                    {
                        "text": "‚úćÔłŹ Enter value",
                        "input": "‚úćÔłŹ Enter new time IN SECONDS",
                        "handler": self.input_handler,
                    },
                    {"text": "+1 sec", "callback": self.increment},
                ],
                [
                    {"text": "‚úÖ", "callback": self.proceed},
                    {
                        "text": "‚ĚĆ",
                        "action": "close",
                    },
                ],
            ],
        )

    async def proceed(self, call: InlineCall):
        timer = self.get("timer", 1)
        await call.answer(self.strings("successful").format(timer))
        await call.edit(self.strings("timer_created"))
        self.set("timer", 0)

        await asyncio.sleep(timer)
        await self.inline.bot.send_message(self.tg_id, self.config["text"])

    async def decrement(self, call: InlineCall):
        timer = self.get("timer", 0)
        if timer == 0:
            await call.answer(self.strings("below_zero"))
            return
        timer -= 1
        self.set("timer", timer)
        await call.answer()

        await call.edit(
            text=self.strings("text").format(timer),
            reply_markup=[
                [
                    {
                        "text": "-1 sec",
                        "callback": self.decrement,
                    },
                    {
                        "text": "‚úćÔłŹ Enter value",
                        "input": "‚úćÔłŹ Enter new time IN SECONDS",
                        "handler": self.input_handler,
                    },
                    {"text": "+1 sec", "callback": self.increment},
                ],
                [
                    {"text": "‚úÖ", "callback": self.proceed},
                    {
                        "text": "‚ĚĆ",
                        "action": "close",
                    },
                ],
            ],
        )

    async def increment(self, call: InlineCall):
        timer = self.get("timer", 0)
        timer += 1
        self.set("timer", timer)
        await call.answer()

        await call.edit(
            text=self.strings("text").format(timer),
            reply_markup=[
                [
                    {
                        "text": "-1 sec",
                        "callback": self.decrement,
                    },
                    {
                        "text": "‚úćÔłŹ Enter value",
                        "input": "‚úćÔłŹ Enter new time IN SECONDS",
                        "handler": self.input_handler,
                    },
                    {"text": "+1 sec", "callback": self.increment},
                ],
                [
                    {"text": "‚úÖ", "callback": self.proceed},
                    {
                        "text": "‚ĚĆ",
                        "action": "close",
                    },
                ],
            ],
        )

    async def input_handler(self, call: InlineCall, query: str):
        if not query.isdigit():
            await call.answer("–í—č –≤–≤–Ķ–Ľ–ł –Ĺ–Ķ —á–ł—Ā–Ľ–ĺ!")
            return

        self.set("timer", int(query))

        timer = self.get("timer", int(query))
        await call.answer()

        await call.edit(
            text=self.strings("text").format(timer),
            reply_markup=[
                [
                    {
                        "text": "-1 sec",
                        "callback": self.decrement,
                    },
                    {
                        "text": "‚úćÔłŹ Enter value",
                        "input": "‚úćÔłŹ Enter new time IN SECONDS",
                        "handler": self.input_handler,
                    },
                    {"text": "+1 sec", "callback": self.increment},
                ],
                [
                    {"text": "‚úÖ", "callback": self.proceed},
                    {
                        "text": "‚ĚĆ",
                        "action": "close",
                    },
                ],
            ],
        )