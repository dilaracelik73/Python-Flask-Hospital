from flask import Flask , render_template, redirect,url_for,request, make_response,session
from.session_interface import MySessionInterface,SessionInterface
# flask import edildi. Ardından da HTMLiçin render_template import edildi.
# redirect admin isim kontrolü için import edildi.

app=Flask(__name__)
app.secret_key =b"?039eruif3__"
app.session_interface= MySessionInterface()
hasta_bolum=None

@app.route("/", methods=['POST' ,'GET' ])
def Login():
    if request.method=='POST':
        global hasta_bolum
        hasta_bolum = request.form["hasta_bolum"]
        return redirect(url_for("HastaBolumAl", name=hasta_bolum))
    else:
        return render_template("login.html")

@app.route("/hastabolum/<name>")
def HastaBolumAl(name):
    global hasta_bolum
    if request.method=="POST":
        name=request.form["name"]
        return redirect(url_for("HastaKayıtAl",bolum_gelen=name.title()))
    else:
        return render_template("hastabolumal.html", bolum_gelen=name.upper())


@app.route("/hastakayıt",methods=['POST' ,'GET' ])
def HastaKayıtAl():
    if request.method=="GET":
        return redirect(url_for("RandevuSonuc"))
    else:
        return render_template("hastakayıtal.html")

@app.route("/randevusonuc", methods=["POST"])
def RandevuSonuc():
    global hasta_bolum

    if hasta_bolum == "Ağız, Çene ve Diş Sağlığı":
        hasta_durum = "Muayene Oda:1 Saat:13.45"
    elif hasta_bolum == "Beslenme ve Diyet":
        hasta_durum = "Muayene Oda:2 Saat:14.00"
    elif hasta_bolum == "Çocuk Hastalıkları":
        hasta_durum = "Muayene Oda:3 Saat:14.30"
    elif hasta_bolum == "Plastik Cerrahi":
        hasta_durum = "Muayene Oda:4 Saat:15.00"
    elif hasta_bolum == "Göz Hastalıkları":
        hasta_durum = "Muayene Oda:5 Saat:15.30"
    elif hasta_bolum == "Kardiyoloji":
        hasta_durum = "Muayene Oda:6 Saat:14.45"
    elif hasta_bolum == "Nöroloji":
        hasta_durum = "Muayene Oda:7 Saat:16.00"
    elif hasta_bolum == "Psikoloji":
        hasta_durum = "Muayene Oda:8 Saat:16.30"


    hasta_adı = request.form["hasta_adı"]
    hasta_soyadı=request.form["hasta_soyadı"]
    adres=request.form["adres"]
    tckimlik = int(request.form["tckimlik"])
    telefon = int(request.form["telefon"])
    yasınız= int(request.form["yasınız"])


    if yasınız<18 :
        yas_durum = "cocuk hasta"
    elif yasınız>18 and yasınız<30:
        yas_durum="genç hasta"
    elif yasınız > 30 and yasınız <65:
        yas_durum = "orta yaşlı hasta"
    else :
        yas_durum="65 yaş üstü hasta"


    return render_template("randevusonuc.html",hasta_bolum=hasta_bolum, hasta_adı=hasta_adı,hasta_soyadı=hasta_soyadı,
                           adres=adres, tckimlik=tckimlik,
                           telefon=telefon,yasınız=yasınız, yas_durum=yas_durum,hasta_durum=hasta_durum)









