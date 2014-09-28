import requests
import json


class DisqusAPI(object):
    """
    Lightweight solution to make API calls to Disqus:

    More info:
    https://disqus.com/api/docs
    """
    def __init__(self,
            api_key,
            api_secret,
            version='3.0',
            formats='json'
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.version = version
        self.formats = formats

    def get(self, method, **kwargs):
        """
        Make get requests to retrieve data from Disqus
        """
        endpoint = 'https://disqus.com/api/{version}/{method}.{formats}'
        url = endpoint.format(
            version=self.version,
            method=method.replace('.', '/'),
            formats=self.formats
        )
        kwargs.update({
            'api_key': self.api_key,
            'api_secret': self.api_secret,
        })
        response = requests.get(url, params=kwargs)
        # TODO: support other formats like rss
        if self.formats == 'json':
            return json.loads(response.content.decode())

