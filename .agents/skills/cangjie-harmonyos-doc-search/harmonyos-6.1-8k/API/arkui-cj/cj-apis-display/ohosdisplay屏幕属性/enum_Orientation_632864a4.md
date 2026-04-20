## enum Orientation

```cangjie
public enum Orientation <: Equatable<Orientation> {
    | Portrait
    | Landscape
    | PortraitInverted
    | LandscapeInverted
    | ...
}
```

**功能：** 枚举屏幕方向。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[Orientation](#enum-orientation)>

### Portrait

```cangjie
Portrait
```

**功能：** 竖屏模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### Landscape

```cangjie
Landscape
```

**功能：** 横屏模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### PortraitInverted

```cangjie
PortraitInverted
```

**功能：** 竖屏反向模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### LandscapeInverted

```cangjie
LandscapeInverted
```

**功能：** 横屏反向模式。

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

### operator func ==(Orientation)

```cangjie
public operator func ==(other: Orientation): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Orientation](#enum-orientation)|是|-|要比较的另一个Orientation实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|