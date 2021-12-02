import qrcode
def create_QRcode(*args):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    print("Выберите товар:","1)Молоко","2)Яйца","3)Хлеб","4)Чай","5)Кофе",sep="\n")
    a = int(input("Введите номер товара:"))
    if a == 1:
        qr.add_data('http://surl.li/avhkv')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode1.jpg", "JPEG")
    elif a == 2:
        qr.add_data('http://surl.li/avhkw')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode2.jpg", "JPEG")
    elif a == 3:
        qr.add_data('http://surl.li/avhkx')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode3.jpg", "JPEG")
    elif a == 4:
        qr.add_data('http://surl.li/avhla')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode4.jpg", "JPEG")
    elif a == 5:
        qr.add_data('http://surl.li/avhlb')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode5.jpg", "JPEG")
create_QRcode()