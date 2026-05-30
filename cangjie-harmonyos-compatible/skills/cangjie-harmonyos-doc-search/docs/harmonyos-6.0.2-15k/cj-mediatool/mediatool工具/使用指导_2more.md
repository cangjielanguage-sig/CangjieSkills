## 使用指导

以下使用指导说明了一些常见的mediatool使用场景。

### 导出特定媒体库资产

示例导出图库中名字叫MyImage的jpg图片。

```shell
> hdc shell mediatool query -u MyImage.jpg
find 1 result
uri
"file://media/Photo/1/IMG_1743078145_000/MyImage.jpg"

> hdc shell mediatool recv file://media/Photo/1 /data/local/tmp/out.jpg
Table Name: Photos
/data/local/tmp/out.jpg

> hdc file recv /data/local/tmp/out.jpg .
FileTransfer finish, Size:10015455, File count = 1, time:679ms rate:14750.30kB/s
```

### 导出所有媒体库资产

```shell
> hdc shell mediatool recv all /data/local/tmp/media
Table Name: Photos
/data/local/tmp/media/MyImage.jpg

Table Name: Audios

> hdc shell tar -cvf /data/local/tmp/media.tar /data/local/tmp/media/*
removing leading '/' from member names
data/local/tmp/media/MyImage.jpg

> hdc file recv /data/local/tmp/media.tar .
FileTransfer finish, Size:10017280, File count = 1, time:664ms rate:15086.27kB/s
```

### 删除特定媒体库资产

示例删除图库中名字叫MyImage的jpg图片。

```shell
> hdc shell mediatool query -u MyImage.jpg
find 1 result
uri
"file://media/Photo/1/IMG_1743078145_000/MyImage.jpg"

> hdc shell mediatool delete file://media/Photo/1/IMG_1743078145_000/MyImage.jpg
[SUCCESS] delete success.
```

### 彻底重置媒体库数据库

```shell
> hdc shell mediatool delete all
```

## 媒体库uri介绍/获取方式

uri是媒体库资产的唯一标识符，每个uri都对应一个媒体资产。mediatool使用uri来判断需要操作的媒体资产对象。

可使用以下方式获取uri：

- mediatool query 加上 -u 的选项可以返回对应媒体资产的uri。需要输入对应资产的显示名（在图库中展示的名字带后缀名）。

媒体库uri可以用于mediatool recv命令导出特定媒体库资产，也可以用于mediatool delete删除特定媒体库资产。

uri样例：`file://media/Photo/1/IMG_1743078145_000/MyImage.jpg`。
在mediatool操作中，需要使用以上uri时，无论使用`file://media/Photo/1/IMG_1743078145_000/MyImage.jpg`还是`file://media/Photo/1`都能够正确的定位到目标资产。