import json, glob
from steam import vdf
from heroes import Hero
from utils import colorize
from os import path
from os import makedirs
from addon import Addon
import io


def _file_exists(file_path):
    if not path.isfile(file_path):
        _error('File not found: %s' % path.basename(file_path))
        return False
    else:
        _success('%s found!' % path.basename(file_path))
        return True


def _read_file(file_path):
    with open(file_path, 'r') as file:
        return vdf.load(file)


def _error(msg):
    _log('Error', msg, 'red')


def _info(msg):
    _log('Info', msg, 'cyan')


def _success(msg):
    _log('Ok', msg, 'green')


def _log(label, msg, color='white'):
    print('[%s] %s' % (colorize(label, color), msg))


def _dump(content, output_path):
    with io.open(output_path, 'w', encoding='utf8') as outfile:
        _info('Saving file in %s' % output_path)
        data = json.dumps(content, sort_keys=False, indent=4, ensure_ascii=False)
        outfile.write(unicode(data))


def dump(addon_path, addon_name, output_directory, language=None, include=[]):
    print('Generating JSON for mod %s at %s' % (addon_name, addon_path))
    print('Finding required files...')

    addon = Addon(addon_name, addon_path)
    addon.open()

    if _file_exists(addon.npc_abilities_custom) and _file_exists(addon.npc_heroes_custom):

        _info('Required files has been found')

        if len(addon.language_files) == 0:
             _error('No languages were found')
             return
        else:
            _info('Languages found: %s' % ', '.join(addon.languages()))

        if language is None:
            languages = addon.languages()
        else:
            language_file = addon.get_file(language)
            if language_file is None:
                _error('Language %s not found' % language)
                return
            else:
                _info('Using %s' % language)
                languages = [language]

        if not path.exists(output_directory):
            _info('Creating output directory: %s' % output_directory)
            makedirs(output_directory)

        _info('Extracting data...')

        if len(include) > 0:
            _info('Following hero attributes will be included: %s' % ', '.join(include))

        for language in languages:
            language_file = addon.get_file(language)
            heroes = _read_file(addon.npc_heroes_custom)
            abilities = _read_file(addon.npc_abilities_custom)
            english = _read_file(language_file)
            hero_dump = Hero(heroes, abilities, english, addon, include).parse()
            _dump(hero_dump, path.join(output_directory, language) + '.json')