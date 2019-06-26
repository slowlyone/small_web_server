import socket
import re
import multiprocessing
import  sys
#import dynamic.webserver
 

#tcp服务器
class WSGIServer(object):
	"""docstring for ClassName"""

	def  __init__(self,port,app):
		''' 初始化'''
		self.port = port
		self.app=app

		self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	#绑定端口，里面是一个元组，‘’空字段表上本机，port
		self.tcp_socket.bind(('',self.port))
	##监听状态, 监听字节长度
		self.tcp_socket.listen(128)

	def  run(self):

		while True:
	# accept(),接受到的连接信息，是元组，通过元组拆包。一个是给客户端的套接字   #一个是记录客户端对地址。
	
			client_socket,client_add = self.tcp_socket.accept()
	#然后对具体对客户进行服务 #服务套接字接受信息， ，
		#manager(client_socket)
			p1=multiprocessing.Process(target=self.function,args=(client_socket ,))
			p1.start()
		#主子进程间硬链接式
			client_socket.close()
				
		self.tcp_socket.close() 



	def function(self,client_socket):
		'''处理用户数据'''

		recv_mes=client_socket.recv(1024).decode('utf-8')   
	#recv 是三次握手成功
	#请求响应 进行切片,获取url
	
		request_header=recv_mes.splitlines()[0]

	#按行切片
	#print(request_header)
				
		ret=re.match(r'[^/]+(/[^ ]*)',request_header)

		if ret :
			request_http=ret.group(1)   
			print(request_http)
		
		if request_http =='/':
			request_http = '/index.html'			
			
		  	#如果访问对是/index, 就给相应的html --->不可取，因为还有很多被动请求
		  	#if request_http == '/index.html':	
		 	#body 为打开html文件存储对内容,可以二进制方式打开
		 	#with open('./index.html','rb') as f:
		 	#   context= f.read()
		if not request_http.endswith(".html"):
			#不是以 结尾的。就进入静态网页流程：
			print('static com')
			print(request_http)
			try:
				f=open('./static'+request_http,'rb')
			
			#context=f.read()                         
			#f.close()  
			except Exception as ret:
				print(ret)
				header = "HTTP/1.1 404 not fault\r\n"
			#body 为打开html文件存储对内容,可以二进制方式打开
				respon = header +'\r\n'
				respon += "<h1>----not found----<\h1>"         
				print(respon)
				client_socket.send(respon.encode('utf-8'))
					#client_socket .close()
					#不能关闭套接字，
				
			else:
				context = f.read()                         
				f.close()   

				# retu
				#分开给 浏览器，发送信息a
				header = "HTTP/1.1 200 OK \r\n"
				respon = header +'\r\n'
				
				client_socket.send(respon.encode('utf-8'))
				
				client_socket.send(context)

		else:
			#动态请求 流程，对应动态网页
			#解析application 返回的头
			#header ="HTTP/1.1 200 OK/r/n"
			env = dict()
			
			env['PATH_INFO']=request_http

			#body = dynamic.webserver.application(env,self.start_respon)

			body = self.app(env,self.start_respon)

			header ="HTTP/1.1 %s\r\n" % self.status

#			header += '/r/n'

			for  temp in  self.header_mes:
				#temp[0]、[1]
				header += "%s:%s\r\n" %(temp[0],temp[1])

			header +="\r\n"


			respon = header+body
			#print(respon)

			#client_socket.send(respon.encode('utf-8'))
			client_socket.send(header.encode('utf-8'))
			client_socket.send(body.encode('utf-8'))


		client_socket.close()

	def  start_respon(self,status,header_mes):
		# 用于接受'
		self.status=status
		self.header_mes=header_mes     #header_mes是列表


def  main():
	''' '''
	if len(sys.argv)==3:
		#有了两个参数a
		try:
			port=int(sys.argv[1])
		except:
			print('python WSGI.py  8099  dynamic/webserver  ')
			print('python  WSGI.py 端口号  dynamci文件夹下的框架')
			return     #直接结束程序

	else:
		print('python WSGI.py  8099  dynamic/webserver ')
		print('python  WSGI.py 端口号  dynamci文件夹下的框架')
		return 

	frame_path = sys.argv[2]  
	# python WSGI.py 8099 dynamic/webserver.py
	#dynamic/webserver.py
	ret_zhengze=re.match(r'([^/]+)/([^.]+)',frame_path)
	if ret_zhengze:
		fold_of_module = ret_zhengze.group(1)
		target_modelu = ret_zhengze.group(2)

	sys.path.append(fold_of_module)

	app_content=__import__(target_modelu)
	app=getattr(app_content,'application')

	#  对象=类()       
	#对象.run()
	wsgione=WSGIServer(port,app)
	wsgione.run()



if __name__ == "__main__":
	main()
	
