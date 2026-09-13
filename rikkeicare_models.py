class NhanVienYTe:
    def __init__(self, ma_nhan_vien: str, ho_ten: str, so_dien_thoai: str):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.so_dien_thoai = so_dien_thoai

    def get_thong_tin(self) -> str:
        return f'[{self.ma_nhan_vien}] {self.ho_ten} - SĐT: {self.so_dien_thoai}'


class BacSi(NhanVienYTe):
    def __init__(self, ma_nhan_vien: str, ho_ten: str, so_dien_thoai: str, chuyen_khoa: str):
        super().__init__(ma_nhan_vien, ho_ten, so_dien_thoai)
        self.chuyen_khoa = chuyen_khoa

    def kham(self, benh_nhan: str) -> None:
        print(f'Bác sĩ {self.ho_ten} ({self.chuyen_khoa}) đang khám cho bệnh nhân {benh_nhan}.')


class YTa(NhanVienYTe):
    def __init__(self, ma_nhan_vien: str, ho_ten: str, so_dien_thoai: str, khu_vuc_truc: str):
        super().__init__(ma_nhan_vien, ho_ten, so_dien_thoai)
        self.khu_vuc_truc = khu_vuc_truc

    def tiem_thuoc(self, benh_nhan: str) -> None:
        print(f'Y tế {self.ho_ten} (Khu vực {self.khu_vuc_truc}) đang tiêm thuốc cho bệnh nhân {benh_nhan}.')


class KhoaKham:
    def __init__(self, ma_khoa: str, ten_khoa: str):
        self.ma_khoa = ma_khoa
        self.ten_khoa = ten_khoa
        self.danh_sach_nhan_vien: list[NhanVienYTe] = []

    def them_nhan_vien(self, nhan_vien: NhanVienYTe) -> None:
        self.danh_sach_nhan_vien.append(nhan_vien)
        print(f'Đã thêm nhân viên {nhan_vien.ho_ten} vào khoa {self.ten_khoa}.')

    def xoa_nhan_vien(self, ma_nhan_vien: str) -> NhanVienYTe | None:
        for nv in self.danh_sach_nhan_vien:
            if nv.ma_nhan_vien == ma_nhan_vien:
                self.danh_sach_nhan_vien.remove(nv)
                print(f'Đã điều chuyển/xóa nhân viên {nv.ho_ten} khỏi khoa {self.ten_khoa}.')
                return nv
        return None
