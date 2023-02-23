from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from tiktok import tik
from  aiogram.dispatcher.filters import Text
from  aiogram.dispatcher.filters.builtin import CallbackQuery

@dp.message_handlers(Text(startswith='https://www.tiktok.com'))
async def test (message:types.Message):
    natija = tik(message.text)
    music = natija['music']
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='download music', url='{}'.format(music))]
        ]
    )
    await message.answer_audio(natija['video'], reply_markup=btn)


@dp.callback_query_handlers(Text(startswith='🎼'))
async def test2(call:CallbackQuery):
    await call.answer(cache_time=60)
    data = call.data[1:]
    await call.message.answer_audio(data)