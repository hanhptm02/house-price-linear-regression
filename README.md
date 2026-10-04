# Hồi quy tuyến tính đa biến (Multiple Linear Regression) 🏠

Tài liệu này tổng hợp toàn bộ lộ trình thực hành từ xây dựng mô hình OLS cơ bản, đánh giá mô hình, kiểm tra phương sai phần dư cho đến kiểm định giả thuyết thống kê cho các hệ số hồi quy.

> 📊 **Báo cáo & Code trực quan:** Xem toàn bộ quá trình tính toán OLS và biểu đồ tại [`linear_regression.ipynb`](linear_regression.ipynb).  
> 🛠️ **Cài đặt môi trường:** `pip install -r requirements.txt`  
> 📁 **Tập dữ liệu gốc:** Xem chi tiết tại [`house_price.csv`](house_price.csv).  
---

## Dataset: Dự đoán giá nhà

Bạn có dataset gồm 10 căn nhà:

| Nhà | Diện tích (m²) | Số phòng ngủ | Tuổi nhà (năm) | Giá nhà (triệu) |
| --: | -------------: | -----------: | -------------: | --------------: |
|   1 |             50 |            2 |              5 |            2500 |
|   2 |             55 |            2 |             10 |            2600 |
|   3 |             60 |            3 |              5 |            3100 |
|   4 |             65 |            3 |             10 |            3200 |
|   5 |             70 |            3 |             15 |            3250 |
|   6 |             75 |            4 |              5 |            3800 |
|   7 |             80 |            4 |             10 |            3900 |
|   8 |             85 |            4 |             20 |            3850 |
|   9 |             90 |            5 |             10 |            4500 |
|  10 |            100 |            5 |              5 |            4800 |

Trong đó:
* **$Y$ = Giá nhà (`Price`)** (Biến phụ thuộc / mục tiêu)
* **$X_1$ = Diện tích (`Area`)**
* **$X_2$ = Số phòng ngủ (`Bedrooms`)**
* **$X_3$ = Tuổi nhà (`Age`)**

Mô hình cần xây dựng:
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \varepsilon$$

---

# Phần 1 — Xây dựng mô hình OLS cơ bản

### Bước 1 — Làm quen với dữ liệu
Tạo DataFrame bằng `pandas`:
1. Tạo 4 cột: `Area`, `Bedrooms`, `Age`, `Price`.
2. In DataFrame.
3. Kiểm tra:
   * Số dòng, số cột (`shape`)
   * Kiểu dữ liệu (`dtypes`)
   * Missing values (`isnull().sum()`)

### Bước 2 — Tách $X$ và $Y$
Tạo:
```text
X = Area, Bedrooms, Age
Y = Price
```
Sau đó kiểm tra kích thước (`shape`):
* $X$: kích thước $10 \times 3$
* $Y$: kích thước $10 \times 1$

### Bước 3 — Thêm hệ số chặn (Intercept)
OLS sử dụng ma trận thiết kế (design matrix):
$$X = \begin{bmatrix} 1 & \text{Area} & \text{Bedrooms} & \text{Age} \end{bmatrix}$$

Hãy tạo ma trận $X$ mới có thêm cột $1$:
```text
[1  50   2   5]
[1  55   2  10]
[1  60   3   5]
...
```
Kiểm tra `X.shape`, kết quả phải là: `(10, 4)`.

### Bước 4 — Tính hệ số OLS bằng NumPy
Sử dụng công thức giải tích nghiệm chính xác (Normal Equation):
$$\beta = (X^T X)^{-1} X^T Y$$

Tự tính bằng NumPy (không dùng thư viện ngoài):
1. $X^T$
2. $X^T X$
3. $(X^T X)^{-1}$
4. $X^T Y$
5. $\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \end{bmatrix}$

Sau đó viết phương trình hồi quy cụ thể:
$$\text{Price} = \beta_0 + \beta_1 \times \text{Area} + \beta_2 \times \text{Bedrooms} + \beta_3 \times \text{Age}$$

### Bước 5 — Dự đoán (Prediction)
Sử dụng công thức:
$$\hat{Y} = X\beta$$
để tính giá nhà dự đoán cho cả 10 căn. Tạo thêm cột `Predicted_Price` vào DataFrame.

### Bước 6 — Phần dư (Residual)
Tính:
$$\text{Residual } (e) = Y - \hat{Y}$$
Tạo cột `Residual` trong DataFrame. Kiểm tra tổng phần dư `Residual.sum()` (với mô hình có Intercept, tổng này xấp xỉ $0$).

### Bước 7 — Tổng bình phương sai số (SSE / RSS)
Tính:
$$SSE = \sum (Y_i - \hat{Y}_i)^2 = \sum e_i^2$$
*(Đại lượng này còn được gọi là RSS - Residual Sum of Squares)*. Tự tính bằng NumPy.

### Bước 8 — Dự đoán cho căn nhà mới
Một căn nhà mới có:
* `Area` = 80 m²
* `Bedrooms` = 3
* `Age` = 8 năm

Tạo vector $X_{\text{new}} = [1, 80, 3, 8]$ và tính giá trị dự đoán $$\hat{Y}_{\text{new}} = X_{\text{new}}\beta$$.

### Bước 9 — Câu hỏi củng cố hiểu bài
1. $\beta_1$ có ý nghĩa gì?
2. $\beta_2$ có ý nghĩa gì?
3. $\beta_3$ có ý nghĩa gì?
4. Nếu `Age` tăng 1 năm thì giá nhà dự đoán thay đổi thế nào, **giữ nguyên Area và Bedrooms**?
5. Tại sao OLS lại tìm $\beta$ sao cho **SSE nhỏ nhất**?

---

# Phần 2 — Đánh giá mô hình với $R^2$ và Adjusted $R^2$ 📊

### Bước 10 — Tính $R^2$ (Hệ số xác định)
Từ các kết quả đã có, hãy tính:
1. **Phần dư (Residual):** $e = Y - \hat{Y}$
2. **RSS (Residual Sum of Squares):** $RSS = \sum (Y_i - \hat{Y}_i)^2$
3. **TSS (Total Sum of Squares):** $TSS = \sum (Y_i - \bar{Y})^2$ *(với $\bar{Y}$ là trung bình của $Y$)*
4. **$R^2$:**
   $$R^2 = 1 - \frac{RSS}{TSS}$$
5. In kết quả $R^2$ ra màn hình.

### Bước 11 — Giải thích ý nghĩa của $R^2$
Dựa trên kết quả ở Bài 10, trả lời câu hỏi:
> **$R^2$ của mô hình này có ý nghĩa kinh tế / thực tế là gì?**

*(⚠️ Lưu ý: Giải thích chuẩn mực theo khái niệm mức độ giải thích sự biến thiên (variation) của biến mục tiêu `Price`, không dùng lối diễn đạt "dự đoán đúng X%")*.

### Bước 12 — Tính Adjusted $R^2$ (Hệ số xác định hiệu chỉnh)
Tính Adjusted $R^2$ theo công thức phạt số lượng biến:
$$\text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - k - 1} \right]$$
Với:
* $n$: Số quan sát ($n = 10$)
* $k$: Số biến độc lập ($k = 3$, không tính Intercept)

### Bước 13 — So sánh $R^2$ và Adjusted $R^2$
1. Lập bảng so sánh $R^2$ và Adjusted $R^2$.
2. Trả lời: Tại sao Adjusted $R^2$ lại khác (và thường nhỏ hơn) $R^2$?

### Bước 14 — Thử nghiệm: Thêm biến vô nghĩa vào mô hình (optional)
1. Tạo biến `Random` gồm 10 giá trị ngẫu nhiên bất kỳ.
2. Xây dựng mô hình 4 biến: $\text{Price} = \beta_0 + \beta_1\text{Area} + \beta_2\text{Bedrooms} + \beta_3\text{Age} + \beta_4\text{Random} + \varepsilon$.
3. Lập bảng so sánh $R^2$ và Adjusted $R^2$ giữa mô hình 3 biến và 4 biến:

| Chỉ số (Metric) | Mô hình cũ (3 biến) | Mô hình mới (4 biến) |
| :--- | :---: | :---: |
| **$R^2$** | `?` | `?` |
| **Adjusted $R^2$** | `?` | `?` |

4. Trả lời:
   * $R^2$ thay đổi như thế nào khi thêm biến ngẫu nhiên vô nghĩa?
   * Adjusted $R^2$ thay đổi như thế nào?
   * Adjusted $R^2$ sinh ra để giải quyết vấn đề gì trong thống kê và học máy?

---

# Phần 3 — Phương sai sai số & Kiểm tra phương sai thay đổi (Heteroskedasticity) 📈

### Bước 15 — Tính phương sai sai số ($\sigma^2$) và sai số chuẩn ($\sigma$)
1. **Bậc tự do phần dư (Degrees of Freedom):**
   $$df = n - k - 1$$
2. **Ước lượng phương sai sai số ($\sigma^2$):**
   $$\sigma^2 = \frac{RSS}{n - k - 1}$$
3. **Độ lệch chuẩn của sai số ($\sigma$ - Residual Standard Error):**
   $$\sigma = \sqrt{\sigma^2}$$
4. In kết quả $\sigma^2$ và $\sigma$.

### Bước 16 — Nhận xét về quy mô sai số (Magnitude of Error)
Dựa vào giá trị $\sigma$ và đơn vị của `Price` (triệu đồng), trả lời:
> **Sai số dự đoán trung bình của mô hình có quy mô khoảng bao nhiêu triệu VNĐ? So với mức giá trung bình của các căn nhà thì độ sai lệch này chiếm bao nhiêu phần trăm?**

### Bước 17 — So sánh độ phân tán phần dư theo nhóm giá trị dự đoán
Kiểm tra giả định phần dư đồng nhất (Homoskedasticity):
1. Tạo bảng gồm 4 cột: `House`, $\hat{Y}$ (`Predicted_Price`), `Residual`, `|Residual|` (`abs(Residual)`).
2. Chia thành 2 nhóm:
   * **Nhóm 1 (Giá dự đoán thấp):** 5 căn có $\hat{Y}$ nhỏ nhất.
   * **Nhóm 2 (Giá dự đoán cao):** 5 căn có $\hat{Y}$ lớn nhất.
3. So sánh trung bình của `|Residual|` giữa hai nhóm và rút ra nhận xét.

### Bước 18 — Kiểm tra giả định bằng biểu đồ phần dư (Residual Plot)
Sử dụng `matplotlib.pyplot`:
1. Vẽ biểu đồ phân tán (Scatter Plot):
   * Trục hoành ($X$-axis): $\hat{Y}$ (`Predicted_Price`)
   * Trục tung ($Y$-axis): `Residual` ($e$)
   * Đường chuẩn nét đứt màu đỏ tại $y = 0$.
2. Phân tích: Các điểm có phân tán ngẫu nhiên quanh trục 0 không? Có dấu hiệu hình phễu hay phương sai thay đổi (Heteroskedasticity) không?

---

# Phần 4 — Kiểm định giả thuyết cho hệ số hồi quy (Hypothesis Testing) 🎯

## Lý thuyết cốt lõi cần nhớ:
1. **Ma trận hiệp phương sai của các hệ số (Covariance Matrix):**
   $$\text{Var}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$$
2. **Sai số chuẩn của từng hệ số (Standard Error):**
   $$SE(\hat{\beta}_j) = \sqrt{\text{Var}(\hat{\beta})_{jj}} \quad \text{(căn bậc 2 các phần tử trên đường chéo chính)}$$
3. **Giá trị thống kê $t$ ($t$-statistic):**
   $$t = \frac{\hat{\beta}_j - 0}{SE(\hat{\beta}_j)}$$
4. **Giá trị $p$ ($p$-value):**
   * Tính theo phân phối Student $t$ hai phía với bậc tự do $df = n - k - 1$.
   * Quy tắc kiểm định với mức ý nghĩa $\alpha = 5\% = 0.05$:
     * Nếu **$p\text{-value} < 0.05$**: Bác bỏ $H_0 \rightarrow$ Biến có tác động có ý nghĩa thống kê.
     * Nếu **$p\text{-value} \ge 0.05$**: Chưa đủ bằng chứng bác bỏ $H_0 \rightarrow$ Biến không có ý nghĩa thống kê rõ rệt.

---

### Bước 19 — Kiểm định hệ số tự do: Intercept ($\beta_0$)
Thực hiện kiểm định giả thuyết hai phía với mức ý nghĩa $\alpha = 5\%$:
* $H_0: \beta_0 = 0$ *(Hệ số chặn bằng 0)*
* $H_1: \beta_0 \ne 0$ *(Hệ số chặn khác 0)*

#### Yêu cầu:
1. Lấy giá trị ước lượng $\hat{\beta}_0$.
2. Tính Standard Error của $\hat{\beta}_0$: $SE(\hat{\beta}_0) = \sqrt{\text{Var}(\hat{\beta})_{00}}$.
3. Tính $t\text{-statistic}$: $t_0 = \frac{\hat{\beta}_0}{SE(\hat{\beta}_0)}$.
4. Xác định giá trị $p\text{-value}$.
5. **Kết luận:** Có bác bỏ $H_0$ hay không?
6. Diễn giải ý nghĩa thực tế và mặt toán học của hệ số chặn Intercept trong bài toán giá nhà này.

---

### Bước 20 — Kiểm định hệ số diện tích: $\text{Area}$ ($\beta_1$)
Thực hiện kiểm định với $\alpha = 5\%$:
* $H_0: \beta_1 = 0$ *(Diện tích không ảnh hưởng đến giá nhà)*
* $H_1: \beta_1 \ne 0$ *(Diện tích có ảnh hưởng đến giá nhà)*

#### Yêu cầu:
1. Lấy giá trị ước lượng $\hat{\beta}_1$.
2. Tính $SE(\hat{\beta}_1) = \sqrt{\text{Var}(\hat{\beta})_{11}}$.
3. Tính $t\text{-statistic}$: $t_1 = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}$.
4. Xác định giá trị $p\text{-value}$.
5. Kết luận bác bỏ $H_0$ hay không.
6. Diễn giải kết quả bằng ngôn ngữ đời thường (chú ý điều kiện các yếu tố khác không đổi).

---

### Bước 21 — Kiểm định hệ số số phòng ngủ: $\text{Bedrooms}$ ($\beta_2$)
Thực hiện kiểm định với $\alpha = 5\%$:
* $H_0: \beta_2 = 0$ *(Số phòng ngủ không ảnh hưởng đến giá nhà)*
* $H_1: \beta_2 \ne 0$ *(Số phòng ngủ có ảnh hưởng đến giá nhà)*

#### Câu hỏi:
> **Có bằng chứng thống kê cho thấy số phòng ngủ có liên quan đến giá nhà hay không, khi đã giữ nguyên diện tích và tuổi nhà?**

---

### Bước 22 — Kiểm định hệ số tuổi nhà: $\text{Age}$ ($\beta_3$)
Thực hiện kiểm định với $\alpha = 5\%$:
* $H_0: \beta_3 = 0$ *(Tuổi nhà không ảnh hưởng đến giá nhà)*
* $H_1: \beta_3 \ne 0$ *(Tuổi nhà có ảnh hưởng đến giá nhà)*

#### Câu hỏi:
> **Có bằng chứng thống kê cho thấy tuổi nhà có liên quan đến giá nhà hay không, khi đã kiểm soát diện tích và số phòng ngủ?**

---

### Bước 23 — Bảng tổng hợp kiểm định & Chuỗi tư duy logic
1. **Lập bảng tổng hợp kết quả kiểm định cho cả 4 hệ số:**

| Biến (Variable) | Hệ số ($\hat{\beta}$) | Sai số chuẩn ($SE$) | Giá trị $t$ ($t\text{-stat}$) | Giá trị $p$ ($p\text{-value}$) | Có ý nghĩa ở mức 5%? (Yes/No) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Intercept ($\beta_0$)** | `?` | `?` | `?` | `?` | `?` |
| **Area ($\beta_1$)** | `?` | `?` | `?` | `?` | `?` |
| **Bedrooms ($\beta_2$)** | `?` | `?` | `?` | `?` | `?` |
| **Age ($\beta_3$)** | `?` | `?` | `?` | `?` | `?` |

2. **Tóm tắt chuỗi tư duy logic trong thống kê suy diễn:**
$$\text{Coefficient } (\hat{\beta}) \longrightarrow \text{Standard Error } (SE) \longrightarrow t\text{-statistic} \longrightarrow p\text{-value} \longrightarrow \text{Kết luận ý nghĩa thống kê}$$
