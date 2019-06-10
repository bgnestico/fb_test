from pages.methods import Methods


def test_post():
    msg = "Hello. world!!!"
    api = Methods.get_api(config)
    api.put_object(parent_object="me", connection_name="feed", message=msg)
