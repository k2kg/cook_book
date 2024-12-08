def merge_files(file_list, output_file):
    file_data = []

    # Считываем содержимое файлов и определяем количество строк
    for file_name in file_list:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            file_data.append((file_name, len(lines), lines))

    # Сортируем файлы по количеству строк
    file_data.sort(key=lambda x: x[1])

    # Записываем в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_name, line_count, lines in file_data:
            out_f.write(f'{file_name}\n{line_count}\n')
            out_f.writelines(lines)
            out_f.write('\n')


# Пример вызова функции
if __name__ == "__main__":
    file_list = ['1.txt', '2.txt', '3.txt']
    merge_files(file_list, 'result.txt')
