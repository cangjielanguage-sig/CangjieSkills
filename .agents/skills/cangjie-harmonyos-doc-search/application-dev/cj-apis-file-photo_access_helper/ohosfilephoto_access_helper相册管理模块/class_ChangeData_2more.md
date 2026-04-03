## class ChangeData

```cangjie
public class ChangeData {
    public var notifyType: NotifyType
    public var uris: Array<String>
    public var extraUris: Array<String>
}
```

**功能：** 监听器回调函数的返回值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var extraUris

```cangjie
public var extraUris: Array<String>
```

**功能：** 相册中变动文件的uri数组。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var notifyType

```cangjie
public var notifyType: NotifyType
```

**功能：** ChangeData的通知类型。

**类型：** [NotifyType](#enum-notifytype)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var uris

```cangjie
public var uris: Array<String>
```

**功能：** 相同[NotifyType](#enum-notifytype)的所有uri，可以是PhotoAsset或Album。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

## class CreateOptions

```cangjie
public class CreateOptions {
    public var title: String = ""
    public var subtype: PhotoSubtype
    public init(title!: String = "", subtype!: PhotoSubtype = Default)
}
```

**功能：** 图片或视频的创建选项。

title参数的规格如下：

- 不应包含扩展名。
- 文件名字符串长度为1~255。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var subtype

```cangjie
public var subtype: PhotoSubtype
```

**功能：** 图片或者视频的文件子类型。

**类型：** [PhotoSubtype](#enum-photosubtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### var title

```cangjie
public var title: String = ""
```

**功能：** 图片或者视频的标题。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### init(String, PhotoSubtype)

```cangjie
public init(title!: String = "", subtype!: PhotoSubtype = Default)
```

**功能：** 构造CreateOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 图片或者视频的标题。|
|subtype|[PhotoSubtype](#enum-photosubtype)|否|Default| **命名参数。** 图片或者视频的文件子类型。|