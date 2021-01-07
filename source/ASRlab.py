from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '23492382'
API_KEY = 'XYLAuzkjAmYnhpGeKGA5ECio'
SECRET_KEY = 'l8EBWlAEwic57aVxmVgxoPgemVrikSCy'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


# 识别本地文件


result = client.asr(get_file_content(r'../data/speech/h1.wav'), 'wav', 16000, {
            'dev_pid': 1537,  # 默认1537（普通话 输入法模型）
        })
text = result['result'][0]

print(text)

