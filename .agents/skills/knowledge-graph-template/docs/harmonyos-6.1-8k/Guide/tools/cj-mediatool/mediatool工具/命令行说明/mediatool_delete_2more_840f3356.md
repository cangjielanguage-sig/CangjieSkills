### mediatool delete

```shell
mediatool delete <resource-uri>
```

该命令能够彻底删除`<resource-uri>`指定uri的媒体库资源。被删除的资源无法恢复，请谨慎执行。

媒体库资源uri的获取可参考[媒体库uri介绍/获取方式](#媒体库uri介绍获取方式)。

将`<resource-uri>`指定为`all`则删除所有媒体库资源，并重置媒体库的所有数据。

**使用示例：**

```shell
> mediatool delete file://media/Photo/3
[SUCCESS] delete success.

> mediatool delete all # delete all 执行成功不会有任何打印
```

### mediatool query

```shell
mediatool query <display-name> [-p] [-u]
```

该命令能够查询出所有名字为`<display-name>`的媒体库资源，返回资源的源文件真实路径或媒体资源uri。默认返回源文件真实路径。

该命令无法查询出隐藏相册内的媒体资产。

| 选项   | 说明  |
| ---- |----- |
| -p | 返回媒体资源源文件在设备中的真实路径。（默认） |
| -u | 返回媒体资源uri。不能与-p选项同时使用。 |

**使用示例：**

```shell
# 所查询媒体资源存在
> mediatool query MyImage.jpg
find 1 result:
path
/storage/cloud/100/files/Photo/2/IMG_1721381297_001.jpg

# 所查询媒体资源不存在
> mediatool query non_exist.jpg
find 0 result

# 查询的名字格式不正确
> mediatool query IMG_001
find 0 result
The displayName format is not correct!

# 查询媒体资源源文件路径
> mediatool query MyImage.jpg -p
find 1 result:
path
/storage/cloud/100/files/Photo/2/IMG_1721381297_001.jpg

# 查询媒体资源uri
> mediatool query MyImage.jpg -u
find 1 result:
uri
"file://media/Photo/2/IMG_1721381297_001/MyImage.jpg"
```