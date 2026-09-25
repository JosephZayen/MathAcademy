# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import threading
import time
from random import randint
from blueprints.ai_textbook_factory.config import LABEL_S,delimiter,no_formula, model,extra_body,reasoning_effort

def gen_textbook(LABEL_A, LABEL_B, to_read, to_store, rsysPrompt):

    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    def call_ai(s, index):
        if(not 'LABEL_S' in s):
            if('LABEL_A' in s):
                sysPrompt = rsysPrompt + LABEL_A + no_formula
            elif('LABEL_B' in s):
                sysPrompt = rsysPrompt + LABEL_B + no_formula
            else:
                sysPrompt = rsysPrompt
        else:
            if('LABEL_A' in s):
                sysPrompt = rsysPrompt + LABEL_A + LABEL_S
            elif('LABEL_B' in s):
                sysPrompt = rsysPrompt + LABEL_B + LABEL_S
            else:
                sysPrompt = rsysPrompt + LABEL_S
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": sysPrompt},
                    {"role": "user", "content": s},
                ],
                reasoning_effort=reasoning_effort,
                extra_body=extra_body,
                stream=False 
            )

            content = response.choices[0].message.content

            with open('tutorial_archieved.txt','a',encoding='utf-8') as f:
                f.write(f"\n\n\n\n{index} === {content}")
                f.flush()

            time.sleep(1 + randint(0,5))
            print(f"index {index} finished")
            results[index] = content

        except Exception as e:
            print(e)
            print(f"index: {index}")
            results[index] = ''
            time.sleep(5)

    with open(to_read,'r',encoding='utf-8') as f:
        raw = f.read()
        prompt_lst = raw.split(delimiter)

    threads = []
    results = {}

    for index,prompt in enumerate(prompt_lst):
        threads.append(threading.Thread(target=call_ai,args=[prompt, index]))

    for i, thread in enumerate(threads):
        thread.start()
        if i != 0:
            if i % 60 == 0:
                time.sleep(300 + randint(45,60))
            if i % 5 == 0:
                time.sleep(1)

    for thread in threads:
        thread.join()

    for index, content in sorted(results.items()):
        with open(to_store,"a",encoding = 'utf-8') as f:
            f.write(f"\n\n\n\n\n\n\n{prompt_lst[index]} \n\n index: {index} === content: {content}")