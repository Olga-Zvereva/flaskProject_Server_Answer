from flask import Flask, render_template, make_response, redirect, url_for, request

app = Flask(__name__)

'''@app.route('/')
def index():
    #хотим вернуть строку
    body = render_template("index.html")
    res = make_response(body, 200)
    res.headers['Content-Type'] = "text/html"
    res.headers['Server'] = "Server_Answer"
    print(res)
    return res
'''

@app.route('/')
def index():
    return "<h1>Main Page</h1>", 200

@app.route('/login')
def login():
    log = ""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')
    res = make_response(f"<h1>Форма авторизации</h1><p>Logged: {log}")
    res.set_cookie("logged", "yes")
    return res

@app.route('/logout')
def logout():
    '''Выход - не авторизованы'''
    res = make_response("<h1>Вы больше не авторизованы</h1>")
    res.set_cookie("logged", "", 0) #удаление cookies
    return res

@app.errorhandler(404)
def index(error):
    return "<h1>Страница не найдена</h1>", 404

@app.route('/transfer')
def transfer():
    '''Перенаправление на другой url'''
    return redirect(url_for('show'), 301)


@app.route('/show_image')
def show():
    #хотим вернуть картинку
    img = None
    with  app.open_resource(app.root_path+"/static/images/Zina.jpg", mode="rb") as f:
        img = f.read()
    if img is None: return "No image"
    res = make_response(img)
    res.headers["Content-Type"] = "image/jpeg"
    return res

'''@app.before_first_request
def before_first_request():
    print ("Работает before_first_request()")

@app.before_request
def before_first_request():
    print ("Работает before_request()")

@app.after_request
def after_request(response):
    print ("Работает after_request()")
    return response

@app.teardown_request
def after_request(response):
    print ("Работает teardown_request()")
    return response'''


if __name__ == '__main__':
    app.run()
