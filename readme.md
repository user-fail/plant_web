# 在Vercel部署django
不包含Vercel注册,中文没看到好的教程
## 一 配置Vercel
新建两个文件:
1. vercel.json
2. build_files.sh

vercel.json是用来配置环境的
```angular2html
{
    "version": 2,
    "builds": [
      {
        "src": "<appname>/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
      },
      {
        "src": "<namesh>.sh",
        "use": "@vercel/static-build",
        "config": {
          "distDir": "staticfiles"
        }
      }
    ],
    "routes": [
      {
        "src": "/static/(.*)",
        "dest": "/staticfiles/$1"
      },
      {
        "src": "/(.*)",
        "dest": "<appname>/wsgi.py"
      }
    ]
  }

```

appname是python manage.py startapp appname    

distDir是执行python manage.py collectstatic收集文件存放位置一定要配置不然找不到静态文件

shname就是你的sh文件   

build_files.sh
```angular2html
echo "BUILD START"
echo "vercel环境中不包含pip"
python3.9 -m ensurepip
echo "安装pip"
python3.9 -m pip install -r requirements.txt
echo "收集静态文件"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
```
## 配置django
1. wsgi.py
2. setting.py

wsgi.py 与wsgi通信的接口
只需要将新建一个app变量赋值给application，前提是application = get_wsgi_application()

setting.py     
设置collectstatic收集的静态文件的路径   
static_root= 'staticfiles'
