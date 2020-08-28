club = ["Club", 0.1, "1d4 bludgeoning", "Light"]
dagger = ["Dagger", 2, "1d4 piercing", "Finesse, light, thrown (range 20/60)"]
greatclub = ["Greatclub", 0.2, "1d8 bludgeoning", "Two-handed"]
handaxe = ["Handaxe", 5, "1d6 slashing", "Light, thrown (range 20/60)"]
javelin = ["Javelin", 0.5, "1d6 piercing", "Thrown (range 30/120)"]
lighthammer = ["Light Hammer", 2, "1d4 bludgeoning", "Light, thrown (range 20/60)"]
mace = ["Mace", 5, "1d6 bludgeoning", ""]
quarterstaff = ["Quarterstaff", 0.2, "1d6 bludgeoning", "Versatile (1d8)"]
sickle = ["Sickle", 1, "1d4 slshing", "Light"]
spear = ["Spear", 1, "1d6 piercing", "Thrown (range 20/60), versatile (1d8)"]

crossbowLight = ["Light Crossbow", 25, "1d8 piercing", "Ammunition (range 80/320), loading, two-handed"]
dart = ["Dart", 0.05, "1d4 piercing", "Finesse, thrown (range 20/60)"]
shortbow = ["Shortbow", 25, "1d6 piercing", "Ammunition (range 80/320), two-handed"]
sling = ["Sling", 0.1, "1d4 bludgeoning", "Ammunition (range 30/120)"]

simpleMelee = {club: False, dagger: False, greatclub: False, handaxe: False, javelin: False, lighthammer: False, mace: False, quarterstaff: False, sickle: False, spear: False}
simpleRanged = {crossbowLight: False, dart: False, shortbow: False, sling: False}
simpleWeapons = {simpleMelee: False, simpleRanged: False}

battleaxe = ["Battleaxe", 10, "1d8 slashing", "Versatile (1d10)"]
flail = ["Flail", 10, "1d8 bludgeoning", ""]
glaive = ["Glaive", 20, "1d10 slashing", "Heavy, reach, two-handed"]
greataxe = ["Greataxe", 30, "1d12 slashing", "Heavy, two-handed"]
greatsword = ["Greatsword", 50, "2d6 slashing", "Heavy, two-handed"]
halberd = ["Halberd", 20, "1d10 slashing", "Heavy, reach, two-handed"]
lance = ["Lance", 10, "1d12 piercing", "Reach, special"]
longsword = ["Longsword", 15, "1d8 slashing", "Versatile (1d10)"]
maul = ["Maul", 10, "2d6 bludgeoning", "Heavy, two-handed"]
morningstar = ["Morningstar", 15, "1d8 piercing", ""]
pike = ["Pike", 5, "1d10 piercing", "Heavy, reach, two-handed"]
rapier = ["Rapier", 25, "1d8 piercing", "Finesse"]
scimitar = ["Scimitar", 25, "1d6 slashing", "Finesse, light"]
shortsword = ["Shortsword", 10, "1d6 piercing", "Finesse, light"]
trident = ["Trident", 5, "1d6 piercing", "Thrown (range 20/60), versatile (1d8)"]
warpick = ["War pick", 5, "1d8 piercing", ""]
warhammer = ["Warhammer", 15, "1d8 bludgeoning", "Versatile (1d10)"]
whip = ["Whip", 2, "1d4 slashing", "Finesse, reach"]

blowgun = ["Blowgun", 10, "1 piercing", "Ammunition (range 25/100), loading"]
handcrossbow = ["Hand Crossbow", 75, "1d6 piercing", "Ammunition (range 30/120), light, loading"]
heavycrossbow = ["Heavy Crossbow", 50, "1d10 piercing", "Ammunition (range 100/400), heavy, loading, two-handed"]
longbow = ["Longbow", 50, "1d8 piercing", "Ammunition (range 150/600), heavy, two-handed"]
net = ["Net", 1, "", "Special, thrown (range 5/15)"]

martialMelee = {battleaxe: False, flail: False, glaive: False, greataxe: False, greatsword: False, halberd: False, lance: False, longsword: False, maul: False, morningstar: False, pike: False, rapier: False, scimitar: False, shortsword: False, trident: False, warpick: False, warhammer: False, whip: False}
martialRanged = {blowgun: False, handcrossbow: False, heavycrossbow: False, longbow: False, net: False}
martialWeapons = {martialMelee: False, martialRanged: False}

weapons = {simpleWeapons: False, martialWeapons: False}
