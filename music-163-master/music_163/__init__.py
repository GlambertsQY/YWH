"""
__init__.py 用于告诉 Python 这个文件夹是一个 Python 的包
"""
from music_163 import sql

if __name__ == '__main__':
    a = sql.get_all_artist()
    for i in a:
        print(i)
