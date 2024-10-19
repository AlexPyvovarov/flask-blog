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
    id = int(request.args.get("post_id"))
    post = session.get_one(Posts, id)
    post = post.model_dump()
    return render_template("view.html", post=post)


@app.post("/posts/create")
def post_create():
    pass


def post_mock_data():
    posts = [Posts(title=f"{x}", content=f"{x}") for x in range(1, 11)]
    session.add_all(posts)
    session.commit()




if __name__ == "__main__":
    post_mock_data()
    app.run(debug=True)