import json
import os

from db import db
from db import Article
from db import Comment
from db import Category
from db import Citation
from db import User 

from flask import Flask
from flask import request

# define db filename
db_filename = "todo.db"
app = Flask(__name__)

# setup config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# initialize app
db.init_app(app)
with app.app_context():
    db.create_all()


# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


# -- ARTICLE ROUTES ------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return failure_response("Page not found", 404)
@app.route("/")
def welcome():
    return """Welcome to my news site! Feel free to add whatever articles and 
    comments you'd like."""

@app.route("/articles/")
def get_articles():
    return success_response(
        {"articles" : [a.serialize() for a in Article.query.all()]}
    )


@app.route("/articles/", methods=["POST"])
def create_article():
    body = json.loads(request.data)
    if body.get("description") is None or not isinstance(body.get("description"), str):
        return failure_response("Invalid description.", 400)
    if not Article.query.filter_by(description = body.get("description")).first() is None:
        return failure_response("Enter a unique description.", 400)
    new_article = Article(description=body.get("description"))
    db.session.add(new_article)
    db.session.commit()
    return success_response(new_article.serialize(), 201)


@app.route("/articles/<int:article_id>/")
def get_article(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found")
    return success_response(article.serialize())


@app.route("/articles/<int:article_id>/", methods=["POST"])
def update_article(article_id):
    body = json.loads(request.data)
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    if body.get("description") is None or not isinstance(body.get("description"), str):
        return failure_response("Invalid description.", 400)  
    article.description = body.get("description", article.description)
    db.session.commit()
    return success_response(article.serialize())


@app.route("/articles/<int:article_id>/", methods=["DELETE"])
def delete_article(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    db.session.delete(article)
    db.session.commit()
    return success_response(article.serialize())

@app.route("/articles/<int:article_id>/user/", methods=["POST"])
def follow_user_article(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    body = json.loads(request.data)
    username = body.get("username")
    user = User.query.filter_by(username = username).first()
    if user is None:
        return failure_response("Invalid username.", 404)
    article.users.append(user)
    db.session.commit()
    return success_response(article.serialize())


# -- COMMENT ROUTES ---------------------------------------------------

@app.route("/articles/<int:article_id>/comments/")
def get_comments(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    return success_response(
        {"comments" : [c.serialize() for c in Comment.query.all()]}
    )

@app.route("/articles/<int:article_id>/comments/", methods=["POST"])
def create_comment(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    body = json.loads(request.data)
    if body.get("description") is None or not isinstance(body.get("description"), str):
        return failure_response("Invalid description.", 400)  
    new_comment = Comment(
        description = body.get("description"),
        article_id = article_id,
    )
    db.session.add(new_comment)
    db.session.commit()
    return success_response(new_comment.serialize())

@app.route("/articles/<int:article_id>/comments/<int:comment_id>/", methods=["DELETE"])
def delete_comment(article_id, comment_id):
    article = Article.query.filter_by(id = article_id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    if article is None:
        return failure_response("Article not found!")
    if comment is None:
        return failure_response("Comment not found!")
    db.session.delete(comment)
    db.session.commit()
    return success_response(comment.serialize())

@app.route("/articles/<int:article_id>/comments/<int:comment_id>/", methods=["POST"])
def update_comment(article_id, comment_id):
    body = json.loads(request.data)
    article = Article.query.filter_by(id = article_id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    if article is None:
        return failure_response("Article not found!")
    if comment is None:
        return failure_response("Comment not found!")
    if body.get("description") is None or not isinstance(body.get("description"), str):
        return failure_response("Invalid description.", 400)  
    comment.description = body.get("description", comment.description)
    db.session.commit()
    return success_response(comment.serialize())


# -- CATEGORY ROUTES --------------------------------------------------


@app.route("/articles/<int:article_id>/category/", methods=["POST"])
def assign_category(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    body = json.loads(request.data)
    description = body.get("description")
    category = Category.query.filter_by(description = description).first()
    if category is None:
        category = Category(description = description)
    if not isinstance(description, str) or description is None:
        return failure_response("Invalid description.", 404)
    article.categories.append(category)
    db.session.commit()
    return success_response(article.serialize())

@app.route("/categories/")
def get_categories():
    return success_response(
        {"categories" : [a.serialize() for a in Category.query.all()]}
    )

@app.route("/categories/<int:category_id>/")
def get_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    if category is None:
        return failure_response("Category not found!")
    return success_response(category.serialize())

@app.route("/categories/<int:category_id>/", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    if category is None:
        return failure_response("Article not found!")
    db.session.delete(category)
    db.session.commit()
    return success_response(category.serialize())


# -- USER ROUTES --------------------------------------------------

@app.route("/users/")
def get_users():
    return success_response(
        {"users" : [a.serialize() for a in User.query.all()]}
    )

@app.route("/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    if body.get("username") is None or not isinstance(body.get("username"), str):
        return failure_response("Invalid username.", 400)  
    new_user = User(username=body.get("username"))
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/users/<int:user_id>/")
def get_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("Article not found")
    return success_response(user.serialize())

@app.route("/users/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return failure_response("Article not found!")
    db.session.delete(user)
    db.session.commit()
    return success_response(user.serialize())

# -- CITATION ROUTES --------------------------------------------------

@app.route("/citations/")
def get_citations():
    return success_response(
        {"citations" : [a.serialize() for a in Citation.query.all()]}
    )

@app.route("/citations/<int:citation_id>/")
def get_citation(citation_id):
    citation = Citation.query.filter_by(id = citation_id).first()
    if citation is None:
        return failure_response("Citation not found")
    return success_response(citation.serialize())

@app.route("/citations/<int:citation_id>/", methods=["DELETE"])
def delete_citation(citation_id):
    citation = Citation.query.filter_by(id = citation_id).first()
    if citation is None:
        return failure_response("Citation not found!")
    db.session.delete(citation)
    db.session.commit()
    return success_response(citation.serialize())

@app.route("/articles/<int:article_id>/cite/", methods=["POST"])
def assign_citation(article_id):
    article = Article.query.filter_by(id = article_id).first()
    if article is None:
        return failure_response("Article not found!")
    body = json.loads(request.data)
    title = body.get("title")
    author = body.get("author")
    citation = Citation.query.filter_by(title = title).first()
    if citation is None:
        citation = Citation(title = title, author = author)
    if not isinstance(title, str) or title is None:
        return failure_response("Invalid title.", 404)
    if not isinstance(author, str) or author is None:
        return failure_response("Invalid author.", 404)
    article.citations.append(citation)
    db.session.commit()
    return success_response(article.serialize())


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
