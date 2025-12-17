import random
from datetime import datetime, timedelta

# ============================================================
# Dynamic Stack Implementation
# ============================================================

class DynamicStack:
    def __init__(self, name="Stack"):
        self.stack = []
        self.name = name

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def clear(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def show(self):
        print(f"\n=== {self.name.upper()} ===")
        if self.is_empty():
            print("Kosong.")
        else:
            for item in reversed(self.stack):
                print(item)
        print("=========================\n")


# ============================================================
# Fungsi Pembuat Transaksi & Fitur Tambahan
# ============================================================

def buat_transaksi(jenis, jumlah, status, pihak_terkait, provinsi, kota, daerah, keterangan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"[{waktu}] | {jenis.upper()} | Rp {jumlah:,} | {status}\n"
        f"Pihak terkait: {pihak_terkait}\n"
        f"Lokasi: {daerah}, {kota}, {provinsi}\n"
        f"Keterangan: {keterangan}"
    )

def buat_id_transaksi():
    waktu = datetime.now().strftime("%Y%m%d%H%M%S")
    random_num = random.randint(100, 999)
    return f"TX-{waktu}-{random_num}"

def kategori_pengeluaran(keterangan):
    ket = keterangan.lower()
    if "listrik" in ket: return "Tagihan"
    if "supermarket" in ket: return "Belanja"
    if "motor" in ket: return "Cicilan"
    if "restoran" in ket: return "Makanan & Minuman"
    if "pulsa" in ket: return "Telekomunikasi"
    if "internet" in ket: return "Internet"
    if "obat" in ket: return "Kesehatan"
    if "transportasi" in ket: return "Transportasi"
    return "Lainnya"

def kategori_pemasukan():
    return "Top Up / Setoran"


# ============================================================
# Detail Pihak Terkait (Merchant / Pemasukan)
# ============================================================

merchant_detail = {
    "Membayar listrik": ("PLN", "Tagihan Listrik", "Virtual Account"),
    "Belanja di supermarket": ("Indomaret", "Retail", "Debit Card"),
    "Bayar cicilan motor": ("FIF Group", "Pembiayaan", "Auto Debit"),
    "Makan di restoran": ("Solaria", "Restoran", "QRIS"),
    "Beli pulsa": ("Telkomsel", "Telekomunikasi", "Mobile Banking"),
    "Bayar internet": ("Indihome", "Internet Provider", "Virtual Account"),
    "Beli pakaian": ("Zara", "Fashion Retail", "Debit Card"),
    "Beli obat di apotek": ("Kimia Farma", "Apotek", "QRIS"),
    "Transportasi online": ("Gojek", "Transportasi", "E-Wallet"),
    "Perbaikan rumah": ("Tukang Bangunan", "Jasa", "Transfer Bank")
}

pemasukan_detail = {
    "ATM BCA": ("ATM BCA", "Setoran Tunai", "Mesin ATM"),
    "ATM Mandiri": ("ATM Mandiri", "Setoran Tunai", "Mesin ATM"),
    "ATM BRI": ("ATM BRI", "Setoran Tunai", "Mesin ATM"),
    "ATM Bersama": ("ATM Bersama", "Transfer Antar Bank", "ATM Bersama"),
    "Setoran Tunai di Bank": ("Teller Bank", "Setoran Tunai", "Teller"),
    "Teller Bank BNI": ("Teller BNI", "Setoran Tunai", "Teller"),
    "Mobile Banking": ("Mobile Banking", "Top Up", "Aplikasi Mobile"),
    "Internet Banking": ("Internet Banking", "Top Up", "Aplikasi Web")
}

# ============================================================
# Helper Data
# ============================================================

def random_date(start_year=1960, end_year=2010):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

provinsi_list = [
    "Sumatera Selatan", "DKI Jakarta", "Jawa Barat", "Jawa Timur",
    "Bali", "Sulawesi Selatan", "Sumatera Utara", "DI Yogyakarta"
]

kota_list = [
    "Palembang", "Jakarta", "Bandung", "Surabaya",
    "Denpasar", "Makassar", "Medan", "Yogyakarta"
]

daerah_list = [
    "Sukarami", "Kemuning", "Ilir Timur", "Ilir Barat",
    "Kuta Alam", "Tegalrejo", "Cicendo", "Cibeunying"
]

pengeluaran_keterangan = list(merchant_detail.keys())
lokasi_pemasukan = list(pemasukan_detail.keys())

first_names = ["Andi", "Budi", "Citra", "Dewi", "Eka", "Fajar", "Gita", "Hadi", "Indra", "Joko",
               "Kiki", "Lina", "Maya", "Nina", "Oki", "Putra", "Putri", "Rama", "Sari", "Tono"]
last_names = ["Saputra", "Wijaya", "Pratama", "Siregar", "Hutabarat", "Gunawan", "Santoso", "Mahendra", "Kusuma", "Wibowo"]

# ============================================================
# Generate Dataset 100 Orang
# ============================================================

dataset = []

for _ in range(100):
    birthdate = random_date()
    age = datetime.now().year - birthdate.year

    person = {
        "nama": random.choice(first_names) + " " + random.choice(last_names),
        "umur": age,
        "tanggal_lahir": birthdate.strftime("%d-%m-%Y"),
        "lokasi": random.choice(kota_list),

        "saldo_bank": random.randint(1_000_000, 100_000_000),

        "pemasukan_terakhir": random.randint(1_000_000, 20_000_000),
        "lokasi_pemasukan": random.choice(lokasi_pemasukan),
        "provinsi_pemasukan": random.choice(provinsi_list),
        "kota_pemasukan": random.choice(kota_list),
        "daerah_pemasukan": random.choice(daerah_list),

        "pengeluaran_terakhir": random.randint(500_000, 15_000_000),
        "keterangan_pengeluaran": random.choice(pengeluaran_keterangan),
        "provinsi_pengeluaran": random.choice(provinsi_list),
        "kota_pengeluaran": random.choice(kota_list),
        "daerah_pengeluaran": random.choice(daerah_list)
    }

    dataset.append(person)

# ============================================================
# Stacks
# ============================================================

activity_stack          = DynamicStack("Riwayat Aktivitas")
transaction_stack       = DynamicStack("Riwayat Transaksi (Semua)")
last_transactions_stack = DynamicStack("Transaksi Terakhir")
undo_stack              = DynamicStack("Stack Undo")
location_stack          = DynamicStack("Stack Lokasi Terakhir")
navigation_stack        = DynamicStack("Stack Navigasi Menu")

# ============================================================
# Main Program
# ============================================================

while True:
    navigation_stack.push("Menu Utama")

    print("\n=== DATA NASABAH BANK ===")
    for i, person in enumerate(dataset):
        print(f"{i+1}. {person['nama']}")

    try:
        pilihan = int(input("\nPilih nomor nasabah (1-100), atau 0 untuk keluar: "))
    except ValueError:
        print("Input tidak valid.")
        continue

    if pilihan == 0:
        print("Keluar dari program.")
        break

    if 1 <= pilihan <= 100:
        orang = dataset[pilihan - 1]

        print("\n=== DATA PRIBADI ===")
        print(f"Nama            : {orang['nama']}")
        print(f"Umur            : {orang['umur']}")
        print(f"Tanggal Lahir   : {orang['tanggal_lahir']}")
        print(f"Lokasi          : {orang['lokasi']}")

        while True:
            print("\n=== MENU KEUANGAN ===")
            print("1. Informasi Saldo")
            print("2. Detail Pemasukan")
            print("3. Detail Pengeluaran")
            print("4. Riwayat Transaksi Terakhir")
            print("5. Kembali")

            try:
                opsi = int(input("Pilih opsi: "))
            except ValueError:
                print("Input tidak valid.")
                continue

            # ========================================================
            # OPSI 1: SALDO
            # ========================================================

            if opsi == 1:
                print("\n=== INFORMASI SALDO ===")
                print(f"Saldo Bank Saat Ini: Rp {orang['saldo_bank']:,}")

                transaksi = buat_transaksi(
                    jenis="Cek Saldo",
                    jumlah=orang["saldo_bank"],
                    status="Berhasil",
                    pihak_terkait=orang["nama"],
                    provinsi="-",
                    kota=orang["lokasi"],
                    daerah="-",
                    keterangan="Pengecekan saldo"
                )

                last_transactions_stack.push(transaksi)
                if len(last_transactions_stack.stack) > 5:
                    last_transactions_stack.stack.pop(0)

            # ========================================================
            # OPSI 2: PEMASUKAN
            # ========================================================

            elif opsi == 2:
                print("\n=== DETAIL PEMASUKAN ===")

                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                jumlah = orang["pemasukan_terakhir"]
                jenis = "Top Up"
                status = "Berhasil"

                pihak = orang["lokasi_pemasukan"]
                pihak_nama, pihak_jenis, pihak_metode = pemasukan_detail[pihak]

                kategori = kategori_pemasukan()
                id_transaksi = buat_id_transaksi()

                saldo_awal = orang["saldo_bank"]
                saldo_akhir = saldo_awal + jumlah
                orang["saldo_bank"] = saldo_akhir

                print(f"ID Transaksi  : {id_transaksi}")
                print(f"Tanggal/Waktu : {waktu}")
                print(f"Jumlah        : Rp {jumlah:,}")
                print(f"Jenis         : {jenis}")
                print(f"Kategori      : {kategori}")
                print(f"Status        : {status}")
                print(f"Pihak terkait : {pihak_nama}")
                print(f"Jenis Pihak   : {pihak_jenis}")
                print(f"Metode        : {pihak_metode}")
                print(f"Saldo Awal    : Rp {saldo_awal:,}")
                print(f"Saldo Akhir   : Rp {saldo_akhir:,}")

                transaksi = buat_transaksi(
                    jenis=jenis,
                    jumlah=jumlah,
                    status=status,
                    pihak_terkait=pihak_nama,
                    provinsi=orang["provinsi_pemasukan"],
                    kota=orang["kota_pemasukan"],
                    daerah=orang["daerah_pemasukan"],
                    keterangan=f"{kategori} | ID: {id_transaksi}"
                )

                last_transactions_stack.push(transaksi)
                if len(last_transactions_stack.stack) > 5:
                    last_transactions_stack.stack.pop(0)

            # ========================================================
            # OPSI 3: PENGELUARAN
            # ========================================================

            elif opsi == 3:
                print("\n=== DETAIL PENGELUARAN ===")

                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                jumlah = orang["pengeluaran_terakhir"]
                jenis = "Pembayaran"
                status = "Berhasil"

                pihak = orang["keterangan_pengeluaran"]
                pihak_nama, pihak_jenis, pihak_metode = merchant_detail[pihak]

                kategori = kategori_pengeluaran(pihak)
                id_transaksi = buat_id_transaksi()

                saldo_awal = orang["saldo_bank"]
                saldo_akhir = saldo_awal - jumlah
                orang["saldo_bank"] = saldo_akhir

                print(f"ID Transaksi  : {id_transaksi}")
                print(f"Tanggal/Waktu : {waktu}")
                print(f"Jumlah        : Rp {jumlah:,}")
                print(f"Jenis         : {jenis}")
                print(f"Kategori      : {kategori}")
                print(f"Status        : {status}")
                print(f"Pihak terkait : {pihak_nama}")
                print(f"Jenis Pihak   : {pihak_jenis}")
                print(f"Metode        : {pihak_metode}")
                print(f"Saldo Awal    : Rp {saldo_awal:,}")
                print(f"Saldo Akhir   : Rp {saldo_akhir:,}")

                transaksi = buat_transaksi(
                    jenis=jenis,
                    jumlah=jumlah,
                    status=status,
                    pihak_terkait=pihak_nama,
                    provinsi=orang["provinsi_pengeluaran"],
                    kota=orang["kota_pengeluaran"],
                    daerah=orang["daerah_pengeluaran"],
                    keterangan=f"{kategori} | ID: {id_transaksi}"
                )

                last_transactions_stack.push(transaksi)
                if len(last_transactions_stack.stack) > 5:
                    last_transactions_stack.stack.pop(0)

            # ========================================================
            # OPSI 4: RIWAYAT TRANSAKSI TERAKHIR
            # ========================================================

            elif opsi == 4:
                print("\n=== RIWAYAT TRANSAKSI TERAKHIR ===")

                if last_transactions_stack.is_empty():
                    print("Belum ada transaksi.")
                else:
                    for idx, item in enumerate(reversed(last_transactions_stack.stack), start=1):
                        print(f"\n--- Transaksi {idx} ---")
                        print(item)
                        print("------------------------")

            # ========================================================
            # OPSI 5: KEMBALI
            # ========================================================

            elif opsi == 5:
                break

            else:
                print("Opsi tidak valid.")