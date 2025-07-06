import matplotlib.pyplot as plt

# Dữ liệu mẫu
mon_hoc = ['Toán', 'Văn', 'Lý', 'Hóa', 'Anh']
diem = [8.5, 7.0, 9.0, 8.0, 7.5]
mau_cot = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1']  # mỗi cột một màu

# Cài đặt kích thước biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ cột
bars = plt.bar(mon_hoc, diem, color=mau_cot, width=0.6)

# Thêm tiêu đề và nhãn trục
plt.title('Biểu đồ điểm các môn học', fontsize=16)
plt.xlabel('Môn học', fontsize=12)
plt.ylabel('Điểm số', fontsize=12)

# Thêm lưới nền
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Hiển thị số điểm trên đầu cột
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2,
             height + 0.1,
             f'{height}',
             ha='center',
             va='bottom',
             fontsize=10)

# Giới hạn trục tung để tạo khoảng trống phía trên
plt.ylim(0, max(diem) + 2)

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
