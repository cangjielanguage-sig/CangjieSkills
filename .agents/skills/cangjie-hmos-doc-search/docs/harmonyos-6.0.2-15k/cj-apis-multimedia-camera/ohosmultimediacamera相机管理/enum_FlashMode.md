## enum FlashMode

```cangjie
public enum FlashMode <: Equatable<FlashMode> & ToString {
    | FLASH_MODE_CLOSE
    | FLASH_MODE_OPEN
    | FLASH_MODE_AUTO
    | FLASH_MODE_ALWAYS_OPEN
    | ...
}
```

**功能：** 闪光灯模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<FlashMode>
- ToString

### FLASH_MODE_ALWAYS_OPEN

```cangjie
FLASH_MODE_ALWAYS_OPEN
```

**功能：** 闪光灯常亮。

**起始版本：** 19

### FLASH_MODE_AUTO

```cangjie
FLASH_MODE_AUTO
```

**功能：** 自动闪光灯。

**起始版本：** 19

### FLASH_MODE_CLOSE

```cangjie
FLASH_MODE_CLOSE
```

**功能：** 闪光灯关闭。

**起始版本：** 19

### FLASH_MODE_OPEN

```cangjie
FLASH_MODE_OPEN
```

**功能：** 闪光灯打开。

**起始版本：** 19

### func !=(FlashMode)

```cangjie
public operator func !=(other: FlashMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

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

**起始版本：** 19

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

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|