## enum AudioEffectMode

```cangjie
public enum AudioEffectMode <: Equatable<AudioEffectMode> & ToString {
    | EFFECT_NONE
    | EFFECT_DEFAULT
    | ...
}
```

**功能：** 音效模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioEffectMode](#enum-audioeffectmode)>
- ToString

### EFFECT_DEFAULT

```cangjie
EFFECT_DEFAULT
```

**功能：** 默认音效。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### EFFECT_NONE

```cangjie
EFFECT_NONE
```

**功能：** 关闭音效。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioEffectMode)

```cangjie
public operator func !=(other: AudioEffectMode): Bool
```

**功能：** 对音效模式枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioEffectMode](#enum-audioeffectmode)|是|-|音效模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音效模式不同，返回true，否则返回false。|

### func ==(AudioEffectMode)

```cangjie
public operator func ==(other: AudioEffectMode): Bool
```

**功能：** 对音效模式枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioEffectMode](#enum-audioeffectmode)|是|-|音效模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频声道相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音效模式枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音效模式枚举值的字符串表示。|