class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        for letter in original_text:
            low_letter = letter.lower()
            if low_letter in self.alphabet:
                index = self.alphabet.find(low_letter)
                ciper_index = (index + shift) % 33
                result.append(self.alphabet[ciper_index])
            else:
                result.append(letter)
        return ''.join(result)


    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text:
            low_letter = letter.lower()
            if low_letter in self.alphabet:
                index = self.alphabet.find(low_letter)
                ciper_index = (index - shift) % 33
                result.append(self.alphabet[ciper_index])
            else:
                result.append(letter)
        return ''.join(result)
    def process_text(self,text, shift, is_encrypt):
        result = []
        for letter in text:
            low_letter = letter.lower()
            if low_letter in self.alphabet:
                index = self.alphabet.find(low_letter)
                if is_encrypt:
                    ciper_index = (index + shift) % 33
                else:
                    ciper_index = (index - shift) % 33
                result.append(self.alphabet[ciper_index])
            else:
                result.append(letter)
        return ''.join(result)

# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))