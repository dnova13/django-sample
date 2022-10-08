import hashlib
import random
import time


def string_to_int(s):
    try:
        return int(s)
    except:
        return None


def get_item_by_key(target, key):

    for c in target:
        if c[0] == key:
            return c

    return None


def get_value_by_key(target, key):
    item = get_item_by_key(target, key)
    if item:
        return item[1]

    return None


def get_filename(filename):
    extension = filename.rsplit('.', 1)[-1]
    filename = hashlib.md5(
        ('{}_{}'.format(filename, time.time())).encode('utf8')).hexdigest()
    return '{}.{}'.format(filename, extension)


def make_random_nickname():
    adjectives = [
        "귀여운",
        "심심한",
        "팔팔한",
        "호감있는",
        "산뜻한",
        "화사한",
        "파스텔톤",
        "거침없는",
        "최애",
        "부드러운",
        "멋진",
        "피곤한",
        "향기로운",
        "달콤한",
        "희망적인",
        "반짝이는",
        "똑똑한",
        "호기심많은",
        "가정적인",
        "친절한",
        "즐거운",
        "야성적인",
        "용감한",
        "어설픈",
        "성실한",
        "정직한",
        "신비한",
        "재능있는",
        "현명한",
        "엉뚱한",
        "애교있는",
        "다정한",
        "믿을만한",
        "침착한",
        "단호한",
        "겸손한",
        "로맨틱한",
        "감성적인",
        "투머치토커",
        "즉흥적인",
        "수줍은",
        "자유로운",
        "호감가는",
        "바쁜",
        "능력있는",
    ]

    characters = ['꼼비', '뚜야', '상구']

    random_nickname = f"{random.sample(adjectives, k=1)[0]} {random.sample(characters, k=1)[0]}"
    return random_nickname
