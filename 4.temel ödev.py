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
        XA = float(entry_XA.get())
        YA = float(entry_YA.get())
        XB = float(entry_XB.get())
        YB = float(entry_YB.get())
        XC = float(entry_XC.get())
        YC = float(entry_YC.get())
        
        # İki nokta arasındaki açıklığı hesapla
        delx = XA - XB
        dely = YA - YB
        s = sqrt(delx**2 + dely**2)  # Mesafe
        t1 = (2 * atan(dely / (delx - s))) * (200 / pi) + 200  # Açıklık
        
        delx1 = XC - XB
        dely1 = YC - YB
        s1 = sqrt(delx1**2 + dely1**2)  # Mesafe
        t2 = (2 * atan(dely1 / (delx1 - s1))) * (200 / pi) + 200  # Açıklık
        
        dt = t2 - t1
        if dt < 0:
            dt = dt + 400
        if dt >= 0:
            dt = dt
        
        # Sonuçları göster
        result_label.config(text=f"BC Arasındaki Açıklık Açısı: {dt:.3f} gon\nAB Arasındaki Uzunluk: {s:.3f} m\nBC Arasındaki Uzunluk: {s1:.3f} m")
        
    except ValueError:
        # Hata durumunda uyarı mesajı göster
        messagebox.showerror("Geçersiz giriş", "Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        result_label.config(text="Hata: " + str(e))
        
# Ana pencere oluşturma
root = tk.Tk()
root.title("4.Temel Ödev Uygulaması")

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

tk.Label(frame_a, text="XA değeri:").grid(row=0, column=0)
entry_XA = tk.Entry(frame_a)
entry_XA.grid(row=0, column=1)

tk.Label(frame_a, text="YA değeri:").grid(row=1, column=0)
entry_YA = tk.Entry(frame_a)
entry_YA.grid(row=1, column=1)

# B Noktası için girdi alanları
frame_b = tk.LabelFrame(root, text="B Noktası")
frame_b.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame_b, text="XB değeri:").grid(row=0, column=0)
entry_XB = tk.Entry(frame_b)
entry_XB.grid(row=0, column=1)

tk.Label(frame_b, text="YB değeri:").grid(row=1, column=0)
entry_YB = tk.Entry(frame_b)
entry_YB.grid(row=1, column=1)

# C Noktası için girdi alanı
frame_c = tk.LabelFrame(root, text="C Noktası")
frame_c.grid(row=2, column=0, padx=10, pady=10)

tk.Label(frame_c, text="XC değeri:").grid(row=0, column=0)
entry_XC = tk.Entry(frame_c)
entry_XC.grid(row=0, column=1)

tk.Label(frame_c, text="YC değeri:").grid(row=1, column=0)
entry_YC = tk.Entry(frame_c)
entry_YC.grid(row=1, column=1)

# Hesapla düğmesi
calculate_button = tk.Button(root, text="Hesapla", command=hesapla, bg="lightblue")
calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Sonuç etiketi
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10, bg="#F5F5DC", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=4, sticky="ew")

# Ana döngüyü başlat
root.mainloop()