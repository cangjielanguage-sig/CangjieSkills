## enum ProgressType

```cangjie
public enum ProgressType <: Equatable<ProgressType> {
    | Linear
    | Ring
    | Eclipse
    | ScaleRing
    | Capsule
    | ...
}
```

**功能：** Progress组件的样式类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ProgressType](#enum-progresstype)>

### Linear

```cangjie
Linear
```

**功能：** 线性样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Ring

```cangjie
Ring
```

**功能：** 环形无刻度样式，环形圆环逐渐显示至完全填充效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Eclipse

```cangjie
Eclipse
```

**功能：** 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ScaleRing

```cangjie
ScaleRing
```

**功能：** 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Capsule

```cangjie
Capsule
```

**功能：** 胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同；中段处的进度展示效果与Linear相同。高度大于宽度的时候自适应垂直显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ProgressType)

```cangjie
public operator func ==(other: ProgressType): Bool
```

**功能：** 判断两个ProgressType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProgressType](#enum-progresstype)|是|-|要比较的另一个ProgressType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ProgressType)

```cangjie
public operator func !=(other: ProgressType): Bool
```

**功能：** 判断两个ProgressType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProgressType](#enum-progresstype)|是|-|要比较的另一个ProgressType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|