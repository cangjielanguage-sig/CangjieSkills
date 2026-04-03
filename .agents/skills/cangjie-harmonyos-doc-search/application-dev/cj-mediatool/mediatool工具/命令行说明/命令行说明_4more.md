## 命令行说明

<!--Del-->

### mediatool send

```shell
mediatool send <path-to-local-media-file> [-ts] [-tas] [-rf] [-urf]
```

该命令能够将设备`<path-to-local-media-file>`路径下的图片、视频或音频文件推入媒体库中保存。支持保存图片、视频和音频文件。文件在媒体库中会保留原有的名字。`<path-to-local-media-file>`可以为文件夹，mediatool会将文件夹里的所有文件置入媒体库中。保存成功后会打印成功置入的资源的uri。

默认情况下，将媒体文件保存进媒体库是以同步方式创建缩略图，并且置入后`<path-to-local-media-file>`下的文件会被删除。

| 选项               | 说明             |
| :---- | :--------------- |
| -ts | 保存图片视频时以同步方式创建缩略图。能够保证缩略图正常生成之后图片视频才会显示，但是会导致保存耗时较长。（默认） |
| -tas | 保存图片视频时以异步方式创建缩略图。不能与-ts选项同时使用。图片视频保存后会立即显示，不会等待缩略图先生成。保存耗时较短。 |
| -rf | 媒体文件置入后删除源文件。（默认） |
| -urf | 媒体文件置入后不删除源文件。不能与-rf选项同时使用。 |

**使用示例：**

```shell
> mediatool send /data/tmp/MyImage.jpg
file://media/Photo/3/IMG_1721381297_001/MyImage.jpg # 推图成功，打印推入资源的uri
```

### mediatool list

```shell
mediatool list <resource-uri>
```

该命令能够将`<resource-uri>`指定uri对应的媒体库内资源信息以csv格式打印出来。

例如媒体库内图片资源A的uri为file://media/Photo/3/IMG_1721381297_001/MyImage.jpg, `mediatool list file://media/Photo/3`或者`mediatool list file://media/Photo/3/IMG_1721381297_001/MyImage.jpg`都能成功打印出该资源信息。

所打印信息包含：

- uri: 媒体资源的uri。
- display_name: 媒体资源的名字。
- data: 媒体资源的源文件在设备中的物理路径。

还可以将`<resource-uri>`指定为`all`。`mediatool list all`会将媒体库内所有资源的信息打印出来。

**使用示例：**

```shell
# 使用存在的uri查询
> mediatool list file://media/Photo/3
Table Name: Photos
uri, display_name, data
"file://media/Photo/3/IMG_1721381297_001/MyImage.jpg", "MyImage.jpg", "/storage/cloud/100/files/Photo/2/IMG_1721381297_001.jpg"

# 使用格式错误的uri查询
> mediatool list file://media/Photo/
[FAIL] uri invalid. uri:file://media/Photo/
```

<!--DelEnd-->

### mediatool recv

```shell
mediatool recv <resource-uri> <dest-path>
```

该命令能够将`<resource-uri>`指定uri对应的媒体库资源的源文件内容导出到`<dest-path>`指定的设备路径下。

`<dest-path>`可以指定为待创建文件路径或者文件夹路径，若为文件夹路径则会导出到该文件夹下，文件保留媒体库中的名字。

当`<dest-path>`指定待创建文件路径时，不能是已经存在文件的路径。<!--Del-->`<dest-path>`需要指定有权限访问的路径。<!--DelEnd--><!--RP1--><!--RP1End-->

文件导出成功后会打印导出文件的路径。

媒体库资源uri获取可参考[媒体库uri介绍/获取方式](#媒体库uri介绍获取方式)。

将`<resource-uri>`指定为`all`则能够将所有媒体库资源的源文件导出。当`<resource-uri>`为`all`时，`<dest-path>`必须为文件夹路径。

该命令无法导出隐藏相册内的媒体资产。

**使用示例：**

```shell
> mediatool recv file://media/Photo/3 /data/local/tmp/out.jpg
Table Name: Photos
/data/local/tmp/out.jpg
```