# 应用文件访问(仓颉)

应用需要对应用文件目录下的应用文件进行查看、创建、读写、删除、移动、复制、获取属性等访问操作，下文介绍具体方法。

## 接口说明

开发者通过基础文件操作接口（[ohos.file_fs](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md)）实现应用文件访问能力，主要功能如下表所示。

| 接口名       | 功能                   | 接口类型 |
| ------------ | ---------------------- | -------- |
| access       | 检查文件是否存在       | 方法     |
| close        | 关闭文件               | 方法     |
| copyFile     | 复制文件               | 方法     |
| createStream | 基于文件路径打开文件流 | 方法     |
| listFile     | 列出文件夹下所有文件名 | 方法     |
| mkdir        | 创建目录               | 方法     |
| moveFile     | 移动文件               | 方法     |
| open         | 打开文件               | 方法     |
| read         | 从文件读取数据         | 方法     |
| rename       | 重命名文件或文件夹     | 方法     |
| rmdir        | 删除整个目录           | 方法     |
| stat         | 获取文件详细属性信息   | 方法     |
| unlink       | 删除单个文件           | 方法     |
| write        | 将数据写入文件         | 方法     |
| Stream.close | 关闭文件流             | 方法     |
| Stream.flush | 刷新文件流             | 方法     |
| Stream.write | 将数据写入流文件       | 方法     |
| Stream.read  | 从流文件读取数据       | 方法     |
| File.fd      | 获取文件描述符         | 属性     |
| OpenMode     | 设置文件打开标签       | 属性     |
| Filter       | 设置文件过滤配置项     | 类型     |