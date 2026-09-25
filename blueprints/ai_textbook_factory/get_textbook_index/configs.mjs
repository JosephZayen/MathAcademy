
export const delimiter = ">_<"

/**
  * @param {string} textbook 
  * @param {string} abstractLevel 
  * @param {string} examples 
  * @returns {string} prompt
 */

export function genPrompt(textbook, abstractLevel, examples, requirements) { 

  return `
  #身份
  你是一位职业前端程序员

  #任务
  根据提供的信息，按照规定格式返回一段${textbook}教材${abstractLevel}的目录

  #要求
  1.返回的目录务必准确，与原书相符
  2.依照规定格式返回内容，章节或小节间使用${delimiter}进行分隔
  ${requirements}

  #返回内容示例:
  ${examples}

  #返回格式示例:
  {content of chapter or section}
  ${delimiter}
  {content of chapter or section}
  ${delimiter}
  {content of chapter or section}
  ...
  `.trim();

}
