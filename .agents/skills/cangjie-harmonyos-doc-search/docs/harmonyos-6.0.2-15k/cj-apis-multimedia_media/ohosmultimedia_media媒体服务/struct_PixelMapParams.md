## struct PixelMapParams

```cangjie
public struct PixelMapParams {
    public PixelMapParams(
        public var width: Int32,
        public var height: Int32
    )
}
```

**功能：** 获取视频缩略图时，输出缩略图的格式参数。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### var height

```cangjie
public var height: Int32
```

**功能：** 输出的缩略图高度。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: Int32
```

**功能：** 输出的缩略图宽度。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### PixelMapParams(Int32, Int32)

```cangjie
public PixelMapParams(public var width: Int32, public var height: Int32)
```

**功能：** 构造缩略图的格式参数。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int32|是|-|输出的缩略图宽度。应保证大于0且不大于原始视频宽度。否则返回的缩略图不会进行缩放。|
|height|Int32|是|-|输出的缩略图高度。应保证大于0且不大于原始视频高度。否则返回的缩略图不会进行缩放。|