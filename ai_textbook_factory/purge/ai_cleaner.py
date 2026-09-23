# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import threading
import time
from random import randint


def ai_clean(identity,textbook,book_index,raw):

    sysPrompt = f'''
    #身份
    你是一位中国{identity}
    #任务
    你将被提供一段存在大量错别字的{textbook}教材目录，你
    将使用你的学科知识，纠正错别字，去掉无效内容，让该目录完整而清晰
    #指导原则
    1.避免冗长地讲授内容，你的任务是尽可能简洁并且完整地补全该目录
    2.返回纠正和补全后的目录
    3.不可遗漏有效内容，必须返回所有修改后的有效内容
    4.推理过程保持简洁和高效
    #额外提醒
    1.重点关注完整的索引，如2.5.2，依据该索引确定上下文在目录中的位置，
    确保位置正确
    2.该教材目录是OCR识别出的，故而有许多错别字
    3.顶部出现“第二章”之类的顶级目录标题，并不意味着接下来的目录是第二章的开头部分，反而可能是第二章的结尾部分，
    因为这可能是OCR从教材页面中扫描得出的内容，你应该根据完整的索引确定位置

    #示例
    该教材的部分目录结构示例（并非待处理内容，仅帮助你理解目录结构）
    {book_index}
    '''.strip()

    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    def call_ai(s, index):
        try:
            response = client.chat.completions.create(
                model="deepseek-reasoner",
                messages=[
                    {"role": "system", "content": sysPrompt},
                    {"role": "user", "content": s},
                ],
                stream=False
            )

            content = response.choices[0].message.content
            reasoning_content = response.choices[0].message.reasoning_content

            with open('ai_corrected','a',encoding='utf-8') as f:
                f.write(f"\n{index} === {content}")
                f.flush()
            with open('ai_reasoning','a',encoding='utf-8') as f:
                f.write(f"\n{index} === reasoning: {reasoning_content}")
                f.flush()
            time.sleep(1 + randint(0,5))
            print(f"index {index} finished")
            results[index] = content
        except Exception as e:
            print(e)
            print(f"index: {index}")
            results[index] = '\n'
            time.sleep(5)

    lines = raw.split("\n")

    s = ''
    prompt_lst = []
    n = 0

    for line in lines:
        if(n < 60):
            s += line
        else:
            s += line
            prompt_lst.append(s)
            s = ''
            n = -1
        n += 1

    threads = []
    results = {}

    for index,prompt in enumerate(prompt_lst):
        threads.append(threading.Thread(target=call_ai,args=[prompt, index]))

    for i, thread in enumerate(threads):
        thread.start()
        if(i != 0):
            if i % 40 == 0:
                time.sleep(120 + randint(45,60))
            if i % 5 == 0:
                time.sleep(10)

    for thread in threads:
        thread.join()

    final_result = ''

    for index, content in sorted(results.items()):
        final_result += f"\n\nindex: {index} === content: {content}"
    
    return final_result