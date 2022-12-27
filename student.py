from conn import students
from bson.objectid import ObjectId


class Student():
    # Tạo sinh viên
    def createStudent(self):
        name = input("Nhập vào họ và tên: ")
        age = input("Nhập vào tuổi: ")
        gender = input("Nhập vào giới tính: ")
        math = input("Nhập vào điểm toán: ")
        physics = input("Nhập vào điểm vật lý: ")
        chemistry = input("Nhập vào điểm hóa học: ")
        student = {
            "name": name,
            "age": age,
            "gender": gender,
            "scores": [math, physics, chemistry],
            "total": float(math) + float(physics) + float(chemistry)
        }
        student_id = students.insert_one(student).inserted_id
        print(F"\nTạo thành công sinh viên: {student_id}\n")

    # Hiển thị các sinh viên cùng thông tin về điểm số
    def getAllStudentInfo(self):
        return students.find({})

    # Tìm kiếm sinh viên có điểm môn xxx > yyy
    def findStudentByCompareScore(self, subject1, subject2):
        dict = {"TO": 0, "LY": 1, "HO": 2}
        results = students.find(
            {
                "$expr": {
                    "$gt": [
                        {"$arrayElemAt": ["$scores", dict[subject1]]},
                        {"$arrayElemAt": ["$scores", dict[subject2]]}
                    ]
                }
            }
        )
        return results

    # Xóa sinh viên với ID
    def deleteStudent(self, student_id):
        student = students.delete_one({"_id": ObjectId(student_id)})
        print(F"\nBạn đã xóa thành công sinh viên id: {student_id}\n")

    # Tìm kiếm sinh viên theo tên, tuổi
    def searchStudent(self, name, age):
        query = {"name": name, "age": age}
        results = students.find(query)
        return results

    # Tìm kiếm sinh viên có tổng điểm 3 môn > xxx
    def findStudentByTotalScore(self, total_score):
        query = {"total": {"$gt": float(total_score)}}
        results = students.find(query)
        return results

    def showStudent(self, stds):
        print(
            "\n\n*********************************DANH SÁCH SINH VIÊN**********************************")
        print(
            "**                                                                                  **")
        print("** {:<20} {:<15} {:<10} {:<10} {:<10} {:<10} **"
              .format("Họ và tên", "Giới tính", "Tuổi", "Toán", "Lý", "Hóa"))
        for std in stds:
            print("** {:<20} {:<15} {:<10} {:<10} {:<10} {:<10} **"
                  .format(std["name"], std["gender"], std["age"], std["scores"][0], std["scores"][1], std["scores"][2]))
        print(
            "**************************************************************************************\n\n")
