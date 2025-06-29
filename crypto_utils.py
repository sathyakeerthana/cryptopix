from Crypto.Cipher import AES
import os

BLOCK = AES.block_size

def pad(data):
    pad_len = BLOCK - len(data) % BLOCK
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(key, plaintext):
    iv = os.urandom(BLOCK)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext.encode()))
    return iv + ct

def aes_decrypt(key, iv_ct):
    iv, ct = iv_ct[:BLOCK], iv_ct[BLOCK:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ct))
    return data.decode()
