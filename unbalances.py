import os

def show_menu_home():
    print("""
=====================================
SELAMAT DATANG DI TOKO PARFUME ZAMORA
=====================================
1. Cek Parfum
2. Cek Ketersediaan
3. Beli Parfum
4. Cetak Struk
5. Exit                                                  
""")

def cek_parfum(parfum):
    print('\nList Parfum Zamora:')
    for i, (nama, data) in enumerate(parfum.items(), start=1):
        print(f'{i}. {nama} : Rp.{data["harga"]}')

def cek_ketersediaan(parfum):
    print('\nList Ketersediaan Barang:')
    for nama, data in parfum.items():
        print(f'{nama}: {data["stok"]} tersedia')

def beli_parfum(parfum, saldo):
    cek_parfum(parfum)
    pilihan = input('\nPilih Parfum yang ingin dibeli (angka): ')
    try:
        pilihan = int(pilihan) - 1
        nama_parfum = list(parfum.keys())[pilihan]
        jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
        total_harga = parfum[nama_parfum]["harga"] * jumlah
        
        if parfum[nama_parfum]["stok"] < jumlah:
            print('Maaf, stok tidak mencukupi.')
        elif total_harga > saldo:
            print('Maaf, saldo tidak cukup.')
        else:
            parfum[nama_parfum]["stok"] -= jumlah
            saldo -= total_harga
            print(f'Berhasil membeli {jumlah} {nama_parfum} seharga Rp.{total_harga}')
            simpan_struk(nama_parfum, jumlah, parfum[nama_parfum]["harga"], total_harga)
    except (IndexError, ValueError):
        print('Input tidak valid.')
    return saldo

def simpan_struk(nama, jumlah, harga, total):
    os.makedirs('struk', exist_ok=True)
    with open('struk/struk.txt', 'w') as file:
        file.write('===============\n')
        file.write('STRUK PEMBELIAN\n')
        file.write('===============\n')
        file.write(f'Jenis  : {nama}\n')
        file.write(f'Jumlah : {jumlah}\n')
        file.write(f'Harga  : Rp.{harga}\n')
        file.write(f'Total  : Rp.{total}\n')

def cetak_struk():
    try:
        with open('struk/struk.txt', 'r') as file:
            print('\n' + file.read())
    except FileNotFoundError:
        print('Tidak ada struk untuk dicetak.')

def main():
    saldo = 1000000
    parfum = {
        "Mist Blood Eu De Cologne": {"harga": 265000, "stok": 8},
        "Frozen Shower De Blower": {"harga": 300000, "stok": 5},
        "Chill Guy Mist Underperformance": {"harga": 690000, "stok": 5},
    }

    while True:
        show_menu_home()
        pilihan = input('Pilih menu di atas (1-5): ')
        if pilihan == '1':
            cek_parfum(parfum)
        elif pilihan == '2':
            cek_ketersediaan(parfum)
        elif pilihan == '3':
            saldo = beli_parfum(parfum, saldo)
        elif pilihan == '4':
            cetak_struk()
        elif pilihan == '5':
            print('Terima kasih, semoga datang kembali!')
            break
        else:
            print('Input tidak valid.')

if __name__ == '__main__':
    main()
