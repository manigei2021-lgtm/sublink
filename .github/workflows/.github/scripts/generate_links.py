import requests
import os

# 你的个人配置
UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"
# 抓取公开的高速反代 IP 源，彻底绕过你的 Cloudflare 风控
SOURCE_URL = "https://raw.githubusercontent.com/Alvin9999/new-pac/master/fetch_ips.txt"

def generate():
    # 确保文件夹存在
    os.makedirs(".github/scripts", exist_ok=True)
    try:
        response = requests.get(SOURCE_URL, timeout=10)
        ips = response.text.splitlines()
        nodes = []
        for ip in ips:
            # 关键补偿逻辑：自动筛选美国(US)节点，保障你的 TikTok 需求
            if "US" in ip or "United States" in ip:
                # 拼装成 v2rayN 通用的 VLESS 格式
                link = f"vless://{UUID}@{ip}:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#US_Auto_{ip.split(':')[0]}"
                nodes.append(link)
        
        # 将生成的节点写进订阅文件
        with open("sub_link.txt", "w") as f:
            f.write("\n".join(nodes))
        print(f"成功生成 {len(nodes)} 个美国节点")
    except Exception as e:
        print(f"出错啦: {e}")

if __name__ == "__main__":
    generate()
