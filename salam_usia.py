import streamlit as st
import datetime

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Aplikasi Sederhana",
    layout="centered"
)

# --- Judul dan Deskripsi ---
st.title("👋 Kalkulator Usia Sederhana")
st.write("Masukkan nama Anda dan tahun lahir untuk melihat hasilnya.")

# --- Bagian Input Pengguna ---

# Input Nama
nama = st.text_input("Masukkan Nama Anda:")

# Input Tahun Lahir
# Gunakan slider untuk membatasi input pada tahun yang masuk akal
tahun_saat_ini = datetime.date.today().year
tahun_lahir = st.slider(
    "Pilih Tahun Lahir Anda:",
    min_value=1900,
    max_value=tahun_saat_ini,
    value=2000 # Nilai default
)

# Tombol untuk memproses input
if st.button("Hitung Usia"):
    # Cek apakah nama sudah diisi
    if nama:
        # --- Bagian Logika ---
        usia = tahun_saat_ini - tahun_lahir
        
        # --- Bagian Output ---
        st.success(f"Halo, **{nama}**!")
        
        if usia >= 0:
            st.info(f"Anda lahir pada tahun {tahun_lahir}. Saat ini, Anda berusia **{usia}** tahun.")
        else:
            st.error("Tahun lahir tidak valid.")
    else:
        st.warning("Mohon masukkan nama Anda terlebih dahulu.")

st.markdown("---")
st.caption("Dibuat dengan Python dan Streamlit.")