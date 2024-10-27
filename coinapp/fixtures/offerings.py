from coinapp.models import Offering
offerings = [
    ["Food", "rice", "Matta rice", 50],
    ["Food", "coconut", "Thenga. Coconut for chutney and curry.", 20],
    ["Food", "egg", "Egg recipies per piece", 1],
    ["Food", "brinjal", "Vazhuthanangal, per kg", 1],
    ["Food", "mulak_podi", "Mulaku podi per 100gram", 2],
    ["Food", "salt", "uppu per kg", 1],
    ["Water", "drinking_water", "Drinking water", 0],
    ["Water", "non_drinking_water", "Non drinking water", 0],
    ["Electronics", "earphone", "Earphone", 100],
    ["Electronics", "mp3_player", "MP3 Player for listening songs", 500],
    ["Electronics", "solarpanel", "Solar panel", 100],
    ["Clothing", "underwear", "UnderWear", 20],
    ["Clothing", "tracksuit", "Track suit pants", 50],
    ["Clothing", "tshirt", "Tshirt", 30],
    ["Shelter", "land", "25 meter/sq land", 5000],
    ["Shelter", "room_rent", "Room rent/month", 500]
]
for o in offerings:
    result = Offering.objects.get_or_create(
        heading=o[1],
        category=o[0],
        defaults={"detail":o[2],"amount":o[3]}
    )
    print(result)