import qrcode
import uuid

whatsapp_group_link = 'https://chat.whatsapp.com/JTFCOJYscs3271Ua5X2Qfh'

for i in range(1, 11):
    unique_id = str(uuid.uuid4())
    unique_link = f'{whatsapp_group_link}?id={unique_id}'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(unique_link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img.save(f'whatsapp_group_qr_{i}.png')

    print(f"{i}. QR Code created and saved.")
