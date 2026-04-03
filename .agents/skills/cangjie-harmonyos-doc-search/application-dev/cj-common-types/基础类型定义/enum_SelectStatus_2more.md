## enum SelectStatus

```cangjie
public enum SelectStatus <: Equatable<SelectStatus> {
    | All
    | Part
    | None
    | ...
}
```

**功能：** 多选框选择状态类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SelectStatus](#enum-selectstatus)>

### All

```cangjie
All
```

**功能：** 群组多选择框全部选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Part

```cangjie
Part
```

**功能：** 群组多选择框部分选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 群组多选择框全部没有选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SelectStatus)

```cangjie
public operator func ==(other: SelectStatus): Bool
```

**功能：** 判断两个SelectStatus枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SelectStatus](#enum-selectstatus)|是|-|要比较的另一个SelectStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SelectStatus)

```cangjie
public operator func !=(other: SelectStatus): Bool
```

**功能：** 判断两个SelectStatus枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SelectStatus](#enum-selectstatus)|是|-|要比较的另一个SelectStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum AnimationStatus

```cangjie
public enum AnimationStatus <: Equatable<AnimationStatus> {
    | Initial
    | Running
    | Paused
    | Stopped
    | ...
}
```

**功能：** 动画播放状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[AnimationStatus](#enum-animationstatus)>

### Initial

```cangjie
Initial
```

**功能：** 动画初始状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Running

```cangjie
Running
```

**功能：** 动画正在播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Paused

```cangjie
Paused
```

**功能：** 动画已暂停。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Stopped

```cangjie
Stopped
```

**功能：** 动画已停止。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(AnimationStatus)

```cangjie
public operator func ==(other: AnimationStatus): Bool
```

**功能：** 判断两个AnimationStatus枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimationStatus](#enum-animationstatus)|是|-|要比较的另一个AnimationStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(AnimationStatus)

```cangjie
public operator func !=(other: AnimationStatus): Bool
```

**功能：** 判断两个AnimationStatus枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimationStatus](#enum-animationstatus)|是|-|要比较的另一个AnimationStatus枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|