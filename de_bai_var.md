# Bài tập: Phương sai sai số & Kiểm tra phương sai thay đổi (Heteroskedasticity) 📈

Bài tập này giúp bạn hiểu sâu về **Phương sai sai số (Error Variance - $\sigma^2$)**, **Độ lệch chuẩn sai số (Residual Standard Error - $\sigma$)**, và kiểm tra giả định quan trọng bậc nhất của mô hình OLS: **Phương sai phần dư đồng nhất (Homoskedasticity)**.

---

## Bài 1 — Tính phương sai sai số ($\sigma^2$) và độ lệch chuẩn sai số ($\sigma$)

Từ các bài trước, bạn đã có:
* $RSS$ (Residual Sum of Squares): tổng bình phương phần dư
* $n$ (Số quan sát): $10$
* $k$ (Số biến độc lập): $3$ (`Area`, `Bedrooms`, `Age`)

### Yêu cầu:
1. **Tính bậc tự do của phần dư (Degrees of Freedom):**
   $$df = n - k - 1$$
2. **Tính ước lượng phương sai của sai số ($\sigma^2$):**
   $$\sigma^2 = \frac{RSS}{n - k - 1}$$
3. **Tính độ lệch chuẩn của sai số ($\sigma$ - Residual Standard Error):**
   $$\sigma = \sqrt{\sigma^2}$$
4. In kết quả ra màn hình:
   * $\sigma^2 = ?$
   * $\sigma = ?$

---

## Bài 2 — Nhận xét về quy mô sai số (Magnitude of Error)

Dựa vào giá trị $\sigma$ vừa tính và đơn vị của `Price` (triệu đồng), hãy trả lời:

> **Sai số dự đoán trung bình của mô hình có quy mô khoảng bao nhiêu triệu VNĐ?**

*(Gợi ý: $\sigma$ cho biết trung bình mức chênh lệch giữa giá nhà thực tế và giá dự đoán rơi vào khoảng bao nhiêu).*

---

## Bài 3 — So sánh độ phân tán phần dư theo nhóm giá trị dự đoán

Giả định OLS yêu cầu phương sai của sai số phải là một hằng số không đổi (**Homoskedasticity**). Hãy kiểm tra bước đầu bằng số liệu:

### 1. Tạo bảng gồm 4 cột:
* `House` (Số thứ tự căn nhà: 1 đến 10)
* $\hat{Y}$ (`Predicted_Price`: Giá dự đoán)
* `Residual` ($e = Y - \hat{Y}$)
* `|Residual|` (Giá trị tuyệt đối của phần dư: `abs(Residual)`)

### 2. Chia thành 2 nhóm theo giá trị dự đoán $\hat{Y}$:
* **Nhóm 1 (Giá dự đoán thấp):** 5 căn có $\hat{Y}$ nhỏ nhất.
* **Nhóm 2 (Giá dự đoán cao):** 5 căn có $\hat{Y}$ lớn nhất.

### 3. Câu hỏi quan sát:
* So sánh độ lớn trung bình của `|Residual|` giữa Nhóm 1 và Nhóm 2.
* Phương sai sai số giữa hai nhóm này có vẻ tương đương nhau (Homoskedasticity) hay có sự chênh lệch rõ rệt (Heteroskedasticity)?

---

## Bài 4 — Kiểm tra giả định bằng biểu đồ phần dư (Residual Plot)

Sử dụng thư viện `matplotlib.pyplot` để trực quan hóa:

### Yêu cầu:
1. Vẽ biểu đồ phân tán (Scatter Plot):
   * **Trục hoành (X-axis):** Giá trị dự đoán $\hat{Y}$ (`Predicted_Price`)
   * **Trục tung (Y-axis):** Phần dư `Residual` ($e$)
2. Thêm một đường chuẩn ngang màu đỏ nét đứt tại vị trí **$\text{Residual} = 0$**.

### Câu hỏi phân tích biểu đồ:
1. Các điểm phần dư có phân tán tương đối ngẫu nhiên và đều đặn quanh đường $0$ không?
2. Độ phân tán (độ mở rộng lên/xuống) của phần dư có xu hướng phình to ra (hình phễu) hoặc thu hẹp lại khi $\hat{Y}$ tăng lên không?
3. Mô hình có dấu hiệu rõ ràng của hiện tượng **Phương sai sai số thay đổi (Heteroskedasticity)** không?

> ⚠️ **Lưu ý thực tế:** Với tập dữ liệu mẫu nhỏ chỉ có 10 quan sát, chúng ta không thể khẳng định tuyệt đối về mặt thống kê. Mục tiêu chính của bài này là giúp bạn làm quen với cách dựng biểu đồ **Residuals vs Fitted Plot** — công cụ chẩn đoán mô hình kinh điển trong Machine Learning và Kinh tế lượng.