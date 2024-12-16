import PyPDF2

# 删除pdf单个页面
def delete_pdf_page(input_path, output_path, page_number):
    with open(input_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page in range(len(pdf_reader.pages)):
            if page + 1 != page_number:
                pdf_writer.add_page(pdf_reader.pages[page])

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f'Page {page_number} is deleted successfully.')

delete_pdf_page(r"C:\\Users\\Peng Liu\\Pictures\\C程序设计语言（第2版 新版）习题解答.pdf", r"C:\\Users\\Peng Liu\\Pictures\\3.pdf", 1)