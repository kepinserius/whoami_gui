# 🔐 Kali-Whoami GUI (Python + Tkinter)

Versi antarmuka grafis (GUI) dari tool [kali-whoami](https://gitlab.com/kalilinux/packages/kali-whoami), dibuat menggunakan Python + Tkinter. Tool ini mempermudah pengelolaan anonimitas pengguna di Kali Linux melalui tampilan sederhana dan fitur tambahan yang tidak ada di versi CLI.

---

## ✨ Fitur Utama

- ✅ **Tombol Start/Stop** untuk mengaktifkan dan menonaktifkan `kali-whoami`
- 🟢 **Indikator Status**:
  - Status **VPN aktif/tidak**
  - Status **Tor aktif/tidak**
- 🌑 **Tema Gelap (Dark Mode)**
- 💾 **Export Log Aktivitas** (catat status anonimitas ke file teks)
- 📥 **Integrasi System Tray**:
  - Minimalkan ke tray
  - Menu tray: Show Window, Exit

---

## 📦 Dependency / Requirements

Jalankan perintah berikut untuk menginstal semua paket Python yang dibutuhkan:

```bash
sudo apt install python3 python3-tk python3-psutil python3-pystray python3-pil

```bash
git clone https://github.com/username/kali-whoami-gui.git
```bash
cd kali-whoami-gui

Pastikan tool kali-whoami sudah terinstal:

1. Jalankan "kali-whoami start" di terminal
2. Jika belum ada, install dari repositori aslinya atau source Makefile

```bash
python3 whoami_gui.py


