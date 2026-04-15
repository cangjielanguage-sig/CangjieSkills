## class FileSpec

```cangjie
public class FileSpec {
    public var path: String
    public var mimeType:?String
    public var filename:?String
    public var extras: HashMap<String, String>

    public init(
        path: String,
        mimeType!: ?String = None,
        filename!: ?String = None,
        extras!: HashMap<String, String> = HashMap<String, String>()
    )
}
```

**功能：** 表单项的文件信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var extras

```cangjie
public var extras: HashMap<String, String>
```

**功能：** 文件信息的附加内容，该属性不会体现在HTTP请求中。

**类型：** HashMap\<String,String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var filename

```cangjie
public var filename:?String
```

**功能：** 文件名。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var mimeType

```cangjie
public var mimeType:?String
```

**功能：** 文件的mimeType，通过文件名获取。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var path

```cangjie
public var path:String
```

**功能：** 文件路径。

相对路径，位于调用方的缓存路径下。

例如："./xxx/yyy/zzz.html"、"xxx/yyy/zzz.html"。

internal协议路径，支持"internal://"及其子路径。internal为调用方（即传入的context）对应路径，"internal://cache"对应context.cacheDir。

例如："internal://cache/path/to/file.txt"。

应用沙箱目录，只支持到base及其子目录下。

例如："/data/storage/el1/base/path/to/file.txt"。

file协议路径，必须匹配应用包名，只支持到base及其子目录下。

例如："file://com.example.test/data/storage/el2/base/file.txt"。

用户公共文件，仅支持上传任务。

例如："file://media/Photo/path/to/file.img"。仅支持前台任务。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### init(String, ?String, ?String, HashMap\<String,String>)

```cangjie
public init(
    path: String,
    mimeType!: ?String = None,
    filename!: ?String = None,
    extras!: HashMap<String, String> = HashMap<String, String>()
)
```

**功能：** 创建FileSpec对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名   | 类型 | 必填 | 默认值 | 说明 |
| :------- | :----- | :--- | :----- | :---------- |
| path     | String | 是   | - | **命名参数。** 文件路径。|
| mimeType | ?String | 否   | None | **命名参数。** 文件的mimeType，通过文件名获取，默认值为文件名后缀。|
| filename | ?String | 否   | None | **命名参数。** 文件名，默认值通过路径获取。|
| extras   | HashMap\<String,String> | 否   | HashMap<String,String>() | **命名参数。** 文件信息的附加内容，该参数不会体现在HTTP请求中。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let fileSpec = FileSpec(
        "./example.txt",
        mimeType: "text/plain",
        filename: "example.txt"
    )
    Hilog.info(0, "test", "成功创建文件规范对象")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```