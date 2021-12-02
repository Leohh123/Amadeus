# Amadeus

## 项目简介

一个自用QQ机器人。

## 使用方法

1. 下载go-cqhttp，生成配置文件（选择连接方式123），配置QQ号和密码，更改设置 `universal: ws://127.0.0.1:xxxx/cqhttp/ws` ，运行go-cqhttp；
2. 新建虚拟环境 `python3 -m venv venv` ，启用 `source venv/bin/activate` ；
3. 安装依赖 `pip install nb-cli` ；
4. 安装插件 `nb plugin install nonebot-plugin-apscheduler` ；
5. 配置文件 `.env` `.env.dev` `.env.prod` ，内容参考配置文件示例；
6. 启动机器人 `nb run` ，若报错可尝试 `python -m pip install --upgrade pip` 。

## 协议

MIT © Leohh