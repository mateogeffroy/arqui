# Instala la biblioteca si aún no la tienes instalada
# pip install qrcode[pil]

import qrcode

def generar_qr(data, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

# Ejemplo de uso
cantidad_qrs = 10

for i in range(1, cantidad_qrs + 1):
    data = f"Identificador_{i}"
    nombre_archivo = f"qr_{i}.png"
    generar_qr(data, nombre_archivo)