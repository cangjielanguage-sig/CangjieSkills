## struct PositionArea

```cangjie
public struct PositionArea {
    public PositionArea(
        public let pixels: Array<UInt8>,
        public let offset: UInt32,
        public let stride: UInt32,
        public let region: Region
    )
}
```

**功能：** 表示图片指定区域内的数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### let offset

```cangjie
public let offset: UInt32
```

**功能：** 偏移量。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let pixels

```cangjie
public let pixels: Array<UInt8>
```

**功能：** 像素。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 12

### let region

```cangjie
public let region: Region
```

**功能：** 区域，按照区域读写。写入的区域宽度加X坐标不能大于原图的宽度，写入的区域高度加Y坐标不能大于原图的高度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Region](#struct-region)

**读写能力：** 只读

**起始版本：** 12

### let stride

```cangjie
public let stride: UInt32
```

**功能：** 跨距，内存中每行像素所占的空间。stride >= region.size.width*4。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### PositionArea(Array\<UInt8>, UInt32, UInt32, Region)

```cangjie
public PositionArea(
    public let pixels: Array<UInt8>,
    public let offset: UInt32,
    public let stride: UInt32,
    public let region: Region
)
```

**功能：** 创建PositionArea对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixels|Array\<UInt8>|是|-|像素。|
|offset|UInt32|是|-|偏移量。|
|stride|UInt32|是|-|跨距，内存中每行像素所占的空间。stride >= region.size.width*4。|
|region|[Region](#struct-region)|是|-|区域，按照区域读写。写入的区域宽度加X坐标不能大于原图的宽度，写入的区域高度加Y坐标不能大于原图的高度。|