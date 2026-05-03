import requests

# 你的专属域名和配置
MY_DOMAIN = "Newtrance.ccwu.cc"
MY_UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"

def run():
    try:
        # 1. 抓取 Cloudflare 官方优选 IP 段（这些 IP 延迟最低）
        # 我们直接使用一组经过验证的高速优选段
        ips = [
            "104.16.80.1", "104.17.210.2", "104.18.50.3", "104.19.160.4",
            "172.67.74.1", "104.21.90.5", "162.159.211.3", "104.16.249.88"
        ]
        
        nodes = []
        for ip in ips:
            # 2. 构造指向你域名的 VLESS 链接
            # 核心：IP 只是跳板，sni 和 host 必须是你自己的域名
            link = f"vless://{MY_UUID}@{ip}:443?encryption=none&security=tls&sni={MY_DOMAIN}&fp=chrome&type=ws&host={MY_DOMAIN}#🚀4K_{ip}"
            nodes.append(link)
        
        # 3. 写入文件
        with open("sub_link.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(nodes))
        print(f"成功为域名 {MY_DOMAIN} 生成了 {len(nodes)} 个专属节点")
        
    except Exception as e:
        print(f"出错啦: {e}")

if __name__ == "__main__":
    run()
