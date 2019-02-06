from flask import Flask, render_template, request, redirect, send_from_directory, session
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys
from googletrans import Translator
import re
from gensim.models import word2vec
from urllib import request as req
from urllib import error
from urllib import parse
import bs4
import os
import time
import traceback
import flickrapi
from urllib.request import urlretrieve
from urllib.request import urlopen
from retry import retry
from PIL import Image
import io
import json

app = Flask(__name__)

model = word2vec.Word2Vec.load('wiki.pkl')

DATA_FILE = 'norilog.json'


def save_data(Word1, Word2,result,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10):
    try:
        # json モジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []

    database.insert(0, {
        "Word1": Word1,
        "Word2": Word2,
        "result": result,
        "result1": result1,
        "result2": result2,
        "result3": result3,
        "result4": result4,
        "result5": result5,
        "result6": result6,
        "result7": result7,
        "result8": result8,
        "result9": result9,
        "result10": result10,
    })

    json.dump(database, open(DATA_FILE, mode="w", encoding="utf-8"), indent=3, ensure_ascii=False)

def load_data():
    """記録データを返します"""
    try:
        # json モジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []
    return database

@app.route('/')
def index():
	rides = load_data()
	return render_template('index.html',rides=rides)

@app.route('/save', methods=['POST'])
def save():
    word1 = request.form.get('Word1')  # 言葉１
    word2 = request.form.get('Word2')  # 言葉２

    pre = model.most_similar(positive = [word1,word2],topn=10)
    kekka1 = model.most_similar(positive = [pre[0][0]],topn = 4)
    kekka2 = model.most_similar(positive = [pre[1][0]],topn = 4)
    kekka3 = model.most_similar(positive = [pre[2][0]],topn = 4)
    kekka4 = model.most_similar(positive = [pre[3][0]],topn = 4)
    kekka5 = model.most_similar(positive = [pre[4][0]],topn = 4)
    kekka6 = model.most_similar(positive = [pre[5][0]],topn = 4)
    kekka7 = model.most_similar(positive = [pre[6][0]],topn = 4)
    kekka8 = model.most_similar(positive = [pre[7][0]],topn = 4)
    kekka9 = model.most_similar(positive = [pre[8][0]],topn = 4)
    kekka10 = model.most_similar(positive = [pre[9][0]],topn = 4)

    bun = str(pre)
    bun1 = str(kekka1)
    bun2 = str(kekka2)
    bun3 = str(kekka3)
    bun4 = str(kekka4)
    bun5 = str(kekka5)
    bun6 = str(kekka6)
    bun7 = str(kekka7)
    bun8 = str(kekka8)
    bun9 = str(kekka9)
    bun10 = str(kekka10)

    result = re.sub(r'[!-~]', "", bun)
    result1 = re.sub(r'[!-~]', "", bun1)
    result2 = re.sub(r'[!-~]', "", bun2)
    result3 = re.sub(r'[!-~]', "", bun3)
    result4 = re.sub(r'[!-~]', "", bun4)
    result5 = re.sub(r'[!-~]', "", bun5)
    result6 = re.sub(r'[!-~]', "", bun6)
    result7 = re.sub(r'[!-~]', "", bun7)
    result8 = re.sub(r'[!-~]', "", bun8)
    result9 = re.sub(r'[!-~]', "", bun9)
    result10 = re.sub(r'[!-~]', "", bun10)
    save_data(word1,word2,result,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10)
    # 保存後はトップページにリダイレクトします。

    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)