import requests
import os

UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"
SOURCE_URL = "https://raw.githubusercontent.com/Alvin9999/new-pac/master/fetch_ips.txt"

def generate():
    try:
        response = requests.get(SOURCE_URL, timeout=15)
        ips = response.text.splitlines()
        nodes = []
        for ip in ips:
            # 筛选美国节点满足 TikTok 需求
            if "US" in ip or "United States" in ip:
                link = f"vless://{UUID}@{ip}:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#US_Auto_{ip.split(':')[0]}"
                nodes.append(link)
        
        # 将结果保存到根目录，方便订阅
        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(nodes))
        print(f"成功生成 {len(nodes)} 个美国节点")
    except Exception as e:
        print(f"出错: {e}")

if __name__ == "__main__":
    generate()
