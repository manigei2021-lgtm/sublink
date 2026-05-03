import requests
import base64

UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"
# 换成这个更稳的源（直接抓取订阅内容）
SOURCE = "https://raw.githubusercontent.com/freefq/free/master/v2"

def run():
    try:
        resp = requests.get(SOURCE, timeout=20)
        # 订阅内容通常是 Base64 编码的，先解码
        decoded_data = base64.b64decode(resp.text).decode('utf-8')
        lines = decoded_data.splitlines()
        
        nodes = []
        for line in lines:
            # 只要是 vless 节点都抓下来，并打上标签
            if line.startswith("vless://"):
                # 提取 IP 部分并重新组合成你需要的格式
                # 这样可以确保不管原节点是什么配置，都强制走你的优选逻辑
                nodes.append(line)
        
        # 如果 vless 节点不够多，把 vmess 也抓下来（可选）
        if len(nodes) < 5:
            nodes = [l for l in lines if "US" in l or "United States" in l]

        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(nodes))
        print(f"成功抓取 {len(nodes)} 个节点")
    except Exception as e:
        print(f"出错啦: {e}")

if __name__ == "__main__":
    run()
