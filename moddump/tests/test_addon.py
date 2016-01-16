from unittest import TestCase
import moddump
from os import path

class TestAddon(TestCase):

    def test_addon_structure(self):

        npc = path.join('fake_addon/game/dota_addons/fake_addon/scripts/npc')
        resource = path.join('fake_addon/game/dota_addons/fake_addon/resource')
        npc_abilities_custom = path.join('fake_addon/game/dota_addons/fake_addon/scripts/npc/npc_abilities_custom.txt')
        npc_heroes_custom = path.join('fake_addon/game/dota_addons/fake_addon/scripts/npc/npc_heroes_custom.txt')

        addon = moddump.addon.Addon('fake_addon', path.join('fake_addon'))
        self.assertEquals(npc, addon.npc)
        self.assertEquals(resource, addon.resource)
        self.assertEquals(npc_abilities_custom, addon.npc_abilities_custom)
        self.assertEquals(npc_heroes_custom, addon.npc_heroes_custom)

    def test_language_files(self):
        addon_path = path.join(path.dirname(path.abspath(__file__)), 'fake_addon')
        addon = moddump.addon.Addon('fake_addon', addon_path)
        self.assertEquals(len(addon.language_files), 2)

    def test_languages(self):
        addon_path = path.join(path.dirname(path.abspath(__file__)), 'fake_addon')
        addon = moddump.addon.Addon('fake_addon', addon_path)

        self.assertEquals(len(addon.languages()), 2)
        self.assertIn('english', addon.languages())
        self.assertIn('russian', addon.languages())

    def test_language_file(self):
        addon_path = path.join(path.dirname(path.abspath(__file__)), 'fake_addon')
        addon = moddump.addon.Addon('fake_addon', addon_path)
        self.assertEquals(addon.get_file('english'), addon.language_files[1])
        self.assertEquals(addon.get_file('russian'), addon.language_files[0])

    def test_open(self):
        addon_path = path.join(path.dirname(path.abspath(__file__)), 'fake_addon')
        addon = moddump.addon.Addon('fake_addon', addon_path)
        addon.open()
        self.assertEquals(len(addon.available_heroes), 3)