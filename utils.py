import json

def get_posts_all():
    with open('data/posts.json') as file:
        return json.load(file)


def get_comments_all():
    with open('data/comments.json') as file:
        return json.load(file)

def get_comments_by_post_id(post_id):
    comments = get_comments_all()
    po = []
    for i in range(0, len(comments)):
        if comments[i]['post_id'] == post_id:
            po.append(comments[i])
    if len(po) == 0:
        raise ValueError
    return po
def get_posts_by_user(user_name):
    posts = get_posts_all()
    po = []
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            po.append(post)
    if len(po) == 0:
        raise ValueError
    return po
def search_for_posts(query):
    posts = get_posts_all()
    all_posts = []
    for post in posts:
        if query in post['content']:
            all_posts.append(post)
    return all_posts


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post

