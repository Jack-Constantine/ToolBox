import PyPDF2

def extract_pages(pdf_path, page_ranges, start_offset=18):
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        pdf_writer = PyPDF2.PdfWriter()

        for page_range in page_ranges:
            if '-' in page_range:
                start, end = map(int, page_range.split('-'))
                start += start_offset
                end += start_offset
                for page_num in range(start, end + 1):
                    pdf_writer.add_page(pdf_reader.pages[page_num - 1])  # 使用pdf_reader.pages[...]来获取页面
            else:
                page_num = int(page_range)
                pdf_writer.add_page(pdf_reader.pages[page_num + start_offset - 1])

        with open('extracted_pages.pdf', 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    pdf_path = './pdf/2025张宇强化高数18讲.pdf'
    page_ranges = [
        '1-5',
        '46-51',
        '66-68',
        '86-87',
        '101-102',
        '112-114',
        '126-135',
        '159',
        '162-163',
        '167',
        '171-172',
        '180',
        '190-191',
        '196-197',
        '204',
        '208-211',
        '231-233',
        '260-263',
        '281',
        '285',
        '290',
        '299',
        '302',
        '318-319',
        '328',
        '332-334',
        '346-349',
        '380-384',
        '398-408'
    ]

    extract_pages(pdf_path, page_ranges)
