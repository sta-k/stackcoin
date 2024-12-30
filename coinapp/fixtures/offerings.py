from coinapp.models import Offering, Category,User, Exchange

def load_offerings():
    exch,_ =Exchange.objects.get_or_create(
        code='KKDE',
        title='Kolakkode Exchange'
    )
    user,_ = User.objects.get_or_create(username='7356775981',first_name='suhail',exchange=exch)
    user.set_password('sumee1910')
    user.save()
    offerings = [
        ["Food_Drink", "rice", "Matta rice", "50$ per kg"],
        ["Food_Drink", "coconut", "Thenga. Coconut for chutney and curry.", "20$ per piece"],
        ["Food_Drink", "egg", "Egg recipies per piece", "8$ per piece"],
        ["Food_Drink", "brinjal", "Vazhuthanangal, per kg","20$ per kg"],
        ["Food_Drink", "mulak_podi", "Mulaku podi per 100gram", "40$ per 100grams"],
        ["Food_Drink", "salt", "uppu per kg", "20$ per kg"],
        ["Electronics", "earphone", "Earphone", "800$ per piece"],
        ["Electronics", "mp3_player", "MP3 Player for listening songs", "5000$ per piece"],
        ["Electronics", "solarpanel", "Solar panel", "2000$ per piece"],
        ["Clothing_Apparel", "underwear", "UnderWear", "200$ per piece"],
        ["Clothing_Apparel", "tracksuit", "Track suit pants", "600$ per piece"],
        ["Clothing_Apparel", "tshirt", "Tshirt", "300$ per piece"],
        ["Accommodation_Space", "land", "25 meter/sq land", "50000$ per cent"],
        ["Accommodation_Space", "room_rent", "Room rent/month", "5000$ per month"]
    ]
    
    for o in offerings:
        cat = Category.objects.get(name=o[0])
        result = Offering.objects.update_or_create(
            user = user,
            category=cat,
            heading=o[1],        
            defaults={"detail":o[2],"rate":o[3]}
        )
        if result[1]:
            print('created offering',result)
        
def a():
    print(Offering.objects.count())

load_offerings()
a()