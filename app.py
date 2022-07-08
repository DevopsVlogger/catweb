from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# list of cat images
images = [
    "https://giphy.com/clips/bestfriends-cat-cats-kitty-IsDjNQPc4weWPEwhWm",
    "https://giphy.com/clips/bestfriends-best-friends-adopt-animal-adoption-ynmvLvIVxxofJuk9MO",
    "https://giphy.com/clips/bestfriends-best-friends-adopt-animal-adoption-cwQCUhKible5mGrtMO",
    "https://giphy.com/clips/studiosoriginals-good-morning-i0zTwaJzcj2LxCmY5P"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
