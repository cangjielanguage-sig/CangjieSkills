## enum ChannelBlendMode

```cangjie
public enum ChannelBlendMode <: Equatable<ChannelBlendMode> & ToString {
    | MODE_DEFAULT
    | MODE_BLEND_LR
    | MODE_ALL_LEFT
    | MODE_ALL_RIGHT
    | ...
}
```

**功能：** 声道混合模式类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[ChannelBlendMode](#enum-channelblendmode)>
- ToString

### MODE_ALL_LEFT

```cangjie
MODE_ALL_LEFT
```

**功能：** 从左声道拷贝覆盖到右声道混合。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MODE_ALL_RIGHT

```cangjie
MODE_ALL_RIGHT
```

**功能：** 从右声道拷贝覆盖到左声道混合。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MODE_BLEND_LR

```cangjie
MODE_BLEND_LR
```

**功能：** 混合左右声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MODE_DEFAULT

```cangjie
MODE_DEFAULT
```

**功能：** 无声道混合。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(ChannelBlendMode)

```cangjie
public operator func !=(other: ChannelBlendMode): Bool
```

**功能：** 对声道混合模式类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ChannelBlendMode](#enum-channelblendmode)|是|-|声道混合模式类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果声道混合模式类型不同，返回true，否则返回false。|

### func ==(ChannelBlendMode)

```cangjie
public operator func ==(other: ChannelBlendMode): Bool
```

**功能：** 对声道混合模式类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ChannelBlendMode](#enum-channelblendmode)|是|-|声道混合模式类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果声道混合模式类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取声道混合模式类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|声道混合模式类型枚举值的字符串表示。|