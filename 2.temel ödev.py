# NAZIM HAN TARAFINDAN PROGRAMLANMISTIR

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from math import atan, sqrt, degrees, pi

def get_download_url(file_id):
    return f'https://drive.google.com/uc?export=download&id={file_id}'

def extract_file_id(drive_url):
    file_id = drive_url.split('/d/')[1].split('/')[0]
    return file_id

def download_image_from_drive(drive_url):
    try:
        file_id = extract_file_id(drive_url)
        dwn_url = get_download_url(file_id)
        response = requests.get(dwn_url)
        response.raise_for_status()  # Hata durumunda bir exception fırlatır
        return Image.open(BytesIO(response.content))
    except Exception as e:
        messagebox.showerror("Görsel Yüklenemedi", f"Görsel yüklenirken bir hata oluştu: {e}")
        return None

# Hesaplama fonksiyonu
def hesapla():
    try:
        # Kullanıcı girişlerini al
        xa = float(entry_XA.get())
        ya = float(entry_YA.get())
        xb = float(entry_XB.get())
        yb = float(entry_YB.get())
            
        # İki nokta arasındaki mesafeyi ve açıklığı hesapla
        delx = xb - xa
        dely = yb - ya
        s = sqrt(delx**2 + dely**2)  # Mesafe
        t = (2 * atan(dely / (delx - s))) * (200 / pi) + 200  # Açıklık
        
        # Sonuçları göster
        result_label.config(text=f"İki Nokta Arasındaki Uzunluk (m): S= {s:.3f} m\nİki Nokta Arasındaki Açıklık (gon): t= {t:.3f} gon")
        
    except ValueError:
        # Hata durumunda uyarı mesajı göster
        messagebox.showerror("Geçersiz giriş", "Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        result_label.config(text="Hata: " + str(e))

# Ana pencere oluşturma
root = tk.Tk()
root.title("2.Temel Ödev Uygulaması")

# Google Drive'dan fotoğrafı indir ve göster
drive_url = 'https://drive.google.com/file/d/1dKVUndPmAuKFK1DwfWh8rq9ewT9QOxMD/view?usp=sharing'
image = download_image_from_drive(drive_url)
photo = ImageTk.PhotoImage(image)

# Fotoğrafı bir etiket içinde göster
image_label = tk.Label(root, image=photo)
image_label.image = photo  # Referansı kaybetmemek için
image_label.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

# A Noktası için girdi alanı
frame_a = tk.LabelFrame(root, text="A Noktası")
frame_a.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_a, text="XA değeri:").grid(row=0, column=0)
entry_XA = tk.Entry(frame_a)
entry_XA.grid(row=0, column=1)

tk.Label(frame_a, text="YA değeri:").grid(row=1, column=0)
entry_YA = tk.Entry(frame_a)
entry_YA.grid(row=1, column=1)

# B Noktası için girdi alanları
frame_params = tk.LabelFrame(root, text="B Noktası")
frame_params.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame_params, text="XB değeri:").grid(row=0, column=0)
entry_XB = tk.Entry(frame_params)
entry_XB.grid(row=0, column=1)

tk.Label(frame_params, text="YB değeri:").grid(row=1, column=0)
entry_YB = tk.Entry(frame_params)
entry_YB.grid(row=1, column=1)

# Hesapla düğmesi
calculate_button = tk.Button(root, text="Hesapla", command=hesapla, bg="lightblue")
calculate_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Sonuç etiketi
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10, bg="#F5F5DC", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=4, sticky="ew")

# Ana döngüyü başlat
root.mainloop()
