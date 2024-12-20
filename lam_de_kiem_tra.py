sieu_thi = []
while True:
    print("Quản Lí Siêu Thị.")
    print("Các Bước Lần Lượt: ")
    print("B1. Mã Hàng.")
    print("B2. Tên Hàng.")
    print("B3. Đơn vị tính.")
    print("B4. Đơn giá.")
    print("B5. Số lượng")
    lua_chon = input("Hãy lựa chọn yêu cầu của bạn: ")
    if lua_chon.isdigit() == False:
        raise ValueError("Yêu cầu nhập lại.")
    else:
        lua_chon = int(lua_chon)
        if lua_chon == 1:
            ma = input("Nhập vào mã sản phẩm: ")
            ten = input("Nhập tên sản phẩm: ")     
            don_vi = input("Nhập đơn vị tính: ")      
            don_gia = float(input("Nhập đơn giá của sản phẩm: "))      
            so_luong = int(input("Nhập số lượng sản phẩm: "))
    thanh_tien = (don_gia*so_luong) + (don_gia*so_luong)/10
    print(f"Thành tiền: {thanh_tien}")
    thue = thanh_tien/10
    print(f"Thuế VAT là: {thue}")
    break
