import os
import cv2
#pip install opencv-python
# 指定光碟或資料夾路徑
folder_path = "D:/images"

# 支援的圖片格式
image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# 抓取圖片
images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]

if not images:
    print("⚠ 沒有找到圖片檔案！")
else:
    for img_file in images:
        img_path = os.path.join(folder_path, img_file)
        print(f"顯示圖片：{img_file}")

        # 使用 OpenCV 顯示
        img = cv2.imread(img_path)
        cv2.imshow("Image Viewer", img)

        # 按任意鍵顯示下一張，按 q 離開
        key = cv2.waitKey(0)
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
