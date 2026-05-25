## enum FlashMode

```cangjie
public enum FlashMode {
    | FlashModeClose
    | FlashModeOpen
    | FlashModeAuto
    | FlashModeAlwaysOpen
    | ...
}
```

**功能：** 枚举，闪光灯模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<FlashMode>
- ToString

### FlashModeAlwaysOpen

```cangjie
FlashModeAlwaysOpen
```

**功能：** 闪光灯常亮。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FlashModeAuto

```cangjie
FlashModeAuto
```

**功能：** 自动闪光灯。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FlashModeClose

```cangjie
FlashModeClose
```

**功能：** 闪光灯关闭。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FlashModeOpen

```cangjie
FlashModeOpen
```

**功能：** 闪光灯打开。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(FlashMode)

```cangjie
public operator func !=(other: FlashMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlashMode](#enum-flashmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FlashMode)

```cangjie
public operator func ==(other: FlashMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlashMode](#enum-flashmode)|是|-|另一个枚举值。|

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