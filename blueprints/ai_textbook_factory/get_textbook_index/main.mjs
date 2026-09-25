// Please install OpenAI SDK first: `npm install openai`

import OpenAI from "openai";
import {genPrompt} from "./try.mjs";
import {delimiter} from "./try.mjs";
import fs from "node:fs/promises"

const openai = new OpenAI({
        baseURL: 'https://api.deepseek.com',
        apiKey: process.env.DEEPSEEK_API_KEY,
});

async function callai(sysPrompt, prompt) {
  if(prompt === null) prompt = "";
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: sysPrompt }, {role: "user", content: prompt}],
    //model: "deepseek-v4-pro",
    model: "deepseek-v4-pro",
    //thinking: {"type": "enabled"},
    thinking: {"type": "disabled"},
    //reasoning_effort: "high",
    stream: false,
  });

  return completion.choices[0].message.content;
}

const chapterPrompt = genPrompt("CSS权威指南第五版", "顶层章节", `
第1章 ...
第2章 ...
第3章 ...
...（剩余章节）
`)

const sectionPrompt = genPrompt("CSS权威指南第五版", "章节内小节", `
1.1
1.2
  1.2.1
  1.2.2
  1.2.3
...(该章节剩余小节)
`.trim(), "3.用户会提供这个章节的名字和内容，依据它生成该章节的各小节")

const chapters = await callai(chapterPrompt, "");

const results = await Promise.all(
  chapters.split(`${delimiter}`).map(
    async (ch) => {
      const section = await callai(sectionPrompt, `以下是你所生成目录的章节，只生成该章节目录：${ch}`);
      return [ch,section];
  })
)

const chAndSection = Object.fromEntries(results);

await fs.writeFile(
  "catalog.json",
  JSON.stringify(chAndSection, null, 4),
  "utf-8"
);




