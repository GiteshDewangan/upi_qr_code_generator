from io import BytesIO
from flask import send_file
import qrcode
import uuid
from PIL import Image
import os.path

from qrcode.image.styledpil import StyledPilImage

script_dir = os.path.dirname(os.path.abspath(__file__))

def generateUPIQR(upi_address,amount,uploadedImage=None,user_name=None,txn_note="Money"):
    # Txn Refernce Id
    try:
        tr = str(uuid.uuid4())
        qr_data = f'upi://pay?pa={upi_address}&am={amount}&tr={tr}&tn={txn_note}&pn={user_name}&tn={txn_note}'
        print(f'Generating QR code for string : {qr_data}')
        # Create the QR code object
        qr = qrcode.QRCode(version=1, box_size=4, border=4)
        # Add the QR code data
        qr.add_data(qr_data)
        # Make the QR code
        qr.make(fit=True)
        overlay_img = getOverlayImage(uploadedImage)
        img = qr.make_image(image_factory=StyledPilImage,
                            embeded_image=overlay_img)
        return serve_pil_image(img)
    except Exception as e:
        return {"error":f"Unable to generate QR Code ,Error: {e}"}

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

def getOverlayImage(imageFile):
    file = imageFile['file']
    img = Image.open(file.stream)
    return img
