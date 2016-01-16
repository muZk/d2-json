import json
import os.path

from pkg_resources import resource_string

cache = {}


def get_from_cache(key, language):
    return cache[language]['lang']['Tokens'].get(key)


def translate(key, language='English', language_file=None):
    if language_file:
        return language_file['lang']['Tokens'].get(key)
    else:
        if language in cache:
            return get_from_cache(key, language)
        else:
            config = resource_string(__name__, 'locales/dota_%s.json' % language.lower())
            cache[language] = json.loads(config)
            return get_from_cache(key, language)


# Alias for translate
def t(key, language='English', language_file=None):
    return translate(key, language, language_file)
