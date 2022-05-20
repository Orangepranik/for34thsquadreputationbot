from importi.importslist import *
import types
from databasesqlite.database import *
API_TOKEN = "5330120564:AAGZNSDlI9VaivqVSq8pE8vxm0mvFdI3wuQ"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage = storage)
uprage_reputation=['+','спасибо','рэхмэт','годно','рэхмэт','годнота','годно','охуенно','хорошо','круто','супер','гуд', 'гут', 'гут', 'молодцы', 'молодец', 'няша', 'няши','милота','вылижу', 'няшнота', 'няха', 'няхи', 'цмок', 'ням', 'бох', 'отсосу', 'высосу']
uprage_reputation_big=[]
for bigwords in uprage_reputation:
    big_words_1 = bigwords.capitalize()
    uprage_reputation_big.append(big_words_1)
uprage_reputation_all = []
for big_words_from_uprage_reputation_big in uprage_reputation_big:
    uprage_reputation_all.append(big_words_from_uprage_reputation_big)
for big_words_from_uprage_reputation_small in uprage_reputation:
    uprage_reputation_all.append(big_words_from_uprage_reputation_small)
@dp.message_handler(Text(equals=uprage_reputation_all))
async def upragereputationfunc(message: types.Message):
    idusereplyer = message.from_user.id
    idusergetreplayed = message.reply_to_message
    username_repleyer = message.from_user.username
    idusergetreplayed1 = idusergetreplayed['from']['last_name']
    cur.execute('INSERT INTO ')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
