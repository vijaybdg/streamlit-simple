import streamlit as st
import datetime

# --- Data Pasangan ---
NAMA_SUAMI = "Fikri"
NAMA_ISTRI = "Inna"
ANNIV_TAHUN = 20

def anniv_app(nama1, nama2, tahun_ke):
    """Aplikasi Streamlit untuk ucapan ulang tahun pernikahan."""
    
    # Konfigurasi Halaman Browser
    st.set_page_config(
        page_title=f"Happy {tahun_ke}th Anniversary!",
        layout="wide",
        # Gunakan ikon hati untuk judul tab browser
        initial_sidebar_state="collapsed"
    )
    
    # 🎆 Efek Visual: Balon dan Kembang Api
    st.balloons()
    st.snow() # Efek salju, bisa diubah jadi confetti jika mau
    
    # --- Konten Utama ---
    
    st.markdown("<h1 style='text-align: center; color: #ff66b2;'>💖 Happy Wedding Anniversary! 💖</h1>", 
                unsafe_allow_html=True)
    
    st.markdown(f"<h2 style='text-align: center;'>Perayaan Cinta ke-{tahun_ke} Tahun</h2>", 
                unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Bagian Nama Pasangan dengan font besar
    st.markdown(f"""
    <div style='text-align: center; margin: 30px 0;'>
        <h1 style='color: #4CAF50; font-size: 5em;'>**{nama1}** & **{nama2}**</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Bagian Metrik atau Fakta
    tahun_saat_ini = datetime.date.today().year
    tahun_mulai = tahun_saat_ini - tahun_ke
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Menghitung durasi tahun
        st.metric(
            label="Durasi Bersama (Tahun)", 
            value=tahun_ke, 
            delta="20 Tahun Kesetiaan"
        )
        
    with col2:
        # Tahun Mulai
        st.metric(
            label="Mulai Sejak Tahun", 
            value=str(tahun_mulai), 
            delta="Perjalanan Cinta Dimulai"
        )

    with col3:
        # Pesan Spesial
        st.metric(
            label="Pencapaian", 
            value="Indah", 
            delta="Cinta Sejati"
        )

    st.markdown("---")
    
    # Pesan Manis
    st.markdown("""
    <div style='text-align: center; padding: 20px; border: 2px solid #ff66b2; border-radius: 10px; background-color: #fff0f5;'>
        <p style='font-size: 1.2em; color: #333;'>
            Dua puluh tahun adalah bukti nyata dari cinta yang kuat dan tak tergoyahkan.
            Semoga kalian terus menjadi inspirasi bagi banyak pasangan,
            dan semoga kebahagiaan selalu mengisi rumah tangga kalian!
        </p>
        <br>
        <p style='font-weight: bold; font-style: italic; color: #ff66b2;'>
            ~ Love always prevails ~
        </p>
    </div>
    """, unsafe_allow_html=True)

# Jalankan Aplikasi
if __name__ == '__main__':
    anniv_app(NAMA_SUAMI, NAMA_ISTRI, ANNIV_TAHUN)