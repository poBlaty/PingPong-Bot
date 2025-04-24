from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable

from aiogram.types import Message, TelegramObject, Update, CallbackQuery

import core.excel_part.xmain as xl
import redis
from redis.asyncio import Redis

from core.telegram_part.utils.Users import User, Player, Trainer, Admin, Referee, StatusRegistration
from core.telegram_part.utils.ConnectionDB import ConnectionDB


class Auth(BaseMiddleware):

    def __init__(self, pool: ConnectionDB):
        self.pool = pool

    @staticmethod
    async def authentication(tid: str | int, db: Redis) -> (User, Player, Trainer, Referee, Admin):
        cash = await db.hget(tid, 'status')

        user_data = {
            'status': 'User',
            'name': 'None',
            'phone_number': 'None',
            'reg': StatusRegistration.not_registered.value
        }

        if cash is not None:
            if cash == 'Admin':  # '6126011940'
                return Admin(tid)
            if cash == 'Trainer':
                return Trainer(tid)
            if cash == 'Referee':
                return Referee(tid)
            if cash == 'Player':
                return Player(tid)

            return User(tid)

        if xl.IsIdInBase(tid):
            role = xl.GetRoles(tid)
            name = str(xl.NameBase(tid) + xl.SurnameBase(tid))
            user_data['name'] = name
            user_data['reg'] = StatusRegistration.registered.value
            if 'Admin' in role:
                user_data['status'] = 'Admin'
                await db.hset(tid, mapping=user_data)  # add to cash
                return Admin(tid)
            if 'Trainer' in role:
                user_data['status'] = 'Trainer'
                await db.hset(tid, mapping=user_data)
                return Trainer(tid)
            if 'Referee' in role:
                user_data['status'] = 'Referee'
                await db.hset(tid, mapping=user_data)
                return Referee(tid)
            if 'Player' in role:
                user_data['status'] = 'Player'
                await db.hset(tid, mapping=user_data)
                return Player(tid)

        await db.hset(tid, mapping=user_data)
        return User(tid)

    async def __call__(self,
                       handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
                       event: Message | CallbackQuery,
                       data: Dict[str, Any]) -> Any:

        async with (await self.pool.get_connection()) as con:
            user = await self.authentication(tid=event.from_user.id,
                                             db=con)  # message.from_user.id 657253131 kate 6126011940 me
            status = await user.isUserSignIn(db=con)
            data['db'] = con
            data['user'] = user
            data['status'] = status
            return await handler(event, data)  # kwargs['state']
