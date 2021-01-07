import paddlehub as hub

ocr = hub.Module(name="chinese_ocr_db_crnn")  # 加载预训练模型

path = r'../data/ocr/'

results = ocr.recognize_text(paths=[path+'ads.jpg',
                                    path+'ads2.jpg',
                                    path+'ads3.jpg',
                                    path+'ChineseClearText.png',
                                    path+'EnglishClearText.png',
                                    path+'photo.JPG',
                                    path+'screenshot.jpg'
                                    ], visualization=True)  # 输入自定义待识别图片路径、并保存可视化图片结果

for i in range(len(results)):
    for j in range(len(results[i]['data'])):
        print(results[i]['data'][j]['text'])
    print("——————这-里-是-分-割-线——————")
