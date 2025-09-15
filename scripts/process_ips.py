#!/usr/bin/env python3
"""
抓取IP地址并按运营商分类
"""
import requests
import os

def fetch_ip_list():
    """从指定URL获取IP列表"""
    url = "https://raw.githubusercontent.com/gdydg/cfipcaiji/refs/heads/main/ip.txt"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        # 按行分割并去除空行
        ips = [line.strip() for line in response.text.splitlines() if line.strip()]
        return ips
    except requests.RequestException as e:
        print(f"获取IP列表失败: {e}")
        return []

def save_ips_by_category(ips):
    """按运营商分类保存IP地址"""
    if not ips:
        print("没有获取到IP地址")
        return
    
    # 确保输出目录存在
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # 分类保存IP
    # 前5个为移动
    mobile_ips = ips[:5] if len(ips) >= 5 else ips[:]
    
    # 中间5个为联通（从第6个开始）
    unicom_start = 5
    unicom_end = 10
    unicom_ips = ips[unicom_start:unicom_end] if len(ips) > unicom_start else []
    
    # 最后5个为电信
    telecom_ips = ips[-5:] if len(ips) >= 5 else []
    
    # 保存到文件
    save_to_file(os.path.join(output_dir, "mobile.txt"), mobile_ips, "移动")
    save_to_file(os.path.join(output_dir, "unicom.txt"), unicom_ips, "联通")
    save_to_file(os.path.join(output_dir, "telecom.txt"), telecom_ips, "电信")
    
    print(f"总共处理了 {len(ips)} 个IP地址")
    print(f"移动: {len(mobile_ips)} 个")
    print(f"联通: {len(unicom_ips)} 个")
    print(f"电信: {len(telecom_ips)} 个")

def save_to_file(filepath, ips, provider_name):
    """保存IP列表到文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        for ip in ips:
            f.write(ip + '\n')
    print(f"{provider_name}IP已保存到: {filepath}")

def main():
    """主函数"""
    print("开始抓取IP列表...")
    ips = fetch_ip_list()
    
    if ips:
        print(f"成功获取 {len(ips)} 个IP地址")
        save_ips_by_category(ips)
        print("处理完成！")
    else:
        print("未能获取到IP地址")

if __name__ == "__main__":
    main()