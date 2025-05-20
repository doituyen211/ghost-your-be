from faker.providers import BaseProvider
import random

class VietnamProvider(BaseProvider):
    
    def vietnam_phone(self):
        return "+84" + self.numerify("9########")
    
    def vietnam_name(self):
        first_names = ["Anh", "An", "Bảo", "Bình", "Cường", "Dũng", "Duy", "Đạt", "Đức", "Hiếu",
    "Hoàng", "Hùng", "Huy", "Khoa", "Khánh", "Lâm", "Long", "Minh", "Nam", "Nghĩa",
    "Phong", "Phúc", "Quân", "Quang", "Sơn", "Thành", "Thiện", "Thịnh", "Tú", "Tuấn",
    "Tùng", "Việt", "Vũ", "Xuân", "Tài", "Tâm", "Thắng", "Tiến", "Trung", "Trường",
    "Hải", "Hào", "Hiệp", "Linh", "Mạnh", "Ngọc", "Nhân", "Phương", "Thanh", "Toàn",
    "Chi", "Dung", "Hà", "Hạnh", "Hiền", "Hoa", "Hồng", "Huệ", "Hương", "Lan",
    "Liên", "Loan", "Mai", "My", "Nga", "Ngân", "Nhung", "Nhi", "Như", "Oanh",
    "Phương", "Quyên", "Thảo", "Thi", "Thu", "Thúy", "Thủy", "Tiên", "Trang", "Trinh",
    "Tuyết", "Vân", "Yến", "Xuân", "Châu", "Diệp", "Diễm", "Giang", "Hằng", "Kim",
    "Khánh", "Linh", "Ly", "Mỹ", "Ngọc", "Quỳnh", "Thanh", "Thơ", "Trâm", "Uyên"]
        middle_names = ["Thị", "Văn", "Đức", "Thế", "Thái", "Quốc", "Ngọc", "Thành", "Hữu", "Trọng",]
        last_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng",
    "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Đinh", "Trịnh", "Đào", "Đoàn",
    "Vương", "Trương", "Tạ", "Lưu", "Lương", "Mai", "Cao", "Thái", "Châu", "Tô",
    "Tăng", "Hà", "Quách", "Tôn", "Mạc", "Lâm", "Thạch", "Diệp", "Phùng", "Tống",
    "Kiều", "Liêu", "Lã", "Hứa", "La", "Thân", "Triệu", "Trang", "Nhữ", "Tôn Nữ",
    "Tiêu", "Doãn", "Chu", "Diêm", "Vi", "Khúc", "Tạ", "Giang", "Bạch", "Từ",
    "Âu", "Hàn", "Thẩm", "Thập", "Ninh", "Lục", "Chế", "Khổng", "Thủy", "Tất",
    "Khuất", "Mã", "Từ", "Chung", "Thái", "Tăng", "Sơn", "Kim", "Kha", "Tiêu",
    "Lục", "Hàn", "Đường", "Ông", "An", "Bành", "Nhâm", "Cù", "Nghiêm", "Kỳ",
    "Lại", "Phó", "Ân", "Danh", "Dư", "Tăng", "Thiều", "Văn"]
        return f"{self.random_element(last_names)} {self.random_element(middle_names)} {self.random_element(first_names)}"
    
    def vietnam_address(self):
        provinces = ["Hà Nội", "TP.HCM", "Đà Nẵng", "Cần Thơ"]
        street_address = ["Nguyễn Thị Minh Khai", "Lê Lợi", "Trần Hưng Đạo", "Đường 1/5", "Đường số 1"]
        return f"{self.random_element(provinces)}, {self.random_element(street_address)}"
    
    def vietnam_id(self):
        return self.numerify("0###########")