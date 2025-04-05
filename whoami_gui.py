import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import datetime
import os
import psutil
import pystray
from PIL import Image

LOG_PATH = "logs/anon-log.txt"

# -------------------------- FUNGSI STATUS --------------------------
def is_vpn_active():
    return "tun0" in [iface.name for iface in psutil.net_if_addrs().values()]

def is_tor_running():
    for p in psutil.process_iter(['name']):
        if 'tor' in p.info['name'].lower():
            return True
    return False

def update_status():
    vpn = "Aktif" if is_vpn_active() else "Tidak Aktif"
    tor = "Aktif" if is_tor_running() else "Tidak Aktif"
    vpn_status.set(f"VPN: {vpn}")
    tor_status.set(f"Tor: {tor}")

# -------------------------- FUNGSI ANON --------------------------
def start_anon():
    subprocess.call(['kali-whoami', 'start'])
    log("Anon mode started")
    update_status()

def stop_anon():
    subprocess.call(['kali-whoami', 'stop'])
    log("Anon mode stopped")
    update_status()

def log(msg):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

def export_log():
    messagebox.showinfo("Log", f"Log tersimpan di:\n{os.path.abspath(LOG_PATH)}")

# -------------------------- SYSTEM TRAY --------------------------
def create_tray_icon():
    image = Image.open("assets/icon.png") if os.path.exists("assets/icon.png") else Image.new("RGB", (64, 64), "black")
    menu = pystray.Menu(
        pystray.MenuItem("Buka GUI", lambda: root.deiconify()),
        pystray.MenuItem("Keluar", lambda: (icon.stop(), root.quit()))
    )
    global icon
    icon = pystray.Icon("whoami", image, "Kali Whoami", menu)
    icon.run()

# -------------------------- GUI UTAMA --------------------------
root = tk.Tk()
root.title("Kali Whoami GUI")
root.configure(bg="#1e1e1e")

# Tema gelap
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#333", padding=6)
style.configure("TLabel", foreground="white", background="#1e1e1e")

# Status indikator
vpn_status = tk.StringVar()
tor_status = tk.StringVar()
update_status()

ttk.Label(root, textvariable=vpn_status).pack(pady=5)
ttk.Label(root, textvariable=tor_status).pack(pady=5)

ttk.Button(root, text="Start Anon Mode", command=start_anon).pack(pady=5)
ttk.Button(root, text="Stop Anon Mode", command=stop_anon).pack(pady=5)
ttk.Button(root, text="Export Log", command=export_log).pack(pady=5)

# Tombol minimize ke tray
ttk.Button(root, text="Minimize to Tray", command=lambda: (root.withdraw(), create_tray_icon())).pack(pady=10)

root.geometry("300x250")
root.mainloop()
``