import time



Dict_web_methon=dict()

#装饰器完成路由
def route(sample):

    def  set_func(func):

        Dict_web_methon[sample]=func
        #再装饰新功能之前， 就添加进“路由表”

        def  create_func():
            ''' new  func装饰部分'''
            #Dict_web_methon[sample]:func

            return func()

        return create_func

    return set_func




@route('/login.html')
def  login():
    return ("1---login %s" %time.ctime())


@route('/register.html')
def  register():
    return "2--register"

#Dict_web_methon=dict()
#   #添加网页
#   '/login.py':login,
#   './register.py':register

# }


#def  application(request_http):
def  application(env,start_respon):
    '''application函数是 WSGI标准的 HTTP处理函数 '''
    start_respon('200 OK',[('Content-Type','text/html;charset=utf-8'),('server','mini_frame v1.0')])
    #return "hello world  我"
    
    file_name = env['PATH_INFO']
    #env['PATH_INFO']=request_http
    
    #字典形式， 由于if elss 判断冗余 ; 由于不存在时 会蹦，
    #使用装饰器，完成自动添加 这些web
    try:
        func = Dict_web_methon[file_name]

    except Exception as ret:
        return "产生了异常, 不存在:%s " % str(ret)

    return func()



