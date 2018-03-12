#coding=utf-8
import web

urls=(
    '/hello','Hello',
    '/','Getda'
)

app=web.application(urls,globals())
render=web.template.render('template/')

class Hello:
    def POST(self):
        data=web.input()
        print data
        return "true"

class Getda:
    def GET(self):
        return render.sendda()

if __name__=='__main__':
    app.run()