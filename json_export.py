from steam import vdf
import pprint
pp = pprint.PrettyPrinter(indent=1)

vscripts_folder = './test/NWU_Reborn/game/dota_addons/nwu/scripts/npc'
resource_folder = './test/NWU_Reborn/game/dota_addons/nwu/resource'

# game/dota_addons/nwu/scripts/npc/npc_abilities_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_items_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_heroes_custom.txt
# game/dota_addons/nwu/scripts/npc/npc_units_custom.txt

heroes = abilities = english = None

with open('%s/npc_heroes_custom.txt' % vscripts_folder, 'r') as file:
	heroes = vdf.load(file)

with open('%s/npc_abilities_custom.txt' % vscripts_folder, 'r') as file:
	abilities = vdf.load(file)

with open('%s/addon_english.txt' % resource_folder, 'r') as file:
	english = vdf.load(file)

pp.pprint(english)