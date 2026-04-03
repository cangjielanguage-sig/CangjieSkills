## struct Region

```cangjie
public struct Region {
    public Region(
        public var size: Size,
        public var x: Int32,
        public var y: Int32
    )
}
```

**功能：** 表示区域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### var size

```cangjie
public var size: Size
```

**功能：** 区域大小。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Size](#struct-size)

**读写能力：** 可读写

**起始版本：** 12

### var x

```cangjie
public var x: Int32
```

**功能：** 区域横坐标。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var y

```cangjie
public var y: Int32
```

**功能：** 区域纵坐标。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### Region(Size, Int32, Int32)

```cangjie
public Region(
    public var size: Size,
    public var x: Int32,
    public var y: Int32
)
```

**功能：** 创建Region对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#struct-size)|是|-|区域大小。|
|x|Int32|是|-|区域横坐标。|
|y|Int32|是|-|区域纵坐标。|

## struct Size

```cangjie
public struct Size {
    public Size(
        public var height!: Int32 = 0,
        public var width!: Int32 = 0
    )
}
```

**功能：** 表示图片尺寸。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### var height

```cangjie
public var height: Int32 = 0
```

**功能：** 输出图片的高。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var width

```cangjie
public var width: Int32 = 0
```

**功能：** 输出图片的宽。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### Size(Int32, Int32)

```cangjie
public Size(
    public var height!: Int32 = 0,
    public var width!: Int32 = 0
)
```

**功能：** 创建Size对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|Int32|否|0| **命名参数。** 输出图片的高。|
|width|Int32|否|0| **命名参数。** 输出图片的宽。|