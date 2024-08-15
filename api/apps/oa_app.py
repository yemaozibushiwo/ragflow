import httpx
import hashlib
import json
from datetime import datetime

# 配置
app_secret = "AI0324F330182543"
action = "GetPublicDocList"
url = "https://oa.gdxinyue.net/WebService/Ai/Default.ashx"

# 时间戳
timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
print(timestamp)

# 请求体参数
params = {
    "BeginID": 0,
    "KIND": 2,
    "BeginUPDATETIME": "2024-01-01 00:00:01",
    "EndUPDATETIME": "2024-08-08 12:00:01",
    "LIMIT": 10,
}

# 生成token
params_str = json.dumps(params, ensure_ascii=False)
print(params_str)
token_str = f"{app_secret}{action}{timestamp}{params_str}"
token = hashlib.md5(token_str.encode("utf-8")).hexdigest().upper()
print(token)

# 请求头
headers = {
    "timestamp": timestamp,
    "action": action,
    "token": token,
    "Content-Type": "application/json; charset=utf-8",
}

# 使用httpx发送请求
with httpx.Client() as client:
    response = client.post(url, headers=headers, content=json.dumps(params))

# 输出响应
if response.status_code == 200:
    print("请求成功:")
    print(response.json())
else:
    print("请求失败:", response.status_code)
    print(response.text)
