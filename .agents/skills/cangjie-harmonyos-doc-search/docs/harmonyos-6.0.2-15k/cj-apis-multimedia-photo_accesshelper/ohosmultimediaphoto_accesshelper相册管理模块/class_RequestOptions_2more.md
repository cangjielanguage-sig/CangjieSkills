## class RequestOptions

```cangjie
public class RequestOptions {
    public RequestOptions(
        public var deliveryMode: DeliveryMode
    )
}
```

**功能：** 请求策略。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var deliveryMode

```cangjie
public var deliveryMode: DeliveryMode
```

**功能：** 请求资源分发模式。

**类型：** [DeliveryMode](#enum-deliverymode)

**读写能力：** 可读写

**起始版本：** 19

### RequestOptions(DeliveryMode)

```cangjie
public RequestOptions(
    public var deliveryMode: DeliveryMode
)
```

**功能：** 构造RequestOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deliveryMode|[DeliveryMode](#enum-deliverymode)|是|-|请求资源分发模式，可以指定对于该资源的请求策略，可被配置为快速模式，高质量模式，均衡模式三种策略。|

## struct CreateOptions

```cangjie
public struct CreateOptions {
    public CreateOptions(
        public var title!: ?String = None,
        public var subtype!: ?PhotoSubtype = None
    )
}
```

**功能：** 图片或视频的创建选项。

title参数规格为：

- 不应包含扩展名。
- 文件名字符串长度为1~255。
- 文件名中不允许出现的非法英文字符，包括：. .. \ / : * ? " ' ` < > | { } [ ]

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var subtype

```cangjie
public var subtype: ?PhotoSubtype = None
```

**功能：** 图片或者视频的标题。

**类型：** ?[PhotoSubtype](#enum-photosubtype)

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: ?String = None
```

**功能：** 图片或者视频的标题。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### CreateOptions(?String, ?PhotoSubtype)

```cangjie
public CreateOptions(
    public var title!: ?String = None,
    public var subtype!: ?PhotoSubtype = None
)
```

**功能：** 构造CreateOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|?String|否|None| **命名参数。** 图片或者视频的标题。|
|subtype|?[PhotoSubtype](#enum-photosubtype)|否|None| **命名参数。** 图片或者视频的文件子类型。|