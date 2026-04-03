## enum Orientation

```cangjie
public enum Orientation <: Equatable<Orientation> {
    | Unspecified
    | Portrait
    | Landscape
    | PortraitInverted
    | LandscapeInverted
    | AutoRotation
    | AutoRotationPortrait
    | AutoRotationLandscape
    | AutoRotationRestricted
    | AutoRotationPortraitRestricted
    | AutoRotationLandscapeRestricted
    | Locked
    | ...
}
```

**功能：** 显示方向。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[Orientation](#enum-orientation)>

### Unspecified

```cangjie
Unspecified
```

**功能：** 默认值。方向模式未明确定义，由系统决定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Portrait

```cangjie
Portrait
```

**功能：** 竖屏显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Landscape

```cangjie
Landscape
```

**功能：** 横屏显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### PortraitInverted

```cangjie
PortraitInverted
```

**功能：** 倒置竖屏显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### LandscapeInverted

```cangjie
LandscapeInverted
```

**功能：** 倒置横屏显示。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotation

```cangjie
AutoRotation
```

**功能：** 跟随传感器旋转，忽略自动旋转锁定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotationPortrait

```cangjie
AutoRotationPortrait
```

**功能：** 跟随传感器旋转，仅在竖直方向工作，忽略自动旋转锁定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotationLandscape

```cangjie
AutoRotationLandscape
```

**功能：** 跟随传感器旋转，仅在水平方向工作，忽略自动旋转锁定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotationRestricted

```cangjie
AutoRotationRestricted
```

**功能：** 跟随传感器旋转，受自动旋转锁定控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotationPortraitRestricted

```cangjie
AutoRotationPortraitRestricted
```

**功能：** 跟随传感器旋转，仅在竖直方向工作，受自动旋转锁定控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### AutoRotationLandscapeRestricted

```cangjie
AutoRotationLandscapeRestricted
```

**功能：** 跟随传感器旋转，仅在水平方向工作，受自动旋转锁定控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Locked

```cangjie
Locked
```

**功能：** 锁定模式，保持与之前相同的方向。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(Orientation)

```cangjie
public operator func !=(other: Orientation): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Orientation](#enum-orientation)|是|-|要比较的另一个Orientation实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|