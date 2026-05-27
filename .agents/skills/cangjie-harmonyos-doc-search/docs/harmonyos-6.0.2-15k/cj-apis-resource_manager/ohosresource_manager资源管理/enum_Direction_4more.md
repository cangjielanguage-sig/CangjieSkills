## enum Direction

```cangjie
public enum Direction {
    | DIRECTION_VERTICAL
    | DIRECTION_HORIZONTAL
    | ...
}
```

**功能：** 用于表示设备屏幕方向。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### DIRECTION_HORIZONTAL

```cangjie
DIRECTION_HORIZONTAL
```

**功能：** 横屏。

**起始版本：** 12

### DIRECTION_VERTICAL

```cangjie
DIRECTION_VERTICAL
```

**功能：** 竖屏。

**起始版本：** 12

### static func parse(Int32)

```cangjie
public static func parse(val: Int32): Direction
```

**功能：** 根据设备屏幕方向值，构造设备屏幕方向实例。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int32|是|-|屏幕方向的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[Direction](#enum-direction)|屏幕方向实例。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取屏幕方向的值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前屏幕方向的值。|

## enum FormatArgs

```cangjie
public enum FormatArgs {
    | INT(Int32)
    | FLOAT(Float32)
    | STRING(String)
    | ...
}
```

**功能：** 表示字符串的格式化数据。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### FLOAT(Float32)

```cangjie
FLOAT(Float32)
```

**功能：** 存储Float32类型值的格式化数据。

**起始版本：** 12

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 存储Int32类型值的格式化数据。

**起始版本：** 12

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 存储String类型值的格式化数据。

**起始版本：** 12

## enum Number

```cangjie
public enum Number {
    | INT(Int32)
    | FLOAT(Float32)
    | ...
}
```

**功能：** 表示从资源中获取到的数字类型。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### FLOAT(Float32)

```cangjie
FLOAT(Float32)
```

**功能：** 存储Float32类型值的Number类型。

**起始版本：** 12

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 存储Int32类型值的Number类型。

**起始版本：** 12

## enum ScreenDensity

```cangjie
public enum ScreenDensity {
    | SCREEN_SDPI
    | SCREEN_MDPI
    | SCREEN_LDPI
    | SCREEN_XLDPI
    | SCREEN_XXLDPI
    | SCREEN_XXXLDPI
    | ...
}
```

**功能：** 用于表示当前设备屏幕密度。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### SCREEN_LDPI

```cangjie
SCREEN_LDPI
```

**功能：** 大规模的屏幕密度。

**起始版本：** 12

### SCREEN_MDPI

```cangjie
SCREEN_MDPI
```

**功能：** 中规模的屏幕密度。

**起始版本：** 12

### SCREEN_SDPI

```cangjie
SCREEN_SDPI
```

**功能：** 小规模的屏幕密度。

**起始版本：** 12

### SCREEN_XLDPI

```cangjie
SCREEN_XLDPI
```

**功能：** 特大规模的屏幕密度。

**起始版本：** 12

### SCREEN_XXLDPI

```cangjie
SCREEN_XXLDPI
```

**功能：** 超大规模的屏幕密度。

**起始版本：** 12

### SCREEN_XXXLDPI

```cangjie
SCREEN_XXXLDPI
```

**功能：** 超特大规模的屏幕密度。

**起始版本：** 12

### static func parse(Int32)

```cangjie
public static func parse(val: Int32): ScreenDensity
```

**功能：** 根据屏幕密度值，构造屏幕密度实例。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int32|是|-|屏幕密度的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ScreenDensity](#enum-screendensity)|屏幕密度实例。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取屏幕密度的值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前屏幕密度的值。|