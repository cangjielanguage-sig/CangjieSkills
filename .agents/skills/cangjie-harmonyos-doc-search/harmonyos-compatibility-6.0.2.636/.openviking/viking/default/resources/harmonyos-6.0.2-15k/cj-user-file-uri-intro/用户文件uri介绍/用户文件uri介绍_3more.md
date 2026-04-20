# 用户文件uri介绍

用户文件uri是文件的唯一标识，在对用户文件进行访问与修改等操作时通常都会使用到uri，不建议开发者解析uri中的片段用于业务代码开发，不同类型的uri使用方式将在下文详细介绍。

## uri的类型

uri类型可以归纳为文档类uri和媒体文件uri两类

- 文档类uri：由picker拉起文件管理器选择或保存返回，以及通过fileAccess模块获取。具体获取方式参见[文档类uri获取方式](#文档类uri获取方式)。
- 媒体文件uri：由picker通过拉起图库选择图片或者视频返回，通过photoAccessHelper模块获取图片或者视频文件的uri，以及通过userFileManager模块获取图片、视频或者音频文件的uri。具体获取方式参见[媒体文件uri获取方式](#媒体文件uri获取方式)。

![user-file-uri-intro](figures/user-file-uri-intro.png)

## 文档类uri

### 文档类uri介绍

**文档类uri的格式类型为：**

'file://docs/storage/Users/currentUser/\<relative_path>/test.txt'

**其中各个字段表示的含义为：**

| uri字段          | 说明        |
| ------------- | ------------------- |
| 'file://docs/storage/Users/currentUser/' | 文件管理器的根目录。|
| '\<relative_path>/' | 文件在根目录下的相对路径。例如：'Download/'和'Documents/'。|
| 'test.txt' | 用户文件系统中存储的文件名，支持的文件类型为文件管理器支持的所有类型，以文件管理器为准。例如txt、jpg、mp4和mp3等格式的文件。|

### 文档类uri获取方式

1. 通过[DocumentViewPicker接口](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-documentviewpicker)选择或保存文件，返回选择或保存的文件uri。

2. 通过[AudioViewPicker接口](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-audioviewpicker)选择或保存文件，返回选择或保存的文件uri。

### 文档类uri的使用方式

normal等级的应用使用此类uri的方式只能通过[fs模块](../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md)进行进一步处理，其他模块使用此uri是会报没有权限的错误。示例代码参见picker中的[选择文档类文件](./cj-select-user-file.md#选择文档类文件)和[保存文档类文件](./cj-save-user-file.md#保存文档类文件)。