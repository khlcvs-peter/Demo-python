import io

# 創建一個StringIO對象
html_content = io.StringIO()

# 寫入HTML代碼

html_content.write("<!DOCTYPE html>\n")
html_content.write("<html>\n")
html_content.write("<head>\n")
html_content.write('    <meta charset= "UTF-8">\n')
html_content.write("<title>My Website</title>\n")
html_content.write("</head>\n")
html_content.write("<body>\n")
html_content.write("<h1>Welcome to my website! V1</h1>\n")
html_content.write("<p>This is a sample HTML file generated using Python.</p>\n")
html_content.write("<p>This is peter HTML file generated using Python.</p>\n")
html_content.write("    <meta charset= 'UTF-8'>\n")
html_content.write("<p>歡迎光臨 AZURE 雲端資料  使用PYTHON 檔案 產生html.</p>\n")
html_content.write("<p>你好 這是peter 所建立的 sample HTML file generated using Python.</p>\n",)
html_content.write("</body>\n")
html_content.write("</html>")

# 將內容保存到index.html文件
with open("index.html", "w") as f:
    f.write(html_content.getvalue())





