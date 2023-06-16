
import random

# 0 index: glowing cube
# 1 index: bright cube

# first, second, third lines for outer index
legendary_weapon_120_200 = [
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
    {},
    {}
]

rng = random.uniform(0, 100)
cur = 100.0
res = ""
for k, v in legendary_weapon_120_200[0].items():

    if rng > cur - v[1]:
        res = k
        break
    
    cur -= v[1]


print(rng, res)