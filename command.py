from function import *

def login(data_user):
    Username=input("Username : ")
    Password=input("Password : ")
    user_valid=False
    pass_valid=False
    for i in range (1,length(data_user)):
        if Username == data_user[i][0] :
            user_valid=True
            if Password==data_user[i][1]:
                pass_valid=True
                break
    
    if user_valid==True and pass_valid==True:
        print (f'\nSelamat datang, {Username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
        return (data_user[i][2],data_user[i][0])
    elif user_valid==True and pass_valid==False:
        print("\nPassword salah!")
        return 0,0
    else:
        print("\nUsername tidak terdaftar!")
        return 0,0

def logout(role):
    if role == 0 :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        role=0
    else :
        role=0
    
    return role

def summonjin():
    data_user = read('user.csv')
    if length(data_user) <= 102:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        jin_type = input("Masukkan nomor jenis jin yang ingin dipanggil:")
        while jin_type != "1" and jin_type != "2":
            print(f"Tidak ada jenis jin bernomor “{jin_type}”!")
            jin_type = input("Masukkan nomor jenis jin yang ingin dipanggil:")
        if jin_type == "1":
            print("Memilih jin “Pengumpul”.")
        else:  # jin_type=2
            print("Memilih jin “Pembangun”.")
        jin_username = input("Masukkan username jin: ")
        jin_already = False
        for i in range(length(data_user)):
            if jin_username == data_user[i][0]:
                jin_already = True
        while jin_already == True:
            jin_username = input("Masukkan username jin: ")
            jin_already = False
            for i in range(length(data_user)):
                if jin_username == data_user[i][0]:
                    jin_already = True
        jin_password = input("Masukkan password jin: ")
        while length(jin_password) > 25 or length(jin_password) < 5:
            print("Password panjangnya harus 5-25 karakter!")
            jin_password = input("Masukkan password jin: ")
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"Jin {jin_username} berhasil dipanggil!")
    else:  # jumlah jin telah melebihi 100
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    return (jin_username, jin_password, jin_type)


def hapusjin():
    jin_username = input("Masukkan username jin : ")
    data_user = read('user.csv')
    data_candi = read('candi.csv')
    jin_already = False
    for i in range(1, length(data_user)):
        if jin_username == data_user[i][0]:
            jin_already = True
            find_jin = i
    if jin_already == True:
        jin_confirm = input(
            "Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?")
        if jin_confirm == "Y":
            delete('user.csv', find_jin)
            for i in range(1, length(data_candi)):
                if data_candi[i][1] == jin_username:
                    delete('candi.csv', i)
            print("Jin telah berhasil dihapus dari alam gaib.")
    else:  # jin_already==False
        print("Tidak ada jin dengan username tersebut.")
    return data_user


def ubahjin():
    jin_username = input("Masukkan username jin :")
    data_user = read('user.csv')
    jin_already = False
    for i in range(1, length(data_user)):
        if jin_username == data_user[i][0]:
            jin_already = True
            find_jin = i
    if jin_already == True:
        if data_user[find_jin][2] == "1":
            jin_confirm = input(
                "Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
            if jin_confirm == "Y":
                data_user[find_jin][2] = "2"
                print("Jin telah berhasil diubah.")
        else:  # tipe jin pengumpul
            jin_confirm = input(
                "Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
            if jin_confirm == "Y":
                data_user[find_jin][2] = "1"
                print("Jin telah berhasil diubah.")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return data_user


def bangun():
    #Akses
    def bangun():
        if data_user:
            if jin_username[2] != 2:
                print("Bangun hanya dapat diakses oleh Jin Pembangun.")
            else:
                print("Bangun hanya dapat diakses oleh Jin Pembangun.")
                return
    #Meng-generate jumlah bahan yang dibutuhkan untuk setiap bahan
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)
        
        jumlah_candi = length(data_candi) - 1
        if ((int(data_bahan[1][2]) < pasir) or (int(data_bahan[2][2]) < batu) or (int(data_bahan[3][2]) < air)):
            print("Bahan bangunan tidak cukup!")
            print("Candi tidak dapat dibangun!")
        elif (jumlah_candi >= 100):
            print("Candi tidak dapat dibangun!")
            print(f"Sisa candi yang perlu dibangun: {100 - (jumlah_candi + 1)}")
    #Meng-update data
    data_bahan[1][2] = int(data_bahan[1][2]) - pasir
    data_bahan[2][2] = int(data_bahan[2][2]) - batu
    data_bahan[3][2] = int(data_bahan[3][2]) - air
    id = create_id()
    candi = [id,data_use[0],pasir,batu,air]
    data_candi.append(candi)


def kumpul():
    return 0


def batchkumpul():
    return 0


def find_jinterajin_jintermalas(data):
    list_jin_pembangun = []
    for i in range(1, length(data)):
        find = False
        for j in range(length(list_jin_pembangun)):
            if (data[i][1] == list_jin_pembangun[j][0]):
                find = True
                list_jin_pembangun[j][1] += 1
        if find == False:
            list_jin_pembangun = append(list_jin_pembangun, [[data[i][1], 1]])
    jin_terajin = ''
    jin_termalas = ""
    candi_terbanyak = 0
    candi_tersedikit = 101
    for i in range(length(list_jin_pembangun)):
        if list_jin_pembangun[i][1] > candi_terbanyak:
            candi_terbanyak = list_jin_pembangun[i][1]
            jin_terajin = list_jin_pembangun[i][0]
        elif list_jin_pembangun[i][1] == candi_terbanyak:
            if jin_terajin > list_jin_pembangun[i][0]:
                jin_terajin = list_jin_pembangun[i][0]
        if list_jin_pembangun[i][1] < candi_tersedikit:
            candi_tersedikit = list_jin_pembangun[i][1]
            jin_termalas = list_jin_pembangun[i][0]
        elif list_jin_pembangun[i][1] == candi_tersedikit:
            if jin_termalas < list_jin_pembangun[i][0]:
                jin_termalas = list_jin_pembangun[i][0]
    return jin_terajin, jin_termalas


def laporanjin():
    data_user = read('user.csv')
    data_candi = read('candi.csv')
    data_bahan_bangunan = read('bahan_bangunan.csv')
    jin_pembangun_amount = 0
    jin_pengumpul_amount = 0
    jin_terajin, jin_termalas = find_jinterajin_jintermalas(data_candi)
    for i in range(length(data_user)):
        if (data_user[i][2] == "1"):
            jin_pembangun_amount += 1
        if (data_user[i][2] == "2"):
            jin_pengumpul_amount += 1
    print(f"Total Jin: {jin_pembangun_amount+jin_pengumpul_amount}")
    print(f"Total Jin Pengumpul: {jin_pengumpul_amount}")
    print(f"Total Jin Pembangun: {jin_pembangun_amount}")
    if jin_pembangun_amount == 0:
        print(f"Jin Terajin: - ")
        print(f"Jin Termalas: - ")
    else:
        print(f"Jin Terajin: {jin_terajin}")
        print(f"Jin Termalas: {jin_termalas}")

    print(f"Jumlah Pasir: {data_bahan_bangunan[1][2]} unit")
    print(f"Jumlah Batu: {data_bahan_bangunan[2][2]} unit")
    print(f"Jumlah Air: {data_bahan_bangunan[3][2]} unit")
    return 0

def hancurkancandi():
    return 0

def ayamberkokok():
    return 0

def load():
    return 0

def save():
    return 0

def help(role):
    if role=="bandung_bondowoso":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. haousjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengumpulkan jin bangun")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja jin")
        print("8. laporancandi")
        print("   Untuk mengetahui proses pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data")

    elif role=="roro_jonggrang":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan data")
    
    elif role=="jin_pengumpul":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif role=="jin_pembangun":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    elif role==0:
        print("====================== HELP ======================")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    else:
        return None

def exit(Exit):
    valid=False
    while valid==False:
        simpan=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if simpan == "y":
            valid=True
            return 0
        elif simpan=="n":
            valid=True
            Exit=True
            return Exit
