import time

while True:  # 👈 Oyunu baştan başlatma döngüsü
    can = 100
    envanter = []

    print("Merhaba")
    isim = input("Adın ne? ")
    print("Tanıştığıma memnun oldum " + isim + "!")
    time.sleep(3)

    yaş = int(input("Kaç yaşındasın? "))

    if yaş < 10:
        print("Senin yaşına göre bu oyun biraz zor olabilir ama sakın hemen pes etme!")
    elif yaş <= 14:
        print("Tam senlik bir oyuna benziyor!")
    elif yaş <= 60:
        print("Bu oyun sana kolay gelecektir!")
    else:
        print("Sen hala mezara gitmedin mi ya?")
    time.sleep(2)

    print("Hadi oyuna başlayalım!")
    time.sleep(2)
    print("Dur bir saniye!")
    time.sleep(1)

    while True:
        cevap = input("Hazır mısın? (evet/hayır): ").lower()
        if cevap == "evet":
            print("Harika! O zaman başlıyoruz!")
            time.sleep(2)
            break
        elif cevap == "hayır":
            print("Tamam, bekliyorum. Hazır olunca tekrar söyle.")
            time.sleep(2)
        else:
            print("Lütfen sadece 'evet' veya 'hayır' yaz.")

    print("Bir ormanın içindesin. Her yer sessiz...")
    time.sleep(2)

    print("4 yön var: sağ - sol - ileri - geri")
    yön = input("Hangi yöne gitmek istersin? ").lower()

    if yön == "sağ":
        print("Sağa doğru gittin... Bir mağara buldun!")
        print("Mağaraya girdin... İçerisi karanlık ve sessiz.")
        time.sleep(2)
        print("Aniden bir ses duydun! Bir yaratık sana doğru geliyor!")
        time.sleep(2)

        karar = input("Savaşmak mı istersin yoksa kaçmak mı? (savaş/kaç): ").lower()

        while karar not in ["savaş", "kaç"]:
            karar = input("Lütfen sadece 'savaş' ya da 'kaç' yaz: ").lower()

        if karar == "savaş":
            print("Cesurca yaratığa saldırdın!")
            time.sleep(2)

            if "kalkan" in envanter:
                print("Kalkanını kullandın, sadece 10 hasar aldın!")
                can -= 10
            else:
                print("Yaratık seni pençeledi! 30 hasar aldın!")
                can -= 30

            print(f"Kalan canın: {can}")

            if can <= 0:
                print("Yaratık seni ağır yaraladı... Gözlerin kararıyor... 💀")
                print("Oyun bitti.")
                tekrar = input("Tekrar oynamak ister misin? (evet/hayır): ").lower()
                if tekrar != "evet":
                    print("Görüşmek üzere!")
                    break
                else:
                    continue
            else:
                print("Ama sonunda yaratığı yendin! 🎉")
                print("Yaratıktan bir kalkan buldun!")
                envanter.append("kalkan")
        else:
            print("Hızlıca mağaradan kaçtın ve ormanda kayboldun...")

    elif yön == "sol":
        print("Sola doğru gittin... Karşında büyük bir nehir var!")
        time.sleep(1)
        print("Nehri geçmek için iki seçeneğin var:")
        time.sleep(1)
        print("- Yüzerek karşıya geç (yüz)")
        print("- Nehir kenarından yürü (yürü)")

        secim = input("Ne yapacaksın? (yüz/yürü): ").lower()

        while secim not in ["yüz", "yürü"]:
            secim = input("Lütfen sadece 'yüz' ya da 'yürü' yaz: ").lower()

        if secim == "yüz":
            print("Cesurca suya atladın ve yüzmeye başladın...")
            time.sleep(2)
            print("Orta noktaya geldiğinde akıntı güçlendi!")
            time.sleep(2)
            print("Ama sonunda karşı kıyıya ulaşmayı başardın! 🎉")
        else:
            print("Nehir kenarından yürümeye başladın.")
            time.sleep(2)

        print("Kıyıda eski bir sandık buldun.")
        time.sleep(2)
        aç = input("Sandığı açmak ister misin? (evet/hayır): ").lower()

        while aç not in ["evet", "hayır"]:
            aç = input("Lütfen sadece 'evet' ya da 'hayır' yaz: ").lower()

        if aç == "evet":
            print("Sandığı açtın ve içinden altınlar çıktı! Zenginsin artık! 💰")
            envanter.append("altın")
        else:
            print("Sandığı açmadın. Belki içinde bir tuzak vardı...")

    elif yön == "ileri":
        print("İleri gittin... Bir hazine sandığı buldun!")
        time.sleep(2)
        print("Sandığı dikkatlice açtın... İçinden gizemli bir iksir çıktı! 🍷")
        envanter.append("iksir")
        kullan = input("İksiri içmek ister misin? (evet/hayır): ").lower()

        while kullan not in ["evet", "hayır"]:
            kullan = input("Lütfen sadece 'evet' ya da 'hayır' yaz: ").lower()

        if kullan == "evet":
            print("İksiri içtin... Canın 20 arttı!")
            can += 20
            print(f"Yeni can: {can}")
        else:
            print("İksiri envanterine koydun.")

    elif yön == "geri":
        print("Geri döndün... Başladığın yere geldin.")
        time.sleep(1)
        print("Ormanın girişindeki tahtadan kulübeyi fark ettin.")
        print("İçeri girdin ve eski bir defter buldun.")
        envanter.append("eski defter")

    else:
        print("Geçerli bir yön yazmadın. Ormanda kayboldun...")

    # 👇 Oyun sonu özeti ve tekrar sorusu
    print("\n--- OYUN BİTTİ ---")
    print(f"Kalan can: {can}")
    print("Envanterin:", ", ".join(envanter) if envanter else "boş")

    tekrar = input("\nTekrar oynamak ister misin? (evet/hayır): ").lower()
    if tekrar != "evet":
        print("Görüşmek üzere!")
        break
