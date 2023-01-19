from flask import Flask, render_template, request, jsonify
from utils import *

app = Flask(__name__, template_folder='templates')


@app.route('/')
def show_index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)

@app.route('/posts/<post_id>')
def show_posts_by_id(post_id):
    comment = get_comments_by_post_id(int(post_id))

    print(len(comment))
    post = get_post_by_pk(int(post_id))
    return render_template('post.html', post=post, comment=comment)


@app.route('/search')
def search_page():
  masha = request.args['s']
  func = search_for_posts(masha)
  return render_template('search.html', func=func)


@app.route('/users/<username>')
def search_by_name(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)

@app.errorhandler(404)
def error_404(e):
    return 'Такое не найдено', 404

@app.errorhandler(500)
def error_500(e):
    return'Internal Server Error ', 500

@app.route('/api/post')
def api_posts():
    posts = get_posts_all()
    return jsonify(posts)

@app.route('/api/post/<pk>')
def api_post(pk):
    post = get_post_by_pk(int(pk))

    return jsonify(post)

app.run()