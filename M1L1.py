memes = {
            "CREEPY": "Korku verici, ürpertici.",
            "LOL": "Komik bir söyleme veya fiile verilen bir ifade, cevap.",
            "AGGRO": "Bir şeye karşı sinirlenmek, tepki göstermek.",
            "ROFL": "Yapılan bir espiri veya şakaya karşılık cevap vermek.",
            "CRINGE": "Yapılan utandırıcı veya yüz kızartıcı bir davranış."
}

while True:
    meme = input("Bildiğiniz bir meme yazınız(büyük harflerle):")
    
    if meme in memes.keys():
        print("Anlamı:", memes[meme])
        
    else:
        print("Bu sözlükte böyle bir kelime bulunmamaktadır.")
