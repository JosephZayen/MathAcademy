from blueprints.ai_textbook_factory.purge.cleaner import clean
from blueprints.ai_textbook_factory.purge.ai_cleaner import ai_clean
from blueprints.ai_textbook_factory.gen import gen_textbook
from blueprints.ai_textbook_factory.config import LABEL_A, LABEL_B, identity, textbook, source_path
from blueprints.ai_textbook_factory.latexer import latexer




#普通文本清洗
#注意在cleaner调用的clean里面放了文本清洗的逻辑，硬编码
#自动存进syntax_clean.txt
with open(source_path / r'processing/raw_text.txt','r',encoding='utf-8') as f:
    rs = f.read()
s = clean(rs)

with open(source_path / r'processing/syntax_clean.txt','w',encoding='utf-8') as f:
    f.seek(0)
    f.write(s)
    f.flush()







#AI文本清洗
#传入经过程序清理后的文本
#自动存进ai_corrected.txt

print("接下来准备开始AI清洗，此前请确定sytax_clean.txt中清洗出了正确的内容")
print("are you ready?")


while(input() != 'go'):
    continue

print("purge!")

ai_cleaned = ai_clean()


with open(source_path / r'processing/ai_corrected.txt','w',encoding='utf-8') as f:
    f.seek(0)
    f.write(ai_cleaned)
    f.flush()








#开始发给AI目录，制作教材
print(r"在labeled.txt里面准备好LABEL和>_<为基础的分段")
print("are you ready?")

while(input() != 'go'):
    continue

print("purge!")
print("开始生成AI教材!")

#读取文本的位置
ai_gen_index = source_path + r'processing/labeled.txt'
to_store = source_path + r'processing/ai_textbook.txt'

gen_textbook(LABEL_A, LABEL_B, identity, textbook, ai_gen_index, to_store)





#最后，调用latex逻辑，处理AI生成的完整教材，生成latex格式文本
with open(to_store,'r',encoding = 'utf-8') as f:
    s = f.read()

latex_text = latexer(s)

with open(source_path + 'processing/latex.txt','w',encoding='utf-8') as f:
    f.seek(0)
    f.write(latex_text)
    f.flush()

