# 🏥 Python Flask Hospital

**Basit bir Hastane Yönetim Mini Uygulaması**  
Kullanıcı girişinden hasta kayıt ve bölüm seçimine, randevu sonucu ekranına kadar temel akışları içerir.

**Demo akışı:** `Giriş → Hasta Kayıt → Bölüm Seçimi → Randevu Sonucu`


## ✨ Özellikler
- 🔐 **Kullanıcı girişi** (login ekranı)
- 👤 **Hasta kayıt** (ad, tc, iletişim vb. form girişi)
- 🏥 **Bölüm seçimi** (poliklinik/bölüm ekranı)
- 🗓️ **Randevu sonucu** (özet ve bilgi ekranı)
- 🧩 **Basit HTML şablonları** ile Flask view entegrasyonu
- 🧪 Demo amaçlı minimal, öğrenmeye uygun kod yapısı


## 🖼️ Ekranlar
- `login.html` — Giriş
- `hastakayıtal.html` — Hasta kayıt formu
- `hastabolumal.html` — Bölüm/poliklinik seçimi
- `randevusonuc.html` — Randevu sonuç özeti

> Not: Şablonlar demo amaçlı düz HTML’dır; Jinja2 templating’e taşınabilir.

## 📂 Dizin Yapısı
```
Python-Flask-Hospital/
├─ views.py                # Flask app ve route'lar
├─ login.html              # Giriş sayfası (demo)
├─ hastakayıtal.html       # Hasta kayıt sayfası (demo)
├─ hastabolumal.html       # Bölüm seçimi sayfası (demo)
├─ randevusonuc.html       # Randevu sonucu sayfası (demo)
└─ README.md               # Bu dosya
```
**Önerilen (ileride):**
```
app/
├─ init.py
├─ routes.py
├─ forms.py
├─ templates/
│ ├─ login.html
│ ├─ register.html
│ ├─ department.html
│ └─ result.html
└─ static/
├─ css/
└─ js/
```

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.10+ (3.12 önerilir)
- `pip` ve (opsiyonel) `venv`

### Kurulum
```bash
# 1) Depoyu kopyala
git clone https://github.com/dilaracelik73/Python-Flask-Hospital.git
cd Python-Flask-Hospital

# 2) Sanal ortam (önerilir)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3) Bağımlılıklar
pip install Flask

# 4) Çalıştırma
# Windows PowerShell
$env:FLASK_APP="views.py"
$env:FLASK_ENV="development"
flask run --port 5000

# macOS/Linux
export FLASK_APP=views.py
export FLASK_ENV=development

```
## 🤝 Katkı

Katkılar memnuniyetle kabul edilir!
- Fork’la
- Branch aç: feature/isim
- Değişikliklerini yap + test et
- PR aç: değişiklik özetini ve nedenini yaz

## 📜 Lisans
MIT © 2025 Dilara Çelik



