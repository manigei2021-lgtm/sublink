import requests

MY_DOMAIN = "Newtrance.ccwu.cc"
MY_UUID = "fb257ee7-386f-4eb6-95c0-6ba00872a588"

def run():
    # 换一组更高带宽的 IP
    ips = ["104.16.80.1", "104.17.210.2", "104.16.249.88", "104.21.90.5"]
    nodes = []
    for ip in ips:
        # 改用 gRPC 模式，并强制开启 TLS
        link = f"vless://{MY_UUID}@{ip}:443?encryption=none&security=tls&sni={MY_DOMAIN}&fp=chrome&type=grpc&serviceName=grpc&host={MY_DOMAIN}#🚀Final_4K_{ip}"
        nodes.append(link)
    
    with open("sub_link.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(nodes))
    print("已切换至 gRPC 模式")

if __name__ == "__main__":
    run()
