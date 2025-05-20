---
Ghost Your BE - Cái Bóng BE của bạn
< Vietnamese > là nền tảng hỗ trợ kỹ thuật viên phần mềm chuyển đổi nhanh chóng các mô tả schema (database/API) thành dữ liệu mẫu, mock API phục vụ frontend, và đồng bộ hóa kiểm thử với API backend thực tế — tối ưu quy trình phát triển và cộng tác giữa các nhóm.
* Nhập cấu hình **`schema.yml`** → sinh dữ liệu mẫu + lưu vào DB thật
* Nhập **API endpoint** → cấu hình + mapping sang DB
* Sinh **Mock API tự động** hỗ trợ frontend dev
* So sánh **Mock API vs Real API** → cảnh báo sai lệch
---
< English > is a developer-first platform that transforms database schemas and APIs into production-ready data samples, mock APIs for frontend teams, and validated sync with real backend endpoints — ensuring smooth collaboration across the stack.
* Import configuration `schema.yml` → generate sample data + save to real DB
* Enter API endpoint → configuration + mapping to DB
* Generate Mock API automatically** to support frontend dev
* Compare Mock API vs Real API** → alert discrepancies
---
Structure
>
ghost-your-be/
├── cli.py                   # Main CLI commands
├── generators/              # Data generation logic
│   ├── vietnam_provider.py  # Custom Faker provider
│   ├── schema_loader.py     # Load và validate schema.yml
│   └── data_generator.py    # Tạo dữ liệu mẫu
├── database/                # Database integration
│   ├── db_connector.py      # Kết nối và lưu dữ liệu vào DB
│   └── db_config.py         # Tạo cấu hình DB từ API
├── mock_api/                # Mock API logic
│   ├── mock_server.py       # FastAPI server cho mock API
│   └── api_generator.py     # Tạo response API từ schema
├── comparers/               # API comparison logic
│   └── api_diff.py          # So sánh mock API và API thật
├── utils/                   # Utilities
│   ├── license.py           # Xử lý license key
│   └── file_exporter.py     # Xuất dữ liệu ra file
├── tests/                   # Unit tests
│   ├── test_generators.py
│   ├── test_database.py
│   └── test_mock_api.py
├── setup.py                 # Package configuration
└── README.md                # Documentation