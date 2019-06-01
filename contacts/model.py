"""
name, phone, email, addr
"""
class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):   # getter
        print('이름 : {}, 전화번호 : {}, 이메일 : {}, 주소 : {}'.format(self.name, self.phone, self.email, self.addr))

    @staticmethod   # 파이썬에서는 self를 써야하는게 필수이지만 이를 쓰지않고 스칼라가 아닌 백터(집단) 데이터로 접근할 때 사용하는 annotation
    def set_contact():
        name = input('이름')
        phone = input('전화번호')
        email = input("이메일")
        addr = input('주소')
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contacts(list):
        for i in list:
            i.print_info()

    @staticmethod
    def del_contact(list, name):
        for i, t in enumerate(list):    # enumerate : 1회만 순환, loop : 여러번 순환
            if t.name ==name:
                del list[i]

    def print_menu():
        print('1. 연락처 입력')
        print('2. 연락처 출력')
        print('3. 연락처 삭제')
        print('4. 종료')
        menu = input('메뉴 선택')
        return  int(menu)

    @staticmethod
    def run():
        list = []
        while 1 :
            menu = Contact.print_menu()
            if menu == 1:
                t = Contact.set_contact()
                list.append(t)
            elif menu == 2:
                Contact.get_contacts(list)
            elif menu == 3:
                name = input('삭제할 이름')
                Contact.del_contact(list, name)
            elif menu == 4:
                break
