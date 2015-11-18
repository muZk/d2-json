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

ability_unit_target_type_list = [
	'DOTA_UNIT_TARGET_ALL',
	'DOTA_UNIT_TARGET_HERO',
	'DOTA_UNIT_TARGET_BASIC',
	'DOTA_UNIT_TARGET_MECHANICAL',
	'DOTA_UNIT_TARGET_BUILDING',
	'DOTA_UNIT_TARGET_TREE',
	'DOTA_UNIT_TARGET_CREEP',
	'DOTA_UNIT_TARGET_COURIER',
	'DOTA_UNIT_TARGET_NONE',
	'DOTA_UNIT_TARGET_OTHER',
	'DOTA_UNIT_TARGET_CUSTOM'
]

ability_target_team_list = [
	'DOTA_UNIT_TARGET_TEAM_BOTH',
	'DOTA_UNIT_TARGET_TEAM_ENEMY',
	'DOTA_UNIT_TARGET_TEAM_FRIENDLY',
	'DOTA_UNIT_TARGET_TEAM_NONE',
	'DOTA_UNIT_TARGET_TEAM_CUSTOM'
]

dota_targeting_keys = [
	"DOTA_ToolTip_Targeting_Enemy",
	"DOTA_ToolTip_Targeting_EnemyCreeps",
	"DOTA_ToolTip_Targeting_EnemyHero",
	"DOTA_ToolTip_Targeting_EnemyUnits",
	"DOTA_ToolTip_Targeting_EnemyHeroesAndBuildings",
	"DOTA_ToolTip_Targeting_EnemyUnitsAndBuildings",
	"DOTA_ToolTip_Targeting_Self",
	"DOTA_ToolTip_Targeting_Allies",
	"DOTA_ToolTip_Targeting_AlliedCreeps",
	"DOTA_ToolTip_Targeting_AlliedHeroes",
	"DOTA_ToolTip_Targeting_AlliedUnits",
	"DOTA_ToolTip_Targeting_AlliedHeroesAndBuildings",
	"DOTA_ToolTip_Targeting_AlliedUnitsAndBuildings",
	"DOTA_ToolTip_Targeting_Trees",
	"DOTA_Tooltip_Targeting_All_Heroes",
	"DOTA_ToolTip_Targeting_Units"
]

def value_to_list(value):
	if value is None:
		value = ''
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

class TargetType:

	def __init__(self, target_type_str):
		self.is_empty = True
		attr_list = value_to_list(target_type_str)
		for target_type in ability_unit_target_type_list:
			name = target_type.split('_')[-1].lower()
			value = target_type in attr_list
			setattr(self, name, value)
			if value:
				self.is_empty = False

class TargetTeam:

	def __init__(self, target_team_str):
		self.is_empty = True
		attr_list = value_to_list(target_team_str)
		for target_team in ability_target_team_list:
			name = target_team.split('_')[-1].lower()
			value = target_team in attr_list
			setattr(self, name, value)
			if value:
				self.is_empty = False

class AffectsTooltip:

	def __init__(self, target_team, target_type):
		self.target_team = target_team
		self.target_type = target_type

	def tooltip_key(self):
		# http://moddota.com/forums/discussion/14/datadriven-ability-breakdown-documentation#Comment_58
		if self.target_type.is_empty:
			if self.target_team.enemy:
				return 'DOTA_ToolTip_Targeting_Enemy'
			elif self.target_team.friendly:
				return 'DOTA_ToolTip_Targeting_Allies'
			elif self.target_team.both:
				return 'DOTA_ToolTip_Targeting_Units'
		elif self.target_team.both:
			if self.target_type.hero and self.target_type.basic:
				return 'DOTA_ToolTip_Targeting_Units'
			elif self.target_type.all or self.target_type.basic or self.target_type.creep:
				return 'DOTA_ToolTip_Targeting_Units'
			elif self.target_type.hero:
				return 'DOTA_Tooltip_Targeting_All_Heroes'
		elif self.target_team.enemy:
			if self.target_type.hero:
				if self.target_type.basic and self.target_type.building:
					return 'DOTA_ToolTip_Targeting_EnemyUnitsAndBuildings'
				elif self.target_type.building:
					return 'DOTA_ToolTip_Targeting_EnemyUnitsAndBuildings'
				elif self.target_type.basic:
					return 'DOTA_ToolTip_Targeting_EnemyUnits'
				else:
					return 'DOTA_ToolTip_Targeting_EnemyHero'
			elif self.target_type.basic:
				return 'DOTA_ToolTip_Targeting_EnemyCreeps'
		elif self.target_team.friendly:
			if self.target_type.hero:
				if self.target_type.basic and self.target_type.building:
					return 'DOTA_ToolTip_Targeting_AlliedUnitsAndBuildings'
				elif self.target_type.building:
					return 'DOTA_ToolTip_Targeting_AlliedUnitsAndBuildings'
				elif self.target_type.basic:
					return 'DOTA_ToolTip_Targeting_AlliedUnits'
				else:
					return 'DOTA_ToolTip_Targeting_AlliedHeroes'
			elif self.target_type.basic:
				return 'DOTA_ToolTip_Targeting_AlliedCreeps'
		else:
			if self.target_type.tree:
				return 'DOTA_ToolTip_Targeting_Trees'
			else:
				return 'DOTA_ToolTip_Targeting_Self'

	def tooltip(self, language = 'English'):
		return i18n.t(self.tooltip_key(), language)

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
				'behaviour': parse_behaviour(self.default(key, 'AbilityBehavior')),
				'affects': self.affects(key),
				'key': key
			}
			if len(self.include) > 0:
				for attr in self.include:
					ability[camelcase(attr)] = self.default(key, attr)
			return ability
		else:
			return None

	def affects(self, key):
		target_type = TargetType(self.default(key, 'AbilityUnitTargetType'))
		target_team = TargetTeam(self.default(key, 'AbilityUnitTargetTeam'))
		affects = AffectsTooltip(target_team, target_type)
		return affects.tooltip()