import os
import requests
import json
from flask import Flask, send_file,render_template

app = Flask(__name__,template_folder='template')

def getMeme():
    res=json.loads(requests.get("https://meme-api.com/gimme").text)
    return res['postLink'],res['title'],res['author'],res['preview'][-2],res['subreddit']



@app.route("/")
def index():
    meme_link,meme_title,meme_author,meme_pic,subreddit=getMeme()
    return render_template(r'index.html',meme_pic=meme_pic,meme_subreddit=subreddit,meme_author=meme_author,meme_title=meme_title,meme_link=meme_link)

def main():
    app.run(host="0.0.0.0",port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
