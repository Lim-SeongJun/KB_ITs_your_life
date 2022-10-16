def hello():
    print("Hello")
    
# 모듈로 사용되는 경우에는 테스트코드 실행 안되게
# 이 파일이 모듈로 사용된 경우
# __name__는 모듈명이 저장
# 이 파일이 독립실행되는 경우
# __name__는 __main__로 저장된다.

if __name__ == "__main__":
    hello() #테스트코드