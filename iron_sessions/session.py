from requests.exceptions import HTTPError
from iron_cache import IronCache
try:
    from django.utils.encoding import force_unicode
except ImportError:  # Python 3.*
    from django.utils.encoding import force_text as force_unicode
from django.contrib.sessions.backends.base import SessionBase, CreateError
from iron_sessions import settings


iron_cache = IronCache(
    project_id=settings.IRON_CACHE_PROJECT_ID, token=settings.IRON_CACHE_TOKEN
)


class SessionStore(SessionBase):
    '''
    iron.io cache as Django sessions backend
    '''
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)

        self.iron_cache = iron_cache
        self.iron_bracket = settings.IRON_SESSIONS_BRACKET

    def _real_key(self, key):
        '''
        shortcut for wrapping cache key and cache bracket to dict
        '''
        return {
            'cache': self.iron_bracket,
            'key': key
        }

    def load(self):
        '''
        get session data from storage
        '''
        try:
            session_data = self.iron_cache.get(
                **self._real_key(self._get_or_create_session_key())
            ).value

            return self.decode(force_unicode(session_data))
        except HTTPError:
            self.create()
            return {}

    def exists(self, session_key):
        '''
        check cache key exists at storage
        '''
        # currently no REST HEAD method at iron.io service
        # so we need whole get
        try:
            self.iron_cache.get(**self._real_key(session_key))

            return True
        except HTTPError:
            return False

    def create(self):
        while True:
            self._session_key = self._get_new_session_key()
            # ensure that session key is unique
            try:
                self.save(must_create=True)
            except CreateError:
                continue
            self.modified = True
            return

    def save(self, must_create=False):
        '''
        store session data to storage
        '''
        if must_create and self.exists(self._get_or_create_session_key()):
            raise CreateError

        data = self.encode(self._get_session(no_load=must_create))
        to_iron = self._real_key(self._get_or_create_session_key())
        to_iron.update({
            'value': data,
            'options': {'expires_in': self.get_expiry_age()}
        })
        self.iron_cache.put(**to_iron)

    def delete(self, session_key=None):
        '''
        delete session_key from storage
        '''
        if session_key is None:
            if self.session_key is None:
                return
            session_key = self.session_key
        try:
            self.iron_cache.delete(**self._real_key(session_key))
        except HTTPError:
            pass
