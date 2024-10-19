from flask import Flask, render_template, request, redirect, url_for
from database import Posts, session
from sqlmodel import select
from dataclasses import dataclass


app = Flask(__name__)
app.secret_key = "iuub#$hnn8h90DSfh;"


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/posts")
def get_posts():
    posts = session.scalars(select(Posts)).all()
    return render_template("index.html", posts = posts)


@app.get("/post_view")
def post_view():
    id = int(request.args.get("post_id"))
    post = session.get_one(Posts, id)
    post = post.model_dump()
    return render_template("view.html", post = post)


@dataclass
class PostForm:
    title: str
    content: str


@app.get("/posts/create")
def post_form():
    return render_template("form.html", post = PostForm("", "").__dict__)


@app.post("/posts/create")
def post_create():
    form_data = request.form
    post = Posts(
        content = form_data.get("content"),
        title = form_data.get("title"),
    )
    if post.title and post.content:
        session.add(post)
        session.commit()
        print(f"{form_data=}")
        return redirect(url_for(index.__name__))
    return render_template("form.html", post = PostForm("", "").__dict__)



if __name__ == "__main__":
    app.run(debug=True)