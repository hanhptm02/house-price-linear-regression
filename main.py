from asyncio import constants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đề bài OLS
# Phần 1 - Làm quen với dữ liệu
# Tạo DataFrame bằng pandas.
df = pd.read_csv("house_price.csv")
print(df)

# Xem số dòng, số cột
print(df.shape)

# Xem kiểu dữ liệu
print(df.dtypes)

# Kiểm tra missing values
print(df.isnull().sum())

# Phần 2 - Tách X và Y
X = df[['Area', 'Bedrooms', 'Age']]
Y = df[['Price']]

print(X)
print(Y)
print(X.shape)
print(Y.shape)

# Phần 3 - Thêm intercept
X['Intercept'] = 1
X = X[['Intercept', 'Area', 'Bedrooms', 'Age']]
print(X)
print(X.shape)

# Phần 4 - Tính hệ số OLS bằng NumPy
# Chuyển thành array numpy để tính toán ma trận
X_mat = X.to_numpy()
Y_mat = Y.to_numpy()
print(X)
print(Y)

# Tính Xᵀ
XT = X_mat.T
print(XT)

# Tính XᵀX
XT_X = XT @ X_mat
print(XT_X)

# Tính (XᵀX)⁻¹
XT_X_inv = np.linalg.inv(XT_X)
print(XT_X_inv)

# Tính XᵀY
XT_Y = XT @ Y_mat
print(XT_Y)

# Tính β = (XᵀX)⁻¹XᵀY
beta = XT_X_inv @ XT_Y
print(beta)

# Phần 5 - Prediction
df['Predicted_Price'] = X @ beta
print(df)

# Phần 6 - Residual
df['Residual'] = df['Price'] - df['Predicted_Price']
print(df)

# Kiểm tra tổng Residual
print(df['Residual'].sum())

# Phần 7 - SSE / RSS
df['SSE'] = df['Residual'] ** 2
print(df)

# Tổng SSE
SSE = df['SSE'].sum()
print(SSE)

# Phần 8 - Thử dự đoán một căn nhà mới
X_new = np.array([1, 80, 3, 8])
print(X_new)

# Tính Ŷ_new = X_newβ
Y_new = X_new @ beta
print(Y_new)

# Phần 9 - Diễn giải phương trình
'''
B0: 633.10626703
B1: 26.03996367
B2: 326.40781108
B3: -13.3106267

B0: Ảnh hưởng của tất cả các biến khác tới giá nhà
B1: Trong điều kiện biến khác không đổi, diện tích tăng 1m2 thì giá nhà tăng 26.03996367 triệu đồng.
B2: Trong điều kiện biến khác không đổi, số phòng ngủ tăng 1 phòng thì giá nhà tăng 326.40781108 triệu đồng.
B3: Trong điều kiện biến khác không đổi, tuổi nhà tăng 1 năm thì giá nhà giảm 13.3106267 triệu đồng.
'''

# Đề bài R2
# Bài 1 - Tính Hệ số xác định R2
# Tính Y trung bình
Y_mean = Y_mat.mean()

# Tính tổng bình phương sai lệch toàn phần TSS
TSS = ((Y_mat - Y_mean) ** 2).sum()

# Tính R2
R2 = 1 - (SSE/TSS)
print(R2)

# Bài 2 - Giải thích ý nghĩa của R2
'''
Mô hình giải thích 99.91% sự biến thiên của giá nhà
'''

# Bài 3 - Tính Adjusted R2
n = df.shape[0]
k = X.shape[1] - 1
print(n)
print(k)
Adjusted_R2 = 1 - ((1 - R2) * (n - 1) / (n - k - 1))
print(Adjusted_R2)

# Bài 4 - So sánh R2 và Adjusted R2
print(R2)
print(Adjusted_R2)

'''
Tại sao Adjust R2 thường nhỏ hơn R2
--> Trong công thức của Adjust R2 có k, k tăng thì Adjust R2 càng nhỏ
'''

# Đề bài Phương sai sai số
# Bài 1 - Tính phương sai sai số và độ lệch chuẩn sai số
# Tính phương sai sai số (sigma^2)
sigma2 = SSE / (n - k - 1)
print(sigma2)

# Tính độ lệch chuẩn sai số (sigma)
sigma = np.sqrt(sigma2)
print(sigma)

# Bài 2 - Nhận xét về quy mô sai số
'''
1. Quy mô sai số tuyệt đối:
   - Độ lệch chuẩn sai số sigma ≈ 27.09 triệu đồng.
   - Cho biết: mức chênh lệch trung bình (điển hình) giữa giá nhà thực tế và giá nhà dự đoán
     rơi vào khoảng 27 triệu đồng mỗi căn.

2. So sánh tương quan với giá nhà:
   - Giá nhà dao động từ 2,500 đến 4,800 triệu đồng (giá trung bình là 3,550 triệu đồng).
   - Tỷ lệ sai số: 27.09 / 3,550 ≈ 0.76% (chưa tới 1% giá trị căn nhà).

--> Kết luận: Quy mô sai số khoảng 27 triệu VNĐ là rất nhỏ, khẳng định mô hình có độ chính xác rất cao.
'''
# Bài 3 - Kiểm tra phương sai sai số thay đổi
# Thêm cột Giá trị tuyệt đối của Residual
df["Residual_abs"] = df["Residual"].abs()
print(df)

# Tạo 2 nhóm với giá dự đoán thấp và cao
# 5 nhà có giá dự đoán thấp nhất
price_low = df.sort_values(by='Predicted_Price').iloc[0:5, :]
print(price_low)

# 5 nhà có giá dự đoán cao nhất
price_high = df.sort_values(by='Predicted_Price').iloc[5:10, :]
print(price_high)

# So sánh độ phân tán phần dư theo nhóm giá trị dự đoán
print("Độ phân tán phần dư của nhóm giá dự đoán thấp:", price_low['Residual_abs'].mean())
print("Độ phân tán phần dư của nhóm giá dự đoán cao:", price_high['Residual_abs'].mean())

'''
Nhận xét Bài 3: 
Mức sai số trung bình giữa 2 nhóm chênh lệch rất ít (17.45 vs 19.85), 
cho thấy phương sai sai số giữa hai nhóm tương đối đồng đều (Homoskedasticity).
'''

# Bài 4 - Vẽ biểu đồ Residual Plot
plt.scatter(df['Predicted_Price'], df['Residual'])
plt.xlabel("Predicted Price")
plt.ylabel("Residual")
plt.title("Residual Plot")
plt.axhline(y=0, color='r', linestyle='--')
plt.show()

'''
Từ biểu đồ residual plot, ta quan sát được:
- Các điểm phần dư phân tán ngẫu nhiên quanh đường y=0
- Không có dấu hiệu rõ ràng của heteroskedasticity
- Độ phân tán phần dư có xu hướng không đổi khi Predicted_Price thay đổi
'''

# Đề bài kiểm định Hệ số hồi quy
# Kiểm định hệ số diện tích
# 1. Lấy giá trị ước lượng beta1
beta1 = beta[1][0]
print(beta1)

# Tính Standard Error của beta1
SE_beta1 = np.sqrt(XT_X_inv[1][1])
print(SE_beta1)

# Tính t-statistic của beta1
t_beta1 = beta1 / SE_beta1
print(t_beta1)

# Tính p-value của beta1
p_beta1 = 2 * (1 - stats.t.cdf(abs(t_beta1), df))
print(p_beta1)

# Kiểm định giả thuyết