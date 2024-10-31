from coinapp.models import Offering, UserOffering, User
def load_offerings():
    offerings = [
        ["Food", "rice", "Matta rice", "50$ per kg"],
        ["Food", "coconut", "Thenga. Coconut for chutney and curry.", "20$ per piece"],
        ["Food", "egg", "Egg recipies per piece", "8$ per piece"],
        ["Food", "brinjal", "Vazhuthanangal, per kg","20$ per kg"],
        ["Food", "mulak_podi", "Mulaku podi per 100gram", "40$ per 100grams"],
        ["Food", "salt", "uppu per kg", "20$ per kg"],
        ["Electronics", "earphone", "Earphone", "800$ per piece"],
        ["Electronics", "mp3_player", "MP3 Player for listening songs", "5000$ per piece"],
        ["Electronics", "solarpanel", "Solar panel", "2000$ per piece"],
        ["Clothing", "underwear", "UnderWear", "200$ per piece"],
        ["Clothing", "tracksuit", "Track suit pants", "600$ per piece"],
        ["Clothing", "tshirt", "Tshirt", "300$ per piece"],
        ["Shelter", "land", "25 meter/sq land", "50000$ per cent"],
        ["Shelter", "room_rent", "Room rent/month", "5000$ per month"]
    ]

    for o in offerings:
        result = Offering.objects.update_or_create(
            category=o[0],
            heading=o[1],        
            defaults={"detail":o[2]}
        )
        if result[1]:
            print('created offering',result)
        user = User.objects.filter(username='7356775981').first()
        if not user:
            user = User.objects.create_user(username='7356775981',password='sumee1910',first_name='suhail vs')
        result = UserOffering.objects.update_or_create(
            offering = result[0],
            user = user,
            rate = o[3]
        )
        if result[1]:
            print('created user offering',result)
        

def a():
    print(Offering.objects.count())

load_offerings()
a()