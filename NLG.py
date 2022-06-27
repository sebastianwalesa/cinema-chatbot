import random

unknown = ['Nie rozumiem. Proszę o powtórzenie.',
          'Czy możesz powiedzieć to innymi słowami?',
          "Nie wiem co masz na myśli",
           "Czy możesz powiedzieć to w inny sposób, proszę?"]

bye =  ["Trzymaj się!",
         "Na razie!",
        "Do zobaczenia później!",
         "Do zobaczenia",
        "Pogadamy później!"
       ]



def nlg(query,frame,text):
    if frame['act'] == "hello":
        print("Witamy w systemie rezerwacji biletów kinowych. W czym mogę pomóc?")
    if frame['act'] == "repertuar":
        print("Aktualnie repertuar zawiera takie filmy jak: \"Batman\" \"Ambulans\" \"Bunkier strachu\" \"Córka\" \"Uncharted\" \"Inni ludzie\" \"Śmierć na Nilu\" \"Skarb Mikołajka\"")
    
    if frame['act'] == 'null':
        if text == 'reset':
            print("Resetowanie dialogu.")
        if text == "exit":
            print('Dziękujemy za skorzystanie z naszych usług!')
        elif text != "reset":
            print(random.choice(unknown))
    
    if frame['act'] == "numer":
        if len(text) != 9 and len(text) >= 3:
            print("Proszę podać poprawny numer telefonu.")
        elif query == None:
            print("Rezerwacja została dokonana. Potwierdzenie rezerwacji wraz z numerem miejsc zostanie niebawem przesłane wiadomością SMS.") 
            print("Proszę o przybycie 15 minut przed rozpoczęciem seansu w celu zakupu biletu, w innym przypadku rezerwacja przepada.\n")
            print("==================================================================================================================\n")
            print("Zachęcamy do wypełnienia ankiety :)\n")
            
            import matplotlib.pyplot as plt
            import matplotlib.image as mpimg
            img = mpimg.imread('QRCode dla System do rezerwacji biletów kinowych.png')
            imgplot = plt.imshow(img)
            imgplot.axes.get_xaxis().set_visible(False)
            imgplot.axes.get_yaxis().set_visible(False)
            plt.show()

    if frame['act'] == "bye" :
        print(random.choice(bye))
        
    if frame['act'] == "cancel":
        print("W celu anulacji biletów prosimy o wysłanie SMS na numer, z którego przyszło potwierdzenie rezerwacji z wiadomością \"ANULUJ\".")

        
    if frame['act'] == "zapytanie":
        print("Po więcej szczegółów zapraszamy na stronę internetową.")
    
    if frame['act'] == "seanse":
        print("Seanse odbywają się w godzinach: 15:30, 17:15 oraz 20")
        
#     if frame['act'] != "hello" and frame['act'] != "null" and :
    if frame['act'] not in ['hello','bye','null',"seanse",'zapytanie',"cancel"]:
        if query == "miejsce":
            print("Czy miejsca mają być z przodu, z tyłu czy na środku?")
        if query == "numer":
            print("Na jaki numer telefonu ma zostać dokonana rezerwacja?")
        if query == 'dzien':
            print("Na który dzień ma być dokonana rezerwacja?")
        if query == 'godzina':
            print("Na którą godzinę ma być dokonana rezerwacja?")
        if query == 'ilosc':
            print("Ile biletów ma zostać zarezerwowanych?")
        if query == 'tytul':
            print("Na jaki film ma zostać dokonana rezerwacja?")
            

            

