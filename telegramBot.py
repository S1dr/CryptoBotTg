from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from main import get_coin_price , luna_stoimost
import sqlite3
import keyboards as nav

bot = Bot(token='5365745142:AAEFHp1sMjZEB2563fdap-UZzBElNWl3NaA')
dp = Dispatcher(bot)

a = get_coin_price("luna")
b = float(a)
print(type(b), b*2)

@dp.message_handler(commands='start')
async def welcome_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id ,
                           text=f'Привет, {message.from_user.full_name}.✌\n '
                                f'Меня зовут Боря. Я твой самый умный друг в мире криптовалюты.💰 \n'
                                f'Позволь мне показать тебе, что я умею 🤖.  \n'
                                f'Кстати цена BTC на данный момент: '
                                f'{(get_coin_price("btc"))}$', reply_markup=nav.mainMenu)

@dp.message_handler(text='LUNA')
async def luna_price(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Твой баланс: \n'
                                f'{(float(get_coin_price("luna"))*8686.95435)}$')




executor.start_polling(dp)

