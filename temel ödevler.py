import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import os

# Mevcut dizini belirle
current_directory = os.path.dirname(os.path.abspath(__file__))

def run_script1():
    script_path = os.path.join(current_directory, "1.temel ödev.py")
    subprocess.run(["python", script_path])

def run_script2():
    script_path = os.path.join(current_directory, "2.temel ödev.py")
    subprocess.run(["python", script_path])

def run_script3():
    script_path = os.path.join(current_directory, "3.temel ödev.py")
    subprocess.run(["python", script_path])

def run_script4():
    script_path = os.path.join(current_directory, "4.temel ödev.py")
    subprocess.run(["python", script_path])

# Fonksiyon: Verilen URL'den resmi indirip Image nesnesi olarak döndürmek
def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP isteğinin başarılı olup olmadığını kontrol et
        image = Image.open(BytesIO(response.content))
        # Resmi LANCZOS filtresiyle yeniden boyutlandır
        image = image.resize((200, 200), Image.LANCZOS)
        return image
    except requests.RequestException as e:
        print(f"HTTP isteği başarısız: {e}")
    except UnidentifiedImageError as e:
        print(f"Görüntü tanınamadı: {e}")

# Ana pencere oluşturma
root = tk.Tk()
root.title("Temel Ödev Uygulamaları")

# Resmi indir ve tkinter için ImageTk.PhotoImage nesnesine dönüştür
image_url = "https://www.yildiz.edu.tr/sites/default/files/2024-02/yildiz-teknik-universitesi-logo-diket-turkce-.png"
image = download_image(image_url)
if image:
    photo = ImageTk.PhotoImage(image)

    # Resmi bir etiket içinde göster
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Referansı kaybetmemek için
    image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)
else:
    image_label = tk.Label(root, text="Resim yüklenemedi", font=("Helvetica", 12, "italic"))
    image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

# "Nazım Han tarafından programlanmıştır" yazısı
author_label = tk.Label(root, text="Nazım Han tarafından programlanmıştır", font=("Helvetica", 12, "italic"))
author_label.grid(row=5, column=0, padx=10, pady=10)

# Script1 butonu
button1 = tk.Button(root, text="1.TEMEL ÖDEV", command=run_script1, bg="lightblue", font=("Helvetica", 12))
button1.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

# Script2 butonu
button2 = tk.Button(root, text="2.TEMEL ÖDEV", command=run_script2, bg="lightblue", font=("Helvetica", 12))
button2.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Script3 butonu
button3 = tk.Button(root, text="3.TEMEL ÖDEV", command=run_script3, bg="lightblue", font=("Helvetica", 12))
button3.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Script4 butonu
button4 = tk.Button(root, text="4.TEMEL ÖDEV", command=run_script4, bg="lightblue", font=("Helvetica", 12))
button4.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

# Ana döngüyü başlatma
root.mainloop()
