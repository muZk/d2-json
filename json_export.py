import pprint
import json
from steam import vdf
from heroes import Hero

pp = pprint.PrettyPrinter(indent=1)
vscripts_folder = './test/NWU_Reborn/game/dota_addons/nwu/scripts/npc'
resource_folder = './test/NWU_Reborn/game/dota_addons/nwu/resource'

# game/dota_addons/nwu/scripts/npc/npc_abilities_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_items_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_heroes_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_units_custom.txt

# Read our JSON files
heroes = abilities = english = None

with open('%s/npc_heroes_custom.txt' % vscripts_folder, 'r') as file:
	heroes = vdf.load(file)

with open('%s/npc_abilities_custom.txt' % vscripts_folder, 'r') as file:
	abilities = vdf.load(file)

with open('%s/addon_english.txt' % resource_folder, 'r') as file:
	english = vdf.load(file)

hero = Hero(heroes, abilities, english, ['Village'])

pp.pprint(hero.parse())

# Export JSON
with open('heroes.json', 'w') as outfile:
    json.dump(hero.parse(), outfile, sort_keys = True, indent = 4)