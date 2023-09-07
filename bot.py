from aiogram import Bot, Dispatcher, types
import asyncio
import datetime
from Singleton import Singleton


class LoggerBot(Singleton):
    def init(self, token: str, logging_chat_id: int):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot)
        self.chat_id = logging_chat_id

    def error(self, error: Exception, title: str = None):
        async def main(self):
            now = datetime.datetime.now()
            message = ''

            if title is not None:
                message += title + '\n'

            message += f'[ERROR - {now}]\n{error}'

            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message
            )

        asyncio.run(main(self))


    def exit(self):
        async def main(self):
            session = await self.bot.get_session()
            await session.close()
        asyncio.run(main(self))


lb = LoggerBot(
    token='6181055502:AAGY4EPBEFq_bb4Z3EMzfhGKkmfOhNCizNc',
    logging_chat_id=2021855860,
    )
ld = LoggerBot(
    token='6181055502:AAGY4EPBEFq_bb4Z3EMzfhGKkmfOhNCizNc',
    logging_chat_id=254245,
    )
print(lb is ld, lb, ld)


a = [i for i in range(100)]
a += ['ff']
a += [i for i in range(100, 200)]

for i in a:
    try:
        float(i)
    except Exception as ex:
        lb.error(error=ex)
lb.exit()
