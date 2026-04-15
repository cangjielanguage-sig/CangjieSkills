## class PositionArea

```cangjie
public class PositionArea {
    public var pixels: Array<UInt8>
    public var offset: UInt32
    public var stride: UInt32
    public var region: Region
    public init(pixels: Array<UInt8>, offset: UInt32, stride: UInt32, region: Region)
}
```

**功能：** 表示图片指定区域内的数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var offset

```cangjie
public var offset: UInt32
```

**功能：** 偏移量。单位：字节。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var pixels

```cangjie
public var pixels: Array<UInt8>
```

**功能：** 像素。仅支持BGRA_8888格式的图像像素数据。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var region

```cangjie
public var region: Region
```

**功能：** 区域，按照区域读写。写入的区域宽度加X坐标不能大于原图的宽度，写入的区域高度加Y坐标不能大于原图的高度。

**类型：** [Region](#class-region)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### var stride

```cangjie
public var stride: UInt32
```

**功能：** 跨距，内存中每行像素所占的空间。stride >= region.size.width*4。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### init(Array\<UInt8>, UInt32, UInt32, Region)

```cangjie
public init(pixels: Array<UInt8>, offset: UInt32, stride: UInt32, region: Region)
```

**功能：** 创建PositionArea对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixels|Array\<UInt8>|是|-|像素。仅支持BGRA_8888格式的图像像素数据。|
|offset|UInt32|是|-|偏移量。单位：字节。|
|stride|UInt32|是|-|跨距，内存中每行像素所占的空间。stride >= region.size.width*4。|
|region|[Region](#class-region)|是|-|区域，按照区域读写。写入的区域宽度加X坐标不能大于原图的宽度，写入的区域高度加Y坐标不能大于原图的高度。|