# Odoo Development Environment - Assignment Questions

## Câu hỏi 1: Vai trò của từng service trong Docker Compose setup

### Câu hỏi:
Hãy giải thích vai trò của từng service trong Docker Compose setup của Odoo.

### Câu trả lời mẫu:
Trong Docker Compose setup, chúng ta có 2 service chính:

1. **Web Service (Odoo):**
   - Sử dụng image `odoo:16.0`
   - Mở port 8069 để truy cập web
   - Mount 2 volume:
     - `./config:/etc/odoo` cho file cấu hình
     - `./addons:/mnt/extra-addons` cho các module tùy chỉnh
   - Kết nối database thông qua biến môi trường
   - Chạy ở chế độ development (`--dev=all`)

2. **Database Service (PostgreSQL):**
   - Sử dụng image `postgres:15`
   - Thiết lập thông tin đăng nhập database ban đầu
   - Duy trì dữ liệu thông qua volume `odoo-db-data`
   - Xử lý tất cả các thao tác database cho Odoo

## Câu hỏi 2: Kết nối Odoo với database

### Câu hỏi:
Giải thích cách Odoo kết nối với database trong setup của bạn.

### Câu trả lời mẫu:
Odoo kết nối với PostgreSQL thông qua các điểm cấu hình sau:

1. **Trong docker-compose.yml:**
   ```yaml
   environment:
     - HOST=db
     - USER=odoo
     - PASSWORD=odoo
   ```

2. **Trong config/odoo.conf:**
   ```ini
   db_host = db
   db_port = 5432
   db_user = odoo
   db_password = odoo
   db_name = odoo
   ```

Kết nối được thiết lập sử dụng:
- Host: Tên service `db` (DNS nội bộ của Docker)
- Port: 5432 (port mặc định của PostgreSQL)
- Thông tin đăng nhập: Username và password từ biến môi trường
- Tên database: `odoo`

## Câu hỏi 3: Lợi ích của chế độ debug

### Câu hỏi:
Nêu các lợi ích của việc sử dụng chế độ debug cho developers.

### Câu trả lời mẫu:
Chế độ debug (`?debug=1`) cung cấp nhiều lợi ích:

1. **Tính năng kỹ thuật:**
   - Truy cập menu kỹ thuật
   - Xem thông tin kế thừa
   - Kiểm tra thuộc tính trường
   - Hiển thị tài nguyên debug

2. **Công cụ phát triển:**
   - Xem QWeb templates
   - Truy cập công cụ developer
   - Xem tài liệu kỹ thuật
   - Debug JavaScript

3. **Giám sát hiệu suất:**
   - Xem các truy vấn SQL
   - Theo dõi thời gian request
   - Kiểm tra sử dụng bộ nhớ
   - Debug cache

## Câu hỏi 4: Ý nghĩa của log entry ORM

### Câu hỏi:
Giải thích ý nghĩa của một log entry liên quan đến ORM trong Odoo.

### Câu trả lời mẫu:
Xét log entry trong `res_partner.py`:

```python
def create(self, vals):
    _logger.info('Creating new partner with values: %s', vals)
    partner = super(ResPartner, self).create(vals)
    _logger.info('Partner created successfully with ID: %s', partner.id)
    return partner
```

Log entry này có ý nghĩa vì:
1. Thể hiện việc tự động tạo ID của ORM
2. Hiển thị quá trình tạo record hoàn chỉnh
3. Cung cấp khả năng theo dõi dữ liệu đang được lưu
4. Hỗ trợ debug các vấn đề về tính toàn vẹn dữ liệu
5. Thể hiện mối quan hệ giữa Python objects và database records

## Câu hỏi 5: So sánh Community và Enterprise

### Câu hỏi:
Nêu các điểm khác biệt chính giữa phiên bản Community và Enterprise của Odoo.

### Câu trả lời mẫu:

**Phiên bản Community:**
1. Miễn phí và mã nguồn mở
2. Tính năng cơ bản cho:
   - CRM
   - Bán hàng
   - Kho
   - Kế toán
   - Website
3. Hỗ trợ hạn chế
4. Phát triển dựa vào cộng đồng
5. Tính năng báo cáo cơ bản

**Phiên bản Enterprise:**
1. Trả phí theo gói
2. Tính năng bổ sung:
   - Báo cáo nâng cao
   - Studio (công cụ tùy chỉnh)
   - Quản lý tài liệu
   - Kho nâng cao
   - Hỗ trợ đa công ty
3. Module bổ sung:
   - Quản lý dự án
   - Timesheet
   - Sản xuất nâng cao
   - Kế toán nâng cao
   - HR nâng cao
4. Hỗ trợ và dịch vụ:
   - Hỗ trợ chính thức
   - Cập nhật thường xuyên
   - Ứng dụng di động
   - Tùy chọn hosting đám mây
   - Tối ưu hiệu suất tốt hơn
   - Tính năng bảo mật nâng cao 