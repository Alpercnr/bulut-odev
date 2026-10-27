from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba Bulut Bilişim - Kararlı Sürüm (v1)"

# Sağlık kontrolü (Health Check) yaptığımız adres burası!
@app.route('/health')
def health():
    # BİLEREK BOZUYORUZ: Sistem çöktü simülasyonu
    return "ERROR: Veritabanı bağlantısı koptu!", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
