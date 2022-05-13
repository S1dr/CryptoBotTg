from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnBack =  KeyboardButton('Назад ↩')             #кнопкаа возврата из второго меню в первое
# --- MAin menu ----


#кнопка принажатии на которую будут показываться топ монет по росту за 24ч
# кнопка луна
btnTopCoins = KeyboardButton('Рост 💹')
# кнопка лидеров падения при нажатии показываются монеты которые наиболее упали за 24часа
btnLowCoins = KeyboardButton('Падение 🗑')
#новости из мира криптовалют
bntNews = KeyboardButton('Горячие Инсайды')
# кнопка луна
btnLunaCoin = KeyboardButton('LUNA')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTopCoins, btnLowCoins, bntNews,btnLunaCoin)

#Other Menu

btnInfo=KeyboardButton('Информация')
btnBtcValue = KeyboardButton('Курс BTC')

otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnBtcValue , btnBack)



