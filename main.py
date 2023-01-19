import win32com.client

wdFormatPDF = 17

in_file = "D:\\BACKUP 2022\\Documents\\CENTRALTI\\modules\\testedoc.docx" # path docx
out_file = "D:\\BACKUP 2022\\Documents\\CENTRALTI\\modules\\testedoc.pdf" # path onde ficará + nome do pdf

word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()