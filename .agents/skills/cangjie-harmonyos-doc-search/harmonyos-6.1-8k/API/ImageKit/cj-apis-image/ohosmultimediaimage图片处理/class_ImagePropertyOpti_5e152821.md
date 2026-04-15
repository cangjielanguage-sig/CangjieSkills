## class ImagePropertyOptions

```cangjie
public class ImagePropertyOptions {
    public var index: UInt32
    public var defaultValue: String
    public init(index!: UInt32 = 0, defaultValue!: String = "")
}
```

**功能：** 表示查询图片属性的索引。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var defaultValue

```cangjie
public var defaultValue: String
```

**功能：** 默认属性值。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### var index

```cangjie
public var index: UInt32
```

**功能：** 图片序号。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

### init(UInt32, String)

```cangjie
public init(index!: UInt32 = 0, defaultValue!: String = "")
```

**功能：** 创建ImagePropertyOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|UInt32|否|0| **命名参数。** 图片序号。默认值为0。|
|defaultValue|String|否|""| **命名参数。** 默认属性值。默认值为空。|