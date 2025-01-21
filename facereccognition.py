# Mengimpor library yang diperlukan
import cv2  # Untuk operasi pemrosesan gambar dan video
import signal  # Untuk menangani sinyal sistem seperti CTRL + C
import sys  # Untuk operasi sistem, seperti keluar dari program

# Fungsi untuk menangani penghentian program menggunakan CTRL + C
def signal_handler(sig, frame):
    print("\nProgram dihentikan dengan CTRL + C.")  # Pesan saat program dihentikan
    cap.release()  # Melepaskan kamera
    cv2.destroyAllWindows()  # Menutup semua jendela OpenCV
    sys.exit(0)  # Keluar dari program dengan status 0

# Menghubungkan sinyal CTRL + C ke fungsi handler
signal.signal(signal.SIGINT, signal_handler)

# Step 2: Memuat model deteksi wajah dari OpenCV (Haar Cascade Classifier)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Membuka kamera untuk menangkap video
cap = cv2.VideoCapture(0)  # Membuka kamera default (0 adalah ID kamera pertama)

# Cek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Kamera kamu tidak bisa diakses!")  # Pesan error jika kamera tidak terbuka
    exit()  # Keluar dari program

# Step 4: Membaca video dari kamera dan mendeteksi wajah dalam loop
while True:
    ret, frame = cap.read()  # Membaca frame dari kamera
    if not ret:
        print("Gagal membaca frame!")  # Pesan error jika gagal membaca frame
        continue  # Lanjutkan ke iterasi berikutnya

    # Membalik frame secara horizontal (efek cermin)
    frame = cv2.flip(frame, 1)

    # Step 5: Deteksi wajah dalam frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Mengonversi frame ke grayscale
    # Mendeteksi wajah dalam gambar grayscale
    faces = face_cascade.detectMultiScale(
        gray,              # Gambar grayscale
        scaleFactor=1.1,   # Faktor skala untuk mengecilkan gambar saat mendeteksi
        minNeighbors=5,    # Jumlah tetangga minimum untuk mendeteksi wajah
        minSize=(50, 70)   # Ukuran minimum untuk mendeteksi wajah
    )

    # Loop melalui semua wajah yang terdeteksi
    for (x, y, w, h) in faces:
        horizontal_padding = 20  # Tambahan lebar di sisi kiri dan kanan kotak
        vertical_padding = 10    # Tambahan tinggi di sisi atas dan bawah kotak

        # Menambahkan padding ke koordinat kotak wajah
        x = x - horizontal_padding
        y = y - vertical_padding
        w = w + horizontal_padding * 2
        h = h + vertical_padding * 2

        # Membuat kotak biru di sekitar wajah yang terdeteksi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Warna biru (BGR) dan ketebalan 3

    # Step 6: Menampilkan frame dengan kotak wajah
    cv2.imshow('Deteksi Wajah dengan Kotak Biru', frame)

    # Tekan tombol 'q' untuk keluar dari loop
    if cv2.waitKey(1) == ord('q'):
        print("\nProgram dihentikan dengan tombol 'q'.")  # Pesan penghentian dengan 'q'
        break

# Melepaskan sumber daya setelah loop selesai
cap.release()  # Melepaskan kamera
cv2.destroyAllWindows()  # Menutup semua jendela OpenCV
