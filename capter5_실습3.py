from validators import validate_email


# 유효성 검사 사용자로부터 입력값이 유효한 값이냐 확인하는 작업
class User:
    def __init__(self, email, password=None, name=None, gender=None, friends=None):

        # 이메일이 형식에 맞는지 확인하고, 설정합니다.
        self.email = validate_email(email)
        # if validate_email(email):
        #     pass
        # else print(valueError("이메일 형식 아님"))

        # 비밀번호가 조건을 만족하는지 확인하고, 설정합니다.
        self.password = password
        # if len(password)>8
        #     pass
        # else print(valueError("비밀번호 8자 이상"))

        # 사용자의 이름이 조건을 만족하는지 확인하고, 설정합니다.
        self.name = name
        # if

        # 성별이 조건을 만족하는지 확인하고, 설정합니다.
        self.gender = None

        # 친구 목록을 설정합니다.
        self.friends = []
        if friend != None:
            self.friends.append(friend)


email = input()
password = input()
name = input()
gender = input()
fried = input()
