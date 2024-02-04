import os


def count_lines_in_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

# def count_lines_in_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = sum(1 for _ in file)
#         return lines


def count_lines_in_directory(directory_path, extension='.py'):
    total_lines = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                total_lines += count_lines_in_file(file_path)
    return total_lines


# 使用示例
directory_path = '.'  # 请将此路径替换为你的Python代码所在的目录
total_lines = count_lines_in_directory(directory_path)
print(f'Total lines of code: {total_lines}')