import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import subprocess

def run_script1():
    subprocess.run(["python", "1.temel ödev.py"])

def run_script2():
    subprocess.run(["python", "2.temel ödev.py"])

def run_script3():
    subprocess.run(["python", "3.temel ödev.py"])

def run_script4():
    subprocess.run(["python", "4.temel ödev.py"])

# Fonksiyon: Verilen URL'den resmi indirip Image nesnesi olarak döndürmek
def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    # Resmi LANCZOS filtresiyle yeniden boyutlandır
    image = image.resize((200, 200), Image.LANCZOS)
    return image

# Ana pencere oluşturma
root = tk.Tk()
root.title("Temel Ödev Uygulamaları")

# Resmi indir ve tkinter için ImageTk.PhotoImage nesnesine dönüştür
image_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/Y%C4%B1ld%C4%B1z_Technical_University_Logo.png"
image = download_image(image_url)
photo = ImageTk.PhotoImage(image)

# Resmi bir etiket içinde göster
image_label = tk.Label(root, image=photo)
image_label.image = photo  # Referansı kaybetmemek için
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
