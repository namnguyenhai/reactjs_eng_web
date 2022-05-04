from selenium import webdriver
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
# from starlette.middleware.cors import CORSMiddleware as CORSMiddleware 
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
async def out():
    return {"hello": "boy"}
class Data(BaseModel):
    vocab_str: str
@app.post('/vocab')
async def post_vocab(vocab_Str: Data):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('/home/hainam/Desktop/leet_code/chromedriver_linux64/chromedriver', options=option)
    driver.get('https://dictionary.cambridge.org/dictionary/essential-american-english/')
    time.sleep(0.5)
    eleme = driver.find_element_by_id('searchword')
    eleme.send_keys(vocab_Str.vocab_str)
    time.sleep(0.5)
    buton = driver.find_element_by_css_selector('button[class="bo iwc iwc-40 hao lb0 cdo-search-button lp-0"]').click()
    time.sleep(1.5)
    file1 = driver.find_element_by_css_selector('span[class="daud"] amp-audio[id="ampaudio1"] audio[class="i-amphtml-fill-content"] source[type="audio/mpeg"]').get_attribute('src')
    type_word = driver.find_elements_by_css_selector('div[class="posgram dpos-g hdib"] span[class="pos dpos"]')
    meaning = driver.find_elements_by_css_selector('div[class="def-head ddef_h"] div[class="def ddef_d db"]')
    speak = driver.find_element_by_css_selector('span[class="pron-info dpron-info"] span[class="pron dpron"] span[class="ipa dipa"]').text
    a = [i.text for i in type_word]
    val = [i.text for i in meaning]
    time.sleep(1)
    out  = {
        'vocab':vocab_Str, 
        'type':a, 
        'meaning':val,
        'mp3': file1,
        'ipa': speak
    }
    with open("data/vocabulary.json","w") as f:
        json.dump(out,f)
    return {
        'vocab':vocab_Str, 
        'type':a, 
        'meaning':val,
        'mp3': file1,
        'ipa': speak
    }
        #



# okay decompiling web_crawl.cpython-38.pyc
