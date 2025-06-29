from stegano import lsb

def embed_image(input_img, output_img, data_bytes):
    secret = lsb.hide(input_img, data_bytes.hex())
    secret.save(output_img)

def extract_image(stego_img):
    b64 = lsb.reveal(stego_img)
    return bytes.fromhex(b64)
