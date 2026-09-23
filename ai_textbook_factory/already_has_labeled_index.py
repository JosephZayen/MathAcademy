from gen import gen_textbook
from config import LABEL_A, LABEL_B, source_path, config, rsysPrompt, coding_prompt
from latexer import latexer
import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', help="subparsers")
parser_coding = subparsers.add_parser(name="coding")
parser_textbook = subparsers.add_parser(name="textbook")

parser_textbook.add_argument("-i", "--identity", required=True)
parser_textbook.add_argument("-t", "--textbook", required=True)

parser_coding.add_argument("-cl", "--coding_language", required=True)
parser_coding.add_argument("-t", "--textbook", required=True)
parser_coding.add_argument("-l", "--language", required=False, default="中文", choices=["英文", "中文"])
parser_coding.add_argument("-n", "--need", required=False, default=None)
parser_coding.add_argument("-o", "--last_output", required=False, default=None)

args = parser.parse_args()

if args.command == "textbook":
    config.init_from_textbook(args)
    identity = config.get_arg("identity")
    textbook = config.get_arg("textbook")
    rsysPrompt = rsysPrompt.format(identity=identity, textbook=textbook)
elif args.command == "coding":
    config.init_from_coding(args)
    cl = config.get_arg("coding_language")
    textbook = config.get_arg("textbook")
    language = config.get_arg("language")
    need = config.get_arg("need")
    last_output = config.get_arg("last_output")
    rsysPrompt = coding_prompt.format(coding_language=cl or "",textbook=textbook or "",language=language or "",need=need or "",last_output=last_output or "")


print("开始生成AI教材!")

#读取文本的位置
ai_gen_index = source_path / r'processing/labeled.txt'
to_store = source_path / r'processing/ai_textbook.txt'


#先清空文件，防止gen里面a方式写入，造成重复
with open(to_store,"w",encoding='utf-8') as f:
    f.write('')
    f.flush()

ai_textbook = gen_textbook(LABEL_A, LABEL_B, ai_gen_index, to_store, rsysPrompt)


#最后，调用latex逻辑，处理AI生成的完整教材，生成latex格式文本
with open(to_store,'r',encoding = 'utf-8') as f:
    s = f.read()

latex_text = latexer(s)

with open(source_path / r'processing/latex.txt','w',encoding='utf-8') as f:
    f.seek(0)
    f.write(latex_text)
    f.flush()