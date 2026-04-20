## class Region

```cangjie
public class Region {
    public var size: Size
    public var x: Int32
    public var y: Int32
    public init(size: Size, x: Int32, y: Int32)
}
```

**功能：** 表示区域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var size

```cangjie
public var size: Size
```

**功能：** 区域大小。

**类型：** [Size](#class-size)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var x

```cangjie
public var x: Int32
```

**功能：** 区域左上角横坐标。单位：像素。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var y

```cangjie
public var y: Int32
```

**功能：** 区域左上角纵坐标。单位：像素。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### init(Size, Int32, Int32)

```cangjie
public init(size: Size, x: Int32, y: Int32)
```

**功能：** 创建Region对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#class-size)|是|-|区域大小。|
|x|Int32|是|-|区域左上角横坐标。单位：像素。|
|y|Int32|是|-|区域左上角纵坐标。单位：像素。|

## class Size

```cangjie
public class Size {
    public var height: Int32
    public var width: Int32
    public init(height: Int32, width: Int32)
}
```

**功能：** 表示图片尺寸。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var height

```cangjie
public var height: Int32
```

**功能：** 输出图片的高，单位：像素。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var width

```cangjie
public var width: Int32
```

**功能：** 输出图片的宽，单位：像素。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### init(Int32, Int32)

```cangjie
public init(height: Int32, width: Int32)
```

**功能：** 创建Size对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|Int32|是|-|输出图片的高，单位：像素。|
|width|Int32|是|-|输出图片的宽，单位：像素。|