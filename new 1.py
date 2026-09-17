class LienLac:
    def __init__(self, ten, sdt, email):
        self.ten = ten
        self.sdt = sdt
        self.email = email

    def hien_thi(self):
        print(f"Tên: {self.ten} | SĐT: {self.sdt} | Email: {self.email}")


class QuanLyDanhBa:
    def __init__(self):
        self.danh_sach = []

    def them_lien_lac(self, ten, sdt, email):
        lien_lac_moi = LienLac(ten, sdt, email)
        self.danh_sach.append(lien_lac_moi)
        print(f"Đã thêm {ten} vào danh bạ.")

    def hien_thi_tat_ca(self):
        if not self.danh_sach:
            print("Danh bạ trống.")
        else:
            print("--- DANH BẠ ---")
            for ll in self.danh_sach:
                ll.hien_thi()

    def tim_kiem(self, tu_khoa):
        ket_qua = [ll for ll in self.danh_sach if tu_khoa.lower() in ll.ten.lower()]
        if not ket_qua:
            print(f"Không tìm thấy liên lạc nào với từ khóa '{tu_khoa}'.")
        else:
            print(f"--- KẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ---")
            for ll in ket_qua:
                ll.hien_thi()


# Chương trình chính
if __name__ == "__main__":
    quan_ly = QuanLyDanhBa()
    quan_ly.them_lien_lac("Nguyễn Văn A", "0123456789", "vana@email.com")
    quan_ly.them_lien_lac("Trần Thị B", "0987654321", "thib@email.com")
    
    quan_ly.hien_thi_tat_ca()
    quan_ly.tim_kiem("Nguyễn")
