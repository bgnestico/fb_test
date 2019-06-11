# Creates a new post to the facebook page
from tools.steps_helper import create_post, get_latest_post_message, get_latest_post_id, get_api, post_msg, delete_post


def test_create_post():
    api = get_api()
    create_post(api, post_msg)
    assert get_latest_post_message(api) == post_msg, "post was not created"
    delete_post(api, get_latest_post_id(api))
