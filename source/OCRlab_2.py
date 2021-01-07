from aip import AipOcr

"""APPID AK SK """
APP_ID = '22849136'
API_KEY = 'tMuFasuy6juP1oYyNxU1vsu3'
SECRET_KEY = 'UPD9kEe5PNR3eNantpF7GyfsmmG5ZTKp'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


path = r'../data/ocr/'
L = [path + 'ads.jpg', path + 'ads2.jpg', path + 'ads3.jpg',
     path + 'ChineseClearText.png', path + 'EnglishClearText.png',
     path + 'photo.JPG', path + 'screenshot.jpg']
for i in range(len(L)):
    image = get_file_content(L[i])
    client.basicAccurate(image)
    options = {"language_type": "CHN_ENG", "probability": "true"}
    Result = client.basicAccurate(image, options)
    show = Result['words_result']
    for i in show:
        print(i['words'])
    print("——————这-里-是-分-割-线——————")
