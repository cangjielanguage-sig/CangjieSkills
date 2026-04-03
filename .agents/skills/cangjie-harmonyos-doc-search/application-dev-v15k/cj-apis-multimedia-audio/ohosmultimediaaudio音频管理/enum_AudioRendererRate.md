## enum AudioRendererRate

```cangjie
public enum AudioRendererRate <: Equatable<AudioRendererRate> & ToString {
    | RENDER_RATE_NORMAL
    | RENDER_RATE_DOUBLE
    | RENDER_RATE_HALF
    | ...
}
```

**功能：** 音频渲染速度。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**父类型：**

- Equatable\<[AudioRendererRate](#enum-audiorendererrate)>
- ToString

### RENDER_RATE_DOUBLE

```cangjie
RENDER_RATE_DOUBLE
```

**功能：** 2倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RENDER_RATE_HALF

```cangjie
RENDER_RATE_HALF
```

**功能：** 0.5倍数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RENDER_RATE_NORMAL

```cangjie
RENDER_RATE_NORMAL
```

**功能：** 正常速度。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioRendererRate)

```cangjie
public operator func !=(other: AudioRendererRate): Bool
```

**功能：** 对音频渲染速度枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRendererRate](#enum-audiorendererrate)|是|-|音频渲染速度。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频渲染速度不同，返回true，否则返回false。|

### func ==(AudioRendererRate)

```cangjie
public operator func ==(other: AudioRendererRate): Bool
```

**功能：** 对音频渲染速度枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRendererRate](#enum-audiorendererrate)|是|-|音频渲染速度。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频渲染速度相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频渲染速度枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频渲染速度枚举值的字符串表示。|