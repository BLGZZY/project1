import os

# 设置环境变量
os.environ["DASHSCOPE_API_KEY"] = "***YOUR_API***"

# 假设你已经安装了必要的库
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.core.base.llms.types import MessageRole, ChatMessage

# 创建 DashScope 对象
dashscope_llm = DashScope(
    model_name=DashScopeGenerationModels.QWEN_MAX,
    api_key=os.environ["DASHSCOPE_API_KEY"]
)

# 开启对话
print("我是阿里云开发的一款超大规模语言模型，我叫通义千问，请问我有什么可以帮你的？")
user_input = input()

messages = [
    ChatMessage(
        role=MessageRole.SYSTEM, content="You are a helpful assistant."
    ),
    ChatMessage(role=MessageRole.USER, content=user_input),
]

# 循环判断输入内容
while user_input.lower() not in ["再见", "谢谢", "谢谢你"]:
    responses = dashscope_llm.stream_chat(messages)
    response_content = ""
    for response in responses:
        if response.delta:
            response_content += response.delta
            print(response.delta, end="", flush=True)
    print("\n")

    if not response_content:
        print("抱歉，我没有理解你的问题。请再试一次。")
    else:
        messages.append(
            ChatMessage(role=MessageRole.ASSISTANT, content=response_content)
        )

    user_input = input()
    messages.append(
        ChatMessage(role=MessageRole.USER, content=user_input)
    )

# 当不满足继续对话条件时，结束对话
print("感谢您的咨询，再见")
