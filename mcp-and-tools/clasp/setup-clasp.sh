#!/usr/bin/env bash
set -e

echo "=== Google Apps Script CLI (clasp) 安裝腳本 ==="

if ! command -v npm &> /dev/null; then
    echo "❌ 找不到 npm。請先安裝 Node.js：https://nodejs.org"
    exit 1
fi

echo "⏳ 正在全域安裝 @google/clasp..."
npm install -g @google/clasp

echo "✅ clasp 安裝成功！"
clasp --version
echo "👉 接下來請執行 'clasp login' 完成 Google 帳號授權。"
