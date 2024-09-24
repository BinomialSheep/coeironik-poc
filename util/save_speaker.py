"""
利用可能なspeaker情報をファイルに出力する。
WEB API経由で使用するために必要なSPEAKER_UUID と STYLE_IDを知ることができる。

speakerを増やすためには、まずはCOEIROINKのGUI上で使える状態にするために音声ダウンロードする必要がある。
COEIROINK起動 → 左上のiアイコン → キャラクターダウンロード

参考：
https://coeiroink.com/download
https://coeiroink.com/q-and-a
"""

import json
import requests

API_SERVER = "http://127.0.0.1:50032"
SPEAKERS_INFO_FILE = "speakers.json"


def save_speakers():
    """
    利用可能なSpeaker情報をファイル出力する
    """
    speakers = []

    response = requests.get(
        f"{API_SERVER}/v1/speakers",
    )

    for item in json.loads(response.content):
        speaker = {
            "speakerName": item["speakerName"],
            "speakerUuid": item["speakerUuid"],
            "styles": [
                {"styleName": style["styleName"], "styleId": style["styleId"]}
                for style in item["styles"]
            ],
            "version": item["version"],
        }

        speakers.append(speaker)

    # 出力ファイルに保存
    with open(SPEAKERS_INFO_FILE, "w", encoding="utf-8") as f:
        json.dump(speakers, f, ensure_ascii=False, indent=4)


save_speakers()
