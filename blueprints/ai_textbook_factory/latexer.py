import re

def latexer(s):
    #s = re.sub(r'1(?: |)\.(?: |)推理.*?2(?: |)\.(?: |)宏观介绍',lambda m: r'\par 1.Reasoning \par 2.宏观介绍', s, flags = re.DOTALL)
    #暂时禁用推理的搜索，现在我已经直接使用推理模式了
    #s = s.replace('-------',r'\par') 
    s = re.sub(r'^-+$', '\n', s, flags=re.MULTILINE)   #去掉所有特殊字符_
    s = s.replace('\n**','')
    s = s.replace('**\n','')
    s = s.replace('##','')
    #s = s.replace('深入讲解','深入讲解-')
    return s
