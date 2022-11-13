from aiogram import types
from dispatcher import dp
import config


@dp.chat_join_request_handler()
async def get_user_join_request(message: types.Message) -> None:
    print(message)


@dp.message_handler()
async def echo(message: types.Message) -> None:
    print(message)
