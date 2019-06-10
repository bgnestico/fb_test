import facebook
from settings import config


class Methods:

    def get_api(self):
        graph = facebook.GraphAPI(config['access_token'])
        my_pages = graph.get_object('me/accounts')
        page_access_token = None
        for page in my_pages['data']:
            if page['id'] == config['page_id']:
                page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        return graph
