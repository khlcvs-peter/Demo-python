import subprocess
import sys

def run(cmd):
    print(">", " ".join(cmd))
    subprocess.check_call(cmd)

def main():
    repo_url = input("請輸入 GitHub 遠端 repo URL（例如 https://github.com/you/repo.git）：").strip()
    if not repo_url:
        print("未提供 repo URL，取消。")
        return

    branch = input("要使用的分支名稱（預設 main）：").strip() or "main"

    try:
        run(["git", "init"])
        run(["git", "add", "."])
        run(["git", "commit", "-m", "Initial commit"])
    except subprocess.CalledProcessError:
        print("git init/add/commit 可能失敗（例如已經是 git repo）。繼續嘗試設定遠端與推送。")

    try:
        # 若已存在 origin，先移除再新增
        subprocess.call(["git", "remote", "remove", "origin"])
    except Exception:
        pass

    try:
        run(["git", "remote", "add", "origin", repo_url])
        run(["git", "branch", "-M", branch])
        run(["git", "push", "-u", "origin", branch])
        print("上傳完成。")
    except subprocess.CalledProcessError as e:
        print("執行 git 指令時發生錯誤：", e)
        print("請確認你已設定好 Git 認證（Personal Access Token 或 SSH key），或手動執行 README 中的步驟。")

if __name__ == "__main__":
    main()
