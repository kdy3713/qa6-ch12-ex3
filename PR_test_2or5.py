# 1부터 100까지 2와 5의배수 확인
for i in range(1, 101):
    print(i)
    if i % 2 == 0 and i % 5 == 0:
        print("2와 5의 배수입니다")
    elif i % 2 == 0:
        print("2의 배수입니다")
    elif i % 5 == 0:
        print("5의 배수입니다")



    # 100부터 1까지 -1씩 감소
    for i in range(100, 0, -1):
        num = str(i)
        
        # 3, 6, 9 개수 카운트
        count = num.count('3') + num.count('6') + num.count('9')
        
        # 3, 6, 9가 들어있으면 개수만큼 '짝' 출력
        if count > 0:
            print(f"{i} {'짝' * count}")
        # 없으면 숫자만 출력
        else:
            print(i)