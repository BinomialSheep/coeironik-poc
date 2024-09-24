"""
テキストから複数行読み込んで、1つのwavファイルとして書き出す

声：つくよみちゃん@COEIROINK
参考：https://zenn.dev/hk03ne/articles/ca4f76ea94bb26
無料AIトークソフトCOEIROINK: https://coeiroink.com
フリー素材キャラクターつくよみちゃん: https://tyc.rei-yumesaki.net
"""

import json
import time
import requests
from io import BytesIO
from pydub import AudioSegment


API_SERVER = "http://127.0.0.1:50032"
INPUT_FILE = "scenario.txt"
OUTPUT_FILE = "audio.wav"

# リリンちゃん（メスガキスタイル）
SPEAKER_UUID = "cb11bdbd-78fc-4f16-b528-a400bae1782d"
STYLE_ID = 92


def synthesize_audio(text: str) -> bytes:
    """
    COEIROINKに投げて、テキストを音声化する
    TODO：失敗時の例外処理
    """
    query = {
        "speakerUuid": SPEAKER_UUID,
        "styleId": STYLE_ID,
        "text": text,
        "speedScale": 1.2,
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
        f"{API_SERVER}/v1/synthesis",
        headers={"Content-Type": "application/json"},
        data=json.dumps(query),
    )
    response.raise_for_status()
    return response.content


def main():
    start_time = time.time()
    final_audio = AudioSegment.silent(duration=0)
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if line == "":
                continue

            # テキストを音声化（bytes形式）
            audio = synthesize_audio(line)
            # pydub.AudioSegment型
            audio = AudioSegment.from_wav(BytesIO(audio))
            # 音声結合
            final_audio += audio

            elapsed_time = time.time() - start_time
            print(f"Line {i + 1} processed. Time taken: {elapsed_time:.2f} seconds")

    final_audio.export(OUTPUT_FILE, format="wav")


if __name__ == "__main__":
    main()
