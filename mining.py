def read_file(filename):
    with open(filename, mode='rt', encoding='utf-8') as file:
        content = file.read()
        return content


def parse_content(content):
    lines = content.strip().split('\n')
    lines = [i.split('\t') for i in lines]
    return lines


fi_lines = parse_content(read_file('fin.txt'))
ru_lines = parse_content(read_file('rus.txt'))

result = {}

for line in fi_lines:
    en_word = line[0]
    tran_dict = result.get(en_word)
    if tran_dict is None:
        result[en_word] = {
            'fi': [line[1]]
        }
    else:
        tran_dict['fi'].append(line[1])

for line in ru_lines:
    en_word = line[0]
    tran_dict = result.get(en_word)
    if tran_dict is None:
        result[en_word] = {
            'ru': [line[1]]
        }
    else:
        ru_trans = tran_dict.get('ru')
        if ru_trans is None:
            tran_dict['ru'] = [line[1]]
        else:
            tran_dict['ru'].append(line[1])

print(result.get('Run!'))
print('Total size:', len(result))

fi_en = []

for items in result.items():
    tran_data = items[1]
    ru = tran_data.get('ru')
    fi = tran_data.get('fi')
    if ru is not None and fi is not None:
        fi_en.append(tran_data)

print(fi_en[1])
print('size:', len(fi_en))


total_result = []

for line in fi_en:
    fi_words = line.get('fi')
    ru_words = line.get('ru')

    for fi_word in fi_words:
        for ru_word in ru_words:
            total_result.append((fi_word, ru_word))

print('-----------------')
print(len(total_result))


with open('result.txt', mode='w', encoding='utf-8') as file:
    for line in total_result:
        file.write(line[0] + '\t' + line[1] + '\n')


