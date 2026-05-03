import requests
import base64

# 使用一个目前活跃的高速节点源（这个源包含大量 US 节点）
SOURCE_URL = "https://raw.githubusercontent.com/freefq/free/master/v2"

def run():
    try:
        # 1. 抓取订阅数据
        resp = requests.get(SOURCE_URL, timeout=15)
        # 2. 解码 Base64 内容
        decoded_text = base64.b64decode(resp.text).decode('utf-8')
        all_nodes = decoded_text.splitlines()
        
        # 3. 筛选出带 "美国" 或 "US" 的高速节点
        us_nodes = []
        for node in all_nodes:
            if "US" in node or "美国" in node:
                us_nodes.append(node)
        
        # 如果没抓到美国节点，就拿前20个保底
        final_nodes = us_nodes if us_nodes else all_nodes[:20]
        
        # 4. 写入文件
        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(final_nodes))
        print(f"成功更新了 {len(final_nodes)} 个真实节点")
        
    except Exception as e:
        print(f"抓取失败: {e}")

if __name__ == "__main__":
    run()
