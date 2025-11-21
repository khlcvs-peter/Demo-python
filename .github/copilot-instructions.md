<!-- Copilot / AI agent instructions for this repository -->
# 對 AI 編碼助手的快速指引

此專案為一組以腳本為主的 Python 工具集合（非同構套件）。以下說明能幫助你快速在此 codebase 中產生有用、低風險的改動。

- **專案概況（大方向）**: 此 repo 主要由獨立的腳本檔案組成，功能包含：
  - 下載與讀取 Google Drive 上的 DOCX（例如 `catch-doc-net.py`, `catch-doc-select.py`, `catch-docx.py`）
  - 網路請求與 API 擷取（多個檔案使用 `requests`，例如 `tc-test-data*.py`, `golb-get-data.py`）
  - 使用 Selenium 做瀏覽器自動化（`selenium-start.py`）
  - MySQL 存取與 CSV 匯入/轉換（`mysql*.py`, `trans-utf8.py`）
  - 資料處理使用 `pandas`（`pandas_stu.py`, `pandas-filter.py`）

- **程式結構要點**:
  - 大多數程式以單檔運作（root 下多個 `.py` 檔），不是安裝式套件；少數共用模組放在 `modules/`（例如 `modules/geometry.py`）。
  - 有些檔名包含空格或非 ASCII（例如 `connetto server.py`），產生或執行時需特別以引號處理。
  - 許多檔案直接操作 CSV（`mysql2.csv`、`mysql3.csv` 等），請注意檔案編碼與路徑。

- **可觀察到的依賴 / 套件（請在修改 README 或新增需求檔時同步列出）**:
  - `requests`（多處使用）
  - `pandas`（`pandas_stu.py`, `pandas-filter.py`）
  - `selenium`（`selenium-start.py`）
  - `pymysql`（`mysql*.py`）
  - `python-docx`（`catch-doc*.py` 中 `from docx import Document`）
  - 其他在註解或程式中提及：`gdown`, `pydrive`（`catch-doc-net.py` 註解）

- **執行與開發工作流程（可被自動化的指令）**:
  - 建議建立虛擬環境：在 PowerShell 下

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

  - 常見安裝指令（根據上述可觀察依賴）：

```powershell
pip install requests pandas selenium pymysql python-docx gdown pydrive
```

  - 直接執行範例：
    - 讀取 DOCX：`python catch-doc-net.py` 或 `python catch-docx.py`
    - 執行 Selenium 範例：`python selenium-start.py`
    - 執行 MySQL 匯出/匯入腳本：`python mysql-dtm.py`（注意：檔內有註解的連線範例，請不要把真實憑證寫入檔案）

- **約定與風險提醒（對 AI 重要）**:
  - 不要自動填入或暴露資料庫/憑證：`mysql*.py` 檔案包含註解的連線範例，任何自動化更改不得把敏感資訊寫回 repo。
  - 檔案多為示範腳本，修改時應保持 backward-compatible 的 CLI 行為（若新增選項，保持預設行為不變）。
  - 檔名中有空格或非標準字元，產生檔案或 shell 指令時請務必轉義或以引號包起。

- **常見改動模式（具體範例）**:
  - 若要把重複程式邏輯抽出，優先放到 `modules/` 下並注明用法（例如 `modules/geometry.py`），避免修改大量 script entrypoints。
  - 若新增依賴，請同步在 `README.md` 或新增 `requirements.txt`（使用 `pip freeze` 產生）並在 PR 說明中列出測試步驟。

- **參考檔案（用於示例或追蹤行為）**:
  - DOCX & GDrive: `catch-doc-net.py`, `catch-doc-select.py`, `catch-doc-select2.py`
  - Requests 範例: `tc-test-data.py`, `tc-test-data2.py`, `golb-get-data.py`
  - Selenium: `selenium-start.py`
  - MySQL + CSV: `mysql.py`, `mysql-dtm.py`, `mysql-moodle.py`, `trans-utf8.py`
  - Data processing: `pandas_stu.py`, `pandas-filter.py`

如果有任何特別想讓 AI 更注意的區域（例如要優先重構的模組、或有敏感資料須保護的路徑），請回覆告知，我會據此更新或精準化本指引。
