from app.core.cache import cached
from ..tmdb import TMDb

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Discover(TMDb):
    _urls = {
        "movies": "/discover/movie",
        "tv": "/discover/tv"
    }

    @cached(maxsize=1, ttl=43200)
    def discover_movies(self, params_tuple):
        """
        Discover movies by different types of data like average rating, number of votes, genres and certifications.
        :param params_tuple: dict
        :return:
        """
        params = dict(params_tuple)
        # 添加默认分级为NC-17（如果用户没有指定分级）
        if 'certification' not in params and 'certification.gte' not in params and 'certification.lte' not in params:
            params['certification_country'] = 'US'
            params['certification'] = 'NC-17'
        return self._request_obj(self._urls["movies"], urlencode(params), key="results", call_cached=False)

    @cached(maxsize=1, ttl=43200)
    def discover_tv_shows(self, params_tuple):
        """
        Discover TV shows by different types of data like average rating, number of votes, genres,
        the network they aired on and air dates.
        :param params_tuple: dict
        :return:
        """
        params = dict(params_tuple)
        # 添加默认分级为TV-MA（如果用户没有指定分级）
        if 'certification' not in params and 'certification.gte' not in params and 'certification.lte' not in params:
            params['certification_country'] = 'US'
            params['certification'] = 'TV-MA'
        return self._request_obj(self._urls["tv"], urlencode(params), key="results", call_cached=False)
