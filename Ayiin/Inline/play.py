from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Ayiin import db_mem


def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 ᴘʟᴀʏ ᴀᴜᴅɪᴏ",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ᴘʟᴀʏ ᴠɪᴅᴇᴏ 🎥",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text=" ᴍᴏʀᴇ ",
                callback_data=f"Search {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• ᴄʟᴏsᴇ •",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons


def url_markup2(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⍟ ᴍᴜsɪᴄ ⍟​",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⍟ ᴠɪᴅᴇᴏ ​⍟",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• ᴄʟᴏsᴇ •",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="¹", callback_data=f"Ayiin {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="²", callback_data=f"Ayiin {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="³", callback_data=f"Ayiin {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⁴", callback_data=f"Ayiin {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⁵", callback_data=f"Ayiin {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="《", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="• ᴄʟᴏsᴇ •​", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="》", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="⁶",
                callback_data=f"Ayiin {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⁷",
                callback_data=f"Ayiin {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⁸",
                callback_data=f"Ayiin {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⁹",
                callback_data=f"Ayiin {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="¹⁰",
                callback_data=f"Ayiin {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="《", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="• ᴄʟᴏsᴇ •", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="》", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def secondary_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="• ᴍᴏʀᴇ •", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
        ],
    ]
    return buttons


def secondary_markup2(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ──𖣠‌─────────── {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="• ᴍᴏʀᴇ •", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
        ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ──𖣠‌─────────── {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="• ᴍᴏʀᴇ •", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
        ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ──𖣠‌─────────── {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close")],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ──𖣠‌─────────── {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close")],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("• ᴄʟᴏsᴇ •​", callback_data="close")],
    ]
)
