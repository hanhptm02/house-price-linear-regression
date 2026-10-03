Được. Mình cho bạn một **bài tập hồi quy tuyến tính đa biến rất cơ bản**, đủ để luyện `pandas → numpy → OLS → prediction → residual → SSE`.

## Bài tập: Dự đoán giá nhà 🏠

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

* **Y = Giá nhà**
* **X₁ = Diện tích**
* **X₂ = Số phòng ngủ**
* **X₃ = Tuổi nhà**

Mô hình cần xây dựng:

**Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ε**

---

# Phần 1 — Làm quen với dữ liệu

### Bài 1

Tạo DataFrame bằng pandas.

Yêu cầu:

1. Tạo 4 cột:

   * `Area`
   * `Bedrooms`
   * `Age`
   * `Price`

2. In DataFrame.

3. Kiểm tra:

   * số dòng, số cột
   * kiểu dữ liệu
   * missing values

---

# Phần 2 — Tách X và Y

### Bài 2

Tạo:

```text
X = Area, Bedrooms, Age
Y = Price
```

Sau đó kiểm tra shape:

```text
X.shape
Y.shape
```

Bạn cần hiểu được:

```text
X: 10 × 3

Y: 10 × 1
```

---

# Phần 3 — Thêm intercept

### Bài 3

OLS sử dụng ma trận:

```text
X = [1  Area  Bedrooms  Age]
```

Hãy tạo ma trận X mới có thêm cột `1`.

Ví dụ:

```text
[1  50   2   5]
[1  55   2  10]
[1  60   3   5]
...
```

Kiểm tra:

```text
X.shape
```

Kết quả phải là:

```text
(10, 4)
```

---

# Phần 4 — Tính hệ số OLS bằng NumPy

Đây là phần quan trọng nhất.

Sử dụng công thức:

**β = (XᵀX)⁻¹XᵀY**

### Bài 4

Tự tính bằng NumPy:

1. Xᵀ
2. XᵀX
3. (XᵀX)⁻¹
4. XᵀY
5. β

Không dùng `sklearn` ở phần này.

Kết quả β sẽ có dạng:

```text
β₀
β₁
β₂
β₃
```

Sau đó viết phương trình hồi quy:

```text
Price = β₀ + β₁ × Area + β₂ × Bedrooms + β₃ × Age
```

---

# Phần 5 — Prediction

### Bài 5

Sử dụng:

**Ŷ = Xβ**

để tính giá nhà dự đoán cho cả 10 căn.

Tạo thêm một cột:

```text
Predicted_Price
```

DataFrame sẽ có dạng:

| Area | Bedrooms | Age | Price | Predicted_Price |
| ---: | -------: | --: | ----: | --------------: |
|   50 |        2 |   5 |  2500 |             ... |
|   55 |        2 |  10 |  2600 |             ... |
|  ... |      ... | ... |   ... |             ... |

---

# Phần 6 — Residual

### Bài 6

Tính:

**Residual = Y − Ŷ**

Tạo cột:

```text
Residual
```

Sau đó kiểm tra:

```text
Residual.sum()
```

Với mô hình OLS có intercept, tổng residual sẽ xấp xỉ **0**.

---

# Phần 7 — SSE / RSS

### Bài 7

Tính:

**SSE = Σ(Yᵢ − Ŷᵢ)²**

hay:

**SSE = Σeᵢ²**

Trong nhiều tài liệu, đại lượng này cũng được gọi là **RSS (Residual Sum of Squares)**.

Hãy tự tính bằng NumPy.

---

# Phần 8 — Thử dự đoán một căn nhà mới

### Bài 8

Một căn nhà mới có:

```text
Area = 80 m²
Bedrooms = 3
Age = 8 năm
```

Hãy dùng mô hình vừa xây dựng để dự đoán giá.

Tức là tạo:

```text
X_new = [1, 80, 3, 8]
```

và tính:

**Ŷ_new = X_newβ**

---

# Phần 9 — Câu hỏi để kiểm tra hiểu bài

Sau khi code xong, hãy tự trả lời 5 câu này:

1. **β₁ có ý nghĩa gì?**
2. **β₂ có ý nghĩa gì?**
3. **β₃ có ý nghĩa gì?**
4. Nếu `Age` tăng 1 năm thì giá nhà dự đoán thay đổi thế nào, **giữ Area và Bedrooms không đổi**?
5. Tại sao OLS lại tìm β sao cho **SSE nhỏ nhất**?

---

## Knowledge map của bài này

Bạn có thể xem toàn bộ bài tập nằm trong nhánh:

```text
Linear Regression
│
├── Data
│   ├── X: Independent Variables
│   │   ├── Area
│   │   ├── Bedrooms
│   │   └── Age
│   │
│   └── Y: Dependent Variable
│       └── Price
│
├── Model
│   └── Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ε
│
├── OLS
│   └── β = (XᵀX)⁻¹XᵀY
│
├── Prediction
│   └── Ŷ = Xβ
│
├── Residual
│   └── e = Y − Ŷ
│
└── Loss
    └── SSE / RSS = Σe²
```

**Mình khuyên bạn làm theo đúng thứ tự Bài 1 → 8, chưa cần `sklearn` hay `statsmodels`.** Mục tiêu lần này là hiểu được **X → β → Ŷ → residual → SSE**, tức là đúng phần lõi của OLS mà bạn đang học.
