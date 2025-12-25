#!/bin/bash

# GitHub 推送脚本
# 请在创建 GitHub 仓库后，替换下面的 URL 为您自己的仓库地址

# 设置您的 GitHub 仓库 URL
# 格式：https://github.com/您的用户名/仓库名.git
GITHUB_REPO_URL="https://github.com/您的用户名/wheel-detection-platform.git"

echo "🚀 开始推送到 GitHub..."

# 添加远程仓库
git remote add origin $GITHUB_REPO_URL

# 推送到 main 分支
git push -u origin main

echo "✅ 推送完成！"
echo "📋 仓库地址: $GITHUB_REPO_URL"
echo "📝 请记得在 GitHub 上查看您的代码！"