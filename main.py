from function import *
from command import *
import time

valid,data_user,data_bahan,data_candi=load()

if valid:
    print("\nLoading...")
    time.sleep(1)
    print("\nSelamat datang di program “Manajerial Candi”")
    print("Silahkan masukkan username Anda")
    role=0
    seed=int(time.time()//1)
    Keluar=False
    while Keluar==False :
        command=input('>>> ')
        if command== "login":
            if role != 0 :
                time.sleep(0.25)
                print("Login gagal!")
                print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
            else :
                (role,username)=login(data_user)
        elif command=="logout":
            role=logout(role)
        elif command=="summonjin":
            result=summonjin(data_user,role)
            if result== 0 :
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            elif result == 1 :
                print("Tidak bisa mengakses command “summonjin” selain Bandung Bondowoso.")
            else :
                for i in range(104):
                    if data_user[i]=="%":
                        data_user[i]=result
                        break
        elif command=="hapusjin" :
            hapus=hapusjin(data_user,data_candi,role)
            if hapus==1:
                print("Tidak bisa mengakses command “hapusjin” selain Bandung Bondowoso.")
            else:
                data_user,data_candi=hapus
        elif command=="ubahjin" :
            ubah=ubahjin(data_user,role) 
            if ubah==1:
                print("Tidak bisa mengakses command “ubahjin” selain Bandung Bondowoso.")
            else:
                data_user=ubah
        elif command=="bangun" :
            bngn=bangun(data_candi,username,data_bahan,role,seed)
            if bngn=="%":
                print("Tidak bisa mengakses command “bangun” selain Jin Pembangun.")
            else:
                seed,data_candi,data_bahan=bngn   
        elif command=="kumpul" :
            kmpl=kumpul(data_bahan,role,seed)
            if kmpl=="%":
                print("Tidak bisa mengakses command “kumpul” selain Jin Pengumpul.")
            else:
                seed,data_bahan=kmpl
        elif command=="batchkumpul" :
            bk=batchkumpul(data_user,data_bahan,role,seed)
            if bk=="%":
                print("Tidak bisa mengakses command “batchkumpul” selain Bandung Bondowoso.")
            else:
                seed,data_bahan=bk
        elif command=="batchbangun" :
            bb=batchbangun(data_user,data_candi,data_bahan,role,seed)
            if bb=="%":
                print("Tidak bisa mengakses command “batchbangun” selain Bandung Bondowoso.")
            else:
                seed,data_candi,data_bahan=bb
        elif command=="laporanjin":
            lj=laporanjin(data_user,data_candi,data_bahan,role)
            if lj==1:
                print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif command=="laporancandi":
            lc=laporancandi(data_candi,role)
            if lc==1:
                print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif command=="hancurkancandi":
            hc=hancurkancandi(data_candi,role)
            if hc==1:
                print("Tidak bisa mengakses command “hancurkancandi” selain Roro Jonggrang.")
            else:
                data_candi=hc
        elif command=="ayamberkokok":
            ab=ayamberkokok(data_candi,role)
            if ab==1:
                print("Tidak bisa mengakses command “ayamberkokok” selain Roro Jonggrang.")
            else:
                Keluar=True
        elif command=="save":
            save(data_user,data_bahan,data_candi)
        elif command == "help":
            help(role)
        elif command=="exit":
            Keluar=exit(Keluar,data_user,data_bahan,data_candi)