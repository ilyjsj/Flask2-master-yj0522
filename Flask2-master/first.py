from flask import Flask, request     # Flask : class
app = Flask(__name__)       # 생성자가 불려지면 객체를 만들기 위해 -> def __init__(self, kkkk):
@app.route('/search')
def search():
    to_echo = request.args.get("input","")
    response = "{}".format(to_echo)
#    print(to_echo)
#    print(response)
#    return response
#    print(type(to_echo))
    return response

if __name__ == "__main__":
    app.run()