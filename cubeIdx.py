cubeList = ["bright", "glowing"]
rankList = ["rare", "epic", "unique", "legendary"]
equipmentList = ["weapon", "emblem", "secondary", "hat", "eye", "face", "earings", "belt", "top", "bottom", "overall"
                    "shoes", "gloves", "shoulder", "cape"]

validCheckList = ["Enables the <Decent Haste> skill", "Enables the <Decent Combat Orders> skill", "Enables the <Decent Advanced Blessing> skill",
                  "Enables the <Decent Mystic Door> skill", "Enables the <Decent Hyper Body> skill", 
                  "Enables the <Decent Speed Infusion> skill", "Enables the <Decent Sharp Eyes> skill", 
                  "Invincible for 3 more seconds after getting attacked", "Ignore Monster DEF : \+\d{0,2}",
                  "\d{0,2}% chance to ignore \d{0,2}% damage when attacked", "\d{0,2}% chance to become invincible for \d{0,2} seconds",
                  "Boss Monster Damage : \+\d{0,2}%", "Item Drop Rate : \+\d{0,2}%"]

rankIdx = {v : i for i, v in enumerate(rankList)}
equipmentIdx = {v : i for i, v in enumerate(equipmentList)}
