from flask import Flask, url_for
#from flask import url_for
from flask import render_template

app = Flask(__name__)
posts = []

@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>")
def post_form(post_id=None):
    return "post_form {}".format(post_id)

if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)
    #print(url_for("index")) # /
    #print(url_for("show_post", slug="leccion-1", preview=True)) # /p/leccion-1/?preview=True