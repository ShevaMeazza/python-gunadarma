# opsi bronze ujian

# =========================
# TAMPILAN MENU TOKO ROTI
# =========================

print('=========================')
print('     SELAMAT DATANG      ')
print('=========================')


with open('dummy.txt','a') as data_diri:
    nama = input('Masukan nama anda : \n')
    kelas = input('Masukan kelas anda : \n')
    npm = input('Masukan npm anda : \n')
    print(f'Halo {nama}, kamu kelas {kelas}, npm kamu {npm}. Selamat datang di toko kami.')

    data_diri.write(nama + '\n')
    data_diri.write(kelas + '\n')
    data_diri.write(npm + '\n')


def lihat_produk():
    print("""
Produk Roti Vaganza :
1. Roti Coklat Rp.6000
2. Roti Keju Rp.7000
3. Roti Daging Ayam Rp.10000
4. Roti Pizza Rp.15000                                        
""")

def pembelian_produk():
    print("""
Produk Roti Vaganza :
1. Roti Coklat Rp.6000
2. Roti Keju Rp.7000
3. Roti Daging Ayam Rp.10000
4. Roti Pizza Rp.15000                                        
""")
    pilihan = input('Kamu Mau beli Roti Apa : ')
    if pilihan == '1':
        print('Roti Coklat')
        jumlah = int(input('Jumlah : \n'))
        harga_jumlah = 6000 * jumlah
        validation = input(f'Yakin membeli roti coklat sebanyak {jumlah} seharga {harga_jumlah} (y/n) : \n')
        print('Berhasil, Terimakasih Telah Berbelanja')
        with open('dummy.txt','a') as file:
            file.write(f'Roti Coklat\n')
            file.write(f'Jumlah : {jumlah} \n')
            file.write(f'Harga persatuan : 6000 \n')
            file.write(f'Total Harga : {harga_jumlah}')

def cek_stok():
    try :
        with open('stok.txt','r') as stok:
            stok_roti = stok.read()
            print(stok_roti)
    except Exception as e:
        print(e)


def cetak_struk():
    print('Berikut Struk Belanja Anda : \n')
    struk = open('dummy.txt','r')
    print(struk.read())

def lihat_saldo():
    try :
        with open('saldo.txt','r') as saldo:
            lihat = saldo.read()
            if not lihat:
                print('saldo kosong')
            else :           
                lihat     
                if lihat == '0':
                    print('saldo kosong gada')
                else:
                    print(f'saldo kamu {lihat}')
    except Exception as e:
        print(e)

def isi_saldo():
    try:
        with open('saldo.txt','w') as saldo_isi:
            isi = int(input('Masukan Saldo yang ingin di isi : RP. '))
            print(f'Saldo Berhasil ditambahkan sebanyak RP.{isi}')
            saldo_isi.write(f'Saldo : {isi}')
    except Exception as e:
        print(e)


def main():

    while True:
        print("""
===========================
SELAMAT DATANG DI TOKO ROTI
===========================
Silahkan Pilih Menu dibawah Ini :
1. Lihat Produk Roti
2. Pembelian
3. Cek Stok Produk
4. Cetak Struk Pembelian
5. Lihat Saldo
6. Isi Saldo                                          
7. Exit                                                             
""")
        inputan = input('Silahkan Pilih Menu (1-5) : ')
        if inputan == '1':
            lihat_produk()
        elif inputan == '2':
            pembelian_produk()
        elif inputan == '3':
            cek_stok()
        elif inputan == '4':
            cetak_struk()
        elif inputan == '5':
            lihat_saldo()
        elif inputan == '6':
            isi_saldo()
        elif inputan == '7':
            print('Terimakasih')
        else :
            print('Maaf Inputan yang anda pilih tidak tersedia.')
            break

if __name__ == '__main__':
    main()
