import streamlit as st
USERS=["admin"]
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

def login():
    st.title("Đăng nhập")
    username=st.text_input("Tên đăng nhập")
    if st.button("Đăng nhập"):
        if username:
            if username in USERS:
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.session_state.logged_in = False
                st.session_state.username = None
                st.warning(f'{username} không phải là người dùng hợp lệ')
        else:
            st.warning("Vui lòng nhập tên đăng nhập")
def factorial_calculate():
    st.write(f"Chào mừng {st.session_state.username} đến với ứng dụng tính giai thừa!")
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("Đăng xuất thành công!")
        st.rerun()
    n = st.number_input("Nhập số nguyên dương n", min_value=0, max_value=900, step=1)
    if st.button("Tính giai thừa"):
        if n < 0:
            st.error("Vui lòng nhập số nguyên dương")
        else:
            result = fact(n)
            st.success(f"Giai thừa của {n} là: {result}")
            st.balloons()
def main():
    st.write("Tính giai thừa")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if st.session_state.logged_in:
        factorial_calculate()
    else:
        login()
        
if __name__ == "__main__":
    main()