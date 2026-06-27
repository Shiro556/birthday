from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

# Route utama untuk nampilin website ulang tahun
@app.route('/')
def home():
    return render_template('index.html')

# Route khusus biar Flask bisa ngebaca file gambar bg.png dan lagu.mp3 di folder utama
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    # Menjalankan server Flask di port 5000
    app.run(debug=True, port=5000)
