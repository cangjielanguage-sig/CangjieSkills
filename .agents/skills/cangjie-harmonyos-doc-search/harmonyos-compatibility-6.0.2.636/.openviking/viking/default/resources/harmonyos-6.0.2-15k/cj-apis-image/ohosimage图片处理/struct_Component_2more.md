## struct Component

```cangjie
public struct Component {
    public Component(
        public let componentType: ComponentType,
        public let rowStride: Int32,
        public let pixelStride: Int32,
        public let byteBuffer: Array<UInt8>
    )
}
```

**功能：** 描述图像颜色分量。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### let byteBuffer

```cangjie
public let byteBuffer: Array<UInt8>
```

**功能：** 组件缓冲区。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 12

### let componentType

```cangjie
public let componentType: ComponentType
```

**功能：** 组件类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [ComponentType](#enum-componenttype)

**读写能力：** 只读

**起始版本：** 12

### let pixelStride

```cangjie
public let pixelStride: Int32
```

**功能：** 像素间距。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let rowStride

```cangjie
public let rowStride: Int32
```

**功能：** 行距。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### Component(ComponentType, Int32, Int32, Array\<UInt8>)

```cangjie
public Component(
    public let componentType: ComponentType,
    public let rowStride: Int32,
    public let pixelStride: Int32,
    public let byteBuffer: Array<UInt8>
)
```

**功能：** 创建Component对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|componentType|[ComponentType](#enum-componenttype)|是|-|组件类型。|
|rowStride|Int32|是|-|行距。|
|pixelStride|Int32|是|-|像素间距。|
|byteBuffer|Array\<UInt8>|是|-|组件缓冲区。|

## struct ImagePropertyOptions

```cangjie
public struct ImagePropertyOptions {
    public ImagePropertyOptions(
        public let index!: UInt32 = 0,
        public let defaultValue!: String = ""
    )
}
```

**功能：** 表示查询图片属性的索引。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

### let defaultValue

```cangjie
public let defaultValue: String = ""
```

**功能：** 默认属性值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let index

```cangjie
public let index: UInt32 = 0
```

**功能：** 图片序号。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### ImagePropertyOptions(UInt32, String)

```cangjie
public ImagePropertyOptions(
    public let index!: UInt32 = 0,
    public let defaultValue!: String = ""
)
```

**功能：** 创建ImagePropertyOptions对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|UInt32|否|0| **命名参数。** 图片序号。|
|defaultValue|String|否|""| **命名参数。** 默认属性值。|