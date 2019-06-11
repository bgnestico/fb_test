# Creates a new post to the facebook page and then updates the message text
from tools.steps_helper import update_post, get_latest_post_message, get_latest_post_id, get_api,\
    create_post, post_msg, updated_msg, delete_post


def test_update_post():
    api = get_api()
    create_post(api, post_msg)
    update_post(api, get_latest_post_id(api), updated_msg)
    assert get_latest_post_message(api) == updated_msg, "post was not updated"
    delete_post(api, get_latest_post_id(api))
