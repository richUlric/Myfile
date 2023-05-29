import qrcode
numeros_telephone = ['0123456789', '9876543210', '5551234567']
for numero in numeros_telephone:
    # Créer un objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Ajouter les données (dans ce cas, le numéro de téléphone)
    qr.add_data(numero)
    
    # Créer le code QR
    qr.make(fit=True)
    
    # Créer une image du code QR
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Enregistrer l'image du code QR
    qr_image.save(f'code_qr_{numero}.png')
