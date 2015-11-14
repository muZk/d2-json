import json
import os.path

cache = {}

def get_from_cache(key, language):
	return cache[language]['lang']['Tokens'].get(key)

def translate(key, language = 'English'):
	if language in cache:
		return get_from_cache(key, language)
	else:
		path = 'locales/dota_%s.json' % language
		if os.path.exists(path) and os.path.isfile(path):
			with open(path) as json_file:
				cache[language] = json.load(json_file)
				return get_from_cache(key, language)
		else:
			print('File not found: %s' % path)
			return None

# Alias for translate
def t(key, language = 'English'):
	return translate(key, language)