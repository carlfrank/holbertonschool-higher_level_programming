for ascii_letters in range(97, 123):
    if ascii_letters == 101:
        continue
    if ascii_letters == 113:
        continue
    print('{}'.format(chr(ascii_letters)), end="")
