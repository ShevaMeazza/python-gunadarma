# membuat toko sayuran
# menu : cek buah, cek ketersediaan, beli, cetak struk


    

def show_menu_home():
    print("""
============================    
SELAMAT DATANG DI TOKO SAYUR
============================
1. Lihat Produk
2. Cek Ketersediaan
3. Beli 
4. Cetak Struk
5. Tambah Barang
6. Exit    
""")

def lihat_produk():
    print('\nList Produk : ')
    print('1. Kangkung : Rp.2000 /iket')
    print('2. Tomat : Rp.5000 /kg')
    print('3. Cabai : Rp.10000 /kg \n')
    with open('HARDPUSH/glorius/produk.txt','r') as file:
        baca = file.read()
        print(f'4. {baca} : Rp.3000 /iket \n')


def cek_ketersediaan(kangkung, tomat, cabe):
    print('\nList Ketersediaan : ')
    print(f'1. Kangkung : {kangkung}')
    print(f'2. Tomat : {tomat}')
    print(f'3. Cabai : {cabe}')

def beli(saldo, kangkung, tomat, cabe):
    lihat_produk()
    pilihan = input('Pilih Yang akan dibeli : ')
    if pilihan == '1':
        saldo
        jenis = 'Kangkung'
        harga = 2000
        jumlah = int(input('Berapa Ikat kangkung : '))
        total = jumlah * harga
        pembelian = saldo - total
        if kangkung < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('HARDPUSH/glorius/struk.txt','a') as struk:                        
                        struk.write('===============\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('===============\n')
                        struk.write(f'Nama Sayur : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                except Exception as e:
                    print(e)
                                            
    elif pilihan == '2':
        saldo
        jenis = 'Tomat'
        harga = 5000
        jumlah = int(input('Berapa Kg tomat : '))
        total = jumlah * harga
        pembelian = saldo - total
        if tomat < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('HARDPUSH/glorius/struk.txt','a') as struk:                        
                        struk.write('===============\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('===============\n')
                        struk.write(f'Nama Sayur : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                except Exception as e:
                    print(e)
    elif pilihan == '3':
        saldo
        jenis = 'Cabai'
        harga = 10000
        jumlah = int(input('Berapa Kg Cabai : '))
        total = jumlah * harga
        pembelian = saldo - total
        if cabe < jumlah:
            print('Maaf stoknya tidak ada')
        else:
            if total > saldo:
                print('Maaf, saldo anda tidak cukup')
            else:
                print(f'Berhasil membeli {jenis} seharga {total} ')
                print(f'Saldo saat ini : {pembelian}')
                try :
                    with open('HARDPUSH/glorius/struk.txt','a') as struk:                        
                        struk.write('===============\n')
                        struk.write('STRUK PEMBELIAN\n')
                        struk.write('===============\n')
                        struk.write(f'Nama Sayur : {jenis} \n')
                        struk.write(f'Harga Satuan : {harga} \n')
                        struk.write(f'total : {total} \n')
                        struk.write(f'Saldo Anda : {saldo} \n')
                        struk.write(f'Kembalian : {pembelian} \n')
                except Exception as e:
                    print(e)            
    else:
        print('Eror')

def cetak_struk():
    try:
        with open('HARDPUSH/glorius/struk.txt','r') as saw:
            lihat = saw.read()
            print(lihat)
    except Exception as e:
        print(e)

def tambah_barang():
    inputan = input('Masukan produk tambahan : ')
    produk = ['kangkung', 'tomat', 'cabe']
    produk.append(inputan)
    with open('HARDPUSH/glorius/produk.txt','a') as new:
        new.write(inputan)
    main()

def main():
    saldo = 50000
    kangkung = 10
    tomat = 10
    cabe = 10
    

    while True:
        
        show_menu_home()
        inputan = input('Pilih menu (1-5) : ')
        if inputan == '1':
            lihat_produk()
        elif inputan == '2':
            cek_ketersediaan(kangkung, tomat, cabe)
        elif inputan == '3':
            beli(saldo, kangkung, tomat, cabe)
        elif inputan == '4' :
            cetak_struk()
        elif inputan == '5':
            tambah_barang()
            break
        else :
            print('Inputan error')
            
if __name__ == '__main__':
    main()


