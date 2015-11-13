from utils import camelcase

damage_type_constants = {
	'DOTA_ATTRIBUTE_STRENGTH': 'str',
	'DOTA_ATTRIBUTE_AGILITY': 'agi',
	'DOTA_ATTRIBUTE_INTELLECT': 'int'
}

class Ability:

	def __init__(self, abilities, language, include = []):
		self.abilities = abilities
		self.language = language
		self.include = include

	def default(self, key, attr, default_value = None):
		return self.abilities[key].get(attr, default_value)

	def parse_ability(self, key):
		if key in self.abilities:
			ability = {
				'name': self.language.get('DOTA_Tooltip_ability_%s' % key),
				'description': self.language.get('DOTA_Tooltip_ability_%s_description' % key),
				'damage_type': self.default(key, 'AbilityUnitDamageType', '').replace('DAMAGE_TYPE_', '').lower(),
				'cooldown': self.default(key, 'AbilityCooldown'),
				'damage': self.default(key, 'AbilityDamage'),
				'mana_cost': self.default(key, 'AbilityManaCost'),
				'texture_name': self.default(key, 'AbilityTextureName')
			}
			if len(self.include) > 0:
				for attr in self.include:
					ability[camelcase(attr)] = self.default(key, attr)
			return ability
		else:
			return None