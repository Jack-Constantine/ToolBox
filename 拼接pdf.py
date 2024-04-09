import glob
from PyPDF3 import PdfFileWriter, PdfFileReader
import re

def sort_key(pdf_file):
    numbers = re.findall(r'\d+', pdf_file)
    return int(numbers[0]) if numbers else pdf_file

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        print(f'Processing {path}')  # 打印正在处理的文件名
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # 将每一页加入到writer对象中
            pdf_writer.addPage(pdf_reader.getPage(page))

    # 写入合并的pdf
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = glob.glob('your_directory/*.pdf')  # 用你的文件夹路径替换 'your_directory'
    paths.sort(key=sort_key)  # 确保 PDF 按文件名中的数字排序
    merge_pdfs(paths, output='Merged.pdf')