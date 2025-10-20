import os
import importlib

def list_py_modules():
    """列出目前資料夾所有可執行的 .py 模組（排除 main.py）"""
    files = [f[:-3] for f in os.listdir() if f.endswith(".py") and f != "main.py"]
    return sorted(files)

def main():
    print("=== Python 模組執行主程式 ===")
    modules = list_py_modules()

    if not modules:
        print("⚠️ 找不到任何可執行的 .py 模組！")
        return

    print("\n可執行的模組如下：")
    for i, mod in enumerate(modules, start=1):
        print(f"{i}. {mod}.py")

    try:
        choice = int(input("\n請輸入要執行的程式編號："))
        if 1 <= choice <= len(modules):
            selected_module = modules[choice - 1]
            print(f"\n▶ 正在執行：{selected_module}.py ...\n")

            # 動態載入與執行
            module = importlib.import_module(selected_module)
            if hasattr(module, "main"):
                module.main()
            else:
                print(f"❌ 模組 {selected_module}.py 沒有 main() 函式。")
        else:
            print("❌ 請輸入有效的選項！")
    except ValueError:
        print("❌ 請輸入數字編號！")
    except Exception as e:
        print(f"⚠️ 執行發生錯誤：{e}")

if __name__ == "__main__":
    main()
