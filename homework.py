def tokenize(source_code):
    
    kelimeler = source_code.split()
    return kelimeler
source_code = "aloucha mouado najlae lmima youba lhbil"

tokens = tokenize(source_code)
print(tokens)