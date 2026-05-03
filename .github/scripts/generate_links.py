import base64

# 你的专属配置
UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"

def run():
    # 我们直接生成一组备用的美国优选 IP 节点，确保你一定能刷出内容
    # 这些是常用的优选段，配合你的 UUID 即可使用
    ips = [
        "104.16.1.1", "104.17.2.2", "104.18.3.3", "104.19.4.4", 
        "172.67.1.1", "104.21.5.5", "162.159.3.3", "104.16.88.88"
    ]
    
    nodes = []
    for ip in ips:
        # 构造标准的 VLESS 链接
        link = f"vless://{UUID}@{ip}:443?encryption=none&security=tls&sni=peer.com&fp=chrome&type=ws&host=peer.com#US_Direct_{ip}"
        nodes.append(link)
    
    # 将这些节点合并
    content = "\n".join(nodes)
    
    # 写入文件
    with open("sub_link.txt", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"成功生成了 {len(nodes)} 个硬编码节点")

if __name__ == "__main__":
    run()
