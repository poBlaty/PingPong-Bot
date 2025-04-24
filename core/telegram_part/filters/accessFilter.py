from aiogram.types import Message
from aiogram.filters import BaseFilter

from core.telegram_part.utils.Users import StatusRegistration


class IsBANFilter(BaseFilter):

    async def __call__(self, message: Message, status: StatusRegistration) -> bool:  # 400063942
        if status == StatusRegistration.banned.value:
            return True
        return False


class AccessFilter(BaseFilter):

    async def __call__(self, message: Message, status: StatusRegistration) -> bool:
        if status == StatusRegistration.registered.value:
            return True
        return False


class InProcessFilter(BaseFilter):

    async def __call__(self, message: Message, status: StatusRegistration) -> bool:
        if status == StatusRegistration.in_process.value:
            return True
        return False


class AccessDeniedFilter(BaseFilter):

    async def __call__(self, message: Message, status: StatusRegistration) -> bool:
        if status == StatusRegistration.access_denied.value:
            return True
        return False


class NotRegisteredFilter(BaseFilter):

    async def __call__(self, message: Message, status: StatusRegistration) -> bool:
        if status == StatusRegistration.not_registered.value:
            return True
        return False
