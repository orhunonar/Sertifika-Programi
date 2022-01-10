from PIL import Image, ImageFont, ImageDraw
import csv


isim=input(".csv uzantılı dosyanın adını giriniz. Örnek : isimler.csv  ")
sertifika=input("sertifika şablonunun adını giriniz. Örnek : sertifika.jpg  ")
font_size=int(input("Fon büyüklüğünü giriniz. Önerilen :30  "))
koordinat_x=int(input("Yazılacak ismin merkezinin x düzleminde koordinatını giriniz. Örnek :450  "))
koordinat_y=int(input("Yazılacak ismin merkezinin y düzleminde koordinatını giriniz. Örnek :330  "))
renk=int(input("Karakter rengi beyazsa 255, siyahsa 0 olarak giriniz.  "))




with open("Dosyalar/"+isim) as f:
    reader = csv.reader(f)
    data = list(reader)


for i in range(0,len(data)):
    my_image = Image.open("Dosyalar/"+sertifika)
    font = ImageFont.truetype("Dosyalar/arial.ttf", font_size)
    draw=ImageDraw.Draw(my_image)
    title_text = str(data[i])
    gereksizler="[']"
    w, h = draw.textsize(title_text, font)
    # print(w)
    for i in gereksizler:
        title_text=title_text.replace(i,"")
        #print(title_text)
    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((koordinat_x-w/2,koordinat_y), title_text,(renk, renk, renk), font=font)
    my_image.save("Sertifikalar/"+title_text+".jpg")
print("Bitti")
