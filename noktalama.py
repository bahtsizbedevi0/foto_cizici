import cv2
import numpy as np
import os

base_path = "C:/Users/musta/Desktop/Projeler/Rastgele Şeyler/Şekiller/Fotolar"


isim = input("🖼️ Görselin ismini gir : ").strip()
uzanti = input("📁 Görselin uzantısını gir : ").strip().lower()


img_path = os.path.join(base_path, f"{isim}.{uzanti}")


img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 40, 100) #100, 200   40, 100

points = np.column_stack(np.where(edges.transpose() > 0))


points = points * 0.5

center = points.mean(axis=0)
points = points - center

np.save("foto.npy", points)
print("✅ Noktalar kaydedildi.")
