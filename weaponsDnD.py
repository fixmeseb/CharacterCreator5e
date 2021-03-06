club = ["Club", 0.1, "1d4 bludgeoning", "Light", False]
dagger = ["Dagger", 2, "1d4 piercing", "Finesse, light, thrown (range 20/60)", False]
greatclub = ["Greatclub", 0.2, "1d8 bludgeoning", "Two-handed", False]
handaxe = ["Handaxe", 5, "1d6 slashing", "Light, thrown (range 20/60)", False]
javelin = ["Javelin", 0.5, "1d6 piercing", "Thrown (range 30/120)", False]
lighthammer = ["Light Hammer", 2, "1d4 bludgeoning", "Light, thrown (range 20/60)", False]
mace = ["Mace", 5, "1d6 bludgeoning", "", False]
quarterstaff = ["Quarterstaff", 0.2, "1d6 bludgeoning", "Versatile (1d8)", False]
sickle = ["Sickle", 1, "1d4 slshing", "Light", False]
spear = ["Spear", 1, "1d6 piercing", "Thrown (range 20/60), versatile (1d8)", False]

crossbowLight = ["Light Crossbow", 25, "1d8 piercing", "Ammunition (range 80/320), loading, two-handed", False]
dart = ["Dart", 0.05, "1d4 piercing", "Finesse, thrown (range 20/60)", False]
shortbow = ["Shortbow", 25, "1d6 piercing", "Ammunition (range 80/320), two-handed", False]
sling = ["Sling", 0.1, "1d4 bludgeoning", "Ammunition (range 30/120)", False]

simpleMelee = [club, dagger, greatclub, handaxe, javelin, lighthammer, mace, quarterstaff, sickle, spear]
simpleRanged = [crossbowLight, dart, shortbow, sling]

battleaxe = ["Battleaxe", 10, "1d8 slashing", "Versatile (1d10)", False]
flail = ["Flail", 10, "1d8 bludgeoning", "", False]
glaive = ["Glaive", 20, "1d10 slashing", "Heavy, reach, two-handed", False]
greataxe = ["Greataxe", 30, "1d12 slashing", "Heavy, two-handed", False]
greatsword = ["Greatsword", 50, "2d6 slashing", "Heavy, two-handed", False]
halberd = ["Halberd", 20, "1d10 slashing", "Heavy, reach, two-handed", False]
lance = ["Lance", 10, "1d12 piercing", "Reach, special", False]
longsword = ["Longsword", 15, "1d8 slashing", "Versatile (1d10)", False]
maul = ["Maul", 10, "2d6 bludgeoning", "Heavy, two-handed", False]
morningstar = ["Morningstar", 15, "1d8 piercing", "", False]
pike = ["Pike", 5, "1d10 piercing", "Heavy, reach, two-handed", False]
rapier = ["Rapier", 25, "1d8 piercing", "Finesse", False]
scimitar = ["Scimitar", 25, "1d6 slashing", "Finesse, light", False]
shortsword = ["Shortsword", 10, "1d6 piercing", "Finesse, light", False]
trident = ["Trident", 5, "1d6 piercing", "Thrown (range 20/60), versatile (1d8)", False]
warpick = ["War pick", 5, "1d8 piercing", "", False]
warhammer = ["Warhammer", 15, "1d8 bludgeoning", "Versatile (1d10)", False]
whip = ["Whip", 2, "1d4 slashing", "Finesse, reach", False]

blowgun = ["Blowgun", 10, "1 piercing", "Ammunition (range 25/100), loading", False]
handcrossbow = ["Hand Crossbow", 75, "1d6 piercing", "Ammunition (range 30/120), light, loading", False]
heavycrossbow = ["Heavy Crossbow", 50, "1d10 piercing", "Ammunition (range 100/400), heavy, loading, two-handed", False]
longbow = ["Longbow", 50, "1d8 piercing", "Ammunition (range 150/600), heavy, two-handed", False]
net = ["Net", 1, "", "Special, thrown (range 5/15)", False]

martialMelee = [battleaxe, flail, glaive, greataxe, greatsword, halberd, lance, longsword, maul, morningstar, pike, rapier, scimitar, shortsword, trident, warpick, warhammer, whip]
martialRanged = [blowgun, handcrossbow, heavycrossbow, longbow, net]

martialWeapons = [martialMelee, martialRanged]
simpleWeapons = [simpleMelee, simpleRanged]
weapons = [simpleWeapons, martialWeapons]