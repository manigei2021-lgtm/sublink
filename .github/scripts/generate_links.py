import requests

UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"
SOURCE = "https://raw.githubusercontent.com/Alvin9999/new-pac/master/fetch_ips.txt"

def run():
    try:
        resp = requests.get(SOURCE, timeout=20)
        lines = resp.text.splitlines()
        nodes = []
        
        for l in lines:
            if ":" in l:
                # 不再筛选 US，先把所有节点抓下来保底
                ip = l.strip()
                link = f"vless://{UUID}@{ip}:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#Node_{ip.split(':')[0]}"
                nodes.append(link)
        
        if not nodes:
            # 如果源文件没数据，造一个保底的
            nodes.append(f"vless://{UUID}@1.1.1.1:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#Check_Source_Error")

        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(nodes))
        print(f"Success: {len(nodes)} nodes")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
