# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from blueprints.ai_textbook_factory.pdf_plain_text.config import source_path,sysPrompt

with open(source_path + "pdf_plain_text/prompt.txt","r",encoding='utf-8') as f:
    f.seek(0)
    prompt = f.read()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "system", "content": sysPrompt},
        {"role": "user", "content": prompt},
    ],
    stream=False
)

print(response.choices[0].message.content)

text = response.choices[0].message.content

with open(source_path + "pdf_plain_text/ds.txt","a",encoding='utf-8') as f:
    f.write(text + "\n"*7)