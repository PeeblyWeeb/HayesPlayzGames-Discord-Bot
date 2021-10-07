from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hayes Bot is Online!"

def run():
  app.run(host='0.0.0.0',port=8080)

def upkeep():
  t = Thread(target=run)
  t.start()
  