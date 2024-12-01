def show_menu_home():
    print("""
=====================================
SELAMAT DATANG DI TOKO PARFUME ZAMORA
=====================================
1. Cek Parfume
2. Cek Ketersediaan
3. Beli Parfume
4. Cetak Struk
5. Exit                                                  
""")

def cek_parfum():
    print('\n List Parfum Zamora : ')
    print('1. Mist blood Eu De Cologne : Rp.265.000 ')
    print('2. Frozen Shower De Blower : Rp.300.000 ')
    print('3. Chill Guy Mist Underperformance : Rp.690.000 ')

def cek_ketersediaan(stok_parfum1, stok_parfum2, stok_parfum3):
    print('\n List Ketersediaan Barang : ')
    print(f'1. Mist blood Eu De Cologne : {stok_parfum1}')
    print(f'2. Frozen Shower De Blower : {stok_parfum2}')
    print(f'3. Chill Guy Mist Underperdormance : {stok_parfum3}')

def beli_parfum(saldo, stok_parfum1, stok_parfum2, stok_parfum3):
    cek_parfum()
    pilihan = input('Pilih Parfum yang ingin dibeli : ')
    if pilihan == '1':
        saldo = 1000000
        harga = 265000
        jenis = 'Mist blood Eu De Cologne'
        jumlah = int(input('Masukan Jumlah yang ingin dibeli : '))
        harga_jumlah = jumlah * harga 
        if stok_parfum1 < jumlah :
            print('Maaf Stok tidak tersedia')
        else:
            if harga_jumlah > saldo:
                print('Maaf, saldo tidak cukup')
            else:
                print(f'Berhasil Membeli {jenis} seharga {harga_jumlah}')
                with open('HARDPUSH/handling/struk.txt','w') as struk:
                    struk.write(f'===============\n')
                    struk.write(f'STRUK PEMBELIAN\n')
                    struk.write(f'===============\n')
                    struk.write(f'Jenis  : {jenis}\n')
                    struk.write(f'Jumlah : {jumlah}\n')
                    struk.write(f'Harga  : {harga}\n')
                    struk.write(f'Total  : {harga_jumlah}\n')

    elif pilihan == '2':
        saldo = 1000000
        harga = 300000
        jenis = 'Frozen Shower De blower'
        jumlah = int(input('Masukan Jumlah yang ingin dibeli : '))
        harga_jumlah = jumlah * harga 
        if stok_parfum2 < jumlah :
            print('Maaf Stok tidak tersedia')
        else:
            if harga_jumlah > saldo:
                print('Maaf, saldo tidak cukup')
            else:
                print(f'Berhasil Membeli {jenis} seharga {harga_jumlah}')
                with open('HARDPUSH/handling/struk.txt','w') as struk:
                    struk.write(f'===============\n')
                    struk.write(f'STRUK PEMBELIAN\n')
                    struk.write(f'===============\n')
                    struk.write(f'Jenis  : {jenis}\n')
                    struk.write(f'Jumlah : {jumlah}\n')
                    struk.write(f'Harga  : {harga}\n')
                    struk.write(f'Total  : {harga_jumlah}\n')

    elif pilihan == '3':
        saldo = 1000000
        harga = 690000
        jenis = 'Chill Guy Mist Underperformance'
        jumlah = int(input('Masukan Jumlah yang ingin dibeli : '))
        harga_jumlah = jumlah * harga 
        if stok_parfum3 < jumlah :
            print('Maaf Stok tidak tersedia')
        else:
            if harga_jumlah > saldo:
                print('Maaf, saldo tidak cukup')
            else:
                print(f'Berhasil Membeli {jenis} seharga {harga_jumlah}')
                with open('HARDPUSH/handling/struk.txt','w') as struk:
                    struk.write(f'===============\n')
                    struk.write(f'STRUK PEMBELIAN\n')
                    struk.write(f'===============\n')
                    struk.write(f'Jenis  : {jenis}\n')
                    struk.write(f'Jumlah : {jumlah}\n')
                    struk.write(f'Harga  : {harga}\n')
                    struk.write(f'Total  : {harga_jumlah}\n')
    else:
        print('Maaf, Input tidak tersedia.')

def cetak_struk():
    with open('HARDPUSH/handling/struk.txt','r') as cetak:
        show = cetak.read()
        print(show)

def main():
    saldo = 1000000
    stok_parfum1 = 8
    stok_parfum2 = 5
    stok_parfum3 = 5

    while True:
        show_menu_home()
        inputan = input('Pilih Menu diatas (1-5) : ')
        if inputan == '1':
            cek_parfum()
        elif inputan == '2':
            cek_ketersediaan(stok_parfum1, stok_parfum2, stok_parfum3)
        elif inputan == '3':
            beli_parfum(saldo, stok_parfum1, stok_parfum2, stok_parfum3)
        elif inputan == '4':
            cetak_struk()
        elif inputan == '5':
            print('Terimakasih, semoga datang kembali')
            break
        else :
            print('Inputan yang anda masukan tidak tersedia')

if __name__ == '__main__':
    main()
