import requests

# 换一个最直接的 VLESS/VMESS 混合源，不需要复杂解码
SOURCE = "https://raw.githubusercontent.com/vpei/free/master/v2ray"

def run():
    try:
        # 获取源数据
        resp = requests.get(SOURCE, timeout=20)
        content = resp.text
        
        # 只要抓到了内容（不管是不是加密的），直接存进文件
        if len(content) > 100:
            with open("sub_link.txt", "w", encoding="utf-8") as f:
                f.write(content)
            print(f"成功搬运数据，大小: {len(content)} 字节")
        else:
            print("源数据太短，可能抓取失败")
            
    except Exception as e:
        print(f"抓取崩溃了: {e}")

if __name__ == "__main__":
    run()
