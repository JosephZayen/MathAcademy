import fs from "node:fs/promises"
import {delimiter} from "./configs.mjs"

//{fs} is right or wrong, why? 外面的{}有啥用
//{}表示命名引用
//如何使用RE正则来着？
//如何处理JSON转换成对象来着？
//JSON.parse()

const reader = fs.readFile(
    String.raw`C:\Users\7\Desktop\VSCProjects\textbook_toolkit\ai_textbook_factory\get_textbook_index\CSS权威指南目录.json`,
    {encoding: "utf-8"}
);


const text = await reader;
const jsonObject = JSON.parse(text);
const re = new RegExp(`\\s*${delimiter}\\s*`, "g");

//entries是静态方法还是可以继承的？这样用可以吗，为什么？
//静态方法，普通方法用的是this就能这么用，不然接收参数的就不行（即使是普通方法）

const chapters = Object.entries(jsonObject).map(arr => {
        return arr[0].replace(/\\n/g, "\n").trim() + "\n"
        + arr[1].replace(/\\n/g, "\n").replace(re, "\n").trim() + "\n" + delimiter;
    }
);

let chaptersIndex = chapters.join("\n");

if(chaptersIndex.endsWith(delimiter)){
    chaptersIndex = chaptersIndex.slice(0, -delimiter.length);
}

await fs.writeFile(
    "cleanText.txt",
    chaptersIndex,
    "utf-8"
);