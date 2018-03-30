这个文件夹用于存放配置文件

该文件夹下的每个文件夹分别为不同的测试环境，其下的所有.ini后缀的配置文件在运行该环境时都会被读取，在新添加配置文件时不需要修改代码

所有配置文件中的sections都会被添加到TestCase.config对象中

在多个配置文件存在相同section的情况下，根据配置文件的读取顺序，后边文件中的配置覆盖前边的配置

帮助文档请查看：https://docs.python.org/3/library/configparser.html
