from easynmt import EasyNMT

print("Loading translation model...")
model = EasyNMT('mbart50_m2m')
print("Translation model loaded.")


def translate(source_text, source_lang, target_lang):
    return model.translate(source_text, source_lang=source_lang, target_lang=target_lang)
