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
    file_id = extract_file_id(drive_url)
    dwn_url = get_download_url(file_id)
    response = requests.get(dwn_url)
    return Image.open(BytesIO(response.content))

# Hesaplama fonksiyonu
def hesapla():
    try:
        # Kullanıcı girişlerini al
        t1 = float(entry1.get())
        b = float(entry2.get())
        
        dt = t1 + b
        if dt < 200:
            dt = dt + 200
        elif 600 >= dt >= 200:
            dt = dt - 200
        elif dt >= 600:
            dt = dt - 600
        
        # Sonuçları göster
        result_label.config(text="BC Arasındaki Açıklık Açısı: t2= {:.3f} gon".format(dt))
        
    except ValueError:
        # Hata durumunda uyarı mesajı göster
        messagebox.showerror("Geçersiz giriş", "Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        result_label.config(text="Hata: " + str(e))

# Ana pencere oluşturma
root = tk.Tk()
root.title("3.Temel Ödev Uygulaması")

# Google Drive'dan fotoğrafı indir ve göster
drive_url = 'https://drive.google.com/file/d/1NGrBlX9WpiQ84-Aar8lJjBWceLCD1YNQ/view?usp=drive_link'
image = download_image_from_drive(drive_url)
photo = ImageTk.PhotoImage(image)

# Fotoğrafı bir etiket içinde göster
image_label = tk.Label(root, image=photo)
image_label.image = photo  # Referansı kaybetmemek için
image_label.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

# A Noktası için girdi alanı
frame_a = tk.LabelFrame(root, text="A Noktası")
frame_a.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_a, text="(AB) açıklık açısı:").grid(row=0, column=0)
entry1 = tk.Entry(frame_a)
entry1.grid(row=0, column=1)

# B Noktası için girdi alanları
frame_params = tk.LabelFrame(root, text="B Noktası")
frame_params.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame_params, text="Kırılma açısı:").grid(row=0, column=0)
entry2 = tk.Entry(frame_params)
entry2.grid(row=0, column=1)

# Hesapla düğmesi
calculate_button = tk.Button(root, text="Hesapla", command=hesapla, bg="lightblue")
calculate_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Sonuç etiketi
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10, bg="#F5F5DC", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=4, sticky="ew")

# Ana döngüyü başlat
root.mainloop()