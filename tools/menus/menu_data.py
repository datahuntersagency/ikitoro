# Content for the two new menus, from "Iki toro Drink Menu 09-26.docx" and
# "Spirts List 9-26.docx". Items struck through in the Word files are omitted.
# Item: (name, italic suffix, description, [prices...])

COCKTAILS = [
    ("Lychee Love Potion Martini", "", "Haku Vodka, floral, exotic and sweet.", [20]),
    ("Black Pearl Espresso Martini", "", "Haku Vodka, rich espresso with coconut cream.", [18]),
    ("Kyoto Breeze Lemongrass Martini", "", "Roku Gin, bright and crisp with yuzu.", [21]),
    ("Rising Sun Spritz", "", "Roku Gin, Mio Crisp sparkling sake, yuzu, Aperol.", [20]),
    ("Japanese Candy Shop", "", "Serrano-infused tequila, passion fruit, cucumber.", [19]),
    ("Ube Old Fashioned", "", "Toki Whisky, velvety purple yam and toasted oak.", [22]),
    ("Hokkaido Highball", "", "Toki Whisky, clean, crisp and refreshingly chilled.", [22]),
    ("Suntory Sour", "", "Toki Whisky with a tart yuzu finish.", [22]),
]

MOCKTAILS = [
    ("Shiso No-Jito", "", "Basil, mint and lime.", [14]),
    ("Tokyo Drifter", "", "Zesty and punchy with citrus elements.", [14]),
    ("Bonsai Mule", "", "Cucumber and ginger with citrus.", [14]),
]

SAKE_GLASS = [
    ("Hot Sake", "Premium · 300 ml", "", [18]),
    ("House Sake", "Premium", "", [14]),
    ("Premium Sake Flight", "3 × 70 ml", "", [22]),
]

# prices: [300 ml, 720 ml]  (None = not offered in that size)
SAKE_BOTTLES = [
    ("Born", "Dreams Come True · 1000 ml", "", [None, 450]),
    ("Dassai 23", "Junmai Daiginjo", "Rice polished to 23%, with delicate floral aromas and a clean finish.", [75, 150]),
    ("Dassai 45", "Junmai Daiginjo", "Smooth, with subtle white peach and green apple.", [35, 65]),
    ("Hakkaisan Dodgers", "Junmai Daiginjo", "Special-edition sake with a pristine, clean, dry profile.", [None, 80]),
    ("Hakushika Sennenju", "Junmai Daiginjo", "Rich and complex, with rice and soft melon notes.", [35, 80]),
    ("KEN Sword", "Daiginjo", "Top-tier handcrafted sake with a rich aroma and crisp finish.", [None, 220]),
    ("Kikusui Blue", "Junmai Ginjo", "Light and crisp, with subtle cantaloupe and citrus.", [None, 65]),
    ("Kikusui", "Junmai Daiginjo", "Smooth, luxurious and slightly sweet, with floral highlights.", [None, 75]),
    ("Kubota Manjyu", "Junmai Daiginjo", "Deeply complex, with a velvety texture and refined finish.", [None, 80]),
    ("Kubota Senjyu", "Junmai Ginjo", "Crisp, dry and versatile with a wide range of dishes.", [None, 70]),
    ("Michinoku Onikoroshi", "Honjozo Dry", "The “Demon Slayer”: dry, with a rich, bold character.", [None, 60]),
    ("Nanbu Bijin", "Tokubetsu Junmai", "Rich and savory, with balanced acidity and deep rice flavor.", [None, 75]),
    ("Shirakabegura", "Junmai Daiginjo", "Delicately fragrant, with soft fruit and a silky mouthfeel.", [None, 135]),
    ("Shirakabegura Matured Kimoto", "Junmai 2017", "Traditional brewing with earthy, complex, savory depth.", [None, 145]),
    ("Shirakabegura Yamahai", "Junmai 10 Year", "Decade-aged, amber, with deep umami and nutty highlights.", [None, 180]),
    ("Mio Crisp", "Sparkling Sake", "Refreshing, effervescent and fruity, with a low ABV.", [25, 50]),
    ("Nigori Sayuri", "Unfiltered", "Sweet and velvety, with light floral tones.", [25, 60]),
]

# prices: [glass, bottle]
WINE_SPARKLING = [
    ("Pommery Brut Royal", "Champagne, France", "Elegant, with fine bubbles and green apple brightness.", [None, 130]),
    ("Moët Impérial", "Champagne, France · 187 ml", "", [None, 29]),
    ("Louis Roederer Cristal 2013", "Champagne, France", "Prestige cuvée with intense citrus and mineral complexity.", [None, 1000]),
]
WINE_WHITE = [
    ("Roc de l’Abbaye Sauvignon Blanc 2024", "Val de Loire, France", "Crisp, with vibrant acidity and citrus.", [15, 55]),
    ("Hess Chardonnay, Shirttail Ranches", "Monterey, California", "Crisp pear, apple and subtle oak.", [14, 50]),
    ("Wagner-Stempel Weissburgunder", "Pinot Blanc, Germany", "Delicate florals, peach and clean minerality.", [16, 60]),
    ("La Chablisienne Chablis 2023", "Burgundy, France", "Unoaked Chardonnay, pure citrus and steely mineral.", [None, 65]),
    ("Louis Latour Montagny 2023", "La Grande Roche Premier Cru, France", "", [None, 100]),
]
WINE_RED = [
    ("The Hess Collection Allomi 2022", "Cabernet Sauvignon, Napa", "Dark fruit, blackberry and vanilla; structured.", [18, 85]),
    ("Renzo Seghesio Barolo 2018", "Ca’ d’Nalin, Italy", "Full-bodied Nebbiolo: dried cherry, spice, leather.", [None, 125]),
    ("Pascal Jolivet Attitude Pinot Noir", "Loire, France", "Light and fruit-forward, with cherry and subtle earth.", [None, 70]),
]
WINE_FRUIT = [
    ("Choya Umeshu", "Plum wine", "", [12, 45]),
    ("Takara Plum Rosé", "", "", [14, None]),
]

BEER_12 = [("Kirin Ichiban", "", "", [9]), ("Sapporo Light", "", "", [9]), ("Echigo Flying IPA", "", "", [10])]
BEER_22 = [("Sapporo", "", "", [12]), ("Sapporo Black", "", "", [12]), ("Asahi", "", "", [12]), ("Orion", "", "", [12])]

TEA = [
    ("Iced Ceremonial Matcha", "", "", [7]),
    ("Iced Matcha Latte", "", "", [9]),
    ("Iced Vanilla Matcha Latte", "", "", [9]),
    ("Matcha Latte", "", "", [9]),
    ("Tea Pot", "small / large", "Green tea, ceremonial matcha, oolong or jasmine.", ["9 / 13"]),
]

SOFT = [
    ("Coca-Cola", "355 ml", "", [6]), ("Diet Coke", "250 ml", "", [5]), ("Sprite", "355 ml", "", [6]),
    ("Evian", "750 ml", "", [9]), ("Evian Sparkling", "750 ml", "", [9]), ("Seasonal Lemonade", "", "", [9]),
    ("Yuzu Lemonade", "", "", [9]), ("Matcha Palmer", "", "", [9]), ("Calpico", "", "", [9]),
    ("Calpico Passionfruit", "", "", [9]), ("Calpico Lychee", "", "", [9]),
]

# ---------------- SPIRITS ----------------
WHISKY = [
    ("Akashi White Oak", "", "Sweet malt, subtle oak and a clean, smooth vanilla finish.", [28]),
    ("The Fujisan", "", "Blended with spring water from Mt. Fuji; smoky, rich spice, caramel and cherry.", [23]),
    ("Hakushu 12", "Suntory", "Vibrant herbal, lightly smoky malt with green apple and crisp pine.", [38]),
    ("Hakushu 18", "Suntory", "Deeply complex herbal single malt with ripe pear, jasmine and gentle peat.", [120]),
    ("Hatozaki Finest", "", "Light, sweet blend with orchard fruit, cereal and soft honey.", [23]),
    ("Hatozaki Small Batch", "", "Pure malt with rich spice, oak depth and dried fruit.", [33]),
    ("Hatozaki 12 Year", "", "Umeshu-cask aged, with a layered, fruit-forward finish and subtle tannins.", [38]),
    ("Hibiki Harmony", "Suntory", "Elegant blend with floral aromas, orange peel and white chocolate.", [28]),
    ("Hibiki 12 Year", "Suntory · Extra Rare", "Plum-wine-cask blend with honeyed citrus and spicy oak.", [110]),
    ("Hibiki 21 Year", "Suntory", "Opulent blend with dried fruit, dark chocolate and long mizunara spice.", [180]),
    ("Kaigan Blend", "", "Maritime style with soft smoke, sea salt and gentle malt sweetness.", [29]),
    ("Kikori Rice Whiskey", "", "100% rice whisky with a light, floral and smooth profile.", [18]),
    ("Kujira", "", "Okinawa rice whisky with toasted grain, light vanilla and soft fruit.", [28]),
    ("Kujira 5 Year", "", "White-oak aged, with caramel, wood spice and a velvety mouthfeel.", [38]),
    ("Maen", "", "Artisan blend with honey, citrus and toasted oak.", [28]),
    ("Mars 45", "", "High-proof blend with bright fruit and bold spice.", [20]),
    ("Mars Iwai Tradition", "", "Rich, malt-driven whisky with cherry, honey and subtle peat.", [25]),
    ("Mars Kisoyama", "", "Balanced, with ripe fruit, baking spice and smooth oak.", [30]),
    ("Mars Kisoyama Yuhi", "", "Ripe orchard fruit, honeyed malt and soft oak.", [38]),
    ("Nikka Coffey", "", "Grain whisky with tropical fruit, vanilla and chocolate.", [33]),
    ("Nikka Days", "", "Vibrant blend with delicate florals and fresh apple sweetness.", [28]),
    ("Nikka Yoichi", "", "Coastal single malt with salinity, bold peat and rich smoke.", [34]),
    ("Sentaru Classic Reserve 10 Year", "", "Aged single grain with vanilla, toasted nut and oak.", [33]),
    ("Shunka Shuto", "Spring · Summer · Autumn · Winter", "A seasonal series balancing fruit, wood and spice.", [28]),
    ("Tenjaku Blended", "", "Soft blend with cereal, pear and sweet spice.", [28]),
    ("Tenjaku Pure Malt", "", "100% malt with green apple, butterscotch and gentle wood.", [38]),
    ("The Shin Malt 10 Year", "", "Mizunara-finished pure malt with sweet spice, sandalwood and citrus zest.", [28]),
    ("The Shinobu 10 Year", "", "Mizunara-aged, with vanilla, nutmeg and aromatic wood.", [39]),
    ("Toki", "Suntory", "Refreshing highball blend with green apple, grapefruit and thyme.", [19]),
    ("Toki Black", "Suntory", "A deeper expression with extra oak richness and rounded spice.", [23]),
    ("Yamato Honda Tadakatsu", "", "Aged in mizunara oak; toasted honeycomb, vanilla and subtle licorice.", [39]),
    ("Yamazaki Blend", "Suntory", "Balanced expression highlighting berry fruit and oak.", [29]),
    ("Yamazaki 12", "Suntory", "Flagship single malt with peach, pineapple, clove and mizunara oak.", [38]),
    ("Yamazaki 18", "Suntory", "Deeply aged single malt with dark chocolate, dried fruit and wood incense.", [120]),
    ("Yamazakura Single Malt", "Sasakawa", "Light and sweet malt, crisp, with soft honey.", [33]),
]

TEQUILA = [
    ("Clase Azul Gold", "", "Ultra-premium blend with extra añejo; hazelnut, dried fruit and toasted oak.", [70]),
    ("Clase Azul Reposado", "", "Aged in American whiskey casks; smooth vanilla, candied orange peel.", [35]),
    ("Don Julio 1942", "Extra", "Velvety, with rich caramel, toasted oak and a vanilla finish.", [35]),
    ("Don Julio Añejo", "", "18 months in white oak; cooked agave, wild honey and warm spice.", [24]),
    ("Don Julio 70 Cristalino", "", "Charcoal-filtered añejo; bright agave, rich vanilla and oak.", [24]),
    ("Don Julio Reposado", "", "Eight months in white oak; citrus, dark chocolate, light cinnamon.", [18]),
    ("Lalo Blanco", "", "Additive-free Blue Weber agave, citrus zest and clean minerality.", [18]),
    ("House Tequila", "", "Crisp, clean agave spirit for sipping or classic cocktails.", [16]),
    ("Verde Amaras", "Mezcal", "Artisanal Espadín with balanced smoke, sweet grass and citrus.", [18]),
    ("Xicaru", "Mezcal", "Small batch; roasted agave, gentle smoke and earthy pepper.", [17]),
]

COGNAC = [
    ("Hennessy Paradis", "25 ml", "Over 100 rare eaux-de-vie; jasmine, candied fruit, cinnamon and a silky finish.", [120]),
    ("Hennessy XO", "", "Dark chocolate, candied citrus, warm leather and baking spice.", [46]),
    ("Remy Martin XO", "", "Fine Champagne cognac with passion fruit, ripe fig and floral honey.", [46]),
    ("Iki Toro House Blend XO Extra", "", "Our house blend, aged to XO minimum with cognacs up to 50 years old.", [35]),
    ("Hennessy VSOP", "", "Candied fruit, delicate clove spice and toasted oak.", [19]),
    ("Remy Martin 1738", "Accord Royal", "Aged in toasted oak, with butterscotch and subtle spice.", [19]),
    ("Tesseron VSOP", "", "Grande and Petite Champagne; floral aromas, dried fruit, delicate oak.", [19]),
]

WHITE_SPIRITS = [
    ("Belvedere", "Vodka", "Polish rye with a velvety texture, vanilla creaminess and a clean pepper finish.", [22]),
    ("Haku", "Vodka", "Japanese white-rice vodka filtered through bamboo charcoal; soft and smooth.", [17]),
    ("Nikka", "Vodka", "Coffey-still vodka with a rich mouthfeel and subtle grain sweetness.", [16]),
    ("Roku", "Gin", "Japanese botanicals: sakura, green tea, yuzu peel and sansho pepper.", [18]),
    ("Nikka", "Gin", "Japanese gin with yuzu, kabosu, amanatsu and sansho pepper.", [16]),
    ("Bacardi", "Rum", "Classic light rum with smooth vanilla, subtle florals and clean sweetness.", [16]),
    ("Takara", "", "Traditional Japanese spirit, light and clean, with subtle rice sweetness.", [16]),
]
