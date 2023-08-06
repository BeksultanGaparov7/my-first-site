from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    contex = {'active': '/'}
    return render_template('index.html', **contex)

@app.route('/blog/')
def blog():
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()

    cur.execute("""select headline, story, image from blog_stories;""")

    stories = []
    for headline, story, image in cur.fetchall():
        stories.append({'headline': headline, 'story': story, 'image': image})
    conn.close()

    contex = {'stories': stories, 'active': 'blog'}

    return render_template('blog.html', **contex)

@app.route('/contacts/')
def contacts():
    contex = {'active': 'contacts'}
    return render_template('contacts.html',**contex)


if __name__ == "__main__":
    app.run(debug=False)