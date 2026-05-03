import requests

UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"
SOURCE = "https://raw.githubusercontent.com/Alvin9999/new-pac/master/fetch_ips.txt"

def run():
    try:
        # 增加超时和重试逻辑
        resp = requests.get(SOURCE, timeout=20)
        # 强制只抓取美国(US)节点
        nodes = [f"vless://{UUID}@{l.strip()}:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#US_{l.split(':')[0]}" 
                 for l in resp.text.splitlines() if "US" in l]
        
        # 强制写在根目录
        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(nodes))
        print(f"Success: {len(nodes)} nodes found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
