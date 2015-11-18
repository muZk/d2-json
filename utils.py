import re

def camelcase(name):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def sanitize_key(key, prefix = ''):
	if key is None:
		key = ''
	if prefix is '':
		key = key.split('_')[-1]
	else:
		key = key.replace(prefix, '')
	return key.lower()