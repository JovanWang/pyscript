import requests
import json
from docx import Document
from docx.shared import Inches

# 网页版有个跟内容加密sign参数，需要计算。为了方便，所以选用手机版的网址进行翻译
url = "https://fanyi.baidu.com/basetrans"
queryList = ["KIEV, Ukraine (AP) — The Ukrainian president has urged NATO to deploy naval ships to the Sea of Azov amid a standoff with Russia, a statement sharply criticized by the Kremlin as a provocation aimed at further inflaming tensions.",
"President Petro Poroshenko made the call in an interview with the German daily Bild published Thursday, saying that “Germany is one of our closest allies and we hope that states within NATO are now ready to relocate naval ships to the Sea of Azov in order to assist Ukraine and provide security.”"
]
imageList = ["timqwqwqwvg.jpg","timqwqwqwvg.jpg"]

headers = {
    'Accept':'*/*',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'BAIDUCUID=++; PSTM=1491655249; BIDUPSID=1ECA43D665529765134F5CCD000FB51A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; hasSeenTips=1; BAIDUID=A57974B94365D8C0357D2613B4050312:FG=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; MCITY=-158%3A; BDUSS=kZLaWJsVDdCLVk4YklFR3ZJbGt-OFdrZXFLTGxBSkNZQXRzTGZTRFlsaThGaHBjQVFBQUFBJCQAAAAAAAAAAAEAAABQ6oU00NDV37OjyN0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALyJ8lu8ifJbW; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1422_21111_26350_27889_22074; BDSFRCVID=nbLOJeC626l72rQ7pkIIuFMPK2zRHN3TH6aoHPR1IWdIjKlHiLPxEG0PjU8g0Kubh02GogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJPHoDI-JKL3j5ruM-rV-JD0-fTBa4oXHD7yWCv8KqRcOR5Jj6K-h5bXKRLfbPnAW6Tl2xJcttcCOhuR3MA--t4n0bKDBlbbWCQiWpnVBUJWsq0x0-6le-bQypoaaT8H3KOMahv1al7xO-JoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjj0Da_83H; delPer=0; PSINO=7; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1543476095; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1543476095; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541765799,1543472813,1543476096; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1543476096',
    'Host':'fanyi.baidu.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
    }

document = Document()
document.add_heading('Document Title', level=1)
i = 0
for query in queryList:
    i += 1
    param = {
        'from':'en',
        'to':'zh',
        'query':query,
    }
    r = requests.post(url=url,data=param,headers=headers).json()
# r = json.loads(requests.post(url=url,data=param,headers=headers).text())
# print(r)
    result = r['trans'][0]['dst']
# r = requests.post(url=url,data=json.dumps(param),headers=headers)
# print(result)
    p = document.add_paragraph(result)
    if i % 3 == 0 and len(imageList) > 0:
        document.add_picture(imageList.pop(), width=Inches(1.25))

document.save('demo.docx')
