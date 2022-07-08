from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# list of cat images
images = [
    "https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif",
    "https://c.tenor.com/7JbbkdTGA38AAAAd/cute-cat.gif",
    "https://c.tenor.com/cS2O4bhrjLkAAAAd/happy-pleased.gif",
    "https://64.media.tumblr.com/bf1931d6ea2d4f204cb23f0e97a4a5e3/9a1e97b225707d24-b1/s640x960/b65654e3cf1770aa933800124ff9cc999a982965.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
