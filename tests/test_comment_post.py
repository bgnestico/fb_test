# Creates a new post and adds a comment to it
from tools.steps_helper import create_post, add_post_comment, get_latest_post_id, get_post_comment, get_api, \
    comment_msg, post_msg, delete_post


def test_comment_post():
    api = get_api()
    create_post(api, post_msg)
    add_post_comment(api, get_latest_post_id(api), comment_msg)
    assert (get_post_comment(api, get_latest_post_id(api))) == comment_msg, "Comment was not added"
    delete_post(api, get_latest_post_id(api))
