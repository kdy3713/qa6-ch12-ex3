from User import User


class Post:  # 글 하나
    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):

        # 속성들을 초기화합니다.
        self.author = author
        self.content = content

        # 아래의 코드를 수정하세요.
        self.likes = []

    # num_likes 메소드를 생성합니다.
    # 아래의 코드를 수정해서 메소드를 완성하세요.
    def num_likes(self):
        return len(self.likes)

    # like 메소드를 생성합니다.
    # 아래의 코드를 수정해서 메소드를 완성하세요.
    def like(self, user):
        if user not in self.likes:
            self.likes.append(user)


# 새로운 사용자 me를 생성합니다.
me = User("Elice")
tom = User("Tom")

# 아래에 자유롭게 인스턴스를 생성하고 테스트해 보세요.
my_post = Post(me, "안녕하세요")
my_post.like(me)
my_post.like(tom)
print(my_post.content)
print(my_post.num_likes())
