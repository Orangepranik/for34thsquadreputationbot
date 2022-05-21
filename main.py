from importi.importslist import *
import types
from databasesqlite.database import *
API_TOKEN = "5330120564:AAGZNSDlI9VaivqVSq8pE8vxm0mvFdI3wuQ"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage = storage)

all_big_words = []
start_reputation = 0
bad_words = ['говно', 'хуйня', 'гадость', 'отвратительно', "удали", "удоли", "борк", "боян", "баян", "было"]
for big_bad_words in bad_words:
    capitalize_bad_words = big_bad_words.capitalize()
    all_big_words.append(capitalize_bad_words)
for small_bad_words in bad_words:
    all_big_words.append(small_bad_words)
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

    id_user_get_replayed_1 = idusergetreplayed['from']['id']
    username_user_get_replayed_1 = idusergetreplayed['from']['username']

    checkid_1 = cur.execute('SELECT * FROM reputation WHERE userid==?', (idusereplyer,)).fetchone()
    checkid_2 = cur.execute('SELECT * FROM reputation WHERE userid==?', (id_user_get_replayed_1,)).fetchone()
    print(username_user_get_replayed_1, id_user_get_replayed_1)
    if checkid_1 is None:
        cur.execute("INSERT INTO reputation(username,userid,reputation) VALUES(?, ?, ?)", (username_repleyer, idusereplyer, start_reputation))
        base.commit()
    if checkid_2 is None:
        cur.execute("INSERT INTO reputation(username,userid,reputation) VALUES(?, ?, ?)", (username_user_get_replayed_1, id_user_get_replayed_1, start_reputation))
        base.commit()
    getreputationuser_1 = checkid_1[2]
    getreputationuser_2 = checkid_2[2]
    print(getreputationuser_2)
    int_getreputationuser_2 = int(float(getreputationuser_2))
    reputation_up = int_getreputationuser_2+1
    print(reputation_up)
    await message.answer(f"{reputation_up}")
    select_user = cur.execute("SELECT reputation FROM reputation WHERE userid==?", (id_user_get_replayed_1,)).fetchone()
    update_reputation_up = ('UPDATE reputation SET reputation = ? WHERE userid =?')
    infoupdate = (reputation_up, id_user_get_replayed_1)
    cur.execute(update_reputation_up, infoupdate)
    base.commit()
@dp.message_handler(Text(equals=all_big_words))
async def decreasereputation(message: types.Message):
    idusereplyer = message.from_user.id
    idusergetreplayed = message.reply_to_message
    username_repleyer = message.from_user.username

    id_user_get_replayed_1 = idusergetreplayed['from']['id']
    username_user_get_replayed_1 = idusergetreplayed['from']['username']

    checkid_1 = cur.execute('SELECT * FROM reputation WHERE userid==?', (idusereplyer,)).fetchone()
    checkid_2 = cur.execute('SELECT * FROM reputation WHERE userid==?', (id_user_get_replayed_1,)).fetchone()
    print(username_user_get_replayed_1, id_user_get_replayed_1)
    if checkid_1 is None:
        cur.execute("INSERT INTO reputation(username,userid,reputation) VALUES(?, ?, ?)", (username_repleyer, idusereplyer, start_reputation))
        base.commit()
    if checkid_2 is None:
        cur.execute("INSERT INTO reputation(username,userid,reputation) VALUES(?, ?, ?)", (username_user_get_replayed_1, id_user_get_replayed_1, start_reputation))
        base.commit()
    getreputationuser_1 = checkid_1[2]
    getreputationuser_2 = checkid_2[2]
    int_getreputationuser_2 = int(float(getreputationuser_2))
    if int_getreputationuser_2 == 0:
        await message.answer('Твою репутацию понизили')
    reputation_down = int_getreputationuser_2-1

    await message.answer(f"{reputation_down}")
    select_user = cur.execute("SELECT reputation FROM reputation WHERE userid==?", (id_user_get_replayed_1,)).fetchone()
    update_reputation_up = ('UPDATE reputation SET reputation = ? WHERE userid =?')
    infoupdate = (reputation_down, id_user_get_replayed_1)
    cur.execute(update_reputation_up, infoupdate)
    base.commit()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
