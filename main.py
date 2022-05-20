from importi.importslist import *
from databasesqlite.database import *
API_TOKEN = "5330120564:AAGZNSDlI9VaivqVSq8pE8vxm0mvFdI3wuQ"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage = storage)
upragereputation=['+','спасибо','рэхмэт','годно','рэхмэт','годнота','годно','охуенно','хорошо','круто','супер','гуд'
                                                                                                'гут', 'гут', 'молодцы', 'молодец', 'няша', 'няши','милота','вылижу', 'няшнота', 'няха', 'няхи', 'цмок', 'ням', 'бох', 'отсосу', 'высосу']
upragereputationbig=[]
for bigwords in upragereputation:
    bigwords1 = bigwords.capitalize()
    upragereputationbig.append(bigwords1)
upragereputationall = []
for bigwordsfromupragereputationbig in upragereputationbig:
    upragereputationall.append(bigwordsfromupragereputationbig)
for bigwordsfromupragereputationsmall in upragereputation:
    upragereputationall.append(bigwordsfromupragereputationsmall)
@dp.message_handler(Text(equals=upragereputationall))
async def upragereputationfunc(message: types.Message):
    print(message.from_user.id)
    idusereplyer = message.from_user.id
    idusergetreplayed = message.reply_to_message
    print(idusergetreplayed)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
