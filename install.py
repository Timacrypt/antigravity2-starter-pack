#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity 2.0 Agent Starter Pack - One-Click Installer
Cross-platform installer for macOS, Windows, and Linux.
"""

import os
import sys
import shutil
import subprocess

def print_banner():
    print("=" * 65)
    print("   🚀 Antigravity 2.0 Agent Starter Pack - 一鍵安裝程式")
    print("=" * 65)

def get_target_dirs():
    home = os.path.expanduser("~")
    skills_dir = os.path.join(home, ".gemini", "config", "skills")
    mcp_dir = os.path.join(home, ".gemini", "antigravity", "mcp", "notebooklm")
    return skills_dir, mcp_dir

def install_skills(source_dir, skills_target):
    print(f"\n[1/4] 📦 正在安裝 Agent Skills 至：{skills_target}")
    os.makedirs(skills_target, exist_ok=True)
    
    skills_src = os.path.join(source_dir, "skills")
    if not os.path.exists(skills_src):
        print(f"❌ 錯誤：找不到來源目錄 {skills_src}")
        return False

    installed_count = 0
    for item in os.listdir(skills_src):
        src_item = os.path.join(skills_src, item)
        if os.path.isdir(src_item):
            dst_item = os.path.join(skills_target, item)
            shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
            print(f"  ✓ 已安裝技能: {item}")
            installed_count += 1
            
    print(f"✨ 成功安裝 {installed_count} 個 Agent Skills！")
    return True

def install_python_deps(source_dir):
    print("\n[2/4] 🐍 正在檢查並安裝 Document 處理必備 Python 套件...")
    req_file = os.path.join(source_dir, "requirements.txt")
    if os.path.exists(req_file):
        try:
            cmd = [sys.executable, "-m", "pip", "install", "-r", req_file]
            subprocess.check_call(cmd)
            print("  ✓ Python 依賴套件（python-docx, openpyxl, python-pptx, pypdf）安裝完成！")
        except Exception as e:
            print(f"  ⚠️ 套件安裝過程中發生提醒: {e}")
            print("  您稍後可手動執行：pip install -r requirements.txt")
    else:
        print("  ⚠️ 找不到 requirements.txt，略過。")

def setup_clasp():
    print("\n[3/4] ☁️ 檢查 Google Apps Script CLI (clasp)...")
    npm_path = shutil.which("npm")
    clasp_path = shutil.which("clasp")
    if clasp_path:
        print(f"  ✓ clasp 已安裝於：{clasp_path}")
    elif npm_path:
        print("  ⏳ 正在安裝 @google/clasp (全域)...")
        try:
            subprocess.check_call(["npm", "install", "-g", "@google/clasp"])
            print("  ✓ clasp 全域安裝成功！")
        except Exception as e:
            print(f"  ⚠️ 自動安裝 clasp 失敗（可能需要 sudo 權限）：{e}")
            print("  建議手動執行：npm install -g @google/clasp")
    else:
        print("  ⚠️ 未偵測到 Node.js (npm)。若需要使用 clasp，請先至 https://nodejs.org 下載安裝。")

def setup_notebooklm(source_dir, mcp_target):
    print(f"\n[4/4] 📓 配置 NotebookLM MCP 設定至：{mcp_target}")
    os.makedirs(mcp_target, exist_ok=True)
    mcp_src = os.path.join(source_dir, "mcp-and-tools", "notebooklm")
    if os.path.exists(mcp_src):
        for item in os.listdir(mcp_src):
            src_file = os.path.join(mcp_src, item)
            dst_file = os.path.join(mcp_target, item)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)
        print("  ✓ NotebookLM MCP 設定檔複製完成！")
        print("  👉 提示：初次使用 NotebookLM 請在終端機執行 `nlm login` 登入 Google 帳號。")
    else:
        print("  ⚠️ 找不到 mcp-and-tools/notebooklm 設定檔。")

def main():
    print_banner()
    source_dir = os.path.dirname(os.path.abspath(__file__))
    skills_target, mcp_target = get_target_dirs()
    
    install_skills(source_dir, skills_target)
    install_python_deps(source_dir)
    setup_clasp()
    setup_notebooklm(source_dir, mcp_target)
    
    print("\n" + "=" * 65)
    print("🎉 恭喜！Antigravity 2.0 Agent Starter Pack 已全數安裝完成！")
    print("您現在可以在 Antigravity 2.0 對話框中直接使用：")
    print("  • /brainstorming  (架構與需求規劃)")
    print("  • /teach          (啟動互動式教學工作區)")
    print("  • /grill-me       (質詢專案盲點)")
    print("  • /wait-what      (台灣高一生繁中生活比喻白話重述)")
    print("  • Word/Excel/PPT/PDF 直接操作與生成")
    print("=" * 65)

if __name__ == "__main__":
    main()
