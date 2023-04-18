from function import *
from command import *

role=0
Keluar=False
while Keluar==False :
    data_user=read('user.csv')
    data_candi=read('candi.csv')
    data_bahan=read('bahan_bangunan.csv')
    command=input('>>> ')
    if command== "login":
        if role != 0 :
            print("Login gagal!")
            print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        else :
            (role,username)=login(data_user)
    elif command=="logout":
        role=logout(role)
    elif command == "help":
        help(role)
    elif command=="exit":
        Keluar=exit(Keluar)
    elif command == "summonjin":
        write('user.csv', summonjin())
    elif command == "hapusjin":
        data_user = hapusjin()
    elif command == "ubahjin":
        data_user = ubahjin()
    elif command == "bangun":
        data_user = bangun()
    elif command == "laporanjin":
        laporanjin()
