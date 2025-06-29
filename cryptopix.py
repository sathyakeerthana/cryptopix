from crypto_utils import aes_encrypt, aes_decrypt
from steg_utils import embed_image, extract_image

def main():
    mode = input("Choose [encrypt/decrypt]: ").strip()
    key = input("Enter 16-byte key: ").encode()
    if mode == "encrypt":
        msg = input("Message to encrypt: ")
        iv_ct = aes_encrypt(key, msg)
        embed_image("images/in.png", "images/out.png", iv_ct)
        print("Encrypted & hidden in images/out.png")
    else:
        iv_ct = extract_image("images/out.png")
        plaintext = aes_decrypt(key, iv_ct)
        print("Decrypted message:", plaintext)

if __name__ == "__main__":
    main()
