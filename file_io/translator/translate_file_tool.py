from translate import Translator
import os

all_files = os.listdir('./files')
process_files = list(filter(lambda file_name: '_translated' not in file_name, all_files))
lang = 'es'

for file in process_files:
    with open(f'./files/{file}', 'r') as current_file:
        text_to_translate = current_file.read()

    translator = Translator(to_lang=lang)
    translation = translator.translate(text_to_translate)

    with open(f'./files/{file.split(".")[0]}_translated_{lang}.txt', 'w', encoding='UTF-8') as new_file:
        new_file.write(translation)

