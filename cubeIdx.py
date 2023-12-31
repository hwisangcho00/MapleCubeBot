"""
Master file that keeps track of names and potentials for the cubing
"""
cubeList = ["glowing", "bright"]
tierList = ["rare", "epic", "unique", "legendary"]
tierUpList = [[14.10, 3.030, 2.484], [21.212, 8.372, 3.882]]
equipmentList = ["weapon", "emblem", "secondary", "eye", "face", "earrings", "pendant", "ring", 
                 "hat", "top", "overall", "bottom", 
                    "shoes", "gloves", "shoulder", "cape", "belt"]

validCheckList = ["Enables the <Decent Haste> skill", "Enables the <Decent Combat Orders> skill", 
                  "Enables the <Decent Advanced Blessing> skill",
                  "Enables the <Decent Mystic Door> skill", "Enables the <Decent Hyper Body> skill", 
                  "Enables the <Decent Speed Infusion> skill", "Enables the <Decent Sharp Eyes> skill", 
                  "Invincible for 3 more seconds after getting attacked", "Ignore Monster DEF : \+\d{0,2}",
                  "\d{0,2}% chance to ignore \d{0,2}% damage when attacked", "\d{0,2}% chance to become invincible for \d{0,2} seconds",
                  "Boss Monster Damage : \+\d{0,2}%", "Item Drop Rate : \+\d{0,2}%"]



tierIdx = {v : i for i, v in enumerate(tierList)}
equipmentIdx = {v : i for i, v in enumerate(equipmentList)}
