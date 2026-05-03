import requests

# 你的专属配置
MY_DOMAIN = "Newtrance.ccwu.cc"
MY_UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"

def run():
    # 使用你测得最快的几个优选 IP
    ips = ["104.17.210.2", "104.16.249.88", "104.21.90.5", "172.67.74.1"]
    nodes = []
    
    for ip in ips:
        # 1. 强制使用 443 端口
        # 2. 增加路径参数 /?ed=2048 (这是目前主流 Worker 的标准增强参数)
        # 3. 确保 host 和 sni 严格一致
        link = (
            f"vless://{MY_UUID}@{ip}:443?"
            f"encryption=none&security=tls&sni={MY_DOMAIN}&"
            f"fp=chrome&type=ws&host={MY_DOMAIN}&path=%2F%3Fed%3D2048"
            f"#🚀Final_4K_{ip}"
        )
        nodes.append(link)
    
    with open("sub_link.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(nodes))
    print(f"已为域名 {MY_DOMAIN} 重新生成 WS 增强节点")

if __name__ == "__main__":
    run()
