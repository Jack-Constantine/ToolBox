import fitz  # PyMuPDF

def crop_pdf(input_pdf, output_pdf):
    # 打开PDF文件
    pdf_document = fitz.open(input_pdf)
    
    for page_num in range(len(pdf_document)):
        # 获取页面对象
        page = pdf_document.load_page(page_num)
        
        # 获取页面的默认边界框（MediaBox）
        media_box = page.mediabox
        
        # 计算裁剪区域的矩形，确保在MediaBox范围内
        crop_rect = fitz.Rect(media_box.x0, media_box.y0+25, media_box.x1, media_box.y1 - 25)
        
        # 裁剪页面
        page.set_cropbox(crop_rect)
    
    # 保存修改后的PDF
    pdf_document.save(output_pdf)
    
    # 关闭PDF文件
    pdf_document.close()

# 使用示例
input_file = "./extracted_pages_B5.pdf"
output_file = "output.pdf"
crop_pdf(input_file, output_file)
