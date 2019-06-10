import facebook
from settings import page_id, access_token


def main():

    # API setup
    config = {
        "page_id": page_id,
        "access_token": access_token
    }
    api = get_api(config)

    # Create a new post
    post_msg = "This is a new post!"
    create_post(api, post_msg)
    assert get_latest_post_message(api) == post_msg, "post was not created"

    # Update the last created post
    updated_msg = "This is a an update to the post!"
    update_post(api, get_latest_post_id(api), updated_msg)
    assert get_latest_post_message(api) == updated_msg, "post was not updated"

    # Delete the updated post
    delete_post(api, get_latest_post_id(api))
    assert api.request(page_id + '/posts?limit=1')['data'] == [], "post was not deleted"


def get_api(config):
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


if __name__ == "__main__":
    main()
