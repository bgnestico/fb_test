# First, it makes sure the post has no likes and then, it adds a "like" to it
from tools.steps_helper import get_api, get_likes_count, get_latest_post_id, like_post, create_post, post_msg, \
    delete_post


def test_like_post():
    api = get_api()
    create_post(api, post_msg)
    assert get_likes_count(api, get_latest_post_id(api)) == 0, "post already has a like"
    like_post(api, get_latest_post_id(api))
    assert get_likes_count(api, get_latest_post_id(api)) == 1, "like not added to the post"
    delete_post(api, get_latest_post_id(api))
