for i in range(1,101,1):
    #숫자를 문자열로 치환해서 알아봄
    num = str(i)
    #num에  3,6,9가 있는지 확인 
    # ex) 33이면 3일 때 count 2개고 나머지는 0 총 2 / 결과 : 33 짝짝 
    # ex) 13 이면 count 1개 나머지 0 / 결과: 13 짝
    # ex) 7 이면 count 0개 / 결과: 7
    count = num.count('3') + num.count('6') + num.count('9')
        #0보다 크고 3,6,9가 있을때 숫자 나오고 짝을 곱해서 출력
    if count > 0:
        print(f"{i} {'짝' * count}")
        #없으면 그냥 숫자만 출력
    else:
        print(i)
        