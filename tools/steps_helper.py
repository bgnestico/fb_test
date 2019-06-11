import facebook
from settings import page_id, access_token

# message variables
post_msg = 'This is a new post!'
updated_msg = 'This is an update to the post!'
comment_msg = 'Nice post and cool test!'

# API setup
config = {
        "page_id": page_id,
        "access_token": access_token
}


def get_api():
    graph = facebook.GraphAPI(config['access_token'])
    my_pages = graph.get_object('me/accounts')
    page_access_token = None
    for page in my_pages['data']:
        if page['id'] == config['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph


def create_post(api, msg):
    api.put_object(page_id, "feed", message=msg)


def update_post(api, post_id, msg):
    api.request(post_id + '?message=' + msg, method='POST')


def delete_post(api, post_id):
    api.delete_object(post_id)


def get_latest_post_message(api):
    latest_post = api.request(page_id + '/posts?limit=1')
    return latest_post['data'][0]['message']


def get_latest_post_id(api):
    latest_post = api.request(page_id + '/posts?limit=1')
    return latest_post['data'][0]['id']


def like_post(api, post_id):
    api.put_like(post_id)


def get_likes_count(api, post_id):
    likes = api.request(post_id + '?fields=likes.summary(true)')
    return likes['likes']['summary']['total_count']


def add_post_comment(api, post_id, msg):
    api.put_comment(post_id, msg)


def get_post_comment(api, post_id):
    comment = api.request(post_id + '?fields=comments')
    return comment['comments']['data'][0]['message']
