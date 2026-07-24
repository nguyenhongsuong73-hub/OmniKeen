import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView

class InternetOmniKeen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internet OmniKeen")
        self.setGeometry(100, 100, 1024, 768)

        # Widget chính và bố cục
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Thanh công cụ (Nút điều hướng và thanh địa chỉ)
        nav_layout = QHBoxLayout()
        nav_layout.setContentsMargins(5, 5, 5, 5)

        self.back_btn = QPushButton("←")
        self.back_btn.setFixedSize(40, 35)
        self.back_btn.clicked.connect(self.navigate_back)
        nav_layout.addWidget(self.back_btn)

        self.forward_btn = QPushButton("→")
        self.forward_btn.setFixedSize(40, 35)
        self.forward_btn.clicked.connect(self.navigate_forward)
        nav_layout.addWidget(self.forward_btn)

        self.reload_btn = QPushButton("🔄")
        self.reload_btn.setFixedSize(40, 35)
        self.reload_btn.clicked.connect(self.navigate_reload)
        nav_layout.addWidget(self.reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.setFixedHeight(35)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_layout.addWidget(self.url_bar)

        self.go_btn = QPushButton("Đi")
        self.go_btn.setFixedSize(60, 35)
        self.go_btn.clicked.connect(self.navigate_to_url)
        nav_layout.addWidget(self.go_btn)

        layout.addLayout(nav_layout)

        # Khung hiển thị trang web (WebEngine)
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # Sự kiện khi trang web thay đổi URL hoặc tải xong
        self.browser.urlChanged.connect(self.update_url_bar)
        
        # Mở trang chủ riêng home.html nằm cùng thư mục
        # Tự động lấy đường dẫn thư mục hiện tại chứa file omnikeen.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        home_path = os.path.join(current_dir, "home.html")
        # Trỏ thẳng tên file vì nó đã nằm chung một thư mục
        self.browser.setUrl(QUrl.fromLocalFile(home_path))

    def navigate_to_url(self):
        url_text = self.url_bar.text().strip()
        if not url_text.startswith("http://") and not url_text.startswith("https://") and not url_text.startswith("file:///"):
            if "." in url_text and " " not in url_text:
                url_text = "https://" + url_text
            else:
                # Nếu là từ khóa tìm kiếm, chuyển hướng sang Google Search
                url_text = f"https://www.google.com/search?q={url_text}"
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def navigate_back(self):
        self.browser.back()

    def navigate_forward(self):
        self.browser.forward()

    def navigate_reload(self):
        self.browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InternetOmniKeen()
    window.show()
    sys.exit(app.exec())