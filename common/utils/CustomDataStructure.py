class CustomDataStructure:
    """
    自定义数据结构.
    该结构实现了字典键的操作与对象的属性操作
    """
    def __getitem__(self, item: str):
        """
        字典索引方法.

        :param item:
        :return:
        """
        if item in self.__dict__ and "_" != item[0]:
            return self.__dict__[item]

        raise AttributeError("'{item}'属性不存在.".format(item=item))

    def __setitem__(self, key: str, value):
        """
        字典键设置方法.

        :param key:
        :param value:
        :return:
        """
        if "_" == key[0]:
            raise KeyError("无法设置私有属性.")
        self.__dict__[key] = value

    def __delitem__(self, key: str):
        """
        字典键删除方法.

        :param key:
        :return:
        """
        if "_" == key[0]:
            raise KeyError("无法设置私有属性.")
        self.__dict__[key] = None

    def __getattr__(self, item: str):
        """
        属性获取方法
        :param item:
        :return:
        """
        if item in self.__dict__ and "_" != item[0]:
            return self.__dict__[item]

        raise AttributeError("'{item}'属性不存在.".format(item=item))

    def __setattr__(self, key: str, value):
        """
        属性设置方法.

        :param key:
        :param value:
        :return:
        """
        if "_" == key[0]:
            raise KeyError("无法设置私有属性.")
        self.__dict__[key] = value

    def __delattr__(self, item: str):
        """
        属性删除方法
        :param item:
        :return:
        """
        if "_" == item[0]:
            raise KeyError("无法设置私有属性.")
        self.__dict__[item] = None
