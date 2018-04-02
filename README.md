# formal-automated-test
课工场正式环境自动化测试

*如果你有协作者账号请使用协作者账号提交；此仓库不接受Pull Request*

# 执行Xvfb虚拟测试说明

## 1.检查是否有已经开启的Xvfb进程
```ps -aux | grep -i xvfb```

## 2.如果没有已经启动的Xvfb进程，通过下面的命令启动
```Xvfb -ac -br -nolisten tcp -screen 0 2880x1720x24 :1121 > /dev/null 2>&1 &```   注：是X不是*

*Tip:1121可以更换为其他数字*

## 3.设置环境变量
```export DISPLAY=:1121```

*Tip:1121为启动Xvfb进程时指定的编号*

## 4.执行测试

执行时分为功能测试与接口测试

### 4.1 执行功能测试
```python3 main.py function```

### 4.2 执行接口测试
```python3 main.py api```

# 允许通过命令行参数指定运行的测试环境
```python3 main.py function -e development```
```python3 main.py function -e pre-production```
```python3 main.py function -e production```

# 允许通过命令行参数指定运行的测试套件
```python3 main.py function -ss homepage course```

# 请通过help参数查看所有可用的命令行参数
```python3 main.py -h```
```python3 main.py --help```
