import json
from datetime import datetime

event = {
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "type": "測試事件",
    "location": "高雄",
    "severity": "低",
    "content": "GitHub Actions測試成功"
}

with open("events.json", "w", encoding="utf-8") as f:
    json.dump([event], f, ensure_ascii=False, indent=2)

print("events.json 更新完成")
