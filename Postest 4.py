#Akun Login
username = 'aldy ramadhan syahputra'
password_admin = '079'
password_user = '210'

#List Barang menggunakan dictionary
baju = {
    'Baju Kaos' : 60000,
    'Baju Lengan Panjang' : 800000,
    'Baju V-Neck' : 65000,
    'Baju Tanpa Lengan' : 50000
}

celana = {
    'Celana Pendek' : 50000,
    'Celana Panjang' : 70000,
    'Celana Jeans' : 75000,
    'Celana bekas' : 40000
}   

jaket = {
    'Jaket Biasa' : 80000,
    'Jaket Hoodie' : 85000,
    'Jaket Pendek' : 75000,
}

#Fungsi-fungsi program CRUD
def tampilkan():
    print('=======================================')
    print('Anda ingin melihat daftar yang mana? : ')
    print('=======================================')
    print('1. baju\n2. celana\n3. jaket')
    print('=======================================')
    choice = input('Masukan pilihan anda:')
    print('=======================================')
    if choice == '1' or choice == 'baju':
        baju
        print('=======================================')
        for key, value in baju.items():
            print(key, ':', value)
        print('=======================================')
    elif choice == '2' or choice == 'celana':
        celana
        print('=======================================')
        for key, value in celana.items():
            print(key, ':', value)
        print('=======================================')
    elif choice == '3' or choice == 'jaket':
        jaket
        print('=======================================')
        for key, value in jaket.items():
            print(key, ':', value)
        print('=======================================')
    else:
        print('=============')
        print('Inputan Salah')
        print('=============')    

def tambah():
    print('=======================================')
    print('Anda ingin menambah daftar yang mana?')
    print('=======================================')
    print('1. baju\n2. celana\n3. jaket')
    print('=======================================')
    choice = input('Masukan pilihan anda:')
    print('=======================================')
    if choice == 'baju' or choice == '1':
        print('=======================================')
        input_baru = input('Silahkan masukan nama barang:')
        input_harga = int(input('Silahkan masukan harga barang:'))
        baju[input_baru] = input_harga
        print('=======================================')
        print('BARANG TELAH DITAMBAHKAN')
        print('=======================================')
    elif choice == 'celana' or choice == '2':
        print('=======================================')
        input_baru = input('Silahkan masukan nama barang:')
        input_harga = int(input('Silahkan masukan harga barang:'))
        celana[input_baru] = input_harga
        print('=======================================')
        print('BARANG TELAH DITAMBAHKAN')
        print('=======================================')
    elif choice == 'jaket' or choice == '3':
        print('=======================================')
        input_baru = input('Silahkan masukan nama barang:')
        input_harga = int(input('Silahkan masukan harga barang:'))
        jaket[input_baru] = input_harga
        print('=======================================')
        print('BARANG TELAH DITAMBAHKAN')
        print('=======================================')
    else:
        print('=============')
        print('Inputan Salah')
        print('=============')

def update():
    print('=======================================')
    print('Anda ingin memperbarui daftar yang mana?')
    print('=======================================')
    print('1. baju\n2. celana\n3. jaket')
    print('=======================================')
    choice = input('Masukan pilihan anda:')
    print('=======================================')
    if choice == 'baju' or choice == '1':
        print('=======================================')
        update_barang = input('Silahkan pilih barang yang ingin diperbarui:')
        update_harga = int(input('Silahkan harga yang baru:'))
        baju[update_barang] = update_harga
        print('=======================================')
        print('BARANG TELAH DIPERBARUI')
        print('=======================================')
    elif choice == 'celana' or choice == '2':
        print('=======================================')
        update_barang = input('Silahkan pilih barang yang ingin diperbarui:')
        update_harga = int(input('Silahkan harga yang baru:'))
        celana[update_barang] = update_harga
        print('=======================================')
        print('BARANG TELAH DIPERBARUI')
        print('=======================================')
    elif choice == 'jaket' or choice == '3':
        print('=======================================')
        update_barang = input('Silahkan pilih barang yang ingin diperbarui:')
        update_harga = int(input('Silahkan harga yang baru:'))
        jaket[update_barang] = update_harga
        print('=======================================')
        print('BARANG TELAH DIPERBARUI')
        print('=======================================')
    else:
        print('=============')
        print('Inputan Salah')
        print('=============')    

def delete():
    print('=======================================')
    print('Anda ingin menghapus daftar yang mana?')
    print('=======================================')
    print('1. baju\n2. celana\n3. jaket')
    print('=======================================')
    choice = input('Masukan pilihan anda:')
    print('=======================================')
    if choice == 'baju' or choice == '1':
        print('=======================================')
        del baju [input('apa yang mau dihapus:')]
        print('=======================================')
        print('BARANG TELAH DIHAPUS')
        print('=======================================')
    elif choice == 'celana' or choice == '2':
        print('=======================================')
        del celana [input('apa yang mau dihapus:')]
        print('=======================================')
        print('BARANG TELAH DIHAPUS')
        print('=======================================')
    elif choice == 'jaket' or choice == '3':
        print('=======================================')
        del jaket [input('apa yang mau dihapus:')]
        print('=======================================')
        print('BARANG TELAH DIHAPUS')
        print('=======================================')
    else:
        print('=============')
        print('Inputan Salah')
        print('=============')    

#fungsi program utama(CRUD)
def crud():
    while True:
        print('=======================================')
        print('      DATABASE ADMINISTRATION          ')
        print('      DISTRO 048//NIGHT\'sClub         ') 
        print('=======================================')
        print('1. Tampilkan Daftar Menu\n2. Tambahkan Daftar Menu\n3. Update Daftar Menu\n4. Hapus Daftar Menu\n0.exit')
        print('=======================================')
        choice = input('Masukan pilihan:')
        print('=======================================')
        if choice == '1':
            tampilkan()
            print('=======================================')
            print('\nTekan [Enter] untuk kembali')
            print('=======================================')
            input()
        elif choice == '2':
            tambah()
            print('=======================================')
            print('\nTekan [Enter] untuk kembali')
            print('=======================================')
            input()
        elif choice == '3':
            update()
            print('=======================================')
            print('\nTekan [Enter] untuk kembali')
            print('=======================================')
            input()
        elif choice == '4':
            delete()
            print('=======================================')
            print('\nTekan [Enter] untuk kembali')
            print('=======================================')
            input()
        elif choice == '0':
            print('=======================================')
            print('ANDA TELAH KELUAR DARI PROGRAM')
            print('=======================================')
            break
        else:
            print('=============')
            print('Inputan Salah')
            print('=============')    

#Fungsi program Kasir
def kasir():
    while True:
        print('=======================================')
        print('       Selamat Datang pada Toko        ')
        print('       DISTRO 048//NIGHT\'sClub        ')
        print('=======================================')
        print('1. baju\n2. cleana\n3. jaket\n0. exit')
        print('=======================================')
        pilih = input('Masukan Pilihan: ')
        print('=======================================')
        if pilih == '1':
            baju
            print('=======================================')
            for key, value in baju.items():
                print(key, ': Rp,', value)
            print('=======================================')
            x = baju[input('Masukan Pesanan anda? :')]
            y = int(input('Berapa banyak yang anda ingin beli? :'))
            z = input('Masukan hari : ')
            print('=======================================')
        elif pilih == '2':
            celana
            print('=======================================')
            for key, value in celana.items():
                print(key, ': Rp,', value)
            print('=======================================')
            x = celana[input('Masukan Pesanan anda? :')]
            y = int(input('Berapa banyak yang anda ingin beli? :'))
            z = input('Masukan hari : ')
            print('=======================================')
        elif pilih == '3':
            jaket
            print('=======================================')
            for key, value in jaket.items():
                print(key, ': Rp,', value)
            print('=======================================')
            x = jaket[input('Masukan Pesanan anda? :')]
            y = int(input('Berapa banyak yang anda ingin beli? :'))
            z = input('Masukan hari : ')
            print('=======================================')
        elif pilih == '0':
            print('=======================================')
            print('Anda telah keluar')
            print('=======================================')
            break
        else:
            print('=============')
            print('Inputan Salah')
            print('=============')    
        
        jumlah = x * y
        if z in ('senin', 'selasa','jum\'at','minggu'):
            print('=======================================')
            print('mohon maaf tidak ada diskon')
            print('Total Pembelian anda adalah Rp, ',jumlah)
            print('=======================================')
            bayar = int(input('Masukan Nominal Pembayaran anda: '))
            print(' . . . . . .')
            hasil = bayar - jumlah
            print('Total Pembayaran anda adalah: Rp,', bayar)
            print('Kembalian anda adalah: Rp,', hasil)
            print('=======================================')
            print('TERIMAKASIH TELAH BERBELANJA DI TOKO KAMI')
            print('=======================================')
        elif z == ('rabu'):
            print('=======================================')
            print('Karna Hari ini adalah Rabu\nAnda mendapatkan diskon sebesar 10%')
            diskon = jumlah * (10/100)
            hasil_diskon = jumlah - diskon
            print('total pembelian anda adalah Rp,', hasil_diskon)
            print('=======================================')
            bayar = int(input('Masukan Nominal Pembayaran anda: '))
            print(' . . . . . .')
            hasil = bayar - hasil_diskon
            print('Total Pembayaran anda adalah: Rp,', bayar)
            print('Kembalian anda adalah: Rp,', hasil)
            print('=======================================')
            print('TERIMAKASIH TELAH BERBELANJA DI TOKO KAMI')
            print('=======================================')
        elif z == ('sabtu'):
            print('=======================================')
            print('Karna Hari ini adalah Sabtu\nAnda mendapatkan diskon sebesar 25%')
            diskon = jumlah * (25/100)
            hasil_diskon = jumlah - diskon
            print('total pembelian anda adalah Rp,', hasil_diskon)
            print('=======================================')
            bayar = int(input('Masukan Nominal Pembayaran anda: '))
            print(' . . . . . .')
            hasil = bayar - hasil_diskon
            print('Total Pembayaran anda adalah: Rp,', bayar)
            print('Kembalian anda adalah: Rp,', hasil)
            print('=======================================')
            print('TERIMAKASIH TELAH BERBELANJA DI TOKO KAMI')
            print('=======================================')
        else:
            print('=============')
            print('Inputan Salah')
            print('=============')    

#Program Utama
while True:
    print('=======================================')
    print('Selamat datang Pada Program Administrasi')
    print('       DISTRO 048//NIGHT\'sClub        ')
    print('=======================================')
    print('             Menu Pilihan              ')
    print('=======================================')
    print('1. Masukan Akun\n2. Keluar')
    print('=======================================')
    choice = input('masukan pilihan: ')
    if choice == '1':
        user_name = input('Masukan Username Anda: ')
        pass_word = input('Masukan Password Anda: ')
        if user_name == username and pass_word == password_admin:
            crud()
        elif user_name == username and pass_word == password_user:
            kasir()
        else:
            print('=============')
            print('Username/password Salah')
            print('=============')
    elif choice == '2':
        print('ANDA TELAH KELUAR')
        break
    else:
            print('=============')
            print('Input Salah')
            print('=============')