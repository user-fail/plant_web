# 在Vercel中部署django(入门教程)
不包含Vercel注册,中文没看到好的部署教程，该项目是个软件工程的大作业。
## 一 配置Vercel
在新建manage.py下两个文件:
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

distDir是执行python manage.py collectstatic收集文件存放位置一定要配置,不然找不到静态文件。
这里可以理解为nginx里面的静态文件目录。

shname就是你的sh文件   

build_files.sh
```angular2html
echo "BUILD START"
echo "vercel的python环境中不包含pip"
python3.9 -m ensurepip
echo "安装pip"
python3.9 -m pip install -r requirements.txt
echo "收集静态文件"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
```
## 二配置django
1. wsgi.py
2. setting.py

wsgi.py 与wsgi通信的接口      
只需要将新建一个app变量赋值给application，前提是application = get_wsgi_application(),具体过程可以看我的代码
```angular2html
app = application
```

setting.py     

static= '/static/'

staticfiles_dir = '静态文件目录,不要提供不存在在的目录会报错' # 具体可以看vercel的build log

设置collectstatic收集的静态文件的路径

static_root = BASE_DIR + "/staticfile/static"  # staticfile指的是vercel.json**查找**静态文件的的确切路径,static是你django static_url 开头的url
，如何你配置过nginx这应该很好理解.  

如果是vue打包的前端，在vue.config.js 配置 public:'/static/'


## 项目说明
数据说明数据只是某个平台的数据,数据获取+Q:MzI4ODg5MjUwMA==
