
import streamlit as st

# Judul aplikasi
st.title("💰 MoneyMate")
st.write("Plan your money, reach your dreams!")
st.write("Kalkulator Target Tabungan")

st.divider()

# 4 Widget Input
target = st.number_input(
    "Target Tabungan (Rp)",
    min_value=1,
    value=5000000,
    step=100000
)

tabungan_sekarang = st.number_input(
    "Tabungan Saat Ini (Rp)",
    min_value=0,
    value=1000000,
    step=100000
)

tabungan_bulanan = st.number_input(
    "Tabungan Per Bulan (Rp)",
    min_value=0,
    value=500000,
    step=50000
)

waktu = st.number_input(
    "Target Waktu (Bulan)",
    min_value=1,
    value=12,
    step=1
)

# Fungsi buatan sendiri
def hitung_tabungan(target, sekarang, bulanan, waktu):
    kekurangan = target - sekarang

    if kekurangan <= 0:
        kebutuhan = 0
    else:
        kebutuhan = kekurangan / waktu

    estimasi = sekarang + (bulanan * waktu)

    return kebutuhan, estimasi


# Tombol hitung
if st.button("Hitung Tabungan"):

    kebutuhan, estimasi = hitung_tabungan(
        target,
        tabungan_sekarang,
        tabungan_bulanan,
        waktu
    )

    st.divider()
    st.subheader("📊 Hasil Perhitungan")

    # Output menggunakan st.metric
    st.metric(
        "Estimasi Tabungan Akhir",
        f"Rp{estimasi:,.0f}"
    )

    st.metric(
        "Minimal Tabungan Per Bulan",
        f"Rp{kebutuhan:,.0f}"
    )

    # Logika if/else
    if estimasi >= target:
        st.success("🎉 Selamat! Target tabunganmu tercapai.")
    else:
        st.warning("Target belum tercapai. Yuk, tingkatkan tabunganmu!")

    # Progress tabungan
    progress = min(estimasi / target, 1.0)

    st.write("Progress Target Tabungan")
    st.progress(progress)

    st.write(f"Progress: {progress * 100:.1f}%")
