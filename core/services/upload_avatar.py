import os
from uuid import uuid1

from core.dataclasses.user_dataclass import CarDataClass


def upload_avatar(instance: CarDataClass, file: str):
    ext = file.split('.')[-1]
    return os.path.join(instance.model, 'avatars', f'{uuid1()}.{ext}')