import os
import PyPDF2

# Mengumpulkan nama file PDF dalam folder saat ini
pdffile = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdffile.append(filename)

# Mengurutkan nama file PDF
pdffile.sort()

# Membuat objek PdfWriter untuk menyimpan hasil penggabungan
pdf_writer = PyPDF2.PdfWriter()

# Iterasi melalui setiap file PDF dan menambahkannya ke objek PdfWriter
for filename in pdffile:
    obj = open(filename, 'rb')
    read = PyPDF2.PdfReader(obj)
    
    # Iterasi melalui setiap halaman dalam file PDF dan menambahkannya ke objek PdfWriter
    for pgn in range(len(read.pages)):
        pgo = read.pages[pgn]
        pdf_writer.add_page(pgo)

    obj.close()

# Menulis hasil penggabungan ke file tunggal
output_filename = f'combined_{filename}'
output_file = open(output_filename, 'wb')
pdf_writer.write(output_file)
output_file.close()

print(f'Penggabungan berhasil! Hasil disimpan dalam file {output_filename}')
