from openai import OpenAI
client = OpenAI(
    api_key="sk-8LuRGc0xCYM7hPs_IKTECcIy1rIjLNBlS-PWbDh5iSJyM4AoJdBajDF-aHs",
    base_url="https://ai.hybgzs.com/v1"  # 指定代理地址
)

def sendMsg(msg):
    print(msg)
    response = client.chat.completions.create(
        model="claude-sonnet-4.5",
        messages=[{"role": "user", "content": msg}]
    )
    text = response.choices[0].message.content
    print(text)
