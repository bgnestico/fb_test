# Creates a post and then deletes it
from tools.steps_helper import create_post, delete_post, get_latest_post_id, get_api, page_id, post_msg


def test_delete_post():
    api = get_api()
    create_post(api, post_msg)
    post_id = get_latest_post_id(api)
    delete_post(api, post_id)
    assert api.request(page_id + '/posts?limit=1')['data'][0]['id'] != post_id, "post was not deleted"
