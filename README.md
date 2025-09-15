# IP地址分类抓取器

这是一个使用GitHub Actions自动抓取IP地址并按运营商分类的项目。

## 功能特性

- 每天自动从指定URL抓取IP地址列表
- 按运营商自动分类：
  - 前5个IP归类为中国移动
  - 中间5个IP归类为中国联通
  - 最后5个IP归类为中国电信
- 生成独立的txt文件保存各运营商的IP地址

## 文件结构

```
.
├── .github/
│   └── workflows/
│       └── fetch-ips.yml    # GitHub Actions工作流配置
├── scripts/
│   └── process_ips.py       # IP抓取和处理脚本
├── output/                  # 输出目录
│   ├── mobile.txt          # 移动IP列表
│   ├── unicom.txt          # 联通IP列表
│   └── telecom.txt         # 电信IP列表
└── README.md               # 项目说明文件
```

## 工作原理

1. GitHub Actions每天UTC时间0点（北京时间8点）自动运行
2. 从 `https://raw.githubusercontent.com/gdydg/cfipcaiji/refs/heads/main/ip.txt` 抓取IP列表
3. 按照预定规则分类IP地址
4. 将分类后的IP保存到对应的txt文件中
5. 自动提交并推送更新到仓库

## 使用方法

1. Fork或克隆此仓库
2. 确保仓库的Actions功能已启用
3. 工作流会自动按计划运行，也可以手动触发

### 手动触发

1. 进入仓库的Actions页面
2. 选择"Fetch and Process IPs"工作流
3. 点击"Run workflow"按钮

## 输出文件

- `output/mobile.txt` - 中国移动IP地址（前5个）
- `output/unicom.txt` - 中国联通IP地址（中间5个）
- `output/telecom.txt` - 中国电信IP地址（最后5个）

## 注意事项

- 确保GitHub Actions有写入权限
- IP分类规则是基于位置的简单划分，实际运营商归属可能不同
- 如果源IP列表少于15个，某些运营商文件可能为空或包含较少IP

## License

MIT