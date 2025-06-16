file_path = input('введите путь к файлу')
with open(file_path, 'r', encoding='utf-8') as text:
    text.seek(0)
    lines=text.readlines() 
    print(f'- в тексте {len(lines)} строк')
    text.seek(0)
    content = text.read()
    print(f'- в тексте {len(content)} символов')
    words = content.split( )
    print(f'- в тексте {len(words)} слов')
    from collections import Counter
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]
    print(f'Самое частое слово: {most_common_word}')
