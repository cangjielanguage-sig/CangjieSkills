## enum LoopMode

```cangjie
public enum LoopMode <: Equatable<LoopMode> & ToString {
    | LOOP_MODE_SEQUENCE
    | LOOP_MODE_SINGLE
    | LOOP_MODE_LIST
    | LOOP_MODE_SHUFFLE
    | LOOP_MODE_CUSTOM
    | ...
}
```

**功能：** 表示媒体播放循环模式的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[LoopMode](#enum-loopmode)>
- ToString

### LOOP_MODE_CUSTOM

```cangjie
LOOP_MODE_CUSTOM
```

**功能：** 自定义播放。

**起始版本：** 19

### LOOP_MODE_LIST

```cangjie
LOOP_MODE_LIST
```

**功能：** 列表循环。

**起始版本：** 19

### LOOP_MODE_SEQUENCE

```cangjie
LOOP_MODE_SEQUENCE
```

**功能：** 顺序播放。

**起始版本：** 19

### LOOP_MODE_SHUFFLE

```cangjie
LOOP_MODE_SHUFFLE
```

**功能：** 随机播放。

**起始版本：** 19

### LOOP_MODE_SINGLE

```cangjie
LOOP_MODE_SINGLE
```

**功能：** 单曲循环。

**起始版本：** 19

### func !=(LoopMode)

```cangjie
public operator func !=(other: LoopMode): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LoopMode](#enum-loopmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(LoopMode)

```cangjie
public operator func ==(other: LoopMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LoopMode](#enum-loopmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|