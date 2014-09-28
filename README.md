# Disqus API

Lightweight Disqus API. Small. Simple

## Usage

It is quite simple:

```python
from disqus_api import DisqusAPI

api = DisqusAPI(api_key=api_key, api_secret=api_secret)
kwargs = {
    'forum': 'myforum',
}
data = api.get('threads.listPopular', **kwargs)
```

