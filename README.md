# Trình chấm bài online mini THNMinOJ

## Giới thiệu sơ lược

Mục đích: 
Giúp HS tự luyện giống các trang như ntucoder,...

Đơn giản là HS đăng nhập, up bài làm và xem kết quả chấm (qua được bao nhiêu test).

GV chỉ cần up file zip chứa các test lên là có bài tập mới.

Vận hành tại http://test.thptccva.edu.vn

Tài khoản cho ai muốn thử nghiệm: guest, mk: thnam

hoặc liên hệ: http://m.me/huunam0 để tạo tk mới.

(chưa có chức năng đăng kí, còn nhiều chức năng nâng cao chưa code kịp)


## Hướng dẫn cài đặt:


+ Một VPS rẻ (5$/ tháng là được rồi) cài Ubuntu (hoặc HĐH tương tự). 
Ubuntu mặc định đã có python3 rồi.

+ Cài unzip và các trình biên dịch g++ , fpc .

+ Upload code lên 1 thư mục (chẳng hạn, /home/thnam/chambai )

+ Cài apache (hoặc webserver tương đương), trỏ root tới thư mục trên /home/thnam/chambai

+ Thêm cronjob chạy chamtudong.py mỗi phút 1 lần.

## Hướng dẫn sử dụng:

+ Thêm user mới: chạy user.py user_name

+ Thêm bài tập

  +Tạo thư mục bài tập:
    - Tên thư mục cũng là mã của bài toán
    - tệp chamthi.inf là file cấu hình của bài toán (xem ví dụ mẫu để biết)
    - tệp test*.inp và test*.out là các bộ test.
    
  +Nén thư mục lại thành file zip và up lên thư mục baitoan (/home/thnam/chambai/baitoan)
