from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)

    @classmethod
    def values(cls):
        return tuple(x.value for x in cls)

    @classmethod
    def keys(cls):
        return tuple(x.name for x in cls)


class SMSScopeEnum(ChoiceEnum):
    SIGN_UP = 'sign_up'


class Oauth2Enum(ChoiceEnum):
    KAKAO = 'kakao'
    NAVER = 'naver'
    APPLE = 'apple'
    OWNER = 'owner'
