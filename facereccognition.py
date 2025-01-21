# Step 1: Import cv2 nya
import cv2

# Step 2: Siapkan alat deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Membaca kamera
cap = cv2.VideoCapture(0)

# Cek kamera
if not cap.isOpened():
    print("Kamera kamu tidak bisa diakses!")
    exit()

# Step 4: Mulai baca video dan deteksi wajah
while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame!")
        continue

    # Membalik frame secara horizontal (mirror effect)
    frame = cv2.flip(frame, 1)

    # Step 5: Deteksi wajah
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 70))

    for (x, y, w, h) in faces:
        horizontal_padding = 20  # Padding horizontal lebih kecil
        vertical_padding = 10    # Padding vertikal lebih kecil

        x = x - horizontal_padding
        y = y - vertical_padding
        w = w + horizontal_padding * 2
        h = h + vertical_padding * 2

        # Membuat kotak biru di sekitar wajah dengan ketebalan lebih tebal
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Kotak biru dengan ketebalan 3

    # Step 6: Tampilkan output program
    cv2.imshow('Deteksi Wajah dengan Kotak Biru', frame)

    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

# Lepaskan sumber daya
cap.release()
cv2.destroyAllWindows()
