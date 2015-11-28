# moddump #

Dota2 command line utility to generate localized JSON of your mod.

## Overview ##

This tool dumps your map information using heroes_custom.txt, abilities_custom.txt and addon_*.txt (language files) of your project.

Minimalist output example:

```
{
    "Heroes":
        "npc_dota_hero_sven": {
            "abilities": {
                "1": {
                    "affects": "Enemy Units", 
                    "behavior": "Unit Target", 
                    "cooldown": "25 22 19 16", 
                    "damage": "120 170 220 270", 
                    "damage_type": "Magical", 
                    "description": null, 
                    "key": "onoki_jinton", 
                    "mana_cost": "75 100 125 150", 
                    "name": null, 
                    "texture_name": "onoki_jinton"
                }, 
                "2": {
                    "affects": "Allied Units", 
                    "behavior": "Unit Target", 
                    "cooldown": "20", 
                    "damage": null, 
                    "damage_type": "<font color=\\\"#d61107\\\">Pure</font>", 
                    "description": null, 
                    "key": "onoki_stalagmite_armor", 
                    "mana_cost": "100", 
                    "name": null, 
                    "texture_name": "onoki_stalagmite_armor"
                }, 
                "3": {
                    "affects": "Enemies", 
                    "behavior": "Aura", 
                    "cooldown": null, 
                    "damage": null, 
                    "damage_type": null, 
                    "description": null, 
                    "key": "onoki_turn_to_dust", 
                    "mana_cost": null, 
                    "name": null, 
                    "texture_name": "onoki_turn_to_dust"
                }, 
                "4": {
                    "affects": "Enemy Units", 
                    "behavior": "No Target", 
                    "cooldown": "2 80 70", 
                    "damage": null, 
                    "damage_type": "<font color=\\\"#d61107\\\">Pure</font>", 
                    "description": null, 
                    "key": "onoki_kajutan_no_jutsu", 
                    "mana_cost": "175 250 325", 
                    "name": null, 
                    "texture_name": "onoki_kajutan_no_jutsu"
                }
            }, 
            "agi": null, 
            "agi_gain": null, 
            "attack_range": null, 
            "damage_max": null, 
            "damage_min": null, 
            "int": null, 
            "int_gain": null, 
            "lore": null, 
            "movement_speed": null, 
            "name": "Sven", 
            "primary_attribute": "str", 
            "str": null, 
            "str_gain": null, 
            "village": "iwagakure"
        },
    }, 
    "Language": "English"
}
```


For localization, the script use your addon language files and internal dota language values. The last values are used to generate behaviour and targeting tooltip texts, as it mentioned in this [guide](http://moddota.com/forums/discussion/14/datadriven-ability-breakdown-documentation#Comment_58).

## Requirements ##

Python 2.7

## Installation ##

From command line:

    $ pip install moddump

If you wish to install it manually, moddump uses the standard distutils 
module. To install it run:

    $ python setup.py install

## How to use ##

If moddump was installed correctly, you will be able to use from your command line. To see available type in command line:

	$ moddump -h

Easiest way to execute the script is the following:

	$ cd YOUR_ADDON_FOLDER
	$ moddump

Where YOUR_ADDON_FOLDER is the container of "content" and "game" folders of your addon.

# TODO
- Add tests