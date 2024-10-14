from flask import Flask, render_template, request
from database import Posts, SQLModel, session
from sqlmodel import select


app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html")


@app.get("/posts")
def get_posts():
    posts = session.scalars(select(Posts)).all()
    return render_template("index.html", posts=posts)


@app.get("/post_view")
def post_view():
    id = str(request.args.get("post_id"))
    post = session.get_one(Posts, id)
    post = post.model_dump()
    return render_template("view.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)