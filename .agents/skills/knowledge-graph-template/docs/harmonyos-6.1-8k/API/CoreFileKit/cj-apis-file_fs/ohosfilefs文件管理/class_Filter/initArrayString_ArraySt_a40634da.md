### init(Array\<String>, Array\<String>, Array\<String>, ?Int64, ?Float64, Bool)

```cangjie
public init(
    suffix!: Array<String> = Array<String>(),
    displayName!: Array<String> = Array<String>(),
    mimeType!: Array<String> = Array<String>(),
    fileSizeOver!: ?Int64 = None,
    lastModifiedAfter!: ?Float64 = None,
    excludeMedia!: Bool = false
)
```

**功能：** 构造Filter对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|suffix|Array\<String>|否|Array\<String>()|**命名参数。** 文件后缀名完全匹配，各个关键词OR关系。|
|displayName|Array\<String>|否|Array\<String>()|**命名参数。** 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。|
|mimeType|Array\<String>|否|Array\<String>()|**命名参数。** mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。|
|fileSizeOver|?Int64|否|None|**命名参数。** 文件大小匹配，大于指定大小的文件。|
|lastModifiedAfter|?Float64|否|None|**命名参数。** 文件最近修改时间匹配，在指定时间点及之后的文件。|
|excludeMedia|Bool|否|false|**命名参数。** 是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。预留字段，暂不支持使用。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900020 | Invalid argument. |