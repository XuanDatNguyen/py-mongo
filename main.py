from student import Student

student = Student()

while (True):

    print("**********************MENU QUẢN LÝ SINH VIÊN**********************")
    print("**  0. Thoát                                                    **")
    print("**  1. Thêm sinh viên.                                          **")
    print("**  2. Hiển thị tất cả sinh viên có cùng thông tin về điểm số.  **")
    print("**  3. Xóa sinh viên với ID nhập vào từ bàn phím.               **")
    print("**  4. Tìm kiếm sinh viên theo tên, tuổi.                       **")
    print("**  5. Tìm kiếm sinh viên có điểm môn xxx > yyy.                **")
    print("**  6. Tìm kiếm sinh viên có tổng điểm 3 môn > xxx.             **")
    print("******************************************************************")
    key = int(input("Nhập lựa chọn menu dạng số: "))
    if key == 0:
        print("Thoát chương trình!!!")
        break
    elif key == 1:
        student.createStudent()
    elif key == 2:
        pass
    elif key == 3:
        student_id = input("Nhập vào id sinh viên cần xóa: ")
        student.deleteStudent(student_id)
    elif key == 4:
        name = input("Nhập họ và tên sinh viên cần tìm kiếm : ")
        age = input("Nhập tuổi sinh viên cần tìm kiếm: ")
        std = student.searchStudent(name, age)
        student.showStudent(std)
    elif key == 5:
        print("Mời bạn lựa chọn môn học cần so sánh \"TO\": Toán, \"LY\": Lý, \"HO\": Hóa")
        subject1 = input("Mời bạn lựa chọn môn học thứ nhất: ").upper()
        subject2 = input("Mời bạn lựa chọn môn học thứ 2: ").upper()
        std = student.findStudentByCompareScore(subject1, subject2)
        student.showStudent(std)
    elif key == 6:
        total_score = input("Mời bạn nhập vào tổng điểm 3 môn: ")
        std = student.findStudentByTotalScore(total_score)
        student.showStudent(std)
    else:
        print("\nChức năng không tồn tại")
        print("Vui lòng chọn lại menu")
