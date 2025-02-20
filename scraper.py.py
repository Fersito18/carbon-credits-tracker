import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from datetime import datetime

def setup_database():
    conn = sqlite3.connect('carbon_credits.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bonos (
            id INTEGER PRIMARY KEY,
            proyecto TEXT,
            comprador TEXT,
            tipo TEXT,
            precio_usd REAL,
            fecha DATE,
            certificadora TEXT,
            pais TEXT
        )
    ''')
    conn.commit()
    conn.close()

def scrape_verra():
    url = "https://registry.verra.org/app/search/VCS/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        proyectos = []
        # Extraer datos y guardar en la base de datos...
        print("Datos guardados exitosamente!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    setup_database()
    scrape_verra()