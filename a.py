import qrcode

def generate_qr_code(data_to_encode, output_filename='qrcode.png'):
    """
    Generates a QR code image.

    Parameters:
        data_to_encode (str): The data to encode in the QR code.
        output_filename (str): The name of the file to save the generated QR code image (default is 'qrcode.png').
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_image = qr.make_image(fill_color="blue", back_color="white")

    # Save the generated QR code as an image
    qr_image.save(output_filename)

# Example usage
data_to_encode = 'write something'
generate_qr_code(data_to_encode, output_filename='my_qr.png')
