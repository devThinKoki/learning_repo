def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')

s = r"Qrn!Mfur!y,pxIMvsMF,BH!rM!rnqv'tMAuv IMAur'JJJMVHzMCr!FIMCr!FMqv n..,v'ArqJMQvqMF,BM!rnyyFMAuv'xMVMD,ByqMB rMAurMPrn r!Mpv.ur!MA,Mr'p,qrMzFMrCvyM.yn'KMc,,!MAuv'tLMjur'MqvqMF,BM A,.MB v'tMF,B!Mo!nv'KMOr AMDv ur IMZ,!vn!AF"
alpha = r" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
# for i in range(len(alpha)):
#     print("="*20, f"  i is {i}  ", '='*20)
#     decode_Caesar_cipher(s, i)
#     print('='*40)
decode_Caesar_cipher(s,45)

import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--file")

# args = parser.parse_args()

# if args.file:
#     file_name = args.file
#     opened_file = open(file_name)
#     encoded_text = opened_file.read()
#     opened_file.close()
#     decode_Caesar_cipher(encoded_text, -13)

import sys
# args = sys.argv
# if len(args) < 2:
#     print('no file_nmae is given')
# elif len(args) == 2:
#     file_name = args[1]
#     opened_file = open(file_name)
#     encoded_text = opened_file.read()
#     opened_file.close()
#     decode_Caesar_cipher(encoded_text, -13)