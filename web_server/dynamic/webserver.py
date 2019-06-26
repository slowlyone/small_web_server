import time
import re


Dict_web_methon=dict()

#装饰器完成路由
def route(sample):

	def  set_func(func):

		Dict_web_methon[sample]=func
        #再装饰新功能之前， 就添加进“路由表”

		def  create_func():
	    #Dict_web_methon[sample]:func
			
			return func()

		return create_func

	return set_func




@route(r'/login.html')
def  login(ret):
	return ("1---login %s" %time.ctime())


@route(r'/register.html')
def  register(ret):
	return "2--register"

# /add/00007.html等，完成使用一次@route（）装饰器， 就能实现对应多个url
#对应一个函数，减少键值对

@route(r"/add/(\d+)\.html")
def add_focus(ret):
	code=ret.group(1)
	return "add ok (%s) .."%code

#Dict_web_methon=dict()
#   #添加网页
#   '/login.py':login,
#   './register.py':register

# }


#def  application(request_http):
def  application(env,start_respon):

	start_respon('200 OK',[('Content-Type','text/html;charset=utf-8'),('server','mini_frame v1.0')])

	file_name = env['PATH_INFO']
    #env['PATH_INFO']=request_http
    
    #字典形式， 由于if elss 判断冗余 ; 由于不存在时 会蹦，
    #使用装饰器，完成自动添加 这些web
   # try:
   #     func = Dict_web_methon[file_name]

   # except Exception as ret:
   #     return "产生了异常, 不存在:%s " % str(ret)

   # return func()
	try:
		for url, func in Dict_web_methon.items():
			#print(url, file_name)
			ret=re.match(url,file_name)

			if ret:
				return func(ret)

		else:
			return "请求对url(%s)没有对应对函数.." %file_name
	
	except Exception as ret:
		return "产生了异常, 不存在:%s " % str(ret)
     

