import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source , duration= 2)
    print("Sesiniz tanımlanıyor..")
    text = r.recognize_google(data, language='tr')
    araci_yazdir = open("C:\\Users\\Reyhan Duygu\\Desktop\\PROJELER\\TEKNOFEST 2022\\yazdir.txt", "w")
    text = text.lower()
    araci_yazdir.write(text)
    print(text)
