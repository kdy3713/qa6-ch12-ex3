# 1부터 100까지 2와 5의배수 확인
for i in range(1, 101):
    if i % 2 == 0 or i % 5 == 0:
        # 2의 배수이거나 5의 배수인 경우 (10의 배수는 둘 다 해당)
        if i % 2 == 0 and i % 5 == 0:
            print("2와 5의 배수입니다")
        elif i % 2 == 0:
            print("2의 배수입니다")
        else:
            print("5의 배수입니다")
    else:
        print(i)