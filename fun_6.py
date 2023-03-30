def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print(connect_param)


connect(user="/home")
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'user': '/home'}}
connect(root="/")
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/'}}
connect(root="/", user="/home")
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/', 'user': '/home'}}
