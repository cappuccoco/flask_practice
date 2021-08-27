import multiprocessing

bind = '0.0.0.0:5000'		# 监听地址和端口
workers = multiprocessing.cpu_count() * 2 + 1	# worker进程的数量。建议值2-4 x $(NUM_CORES)， 缺省为1。

backlog = 2048		# 服务器中在pending状态的最大连接数，即client处于waiting的数目。超过这个数目， client连接会得到一个error

worker_class = "gevent"		# worker进程的工作方式。 有 sync, eventlet, gevent, tornado, gthread, 缺省值sync。

worker_connections = 1000	# 客户端最大同时连接数。只适用于eventlet， gevent工作方式。

daemon = False

debug = True

proc_name = 'gunicorn_flask'		# 设置进程名

pidfile = './log/gunicorn.pid'		# pid存储文件路径

accesslog = './log/access.log'		# 访问日志路径

errorlog = './log/error.log'		# 错误日志路径。