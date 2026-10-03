import pandas as pd
import numpy as np

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
print(df['SSE'].sum())

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

