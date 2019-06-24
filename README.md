# small_web_server
符合WSGI设计的小框架。处理动态、静态请求的小型web服务器

1、WSGI 接口定义函数 
  def  application(env,start_response):
    start_response('200OK',[('Content-Type','text/html;charset=utf-8')])
    
    return ....
    
2、路由功能。 带参数的装饰器，将请求和处理函数 存储入字典

3、伪静态 url
