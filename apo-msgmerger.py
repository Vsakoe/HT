__version__ = (0, 8, 27)


#┃┃━┃┃━━┃┃━━┃┃━━┃┏┓┏┓┃━━━━┏┛┗┓━━━━━━━━━━━
#┃┏━┓┃┣┫┃┗┛┛┃┗┛┛━━┃┃━━┃┃┃┃━┃┃━┃┏┓┃┃┏┛━━━━
#┃┃━┃┃┃┃┃┏┓┓┃┏┓┓━┏┛┗┓━┃┗┛┃━┃┗┓┃┗┛┃┃┃━━━━━
#┗┛━┗┛┗┛┗┛┗┛┗┛┗┛━┗━━┛━┗━━┛━┗━┛┗━━┛┗┛━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ▄▀█ █▄ █ █▀█ █▄ █ █▀█ ▀▀█ █▀█ █ █ █▀
# █▀█ █ ▀█ █▄█ █ ▀█ ▀▀█   █ ▀▀█ ▀▀█ ▄█

# meta developer: @apodiktum_modules
# meta banner: https://t.me/apodiktum_dumpster/11
# meta pic: https://t.me/apodiktum_dumpster/13
# meta translation: t.me/HikkTutor
# scope: hikka_only
# scope: hikka_min 1.6.1


import contextlib
import logging
from datetime import datetime, timezone


from telethon.errors import MessageIdInvalidError
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class ApodiktumMsgMergerMod(loader.Module):
    """
    Этот модуль "склеивает" разные сообщения вместе.
    """

    strings = {
        "name": "Apo-MsgMerger",
        "developer": "@anon97945",
        "_cfg_active": "Независимо от того, включен модуль (или нет).",
        "_cfg_blacklist_chats": "список чатов, которые модуль будет просматривать (или не будет).",
        "_cfg_cst_auto_migrate": "Позволяет автоматически переносить определенные изменения при запуске.",
        "_cfg_new_line_prefix": "префикс, который будет добавлен к новой строке.",
        "_cfg_edit_timeout": (
            "Максимальное время редактирования сообщения в минутах. 0 - без ограничений."
        ),
        "_cfg_ignore_prefix": "Префикс для полного игнорирования слияния.",
        "_cfg_link_preview": (
            "Следует ли отправлять предварительный просмотр веб-страницы.\nОставьте пустым, чтобы использовать "
            "решение будет приниматься автоматически на основе сообщений для объединения."
        ),
        "_cfg_merge_own_reply": "Следует ли объединять какое-либо сообщение из собственного ответа.",
        "_cfg_merge_own_reply_msg": (
            "сообщение, которое останется, если сообщение будет объединено с собственным ответом."
        ),
        "_cfg_merge_urls": "Следует ли объединять сообщения с URL-адресами.",
        "_cfg_new_lines": "Количество новых строк, добавляемых к сообщению.",
        "_cfg_reverse_merge": (
            "Следует ли объединять в новое (true) или старое (false) сообщение."
        ),
        "_cfg_skip_emoji": "Следует ли пропустить объединение сообщений с отдельными эмодзи.",
        "_cfg_skip_reactions": (
            "Следует ли пропустить объединение сообщений с реакциями."
        ),
        "_cfg_skip_length": "Длина сообщения, чтобы пропустить слияние.",
        "_cfg_skip_prefix": "Префикс для пропуска слияния.",
        "_cfg_skip_reply": "Следует ли пропустить объединение сообщений с ответом.",
        "_cfg_whitelist": (
            "Включает ли список чатов (True) или исключает(False) чат."
        ),
        "undo_merge_fail": "<b>Не удалось разъединить сообщения</b>",
        "nothing_to_merge": "<b>Нечего объединять.</b>",
    }

    strings_en = {}

    strings_de = {}

    strings_ru = {}

    all_strings = {
        "strings": strings,
        "strings_en": strings,
        "strings_de": strings_de,
        "strings_ru": strings_ru,
    }

    changes = {
        "migration1": {
            "name": {
                "old": "Apo MsgMerger",
                "new": "Apo-MsgMerger",
            },
        },
    }

    def __init__(self):
        self._ratelimit = []
        self.merged_msgs = {}
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "active",
                True,
                doc=lambda: self.strings("_cfg_active"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "chatlist",
                doc=lambda: self.strings("_cfg_blacklist_chats"),
                validator=loader.validators.Series(loader.validators.TelegramID()),
            ),
            loader.ConfigValue(
                "edit_timeout",
                2,
                doc=lambda: self.strings("_cfg_edit_timeout"),
                validator=loader.validators.Union(
                    loader.validators.Integer(minimum=1),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "ignore_prefix",
                ["+"],
                doc=lambda: self.strings("_cfg_ignore_prefix"),
                validator=loader.validators.Series(
                    loader.validators.Union(
                        loader.validators.String(length=1),
                        loader.validators.NoneType(),
                    ),
                ),
            ),
            loader.ConfigValue(
                "link_preview",
                doc=lambda: self.strings("_cfg_link_preview"),
                validator=loader.validators.Union(
                    loader.validators.Boolean(),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "merge_own_reply",
                False,
                doc=lambda: self.strings("_cfg_merge_own_reply"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "merge_urls",
                True,
                doc=lambda: self.strings("_cfg_merge_urls"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "new_line_pref",
                ">",
                doc=lambda: self.strings("_cfg_new_line_prefix"),
                validator=loader.validators.Union(
                    loader.validators.String(length=1),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "new_lines",
                1,
                doc=lambda: self.strings("_cfg_new_lines"),
                validator=loader.validators.Integer(minimum=1, maximum=2),
            ),
            loader.ConfigValue(
                "own_reply_msg",
                "<code>☝️</code>",
                doc=lambda: self.strings("_cfg_merge_own_reply_msg"),
                validator=loader.validators.Union(
                    loader.validators.String(),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "reverse_merge",
                True,
                doc=lambda: self.strings("_cfg_reverse_merge"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "skip_emoji",
                True,
                doc=lambda: self.strings("_cfg_skip_emoji"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "skip_length",
                doc=lambda: self.strings("_cfg_skip_length"),
                validator=loader.validators.Union(
                    loader.validators.Integer(minimum=0),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "skip_prefix",
                [">"],
                doc=lambda: self.strings("_cfg_skip_prefix"),
                validator=loader.validators.Series(
                    loader.validators.Union(
                        loader.validators.String(length=1),
                        loader.validators.NoneType(),
                    ),
                ),
            ),
            loader.ConfigValue(
                "skip_reactions",
                True,
                doc=lambda: self.strings("_cfg_skip_reactions"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "skip_reply",
                False,
                doc=lambda: self.strings("_cfg_skip_reply"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "whitelist",
                False,
                doc=lambda: self.strings("_cfg_whitelist"),
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        self.apo_lib = await self.import_lib(
            "https://raw.githubusercontent.com/anon97945/hikka-libs/master/apodiktum_library.py",
            suspend_on_error=True,
        )
        await self.apo_lib.migrator.auto_migrate_handler(
            self.__class__.__name__,
            self.strings("name"),
            self.changes,
            self.config["auto_migrate"],
        )
        self.apo_lib.watcher_q.register(self.__class__.__name__)

    async def on_unload(self):
        self.apo_lib.watcher_q.unregister(self.__class__.__name__)

    async def cmsgmergercmd(self, message: Message):
        """
        открыть cfg настройки.
        """
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    async def mergecmd(self, message: Message):
        """
        объединить все собственные сообщения до последнего сообщения другого пользователя..
        """
        chat_id = utils.get_chat_id(message)
        text = ""
        del_msgs = []
        merge_msgs = []
        try:
            msgs = await self._client.get_messages(chat_id, limit=100)
            for i in range(-len(msgs), -1):
                if (
                    not isinstance(msgs[i], Message)
                    or not msgs[i].out
                    or msgs[i].forward
                    or msgs[i].via_bot
                    or msgs[i].sender_id != self.tg_id
                    or (self.config["skip_reactions"] and msgs[i].reactions)
                    or (msgs[i].media and not getattr(msgs[i].media, "webpage", False))
                    or (not self.config["merge_own_reply"] and msgs[i].is_reply)
                ):
                    break
                if i != -len(msgs):
                    del_msgs += [msgs[i].id]
                    merge_msgs += [msgs[i]]
            if merge_msgs:
                for msg in reversed(merge_msgs):
                    if text:
                        text += "\n" * self.config["new_lines"]
                    if self.config["new_line_pref"]:
                        text += self.config["new_line_pref"]
                    if (
                        not text
                        and self.apo_lib.utils.raw_text(msg).startswith(
                            self.get_prefix()
                        )
                        and not self.config["new_line_pref"]
                    ):
                        text += ">"
                    text += self.apo_lib.utils.raw_text(msg, True)
                await self._client.delete_messages(chat_id, del_msgs)
            if not text:
                text = self.apo_lib.utils.get_str(
                    "nothing_to_merge", self.all_strings, message
                )
            return await utils.answer(message, text)
        except IndexError:
            return

    async def unmergecmd(self, message: Message):
        """
        разъединить сообщения.
        """
        chat_id = utils.get_chat_id(message)
        if utils.get_chat_id(message) in self.merged_msgs:
            try:
                for key, msg_value in self.merged_msgs[chat_id]["message"].items():
                    if key == "text":
                        msg_text = msg_value
                    elif key == "link_preview":
                        msg_link_preview = msg_value
                for key, msg_value in self.merged_msgs[chat_id]["last_msg"].items():
                    if key == "id":
                        last_msg_id = msg_value
                    elif key == "text":
                        last_msg_text = msg_value
                    elif key == "link_preview":
                        last_msg_link_preview = msg_value
                await self.client.edit_message(
                    chat_id,
                    last_msg_id,
                    last_msg_text,
                    link_preview=last_msg_link_preview,
                )
                await self.client.edit_message(
                    message, msg_text, link_preview=msg_link_preview
                )
            except MessageIdInvalidError:
                await utils.answer(message, self.strings("undo_merge_fail"))
        else:
            await utils.answer(message, self.strings("undo_merge_fail"))
        self.merged_msgs.clear()

    async def q_watcher(self, message: Message):
        await self._queue_handler(message)

    async def _queue_handler(self, message: Message):
        if (
            not self.config["active"]
            or not isinstance(message, Message)
            or not message.out
            or message.forward
            or message.via_bot
            or self.apo_lib.utils.raw_text(message).startswith(self.get_prefix())
        ):
            return

        chat_id = utils.get_chat_id(message)
        if (self.config["whitelist"] and chat_id not in self.config["chatlist"]) or (
            not self.config["whitelist"] and chat_id in self.config["chatlist"]
        ):
            return

        if self.config["ignore_prefix"] and any(
            self.apo_lib.utils.raw_text(message).startswith(prefix)
            for prefix in self.config["ignore_prefix"]
        ):
            return

        if self.config["skip_prefix"] and (
            found_prefix := next(
                (
                    prefix
                    for prefix in self.config["skip_prefix"]
                    if self.apo_lib.utils.raw_text(message).startswith(prefix)
                ),
                None,
            )
        ):
            text = message.text.replace(utils.escape_html(found_prefix), "", 1)
            if len(text) > 0:
                with contextlib.suppress(Exception):
                    await message.edit(text)
                return

        if (
            (
                self.config["skip_length"]
                and len(self.apo_lib.utils.remove_html(message.text))
                >= self.config["skip_length"]
            )
            or (self.config["skip_reactions"] and message.reactions)
            or (
                message.media
                and not getattr(message.media, "webpage", False)
                or (
                    not self.config["merge_urls"]
                    and self.apo_lib.utils.get_entityurls(message)
                )
            )
        ):
            return
        last_msg = None
        try:
            if utils.get_topic(message):
                last_msg_iter = await self._client.get_messages(
                    chat_id, limit=5, reply_to=utils.get_topic(message)
                )
            else:
                last_msg_iter = await self._client.get_messages(chat_id, limit=5)
            for i in range(-4, -1):
                if last_msg_iter[i].id != message.id:
                    last_msg = last_msg_iter[i]
                    break
        except IndexError:
            return

        if (
            self.config["merge_own_reply"]
            and message.is_reply
            and (
                not message.reply_to_msg_id
                or message.reply_to_msg_id != utils.get_topic(message)
            )
        ):
            last_msg_reply = await message.get_reply_message()
            last_msg = last_msg_reply
        else:
            last_msg_reply = None

        if (
            (
                self.config["skip_emoji"]
                and (
                    self.apo_lib.utils.is_emoji(self.apo_lib.utils.raw_text(message))
                    or self.apo_lib.utils.is_emoji(
                        self.apo_lib.utils.raw_text(last_msg)
                    )
                )
            )
            or (
                self.config["skip_reply"]
                and not self.config["merge_own_reply"]
                and (message.is_reply or last_msg.is_reply)
                and (
                    not message.reply_to_msg_id
                    or message.reply_to_msg_id != utils.get_topic(message)
                )
            )
            or (
                last_msg.is_reply
                and message.is_reply
                and (
                    not message.reply_to_msg_id
                    or message.reply_to_msg_id != utils.get_topic(message)
                )
                and not self.config["merge_own_reply"]
            )
        ):
            return

        if (
            last_msg.sender_id != self.tg_id
            or not isinstance(last_msg, Message)
            or last_msg.via_bot
            or last_msg.fwd_from
            or (self.config["skip_reactions"] and last_msg.reactions)
            or (
                last_msg.media
                and not getattr(last_msg.media, "webpage", False)
                or (
                    not self.config["merge_urls"]
                    and self.apo_lib.utils.get_entityurls(last_msg)
                )
            )
            or self.apo_lib.utils.remove_html(last_msg.text)[0] == self.get_prefix()
        ):
            return

        if self.config["ignore_prefix"] and any(
            self.apo_lib.utils.raw_text(last_msg).startswith(prefix)
            for prefix in self.config["ignore_prefix"]
        ):
            return

        if (
            self.config["edit_timeout"]
            and (
                datetime.now(timezone.utc) - (last_msg.edit_date or last_msg.date)
            ).total_seconds()
            > self.config["edit_timeout"] * 60
        ) and (
            self.config["merge_own_reply"]
            and (
                not message.is_reply
                or message.reply_to_msg_id
                and message.reply_to_msg_id == utils.get_topic(message)
            )
            or not self.config["merge_own_reply"]
        ):
            return

        text = last_msg.text
        text += "\n" * self.config["new_lines"]

        if self.config["new_line_pref"]:
            text += self.config["new_line_pref"]
        text += message.text

        if (
            (message.is_reply and message.reply_to_msg_id != utils.get_topic(message))
            or self.config["reverse_merge"]
        ) and (
            not self.config["merge_own_reply"]
            or not message.is_reply
            or message.reply_to_msg_id == utils.get_topic(message)
        ):
            message, last_msg = last_msg, message
            message_text = last_msg.text
            last_msg_text = message.text
        else:
            message_text = message.text
            last_msg_text = last_msg.text
        if self.config["link_preview"] is None:
            link_preview = getattr(message.media, "webpage", False) or getattr(
                last_msg.media, "webpage", False
            )
        else:
            link_preview = bool(self.config["link_preview"])
        try:
            if self.config["reverse_merge"] and (
                self.config["merge_own_reply"]
                and (
                    (
                        last_msg.is_reply
                        and last_msg.reply_to_msg_id != utils.get_topic(last_msg)
                    )
                    or (
                        message.is_reply
                        and (
                            not message.reply_to_msg_id
                            or message.reply_to_msg_id != utils.get_topic(message)
                        )
                    )
                )
            ):
                if last_msg.is_reply and last_msg.reply_to_msg_id != utils.get_topic(
                    last_msg
                ):
                    reply = await last_msg.get_reply_message()
                else:
                    reply = await message.get_reply_message()
                await last_msg.delete()
                msg = await last_msg.client.send_message(
                    chat_id, text, reply_to=reply, link_preview=link_preview
                )
            else:
                msg = await last_msg.edit(text, link_preview=link_preview)

            if msg.out:
                if (
                    self.config["merge_own_reply"]
                    and self.config["own_reply_msg"]
                    and not self.config["reverse_merge"]
                    and (
                        message.is_reply
                        and (
                            not message.reply_to_msg_id
                            or message.reply_to_msg_id != utils.get_topic(message)
                        )
                    )
                ):
                    await message.edit(
                        self.config["own_reply_msg"], link_preview=link_preview
                    )
                else:
                    await message.delete()
            self.merged_msgs.clear()
            self.merged_msgs[chat_id] = {
                "message": {
                    "text": message_text,
                    "link_preview": link_preview,
                },
                "last_msg": {
                    "id": msg.id or last_msg.id,
                    "text": last_msg_text,
                    "link_preview": link_preview,
                },
            }
            return
        except Exception as exc:
            self.apo_lib.utils.log(
                logging.DEBUG,
                __name__,
                f"Edit failed on last_msg:\n{str(exc)}",
                debug_msg=True,
            )
            return