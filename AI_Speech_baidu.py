from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11033230'
API_KEY = '5FRt7PwnBH550tOBgLypHN3G'
SECRET_KEY = 'S4SEw2HvKaHBqOxv5fz0ysCqRgEDrTLm'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
a = client.asr(get_file_content('test1.wav'), 'wav', 16000, {
    'dev_pid': '1936',
})

# 从URL获取文件识别
# b = client.asr('', 'pcm', 16000, {
#     'url': 'http://www.yourdomain.com/res/16k_test.pcm',
#     'callback': 'http://www.yourdomain.com/post-dump.php',
# })

print(a)