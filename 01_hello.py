"""
API経由で「こんにちは」と喋ってもらって、音声をファイルに保存する

声：つくよみちゃん@COEIROINK
参考：https://zenn.dev/hk03ne/articles/ca4f76ea94bb26
無料AIトークソフトCOEIROINK: https://coeiroink.com
フリー素材キャラクターつくよみちゃん: https://tyc.rei-yumesaki.net
"""

import json
import requests

# しゃべらせたい文字列
text = "こんにちは"

# リクエストボディ
query = {
    "speakerUuid": "3c37646f-3881-5374-2a83-149267990abc",
    "styleId": 0,
    "text": text,
    "speedScale": 1.0,
    "volumeScale": 1.0,
    "prosodyDetail": [],
    "pitchScale": 0.0,
    "intonationScale": 1.0,
    "prePhonemeLength": 0.1,
    "postPhonemeLength": 0.5,
    "outputSamplingRate": 24000,
}

# 音声合成を実行
response = requests.post(
    "http://127.0.0.1:50032/v1/synthesis",
    headers={"Content-Type": "application/json"},
    data=json.dumps(query),
)

response.raise_for_status()

# カレントディレクトリに保存される
with open("audio.wav", "wb") as f_temp:
    f_temp.write(response.content)
