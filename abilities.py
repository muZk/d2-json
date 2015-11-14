from utils import camelcase
import i18n

damage_type_constants = {
	'DOTA_ATTRIBUTE_STRENGTH': 'str',
	'DOTA_ATTRIBUTE_AGILITY': 'agi',
	'DOTA_ATTRIBUTE_INTELLECT': 'int'
}

behaviour_constants = {
	'DOTA_ABILITY_BEHAVIOR_NO_TARGET': 'DOTA_ToolTip_Ability_NoTarget',
	'DOTA_ABILITY_BEHAVIOR_PASSIVE': 'DOTA_ToolTip_Ability_Passive',
	'DOTA_ABILITY_BEHAVIOR_CHANNELLED': 'DOTA_ToolTip_Ability_Channeled',
	'DOTA_ABILITY_BEHAVIOR_AUTOCAST': 'DOTA_ToolTip_Ability_AutoCast',
	'DOTA_ABILITY_BEHAVIOR_AURA': 'DOTA_ToolTip_Ability_Aura',
	'DOTA_ABILITY_BEHAVIOR_TOGGLE': 'DOTA_ToolTip_Ability_Toggle',
	'DOTA_ABILITY_BEHAVIOR_UNIT_TARGET': 'DOTA_ToolTip_Ability_Target',
	'DOTA_ABILITY_BEHAVIOR_POINT': 'DOTA_ToolTip_Ability_Point'
}

def value_to_list(value):
	values = value.split('|')
	values = map(lambda b: b.strip(), values)
	return values

def parse_behaviour(behaviour, language = 'English'):
	#http://moddota.com/forums/discussion/14/datadriven-ability-breakdown-documentation
	behaviours = value_to_list(behaviour)
	if len(behaviours) == 0:
		return None
	elif len(behaviours) == 1:
		return i18n.t(behaviour_constants.get(behaviours[0]), language)
	else:
		if 'DOTA_ABILITY_BEHAVIOR_CHANNELLED' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_CHANNELLED'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_TOGGLE' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_TOGGLE'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_AURA' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_AURA'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_AUTOCAST' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_AUTOCAST'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_UNIT_TARGET' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_UNIT_TARGET'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_POINT' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_POINT'), language)
		elif 'DOTA_ABILITY_BEHAVIOR_PASSIVE' in behaviours:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_PASSIVE'), language)
		else:
			return i18n.t(behaviour_constants.get('DOTA_ABILITY_BEHAVIOR_NO_TARGET'), language)

def parse_affects(target_type, target_team, language = 'English'):
	key = 'Self'
	
	target_types = value_to_list(target_type)
	target_teams = value_to_list(target_team)

	enemies = 'DOTA_UNIT_TARGET_TEAM_ENEMY' in target_teams
	allies  = 'DOTA_UNIT_TARGET_TEAM_FRIENDLY' in target_teams
	both    = 'DOTA_UNIT_TARGET_TEAM_BOTH' in target_teams or (enemies and allies)
	heroes  = 'DOTA_UNIT_TARGET_HERO' in target_types
	creeps  = 'DOTA_UNIT_TARGET_CREEP' in target_types
	units   = 'DOTA_UNIT_TARGET_BASIC' in target_types
	builds  = 'DOTA_UNIT_TARGET_BUILDING' in target_types

	# if both:
	# 	if creeps or units or builds:
	# 		key = 'Units'
	# 	elif heroes:
	# 		key = 'All_Heroes'
	# elif enemies:
	# 	if len(target_types) == 0:
	# 		key = 'Enemy'
	# 	elif heroes:
	# 		if units:
	# 			key = 'EnemyUnits'
	# 		elif builds:
	# 			key = 'EnemyHeroesAndBuildings'
	# 		else:
	# 			key = 'EnemyUnitsAndBuildings'
	# 	else:
	# 		key = 'EnemyCreeps'
	# elif allies:
	# 	if len(target_types) == 0:
	# 		key = 'Enemy'
	# 	elif heroes:
	# 		if units:
	# 			key = 'EnemyUnits'
	# 		elif builds:
	# 			key = 'EnemyHeroesAndBuildings'
	# 		else:
	# 			key = 'EnemyUnitsAndBuildings'
	# 	else:
	# 		key = 'EnemyCreeps'

 #      "DOTA_ToolTip_Targeting": "AFFECTS:",
 #      "DOTA_ToolTip_Targeting_Enemy": "Enemies",
 #      "DOTA_ToolTip_Targeting_EnemyCreeps": "Enemy Creeps",
 #      "DOTA_ToolTip_Targeting_EnemyHero": "Enemy Heroes",
 #      "DOTA_ToolTip_Targeting_EnemyUnits": "Enemy Units",
 #      "DOTA_ToolTip_Targeting_EnemyHeroesAndBuildings": "Enemy Heroes and Buildings",
 #      "DOTA_ToolTip_Targeting_EnemyUnitsAndBuildings": "Enemy Units and Buildings",
 #      "DOTA_ToolTip_Targeting_Self": "Self",
 #      "DOTA_ToolTip_Targeting_Allies": "Allies",
 #      "DOTA_ToolTip_Targeting_AlliedCreeps": "Allied Creeps",
 #      "DOTA_ToolTip_Targeting_AlliedHeroes": "Allied Heroes",
 #      "DOTA_ToolTip_Targeting_AlliedUnits": "Allied Units",
 #      "DOTA_ToolTip_Targeting_AlliedHeroesAndBuildings": "Allied Heroes and Buildings",
 #      "DOTA_ToolTip_Targeting_AlliedUnitsAndBuildings": "Allied Units and Buildings",
 #      "DOTA_ToolTip_Targeting_Trees": "Trees",
 #      "DOTA_Tooltip_Targeting_All_Heroes": "Heroes",
 #      "DOTA_ToolTip_Targeting_Units": "Units",


	return i18n.t('DOTA_ToolTip_Targeting_%s' % key, language)


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
				'texture_name': self.default(key, 'AbilityTextureName'),
				'behaviour': parse_behaviour(self.default(key, 'AbilityBehavior'))
			}
			if len(self.include) > 0:
				for attr in self.include:
					ability[camelcase(attr)] = self.default(key, attr)
			return ability
		else:
			return None