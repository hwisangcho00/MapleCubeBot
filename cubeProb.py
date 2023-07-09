
import random

# 0 index: glowing cube
# 1 index: bright cube

# first, second, third lines for outer index

legendary_weapon_150 = [
    {
        "STR : +12%" : [9.7562, 9.7562],
        "DEX : +12%" : [9.7562, 9.7562],
        "INT : +12%" : [9.7562, 9.7562],
        "LUK : +12%" : [9.7562, 9.7562],
        "ATT : +12%" : [4.8780, 4.8780],
        "Magic ATT : +12%" : [4.8780, 4.8780],
        "Critical Rate : +12%" : [4.8780, 4.8780],
        "Damage : +12%" : [4.8780, 4.8780],
        "All stats: +9%" : [7.3171, 7.3171],
        "ATT : +32" : [4.8780, 4.8780],
        "Magic ATT : +32" : [4.8780, 4.8780],
        "Boss Monster Damage : +35%" : [9.7561, 9.7561],
        "Boss Monster Damage : +40%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +35%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +40%" : [4.8780, 4.8780]
        
    },
    {
        "STR : +9%" : [10.4651, 9.3023],
        "DEX : +9%" : [10.4651, 9.3023],
        "INT : +9%" : [10.4651, 9.3023],
        "LUK : +9%" : [10.4651, 9.3023],
        "ATT : +9%" : [6.2791, 5.5814],
        "Magic ATT : +9%" : [6.2791, 5.5814],
        "Critical Rate : +9%" : [8.3721, 7.4419],
        "Damage : +9%" : [6.2791, 5.5814],
        "All stats: +6%" : [8.3721, 7.4419],
        "Boss Monster Damage : +30%" : [6.2791, 5.5814],
        "Ignore Monster DEF : +30%" : [6.2791, 5.5814],
        "STR : +12%" : [0.9756, 1.9512],
        "DEX : +12%" : [0.9756, 1.9512],
        "INT : +12%" : [0.9756, 1.9512],
        "LUK : +12%" : [0.9756, 1.9512],
        "ATT : +12%" : [0.4878, 0.9756],
        "Magic ATT : +12%" : [0.4878, 0.9756],
        "Critical Rate : +12%" : [0.4878, 0.9756],
        "Damage : +12%" : [0.4878, 0.9756],
        "All stats: +9%" : [0.7317, 1.4634],
        "ATT : +32" : [0.4878, 0.9756],
        "Magic ATT : +32" : [0.4878, 0.9756],
        "Boss Monster Damage : +35%" : [0.4878, 0.9756],
        "Boss Monster Damage : +40%" : [0.4878, 0.9756],
        "Ignore Monster DEF : +35%" : [0.9756, 1.9512],
        "Ignore Monster DEF : +40%" : [0.4878, 0.9756]
    },
    {

        "STR : +9%" : [11.5116, 11.0465],
        "DEX : +9%" : [11.5116, 11.0465],
        "INT : +9%" : [11.5116, 11.0465],
        "LUK : +9%" : [11.5116, 11.0465],
        "ATT : +9%" : [6.9070, 6.6279],
        "Magic ATT : +9%" : [6.9070, 6.6279],
        "Critical Rate : +9%" : [9.2093, 8.8372],
        "Damage : +9%" : [6.9070, 6.6279],
        "All stats: +6%" : [9.2093, 8.8372],
        "Boss Monster Damage : +30%" : [6.9070, 6.6279],
        "Ignore Monster DEF : +30%" : [6.9070, 6.6279],
        "STR : +12%" : [0.0976, 0.4878],
        "DEX : +12%" : [0.0976, 0.4878],
        "INT : +12%" : [0.0976, 0.4878],
        "LUK : +12%" : [0.0976, 0.4878],
        "ATT : +12%" : [0.0488, 0.2439],
        "Magic ATT : +12%" : [0.0488, 0.2439],
        "Critical Rate : +12%" : [0.0488, 0.2439],
        "Damage : +12%" : [0.0488, 0.2439],
        "All stats: +9%" : [0.0732, 0.3659],
        "ATT : +32" : [0.0488, 0.2439],
        "Magic ATT : +32" : [0.0488, 0.2439],
        "Boss Monster Damage : +35%" : [0.0488, 0.2439],
        "Boss Monster Damage : +40%" : [0.0488, 0.2439],
        "Ignore Monster DEF : +35%" : [0.0976, 0.4878],
        "Ignore Monster DEF : +40%" : [0.0488, 0.2439]

    }
]

legendary_weapon_151 = [
    {
        "STR : +13%" : [9.7562, 9.7562],
        "DEX : +13%" : [9.7562, 9.7562],
        "INT : +13%" : [9.7562, 9.7562],
        "LUK : +13%" : [9.7562, 9.7562],
        "ATT : +13%" : [4.8780, 4.8780],
        "Magic ATT : +13%" : [4.8780, 4.8780],
        "Critical Rate : +13%" : [4.8780, 4.8780],
        "Damage : +13%" : [4.8780, 4.8780],
        "All stats: +10%" : [7.3171, 7.3171],
        "ATT : +32" : [4.8780, 4.8780],
        "Magic ATT : +32" : [4.8780, 4.8780],
        "Boss Monster Damage : +35%" : [9.7561, 9.7561],
        "Boss Monster Damage : +40%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +35%" : [4.8780, 4.8780],
        "Ignore Monster DEF : +40%" : [4.8780, 4.8780]
        
    },
    {
        "STR : +10%" : [10.4651, 9.3023],
        "DEX : +10%" : [10.4651, 9.3023],
        "INT : +10%" : [10.4651, 9.3023],
        "LUK : +10%" : [10.4651, 9.3023],
        "ATT : +10%" : [6.2791, 5.5814],
        "Magic ATT : +10%" : [6.2791, 5.5814],
        "Critical Rate : +10%" : [8.3721, 7.4419],
        "Damage : +10%" : [6.2791, 5.5814],
        "All stats: +7%" : [8.3721, 7.4419],
        "Boss Monster Damage : +30%" : [6.2791, 5.5814],
        "Ignore Monster DEF : +30%" : [6.2791, 5.5814],
        "STR : +13%" : [0.9756, 1.9512],
        "DEX : +13%" : [0.9756, 1.9512],
        "INT : +13%" : [0.9756, 1.9512],
        "LUK : +13%" : [0.9756, 1.9512],
        "ATT : +13%" : [0.4878, 0.9756],
        "Magic ATT : +13%" : [0.4878, 0.9756],
        "Critical Rate : +13%" : [0.4878, 0.9756],
        "Damage : +13%" : [0.4878, 0.9756],
        "All stats: +10%" : [0.7317, 1.4634],
        "ATT : +32" : [0.4878, 0.9756],
        "Magic ATT : +32" : [0.4878, 0.9756],
        "Boss Monster Damage : +35%" : [0.4878, 0.9756],
        "Boss Monster Damage : +40%" : [0.4878, 0.9756],
        "Ignore Monster DEF : +35%" : [0.9756, 1.9512],
        "Ignore Monster DEF : +40%" : [0.4878, 0.9756]
    },
    {

        "STR : +10%" : [11.5116, 11.0465],
        "DEX : +10%" : [11.5116, 11.0465],
        "INT : +10%" : [11.5116, 11.0465],
        "LUK : +10%" : [11.5116, 11.0465],
        "ATT : +10%" : [6.9070, 6.6279],
        "Magic ATT : +10%" : [6.9070, 6.6279],
        "Critical Rate : +10%" : [9.2093, 8.8372],
        "Damage : +10%" : [6.9070, 6.6279],
        "All stats: +7%" : [9.2093, 8.8372],
        "Boss Monster Damage : +30%" : [6.9070, 6.6279],
        "Ignore Monster DEF : +30%" : [6.9070, 6.6279],
        "STR : +13%" : [0.0976, 0.4878],
        "DEX : +13%" : [0.0976, 0.4878],
        "INT : +13%" : [0.0976, 0.4878],
        "LUK : +13%" : [0.0976, 0.4878],
        "ATT : +13%" : [0.0488, 0.2439],
        "Magic ATT : +13%" : [0.0488, 0.2439],
        "Critical Rate : +13%" : [0.0488, 0.2439],
        "Damage : +13%" : [0.0488, 0.2439],
        "All stats: +10%" : [0.0732, 0.3659],
        "ATT : +32" : [0.0488, 0.2439],
        "Magic ATT : +32" : [0.0488, 0.2439],
        "Boss Monster Damage : +35%" : [0.0488, 0.2439],
        "Boss Monster Damage : +40%" : [0.0488, 0.2439],
        "Ignore Monster DEF : +35%" : [0.0976, 0.4878],
        "Ignore Monster DEF : +40%" : [0.0488, 0.2439]

    }
]

legendary_hat_150 = [
    {
        "STR : +12%" : [9.7562, 9.7562],
        "DEX : +12%" : [9.7562, 9.7562],
        "INT : +12%" : [9.7562, 9.7562],
        "LUK : +12%" : [9.7562, 9.7562],
        "Max HP : +12%" : [9.7561, 9.7561],
        "Max MP : + 12%" : [9.7561, 9.7561],
        "All stats: +9%" : [7.3171, 7.3171],
        "10% chance to ignore 20% damage when attacked" : [7.3171, 7.3171],
        "10% chance to ignore 40% damage when attacked" : [7.3171, 7.3171],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [7.3171, 7.3171],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [4.8780, 4.8780],
        "Enables the <Decent Advanced Blessing> skill" : [7.3171, 7.3171]
    },
    {
        "STR : +9%" : [8.6538, 7.6923],
        "DEX : +9%" : [8.6538, 7.6923],
        "INT : +9%" : [8.6538, 7.6923],
        "LUK : +9%" : [8.6538, 7.6923],
        "Max HP : +9%" : [10.3846, 9.2308],
        "Max MP : + 9%" : [10.3846, 9.2308],
        "All stats: +6%" : [6.9231, 6.1538],
        "5% chance to ignore 20% damage when attacked" : [6.9231, 6.1538],
        "5% chance to ignore 40% damage when attacked" : [6.9231, 6.1538],
        "Enables the <Decent Mystic Door> skill" : [6.9231, 6.1538],
        "HP Recovery Items and Skills : +30%" : [6.9231, 6.1538],
        "STR : +12%" : [0.9756, 1.9512],
        "DEX : +12%" : [0.9756, 1.9512],
        "INT : +12%" : [0.9756, 1.9512],
        "LUK : +12%" : [0.9756, 1.9512],
        "Max HP : +12%" : [0.9756, 1.9512],
        "Max MP : + 12%" : [0.9756, 1.9512],
        "All stats: +9%" : [0.7317, 1.4634],
        "10% chance to ignore 20% damage when attacked" : [0.7317, 1.4634],
        "10% chance to ignore 40% damage when attacked" : [0.7317, 1.4634],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.7317, 1.4634],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.4878, 0.9756],
        "Enables the <Decent Advanced Blessing> skill" : [0.7317, 1.4634]
    },
    {
        "STR : +9%" : [9.5192, 9.1346],
        "DEX : +9%" : [9.5192, 9.1346],
        "INT : +9%" : [9.5192, 9.1346],
        "LUK : +9%" : [9.5192, 9.1346],
        "Max HP : +9%" : [11.4231, 10.9615],
        "Max MP : + 9%" : [11.4231, 10.9615],
        "All stats: +6%" : [7.6154, 7.3077],
        "5% chance to ignore 20% damage when attacked" : [7.6154, 7.3077],
        "5% chance to ignore 40% damage when attacked" : [7.6154, 7.3077],
        "Enables the <Decent Mystic Door> skill" : [7.6154, 7.3077],
        "HP Recovery Items and Skills : +30%" : [7.6154, 7.3077],
        "STR : +12%" : [0.0976, 0.4878],
        "DEX : +12%" : [0.0976, 0.4878],
        "INT : +12%" : [0.0976, 0.4878],
        "LUK : +12%" : [0.0976, 0.4878],
        "Max HP : +12%" : [0.0976, 0.4878],
        "Max MP : + 12%" : [0.0976, 0.4878],
        "All stats: +9%" : [0.0732, 0.3659],
        "10% chance to ignore 20% damage when attacked" : [0.0732, 0.3659],
        "10% chance to ignore 40% damage when attacked" : [0.0732, 0.3659],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.0732, 0.3659],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.0488, 0.2439],
        "Enables the <Decent Advanced Blessing> skill" : [0.0732, 0.3659]
    }
]

legendary_hat_151 = [
    {
        "STR : +13%" : [9.7562, 9.7562],
        "DEX : +13%" : [9.7562, 9.7562],
        "INT : +13%" : [9.7562, 9.7562],
        "LUK : +13%" : [9.7562, 9.7562],
        "Max HP : +13%" : [9.7561, 9.7561],
        "Max MP : + 13%" : [9.7561, 9.7561],
        "All stats: +10%" : [7.3171, 7.3171],
        "10% chance to ignore 20% damage when attacked" : [7.3171, 7.3171],
        "10% chance to ignore 40% damage when attacked" : [7.3171, 7.3171],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [7.3171, 7.3171],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [4.8780, 4.8780],
        "Enables the <Decent Advanced Blessing> skill" : [7.3171, 7.3171]
    },
    {
        "STR : +10%" : [8.6538, 7.6923],
        "DEX : +10%" : [8.6538, 7.6923],
        "INT : +10%" : [8.6538, 7.6923],
        "LUK : +10%" : [8.6538, 7.6923],
        "Max HP : +10%" : [10.3846, 9.2308],
        "Max MP : + 10%" : [10.3846, 9.2308],
        "All stats: +7%" : [6.9231, 6.1538],
        "5% chance to ignore 20% damage when attacked" : [6.9231, 6.1538],
        "5% chance to ignore 40% damage when attacked" : [6.9231, 6.1538],
        "Enables the <Decent Mystic Door> skill" : [6.9231, 6.1538],
        "HP Recovery Items and Skills : +30%" : [6.9231, 6.1538],
        "STR : +13%" : [0.9756, 1.9512],
        "DEX : +13%" : [0.9756, 1.9512],
        "INT : +13%" : [0.9756, 1.9512],
        "LUK : +13%" : [0.9756, 1.9512],
        "Max HP : +13%" : [0.9756, 1.9512],
        "Max MP : + 13%" : [0.9756, 1.9512],
        "All stats: +10%" : [0.7317, 1.4634],
        "10% chance to ignore 20% damage when attacked" : [0.7317, 1.4634],
        "10% chance to ignore 40% damage when attacked" : [0.7317, 1.4634],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.7317, 1.4634],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.4878, 0.9756],
        "Enables the <Decent Advanced Blessing> skill" : [0.7317, 1.4634]
    },
    {
        "STR : +10%" : [9.5192, 9.1346],
        "DEX : +10%" : [9.5192, 9.1346],
        "INT : +10%" : [9.5192, 9.1346],
        "LUK : +10%" : [9.5192, 9.1346],
        "Max HP : +10%" : [11.4231, 10.9615],
        "Max MP : + 10%" : [11.4231, 10.9615],
        "All stats: +10%" : [7.6154, 7.3077],
        "5% chance to ignore 20% damage when attacked" : [7.6154, 7.3077],
        "5% chance to ignore 40% damage when attacked" : [7.6154, 7.3077],
        "Enables the <Decent Mystic Door> skill" : [7.6154, 7.3077],
        "HP Recovery Items and Skills : +30%" : [7.6154, 7.3077],
        "STR : +13%" : [0.0976, 0.4878],
        "DEX : +13%" : [0.0976, 0.4878],
        "INT : +13%" : [0.0976, 0.4878],
        "LUK : +13%" : [0.0976, 0.4878],
        "Max HP : +13%" : [0.0976, 0.4878],
        "Max MP : + 13%" : [0.0976, 0.4878],
        "All stats: +10%" : [0.0732, 0.3659],
        "10% chance to ignore 20% damage when attacked" : [0.0732, 0.3659],
        "10% chance to ignore 40% damage when attacked" : [0.0732, 0.3659],
        "Skill Colldown : -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.0732, 0.3659],
        "Skill Colldown : -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)": [0.0488, 0.2439],
        "Enables the <Decent Advanced Blessing> skill" : [0.0732, 0.3659]
    }
]

legendary_weapon = [
    legendary_weapon_150,
    legendary_weapon_151
]

legendary_emblem = [
    
]

legendary_secondary = [
    
]

legendary_hat = [
    legendary_hat_150,
    legendary_hat_151
]

legendary = [
    legendary_weapon,
    legendary_emblem,
    legendary_secondary,
    legendary_hat
]

