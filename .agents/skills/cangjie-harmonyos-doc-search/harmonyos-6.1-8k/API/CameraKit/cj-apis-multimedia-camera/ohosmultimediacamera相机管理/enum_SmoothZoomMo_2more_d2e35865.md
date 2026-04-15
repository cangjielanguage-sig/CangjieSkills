## enum SmoothZoomMode

```cangjie
public enum SmoothZoomMode {
    | Normal
    | ...
}
```

**功能：** 平滑变焦模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<SmoothZoomMode>
- ToString

### Normal

```cangjie
Normal
```

**功能：** 贝塞尔曲线模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(SmoothZoomMode)

```cangjie
public operator func !=(other: SmoothZoomMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SmoothZoomMode](#enum-smoothzoommode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SmoothZoomMode)

```cangjie
public operator func ==(other: SmoothZoomMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SmoothZoomMode](#enum-smoothzoommode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22


**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|

## enum TorchMode

```cangjie
public enum TorchMode {
    | Off
    | On
    | Auto
    | ...
}
```

**功能：** 枚举，手电筒模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<TorchMode>
- ToString

### Auto

```cangjie
Auto
```

**功能：** 自动模式，系统根据环境自动调节手电筒亮度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Off

```cangjie
Off
```

**功能：** 常关模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### On

```cangjie
On
```

**功能：** 常开模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(TorchMode)

```cangjie
public operator func !=(other: TorchMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TorchMode](#enum-torchmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(TorchMode)

```cangjie
public operator func ==(other: TorchMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TorchMode](#enum-torchmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|