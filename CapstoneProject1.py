
pasien= [
{   'ID pasien' : 'A01',
    'Nama' : 'Adi',
    'Alamat' : 'Tenayan',
    'Umur' : 31,
    'Gender' : 'Pria',
    'Diagnosa' : 'Demam Berdarah',
    'Kamar' : 'K-01'
},

{   'ID pasien' : 'A02',
    'Nama' : 'Bismo',
    'Alamat' : 'Marpoyan',
    'Umur' : 27,
    'Gender' : 'Pria',
    'Diagnosa' : 'Hepatitis',
    'Kamar' : 'K-02'
},
{   'ID pasien' : 'A03',
    'Nama' : 'Lisa',
    'Alamat' : 'Sukajadi',
    'Umur' : 22,
    'Gender' : 'Wanita',
    'Diagnosa' : 'Meningitis',
    'Kamar' : 'K-03'
},
{   'ID pasien' : 'A04',
    'Nama' : 'Kevin',
    'Alamat' : 'Rejosari',
    'Umur' : 45,
    'Gender' : 'Pria',
    'Diagnosa' : 'Malaria',
    'Kamar' : 'VIP-02'
}]



def seluruhpasien():
        print('                                      =====List Pasien Rumah Sakit Cinta Kasih=====\n')
        print('='* 121)
        print('No\t|ID PASIEN\t|NAMA\t\t|ALAMAT\t\t|UMUR\t|GENDER\t\t|DIAGNOSA\t\t|KAMAR\t\t|')
        print('='* 121)
        for i in range(len(pasien)):
            print(f"{i+1}\t|{pasien[i]['ID pasien']}\t\t|{pasien[i]['Nama']}\t\t|{pasien[i]['Alamat']}\t|{pasien[i]['Umur']}\t|{pasien[i]['Gender']}\t\t|{pasien[i]['Diagnosa']}\t\t|{pasien[i]['Kamar']}\t\t|")

def tampillistpasien():
    while True:
        print(''' 
                                          =====================================
                                          || 1. List Semua Data Pasien       ||
                                          || 2. Cari Pasien berdasarkan ID   ||
                                          || 3. Kembali ke Menu Utama        ||
                                          =====================================
              ''')
        input1= input('Masukkan angka:')
        if (input1 == '1'):
            print(seluruhpasien(),'\n')
            print('silahkan masukkan angka kembali')
        elif (input1 == '2'):
            idinput= input('Masukkan ID:').capitalize()
            for r in range(len(pasien)):
                if pasien[r]['ID pasien'] == idinput:
                    print('                                      =====List Pasien Rumah Sakit Cinta Kasih=====\n')
                    print('='* 115)
                    print('ID PASIEN\t|NAMA\t\t|ALAMAT\t\t|UMUR\t|GENDER\t\t|DIAGNOSA\t\t|KAMAR')
                    print('='* 115)
                    print(f"{pasien[r]['ID pasien']}\t\t|{pasien[r]['Nama']}\t\t|{pasien[r]['Alamat']}\t|{pasien[r]['Umur']}\t|{pasien[r]['Gender']}\t\t|{pasien[r]['Diagnosa']}\t\t|{pasien[r]['Kamar']}")
                    print('\n','Silahkan masukkan angka kembali')
                    return tampillistpasien()
            if pasien[r]['ID pasien'] != idinput:
                print('\n','ID yang di input tidak ditemukan, Silahkan masukkan angka kembali')
                return tampillistpasien()
        elif (input1 == '3'):
            print('Kembali ke Menu Utama')
            return menuutama()
        else:
            print('Input yang anda masukkan tidak valid, mohon masukkan angka kembali')
            return tampillistpasien()

def tambahpasien():

    idbaru = input('Masukkan ID Pasien: ').capitalize()

    for cekID in pasien:
        if cekID['ID pasien'] == idbaru:
            print(f'ID Pasien {idbaru} sudah ada. Mohon masukkan ID Pasien yang berbeda.')
            return tambahpasien()
        
    pasienbaru = {
        'ID pasien': idbaru,
        'Nama': input('Masukkan Nama Pasien: ').capitalize(),
        'Alamat': input('Masukkan Alamat Pasien: ').capitalize(),
        'Umur': int(input('Masukkan Umur Pasien: ')),
        'Gender': input('Masukkan Gender Pasien: ').capitalize(),
        'Diagnosa': input('Masukkan Diagnosa Pasien: ').capitalize(),
        'Kamar': input('Masukkan Kamar Pasien: ').capitalize(),
    }
    pasien.append(pasienbaru)
    print('''
"Pasien berhasil ditambahkan."
          ''')
    print('''
List Pasien Terbaru sebagai berikut:
          ''')
    print(seluruhpasien())

    tambahlagi= input('ingin menambah pasien lagi? (y/n):').lower()
    if tambahlagi== 'y':
        return tambahpasien()
    else:
        return menuutama()


def editpasien():
    edit = input('Masukkan ID Pasien yang akan diedit: ').capitalize()
    for e in range(len(pasien)):
        if pasien[e]['ID pasien'] == edit:
            print('Data Pasien yang akan diubah:')
            print('ID Pasien:', pasien[e]['ID pasien'])
            print('Nama:', pasien[e]['Nama'])
            print('Alamat:', pasien[e]['Alamat'])
            print('Umur:', pasien[e]['Umur'])
            print('Gender:', pasien[e]['Gender'])
            print('Diagnosa:', pasien[e]['Diagnosa'])
            print('Kamar:', pasien[e]['Kamar'])
            
            new_id = input('Masukkan ID Pasien baru: ').capitalize()
            while new_id in {p['ID pasien'] for p in pasien}:
                print(f'ID Pasien {new_id} sudah ada. Mohon masukkan ID Pasien yang berbeda.\n')
                return editpasien()
                
            pasien[e]['ID pasien'] = new_id  
            pasien[e]['Nama'] = input('Masukkan Nama Pasien baru: ').capitalize()
            pasien[e]['Alamat'] = input('Masukkan Alamat Pasien baru: ').capitalize()
            pasien[e]['Umur'] = int(input('Masukkan Umur Pasien baru: '))
            pasien[e]['Gender'] = input('Masukkan Gender Pasien baru: ').capitalize()
            pasien[e]['Diagnosa'] = input('Masukkan Diagnosa Pasien baru: ').capitalize()
            pasien[e]['Kamar'] = input('Masukkan Kamar Pasien baru: ').capitalize()
            print(f"Pasien dengan ID {edit} telah diubah berikut data terupdate \n")
            print('ID PASIEN\t|NAMA\t\t|ALAMAT\t\t|UMUR\t|GENDER\t\t|DIAGNOSA\t\t|KAMAR\t\t|')
            print('='* 115)
            print(f"{pasien[e]['ID pasien']}\t\t|{pasien[e]['Nama']}\t\t|{pasien[e]['Alamat']}\t|{pasien[e]['Umur']}\t|{pasien[e]['Gender']}\t\t|{pasien[e]['Diagnosa']}\t\t|{pasien[e]['Kamar']}")
            return
    print(f'Tidak ada pasien dengan ID {edit}.')

def hapuspasien():
    idhapus = input('Masukkan ID Pasien yang akan dihapus: ').capitalize()
    for h in range(len(pasien)):
        if pasien[h]['ID pasien'] == idhapus:
            print('Data Pasien yang akan dihapus:')
            print('ID Pasien:', pasien[h]['ID pasien'])
            print('Nama:', pasien[h]['Nama'])
            print('Alamat:', pasien[h]['Alamat'])
            print('Umur:', pasien[h]['Umur'])
            print('Gender:', pasien[h]['Gender'])
            print('Diagnosa:', pasien[h]['Diagnosa'])
            print('Kamar:', pasien[h]['Kamar'])

            konfirmasi = input('Apakah Anda yakin ingin menghapus data pasien ini? (y/n): ')
            if konfirmasi.lower() == 'y':
                del pasien[h]
                print(f'Pasien dengan ID {idhapus} telah dihapus.')
            else:
                print(f'Hapus data pasien dibatalkan.')
            return
    print(f'Tidak ada pasien dengan ID {idhapus}.')

            
def menuutama():
    while True:
        print('''
                                --***Aplikasi List Pasien Rumah Sakit Cinta Kasih***--
                                ======================================================
                                     Menu Aplikasi: ||1. List Data Pasien   ||
                                                    ||2. Tambah Pasien      ||
                                                    ||3. Edit Data Pasien   ||
                                                    ||4. Hapus Data Pasien  ||
                                                    ||5. Exit               ||
                                     ''')

        inputangka=input('Masukkan Angka(1-5): ')

        if inputangka == '1':
            tampillistpasien()
        elif inputangka == '2':
            tambahpasien()
        elif inputangka == '3':
            editpasien()
        elif inputangka == '4':
            hapuspasien()
        elif inputangka == '5':
            print('Terima kasih')
            exit()
        else:
            print('Input yang anda masukkan tidak valid, silahkan masukkan angka kembali')
            return menuutama()

menuutama()
            
