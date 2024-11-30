def show_menu_home():
    print("""
================================
SELAMAT DATANG DI RESORT DE LUNA          
================================
1. Tipe Kamar
2. Cek Ketersediaan Kamar
3. Sewa Kamar
4. Isi Saldo          
5. Keluar                                        
""")
    
def tipe_kamar():
    print('\n Tipe Kamar Resort De Luna')
    print('1. Resort Standar :  Rp.200.000 /malam')
    print('2. Resort Deluxe :  Rp.500.000 /malam')
    print('3. Resort Luxury :  Rp.800.000 /malam')

def cek_kamar(kamar_standar, kamar_deluxe, kamar_luxury):
    print('\n Cek Ketersediaan Kamar')
    print(f'1. Resort Standar : {kamar_standar}')
    print(f'2. Resort Deluxe : {kamar_deluxe}')
    print(f'1. Resort Luxury : {kamar_luxury}')

def isi_saldo():
    try:
        with open('handling/saldo.txt','w') as saldo:
            input_saldo = input('Masukan jumlah yang ingin di isi : ')
            saldo.write(input_saldo)
            print(f'Saldo berhasil di tambahkan sebesar : Rp.{input_saldo}')
    except Exception as e:
        print(e)

def sewa_kamar(all_saldo, kamar_standar, kamar_deluxe, kamar_luxury):
    tipe_kamar()
    all_saldo
    pilihan = input('Pilih Tipe Kamar : ')
    if pilihan == '1':
        harga = 200000
        jumlah = int(input('Mau berapa malam : '))
        harga_total = jumlah * harga
        if kamar_standar < jumlah:
            print('Maaf, kamar yang anda pesan tidak tersedia.')
            print(f'Jumlah kamar yang tersedia : {kamar_standar}')
            print(f'Jumlah kamar yang anda pesan : {jumlah}')
            sewa_kamar()
        else :
            if all_saldo < harga_total:
                print('Maaf Saldo kamu kurang.')
                print(f'Saldo kamu : {all_saldo}')
                print(f'Harga Sewa Kamar : {harga_total}')
            else:
                print('Berhasil menyewa kamar')
                main()

    elif pilihan == '2':
        harga = 500000
        jumlah = int(input('Mau berapa malam : '))
        harga_total = jumlah * harga
        if kamar_deluxe < jumlah:
            print('Maaf, kamar yang anda pesan tidak tersedia.')
            print(f'Jumlah kamar yang tersedia : {kamar_deluxe}')
            print(f'Jumlah kamar yang anda pesan : {jumlah}')
            sewa_kamar()
        else :
            if all_saldo < harga_total:
                print('Maaf Saldo kamu kurang.')
                print(f'Saldo kamu : {all_saldo}')
                print(f'Harga Sewa Kamar : {harga_total}')
            else:
                print('Berhasil menyewa kamar')
                main()

    elif pilihan == '3':
        harga = 800000
        jumlah = int(input('Mau berapa malam : '))
        harga_total = jumlah * harga
        if kamar_luxury < jumlah:
            print('Maaf, kamar yang anda pesan tidak tersedia.')
            print(f'Jumlah kamar yang tersedia : {kamar_luxury}')
            print(f'Jumlah kamar yang anda pesan : {jumlah}')
            sewa_kamar()
        else :
            if all_saldo < harga_total:
                print('Maaf Saldo kamu kurang.')
                print(f'Saldo kamu : {all_saldo}')
                print(f'Harga Sewa Kamar : {harga_total}')
            else:
                print('Berhasil menyewa kamar')
                main()
    else:
        print('Maaf, input yang anda masuk tidak ada.')
        sewa_kamar()

    

def main():
    kamar_standar = 10
    kamar_deluxe = 5
    kamar_luxury = 2
    
    with open('handling/saldo.txt','r') as all_saldo:
        all_saldo.read()

    while True:
        show_menu_home()
        pilihan = input('Masukan menu (1-3) : ')

        if pilihan == '1':
            tipe_kamar()
        elif pilihan == '2':
            cek_kamar(kamar_standar, kamar_deluxe, kamar_luxury)
        elif pilihan == '3':
            sewa_kamar(all_saldo, kamar_standar, kamar_deluxe, kamar_luxury)
        elif pilihan == '4':
            isi_saldo()
        else :
            print('inputan tidak sesuai')
            break

if __name__ == '__main__':
    main()
