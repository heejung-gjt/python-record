# -*- coding: utf-8 -*-
from datetime import datetime

time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
print("{} recoding..".format(time))

def record():
    date = datetime.today().strftime("%Y-%m-%d")
    contents = []
    print('>>>>> {} 내용 작성 >>>>>'.format(date))
    while True:
        content = str(input(">> "))
        if content == "-1":
            break
        contents.append(content)
    store_content(date, contents)
        
        
def store_content(date, contents):
    f = open('/home/heejung/Desktop/RECORD/{}'.format(date), 'at', encoding="UTF-8")
    for content in contents:
        con = content.split('~')
        print(con)
        url, title = con
        print(" ".join(title.split()))
        w = [title.strip(), ' ---> ', url, '\n']
        f.writelines(w)   
    f.close() 
   
if __name__ == "__main__":
    record()