from os import path
from glob import glob
from steam import vdf
import re

class Addon:

    def __init__(self, addon_name, addon_path):
        self.path = addon_path
        self.name = addon_name
        self.npc = path.join(self.path, 'game/dota_addons/%s/scripts/npc' % self.name)
        self.resource = path.join(self.path, 'game/dota_addons/%s/resource' % self.name)
        self.npc_heroes_custom = path.join(self.npc, 'npc_heroes_custom.txt')
        self.npc_abilities_custom = path.join(self.npc, 'npc_abilities_custom.txt')
        self.herolist = path.join(self.npc, 'herolist.txt')
        self.language_files = glob(self.resource + '/addon_*.txt')
        self.available_heroes = []

    def open(self):
        if path.isfile(self.herolist):
            with open(self.herolist, 'r') as file:
                for key, value in vdf.load(file)['CustomHeroList'].iteritems():
                    if value == '1':
                        self.available_heroes.append(key)

    def languages(self):
        return [re.match(r'.*addon_(.*).txt', x).group(1) for x in self.language_files]

    def get_file(self, language):
        try:
            return self.language_files[self.languages().index(language)]
        except ValueError:
            return None