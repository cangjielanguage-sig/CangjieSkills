### CH_LAYOUT_AMB_ORDER2_ACN_N3D

```cangjie
CH_LAYOUT_AMB_ORDER2_ACN_N3D
```

**功能：** 声道排序为ACN_N3D（根据ITU标准）的二阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_AMB_ORDER2_ACN_SN3D

```cangjie
CH_LAYOUT_AMB_ORDER2_ACN_SN3D
```

**功能：** 声道排序为ACN_SN3D（根据ITU标准）的二阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_AMB_ORDER2_FUMA

```cangjie
CH_LAYOUT_AMB_ORDER2_FUMA
```

**功能：** 声道排序为FUMA（根据ITU标准）的二阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_AMB_ORDER3_ACN_N3D

```cangjie
CH_LAYOUT_AMB_ORDER3_ACN_N3D
```

**功能：** 声道排序为ACN_N3D（根据ITU标准）的三阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_AMB_ORDER3_ACN_SN3D

```cangjie
CH_LAYOUT_AMB_ORDER3_ACN_SN3D
```

**功能：** 声道排序为ACN_SN3D（根据ITU标准）的三阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_AMB_ORDER3_FUMA

```cangjie
CH_LAYOUT_AMB_ORDER3_FUMA
```

**功能：** 声道排序为FUMA（根据ITU标准）的三阶HOA文件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_HEXADECAGONAL

```cangjie
CH_LAYOUT_HEXADECAGONAL
```

**功能：** 声道布局为HEXADECAGONAL。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_HEXAGONAL

```cangjie
CH_LAYOUT_HEXAGONAL
```

**功能：** 声道布局为HEXAGONAL。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_MONO

```cangjie
CH_LAYOUT_MONO
```

**功能：** 声道布局为MONO。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_OCTAGONAL

```cangjie
CH_LAYOUT_OCTAGONAL
```

**功能：** 声道布局为OCTAGONAL。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_QUAD

```cangjie
CH_LAYOUT_QUAD
```

**功能：** 声道布局为QUAD。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_QUAD_SIDE

```cangjie
CH_LAYOUT_QUAD_SIDE
```

**功能：** 声道布局为QUAD-SIDE。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_STEREO

```cangjie
CH_LAYOUT_STEREO
```

**功能：** 声道布局为STEREO。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_STEREO_DOWNMIX

```cangjie
CH_LAYOUT_STEREO_DOWNMIX
```

**功能：** 声道布局为STEREO-DOWNMIX。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_SURROUND

```cangjie
CH_LAYOUT_SURROUND
```

**功能：** 声道布局为SURROUND。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CH_LAYOUT_UNKNOWN

```cangjie
CH_LAYOUT_UNKNOWN
```

**功能：** 未知声道布局。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioChannelLayout)

```cangjie
public operator func !=(other: AudioChannelLayout): Bool
```

**功能：** 对音频文件声道布局类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioChannelLayout](#enum-audiochannellayout)|是|-|音频文件声道布局类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频文件声道布局类型不同，返回true，否则返回false。|