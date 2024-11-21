from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Konfigurasi koneksi database (ganti kredensial MySQL sesuai kebutuhan)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/myflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi database dan migrasi
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes dari file routes.py (pastikan file ini ada)
from routes import *

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
