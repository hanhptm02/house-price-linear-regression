# Bài tập: Kiểm định giả thuyết cho hệ số hồi quy (Hypothesis Testing for Coefficients) 🎯

Bài tập này giúp bạn kiểm tra xem các biến độc lập (`Area`, `Bedrooms`, `Age`) có **thực sự tác động có ý nghĩa thống kê (statistically significant)** đến giá nhà hay chỉ là do biến động ngẫu nhiên của mẫu dữ liệu.

---

## Lý thuyết cốt lõi cần nhớ

1. **Ma trận hiệp phương sai của các hệ số (Covariance Matrix of Coefficients):**
   $$\text{Var}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$$
   *(với $\sigma^2$ là phương sai sai số đã tính ở bài trước: $\sigma^2 = \frac{RSS}{n - k - 1}$)*

2. **Sai số chuẩn của từng hệ số (Standard Error):**
   $$SE(\hat{\beta}_j) = \sqrt{\text{Var}(\hat{\beta})_{jj}} \quad \text{(căn bậc 2 các phần tử trên đường chéo chính)}$$

3. **Giá trị thống kê t (t-statistic):**
   $$t = \frac{\hat{\beta}_j - 0}{SE(\hat{\beta}_j)}$$

4. **Giá trị p (p-value):**
   * Tính theo phân phối Student t với bậc tự do $df = n - k - 1$.
   * Quy tắc bác bỏ $H_0$ với mức ý nghĩa $\alpha = 5\% = 0.05$:
     * Nếu **$p\text{-value} < 0.05$**: Bác bỏ $H_0$ $\rightarrow$ Biến có tác động có ý nghĩa thống kê đến giá nhà.
     * Nếu **$p\text{-value} \ge 0.05$**: Chưa đủ bằng chứng bác bỏ $H_0$ $\rightarrow$ Biến không có ý nghĩa thống kê rõ rệt.

---

## Phần 1 — Xây dựng mô hình & Chuẩn bị số liệu

### Xác định:
* Biến mục tiêu ($Y$): `Price`
* Các biến độc lập ($X$): `Area`, `Bedrooms`, `Age`
* $n$ (Số quan sát): $10$
* $k$ (Số đặc trưng): $3$
* Bậc tự do của phần dư: $df = n - k - 1 = 6$

### Các hệ số OLS đã có từ bài trước:
$$\hat{\beta} = \begin{bmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \end{bmatrix} = \begin{bmatrix} \text{Intercept} \\ \text{Area} \\ \text{Bedrooms} \\ \text{Age} \end{bmatrix}$$

---

## Phần 2 — Kiểm định hệ số diện tích: $\text{Area}$ ($\beta_1$)

Thực hiện kiểm định giả thuyết hai phía với mức ý nghĩa $\alpha = 5\%$:
* $H_0: \beta_1 = 0$ *(Diện tích không ảnh hưởng đến giá nhà)*
* $H_1: \beta_1 \ne 0$ *(Diện tích có ảnh hưởng đến giá nhà)*

### Yêu cầu:
1. Lấy giá trị ước lượng $\hat{\beta}_1$.
2. Tính Standard Error của $\hat{\beta}_1$: $SE(\hat{\beta}_1)$.
3. Tính giá trị $t\text{-statistic}$: $t_1 = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}$.
4. Xác định giá trị $p\text{-value}$.
5. **Kết luận:** Có bác bỏ $H_0$ hay không?
6. Diễn giải kết quả bằng ngôn ngữ đời thường.

---

## Phần 3 — Kiểm định hệ số số phòng ngủ: $\text{Bedrooms}$ ($\beta_2$)

Thực hiện kiểm định tương tự với $\alpha = 5\%$:
* $H_0: \beta_2 = 0$ *(Số phòng ngủ không ảnh hưởng đến giá nhà)*
* $H_1: \beta_2 \ne 0$ *(Số phòng ngủ có ảnh hưởng đến giá nhà)*

### Câu hỏi:
> **Có bằng chứng thống kê cho thấy số phòng ngủ có liên quan đến giá nhà hay không, khi đã giữ nguyên diện tích và tuổi nhà?**

---

## Phần 4 — Kiểm định hệ số tuổi nhà: $\text{Age}$ ($\beta_3$)

Thực hiện kiểm định với $\alpha = 5\%$:
* $H_0: \beta_3 = 0$ *(Tuổi nhà không ảnh hưởng đến giá nhà)*
* $H_1: \beta_3 \ne 0$ *(Tuổi nhà có ảnh hưởng đến giá nhà)*

### Câu hỏi:
> **Có bằng chứng thống kê cho thấy tuổi nhà có liên quan đến giá nhà hay không, khi đã kiểm soát diện tích và số phòng ngủ?**

---

## Phần 5 — Bảng tổng hợp & Tư duy logic

### 1. Lập bảng kết quả kiểm định:

| Biến (Variable) | Hệ số ($\hat{\beta}$) | Sai số chuẩn ($SE$) | Giá trị $t$ ($t\text{-stat}$) | Giá trị $p$ ($p\text{-value}$) | Có ý nghĩa ở mức 5%? (Yes/No) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | `?` | `?` | `?` | `?` | `?` |
| **Area** | `?` | `?` | `?` | `?` | `?` |
| **Bedrooms** | `?` | `?` | `?` | `?` | `?` |
| **Age** | `?` | `?` | `?` | `?` | `?` |

---

### 2. Chuỗi tư duy logic cần giải thích:

Tóm tắt chuỗi nhân quả trong thống kê:
$$\text{Coefficient } (\hat{\beta}) \longrightarrow \text{Standard Error } (SE) \longrightarrow t\text{-statistic} \longrightarrow p\text{-value} \longrightarrow \text{Kết luận ý nghĩa thống kê}$$