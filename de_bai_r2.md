# Bài tập: Đánh giá mô hình hồi quy với $R^2$ và Adjusted $R^2$ 📊

Bài tập này tiếp nối bài toán dự đoán giá nhà bằng OLS, giúp bạn nắm vững bản chất của **Hệ số xác định ($R^2$ - Coefficient of Determination)** và **Adjusted $R^2$**.

---

## Bài 1 — Tính $R^2$

Bạn đã có sẵn từ bài tập OLS trước:
* `X_mat`
* `Y_mat`
* `beta`
* `Y_hat` (hay `Predicted_Price`)

### Yêu cầu:
1. **Tính Residual (Phần dư):**
   $$e = Y - \hat{Y}$$
2. **Tính RSS (Residual Sum of Squares):**
   $$RSS = \sum (Y_i - \hat{Y}_i)^2$$
3. **Tính TSS (Total Sum of Squares - Tổng bình phương sai lệch toàn phần):**
   $$TSS = \sum (Y_i - \bar{Y})^2$$
   *(với $\bar{Y}$ là giá trị trung bình của $Y$)*
4. **Tính $R^2$:**
   $$R^2 = 1 - \frac{RSS}{TSS}$$
5. In kết quả $R^2$ ra màn hình.

---

## Bài 2 — Giải thích ý nghĩa của $R^2$

Dựa trên kết quả tính được ở Bài 1, hãy trả lời câu hỏi:

> **$R^2$ của mô hình này có ý nghĩa kinh tế / thực tế là gì?**

⚠️ **Lưu ý quan trọng:** Không được giải thích theo kiểu *"Mô hình dự đoán đúng X%"*. Hãy giải thích chuẩn mực theo khái niệm **sự biến thiên (variance / variation)** của biến mục tiêu `Price`.

---

## Bài 3 — Tính Adjusted $R^2$ (Hệ số xác định hiệu chỉnh)

Từ kết quả $R^2$ ở Bài 1, hãy tính **Adjusted $R^2$** theo công thức:

$$\text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - k - 1} \right]$$

### Bạn cần xác định rõ:
* $n = ?$ *(Số lượng mẫu quan sát / căn nhà)*
* $k = ?$ *(Số lượng biến độc lập / đặc trưng dự đoán, không tính intercept)*
* $R^2 = ?$
* $\text{Adjusted } R^2 = ?$

---

## Bài 4 — So sánh $R^2$ và Adjusted $R^2$

### 1. Tạo bảng kết quả:

| Chỉ số (Metric) | Giá trị |
| :--- | :--- |
| **$R^2$** | `?` |
| **Adjusted $R^2$** | `?` |

### 2. Trả lời câu hỏi:
* Tại sao **Adjusted $R^2$** lại khác (và thường nhỏ hơn) **$R^2$**?

---

## Bài 5 — Thử nghiệm: Thêm một biến vô nghĩa vào mô hình

Tạo thêm một biến mới hoàn toàn ngẫu nhiên:
* Tên biến: `Random` (chứa 10 giá trị bất kỳ).

Sau đó xây dựng mô hình hồi quy mới gồm 4 biến:
$$\text{Price} = \beta_0 + \beta_1 \text{Area} + \beta_2 \text{Bedrooms} + \beta_3 \text{Age} + \beta_4 \text{Random} + \varepsilon$$

### Yêu cầu:
1. Tính lại $R^2$ và Adjusted $R^2$ cho mô hình mới này.
2. Lập bảng so sánh với mô hình cũ:

| Chỉ số (Metric) | Mô hình cũ (3 biến) | Mô hình mới (4 biến) |
| :--- | :---: | :---: |
| **$R^2$** | `?` | `?` |
| **Adjusted $R^2$** | `?` | `?` |

### Câu hỏi suy ngẫm:
1. $R^2$ thay đổi như thế nào khi thêm một biến ngẫu nhiên vô nghĩa vào?
2. Adjusted $R^2$ thay đổi như thế nào?
3. Qua thí nghiệm này, bạn hiểu **Adjusted $R^2$ sinh ra để giải quyết vấn đề gì** trong học máy và thống kê?