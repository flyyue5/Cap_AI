from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11033230'
API_KEY = '5FRt7PwnBH550tOBgLypHN3G'
SECRET_KEY = 'S4SEw2HvKaHBqOxv5fz0ysCqRgEDrTLm'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('浙江温州，浙江温州，最大皮革厂江南皮革厂倒闭了！'
                           '王八蛋老板黄鹤吃喝嫖赌，欠下了3.5个亿，'
                           '带着他的小姨子跑了。'
                           '我们没有没有办法，拿着钱包抵公司。'
                           '原价都是三百多、二百多、一百多的钱包，通通二十块，'
                           '通通二十块！黄鹤王八蛋，你不是人，我们辛辛苦苦给你干了大半年，'
                           '你不发工资，你还我血汗钱，还我血汗钱！',
                           'zh', 1, {
    'vol': 15, 'per': 1
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido1.mp3', 'wb') as f:
        f.write(result)