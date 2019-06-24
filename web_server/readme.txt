动态与静态网站结合。
逐渐引入 WSGI框架
index.html 是静态网页

w.. 是处理动态请求对小框架

2、服务器 是 Ngin 服务器。 高端的。  为了我们对处理脚本 能和 Ngin服务器吻合。
脚本必须符合 WSGI 框架。这是由于Ngin的设计，规定了。

3、本次对小型服务器 增加 配置文件， 使其更接近Ngin
运行方式： python WSGI.py 8099 dynamic/webserver.py 
通过sys 模块抓取参数。
而且 固定使用 webserver.py 里的application() 方法， 也就是说框架里必须有这个方法名。

4\\伪静态，  , 把请求 变为.html   
