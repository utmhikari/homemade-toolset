# homemade-toolset

## 介绍

一款用pyside6打造的「家用日常工具集」，适合初入学习pyside6的同学了解GUI开发的基本用法。

## 目录结构

- app：应用内容
  - __init__.py：app初始化逻辑
  - service：业务逻辑
  - util：工具类
  - view：前端逻辑
    - component：可复用的ui组件
    - ui：通过pyside6-designer生成的ui代码
    - worker：后台异步/并发的任务类
    - XXX.py：主页面逻辑
- cfg：配置文件
- etc：静态资源
  - ui：pyside6-designer的ui文件
  - script：研发脚本
    - deploy.sh：app打包，workdir为项目根目录
    - uic.py：pyside6-designer的ui文件转py文件的脚本，workdir为项目根目录
- main.py：程序入口
- pysidedeploy.spec
- README.md：项目介绍

## 快速上手

相关技术文章：

- [【Python随笔】比PyQt5更先进的pyside6安装和使用方法](https://utmhikari.blog.csdn.net/article/details/141107150)
- [【Python随笔】pyside6绘制表盘和数字时钟的方法](https://utmhikari.blog.csdn.net/article/details/142898055)
- [【Python随笔】如何用pyside6开发并部署简单的postman工具](https://utmhikari.blog.csdn.net/article/details/144635170)
  - [【Python随笔】将requests实例转换成curl语句](https://utmhikari.blog.csdn.net/article/details/143463615)

python版本作者用的3.11.9，其他版本可能有兼容性问题，出现的话请自行调整。

下好requirements后直接执行main.py理论上就能打开程序，编译打包用etc/script/deploy.sh即可。

建议把.venv/bin加到PATH当中，方便随时打开pyside6相关程序，ui文件在etc/ui目录下，统一通过etc/script/uic.py脚本转为py文件。
