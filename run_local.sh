#!/bin/bash
# 本地测试脚本

echo "安装依赖..."
pip3 install -r requirements.txt

echo "运行IP抓取脚本..."
python3 scripts/process_ips.py

echo "查看输出结果..."
echo -e "\n=== 移动IP (mobile.txt) ==="
cat output/mobile.txt 2>/dev/null || echo "文件不存在"

echo -e "\n=== 联通IP (unicom.txt) ==="
cat output/unicom.txt 2>/dev/null || echo "文件不存在"

echo -e "\n=== 电信IP (telecom.txt) ==="
cat output/telecom.txt 2>/dev/null || echo "文件不存在"