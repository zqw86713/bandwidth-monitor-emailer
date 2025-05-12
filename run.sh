#!/bin/bash

# 进入脚本所在目录
# 在进入目录失败时输出错误信息并退出
cd /root/bandwidth-monitor-emailer/ || { echo "错误：无法进入目录 /root/bandwidth-monitor-emailer/" >&2; exit 1; }

# 激活 Python 虚拟环境
# 在激活失败时输出错误信息并退出
source venv/bin/activate || { echo "错误：无法激活虚拟环境" >&2; exit 1; }

# 执行 Python 脚本
# 脚本的输出将由外部（cron）处理
python main.py

# 在执行完毕时输出完成信息 (可选，用于调试)
echo "Python 脚本执行完毕"