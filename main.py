import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объектов бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.reply("Добро пожаловать! Пожалуйста, выберите свою роль: /admin, /moderator или /participant.")


# Обработчик команды /admin
@dp.message_handler(commands=['admin'])
async def handle_admin(message: types.Message):
    await message.reply("Здравствуйте, Администратор! Что вы хотите сделать? Вот ваши возможности:\n"
                        "/change_role - Изменить роли участников\n"
                        "/publish_content - Опубликовать контент\n"
                        "/modify_content - Изменить контент\n"
                        "/delete_content - Удалить контент\n"
                        "/view_participants - Просмотреть участников\n"
                        "/start_competition - Запустить конкурс\n"
                        "/receive_content - Получить контент от участников")


# Обработчик команды /moderator
@dp.message_handler(commands=['moderator'])
async def handle_moderator(message: types.Message):
    await message.reply("Здравствуйте, Модератор! Что вы хотите сделать? Вот ваши возможности:\n"
                        "/publish_content - Опубликовать контент\n"
                        "/modify_content - Изменить контент\n"
                        "/delete_content - Удалить контент\n"
                        "/view_participants - Просмотреть участников\n"
                        "/start_competition - Запустить конкурс\n"
                        "/receive_content - Получить контент от участников")


# Обработчик команды /participant
@dp.message_handler(commands=['participant'])
async def handle_participant(message: types.Message):
    await message.reply("Здравствуйте, Участник! Что вы хотите сделать? Вот ваши возможности:\n"
                        "/register - Зарегистрироваться на конкурс\n"
                        "/submit_work - Отправить свою работу")


# Обработчик команды /change_role
@dp.message_handler(commands=['change_role'])
async def handle_change_role(message: types.Message):
    await message.reply("Вы выбрали изменение ролей участников. Пожалуйста, предоставьте необходимую информацию.")


# Обработчик команды /publish_content
@dp.message_handler(commands=['publish_content'])
async def handle_publish_content(message: types.Message):
    await message.reply("Вы выбрали опубликовать контент. Пожалуйста, предоставьте необходимую информацию.")


# Обработчик команды /modify_content
@dp.message_handler(commands=['modify_content'])
async def handle_modify_content(message: types.Message):
    await message.reply("Вы выбрали изменить контент. Пожалуйста, предоставьте необходимую информацию.")


# Обработчик команды /delete_content
@dp.message_handler(commands=['delete_content'])
async def handle_delete_content(message: types.Message):
    await message.reply("Вы выбрали удалить контент. Пожалуйста, предоставьте необходимую информацию.")


# Обработчик команды /view_participants
@dp.message_handler(commands=['view_participants'])
async def handle_view_participants(message: types.Message):
    await message.reply("Вы выбрали просмотр участников. Вот текущие участники:\n"
                        "- Участник 1\n"
                        "- Участник 2\n"
                        "- Участник 3")


# Обработчик команды /start_competition
@dp.message_handler(commands=['start_competition'])
async def handle_start_competition(message: types.Message):
    await message.reply("Вы выбрали запустить конкурс. Пожалуйста, предоставьте необходимую информацию.")


# Обработчик команды /receive_content
@dp.message_handler(commands=['receive_content'])
async def handle_receive_content(message: types.Message):
    await message.reply("Вы выбрали получить контент от участников. Пожалуйста, предоставьте необходимую информацию.")


# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
