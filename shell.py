import karak

while True:
    text = input('Karak >>> ')
    result, error = karak.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)