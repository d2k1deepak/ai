from difflib import SequenceMatcher
with open('file1.docx', errors='ignore') as file_1,open('file2.docx',errors='ignore') as file_2:
    file1_data=file_1.read()
    file2_data = file_2.read()
    difference= SequenceMatcher(None , file1_data ,file2_data).ratio()*100
    difference=round(difference,1)
    print(difference)
