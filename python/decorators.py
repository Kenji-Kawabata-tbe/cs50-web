# 関数型プログラミング
#   関数が他の変数と同じように値として扱われる
#     デコレーター
#       ある関数を入力として受け取り、その関数を修正したものを出力として返す関数

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()


# 
