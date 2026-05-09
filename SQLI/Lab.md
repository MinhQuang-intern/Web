**Kiến thức về SQL Injection**

```Khái niệm```

- SQL Injection là lỗ hổng bảo mật web cho phép kẻ tấn công can thiệp vào các truy vấn mà ứng dụng thực hiện đối với CSDL của nó 

```Nguyên nhân```

- Do ứng dụng ghép trực tiếp input của user vào câu lệnh query
- Không validate dữ liệu đầu vào 

```Tác động```

- Bypass đăng nhập 
- Dump toàn bộ database (user,password)
- Sửa/xóa dữ liệu 
- RCE
- Chiếm quyền admin hệ thống 

```Điều kiện xảy ra```

- Input user được đưa vào câu truy vấn 
- Backend xử lý input không an toàn 
- Không có cơ chế escaping đúng 

LAB: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
Mục tiêu là làm xuất hiện các sản phẩm chưa phát hành 

![alt text](images/image.png)

- Ta bắt gói tin trong burp và gửi đến repeater 

![alt text](images/image-1.png)

Ta thử gõ cách test lỗ hổng SQLI bằng các thêm '-- vào đằng sau 

![alt text](images/image-2.png)

-> Ta nhận thay server trả về 200 OK 
-> Có lỗ  hổng SQLI ở đây 

Ta bypass bằng cách sau 

![alt text](images/image-3.png)

Bypass: ?category='+OR+1=1--

Ở đây khi user chọn 1 categories, application sẽ sử dụng 1 query như:

SELECT * FROM products WHERE category = 'Gifts' AND released = 1

Sau khi dùng dấu ' để đóng lại thì ở đằngc sau là  1 mệnh đề luôn đúng thì các sản phẩm ẩn sẽ hiện ra 




