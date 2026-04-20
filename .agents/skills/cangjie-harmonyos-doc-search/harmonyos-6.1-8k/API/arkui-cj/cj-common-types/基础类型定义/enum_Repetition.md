## enum Repetition

```cangjie
public enum Repetition <: Equatable<Repetition> {
    | Repeat
    | RepeatX
    | RepeatY
    | NoRepeat
    | Clamp
    | Mirror
    | ...
}
```

**功能：** 设置图像重复的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Repetition](#enum-repetition)>

### Repeat

```cangjie
Repeat
```

**功能：** 沿x轴和y轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RepeatX

```cangjie
RepeatX
```

**功能：** 沿x轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RepeatY

```cangjie
RepeatY
```

**功能：** 沿y轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### NoRepeat

```cangjie
NoRepeat
```

**功能：** 不重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Clamp

```cangjie
Clamp
```

**功能：** 在原始边界外绘制时，超出部分使用边缘的颜色绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Mirror

```cangjie
Mirror
```

**功能：** 沿x轴和y轴重复翻转绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Repetition)

```cangjie
public operator func ==(other: Repetition): Bool
```

**功能：** 判断两个Repetition枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Repetition](#enum-repetition)|是|-|要比较的另一个Repetition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Repetition)

```cangjie
public operator func !=(other: Repetition): Bool
```

**功能：** 判断两个Repetition枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Repetition](#enum-repetition)|是|-|要比较的另一个Repetition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|