import os
import logging
import time

from win32com.client import Dispatch
from docx import Document


def write_file(line, file_name="result_4.csv"):
    with open(file_name, "a", encoding="UTF-8") as f:
        f.writelines(line)
    return


def print_table(path,index):
    document = Document(path)
    table_list = []
    for row in document.tables[index-1].rows:
        for cell in row.cells:
            # print(cell.text.replace("\n", "").replace("\r", ""))
            table_list.append(cell.text.replace("\n", "").replace("\r", "").replace(",", ""))
            table_list.append("_")
        table_list.append("|")
    table_content = "".join(table_list)
    print(table_content)
    logging.info(table_content)
    return table_content
def find_above_line(doc,len_table,line,word):
    table_index = 0
    for length in range(0,len_table):
        table_index = length+1
        table = doc.Range().Tables(table_index).Range()
        # print(table)
        x = doc.Range().Tables(table_index).Range.Start

        for i in range(0,line):
            #
            # 第doc.Range(0,x).Paragraphs.Count - i行。
            f = doc.Paragraphs(doc.Range(0,x).Paragraphs.Count - i).Range()
            if word in f.replace(" ", "").replace("\n", "").replace("\r", ""):
                # 返回查找的行以及当前的数组下标
                print(f)
                logging.info(f)
                return table_index
    return table_index
def find_table_index(path,find_str):
    word = Dispatch('Word.Application')
    word.Visible = 0
    word.DisplayAlerts = 0

    doc = word.Documents.Open(path)
    # print(doc.Tables.count)
    # print(path)
    print(find_str)
    logging.info(find_str)
    index = find_above_line(doc,len_table=doc.Tables.count, line=5, word=find_str)
    print(index)
    logging.info(index)
    doc.Close()
    word.Quit()
    return index

# path = "D://抽取样例//自查报告（word文字版）-样本.docx"
# extract_word(path)
def walk_and_extract(dir = "D:\转换docx后"):
    for root, sub, files in os.walk(dir):
        for file in files:
            doc_path = root + "/" + file
            try:
                company_name = doc_path.split("/")[-1].split("_")[0]
                print(company_name)
                logging.info(company_name)
                word_index_1 = find_table_index(doc_path,"运营总体情况")
                table_content_1 = print_table(path=doc_path,index=word_index_1)

                word_index_2 = find_table_index(doc_path,"不同产品的业务情况")
                table_content_2 = print_table(path=doc_path,index=word_index_2)
                write_file(company_name+","+table_content_1+","+table_content_2+","+"\n")
            except Exception as e:
                print(e)
                # logging.error(e.with_traceback())
                logging.error(e)
logging.basicConfig(filename='' + time.strftime("%Y-%m-%d", time.localtime()) + '.log',
                    filemode='a+',
                    format="%(levelname)s : %(asctime)s : %(filename)s %(funcName)s %(lineno)d :  %(message)s",
                    level=logging.INFO)
# walk_and_extract("D:\转换docx后")
# walk_and_extract("D:\原生docx")
