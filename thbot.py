import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message

token_api = '6987631218:AAGYetE4u3v0wdotzDA5AwU8tjmTTeKtNiA'
bot = Bot(token_api)
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет!')

async def main():
    await dp.start_polling(bot) 

if __name__ == '__main__':
    asyncio.run(main())