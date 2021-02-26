from fastpunct import FastPunct

print("Preparing punctuation restorer...")
fastpunct = FastPunct()
print("Punctuation restorer prepared.")

def punctuate(text):
    return fastpunct.punct(text)