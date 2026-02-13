# 👑 Locket Gold Activator Bot V2

Bot Telegram tự động kích hoạt Locket Gold (Premium) sử dụng phương pháp khai thác lỗ hổng receipt (RevenueCat Exploit).
Phiên bản nâng cấp với hỗ trợ đa luồng (Multi-threading), quản lý admin, và thông báo thời gian thực.

## ✨ Tính Năng
- **⚡ Kích Hoạt Tốc Độ Cao**: 2 luồng xử lý đồng thời, cooldown 45s mỗi worker.
- **🛡️ Bypass RevenueCat**: Inject receipt hợp lệ để active Locket Gold.
- **🌐 Tạo Anti-Revoke DNS**: Tự động tạo profile NextDNS để chặn check lại từ server.
- **👑 Admin Panel**: 
  - Broadcast thông báo (`/noti`).
  - Reset lượt dùng (`/rs`).
  - Xem thống kê chi tiết (`/stats`).
  - Cập nhật ảnh donate trực tiếp (`/setdonate`).
- **📊 Thống Kê Realtime**: Theo dõi số lượng request thành công/thất bại.

## 🛠️ Cài Đặt

### Yêu Cầu
- Python 3.8+
- Telegram Bot Token
- NextDNS API Key (để tạo profile chặn)

### Cài Đặt Nhanh
1. Clone repo này về máy:
   ```bash
   git clone https://github.com/thanhdo1110/Locket-Gold.git
   cd Locket-Gold
   ```

2. Cài đặt thư viện:
   ```bash
   pip3 install -r requirements.txt
   ```
   *(Nếu chưa có `requirements.txt`, chạy `pip3 install python-telegram-bot requests`)*

3. Cấu hình Bot:
   Sửa file `app/config.py`:
   - `BOT_TOKEN`: Token bot của bạn.
   - `ADMIN_ID`: ID Telegram của admin.
   - `NEXTDNS_KEY`: API Key NextDNS.
   - `TOKEN_SETS`: Thêm các token Locket vào đây (càng nhiều token càng nhiều luồng).

4. Chạy Bot:
   ```bash
   python3 main.py
   # Hoặc dùng script tiện ích:
   ./run.sh
   ```

## 📜 Danh Sách Lệnh
- `/start`: Khởi động bot & Menu chính.
- `/setlang`: Đổi ngôn ngữ (VI/EN).
- `/help`: Xem trợ giúp.

### Lệnh Admin
- `/noti [msg]`: Gửi thông báo đến tất cả user.
- `/rs [id]`: Reset lượt dùng cho user id.
- `/setdonate`: Reply ảnh hoặc gửi ảnh để set ảnh donate.
- `/stats`: Xem thống kê hệ thống.

## ⚠️ Lưu Ý
Tool này chỉ mang tính chất nghiên cứu và học tập (Educational Purpose Only).
