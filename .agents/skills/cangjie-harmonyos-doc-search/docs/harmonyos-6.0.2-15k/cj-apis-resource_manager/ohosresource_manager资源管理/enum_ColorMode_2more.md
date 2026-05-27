## enum ColorMode

```cangjie
public enum ColorMode {
    | Dark
    | Light
    | ...
}
```

**功能：** 用于表示当前设备颜色模式。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**父类型：**

- Equatable\<ColorMode>
- ToString

### Dark

```cangjie
Dark
```

**功能：** 深色模式。

**起始版本：** 20

### Light

```cangjie
Light
```

**功能：** 浅色模式。

**起始版本：** 20

### func !=(ColorMode)

```cangjie
public operator func !=(other: ColorMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ColorMode)

```cangjie
public operator func ==(other: ColorMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前设备颜色模式的信息，以字符串表示。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前设备颜色模式的信息。|

## enum DeviceType

```cangjie
public enum DeviceType {
    | DEVICE_TYPE_PHONE
    | DEVICE_TYPE_TABLET
    | DEVICE_TYPE_CAR
    | DEVICE_TYPE_PC
    | DEVICE_TYPE_TV
    | DEVICE_TYPE_WEARABLE
    | DEVICE_TYPE_2IN1
    | ...
}
```

**功能：** 用于表示当前设备类型。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

### DEVICE_TYPE_2IN1

```cangjie
DEVICE_TYPE_2IN1
```

**功能：** 二合一设备。

**起始版本：** 12

### DEVICE_TYPE_CAR

```cangjie
DEVICE_TYPE_CAR
```

**功能：** 汽车。

**起始版本：** 12

### DEVICE_TYPE_PC

```cangjie
DEVICE_TYPE_PC
```

**功能：** 电脑。

**起始版本：** 12

### DEVICE_TYPE_PHONE

```cangjie
DEVICE_TYPE_PHONE
```

**功能：** 手机。

**起始版本：** 12

### DEVICE_TYPE_TABLET

```cangjie
DEVICE_TYPE_TABLET
```

**功能：** 平板。

**起始版本：** 12

### DEVICE_TYPE_TV

```cangjie
DEVICE_TYPE_TV
```

**功能：** 电视。

**起始版本：** 12

### DEVICE_TYPE_WEARABLE

```cangjie
DEVICE_TYPE_WEARABLE
```

**功能：** 穿戴。

**起始版本：** 12

### static func parse(Int32)

```cangjie
public static func parse(val: Int32): DeviceType
```

**功能：** 根据设备类型值，构造设备类型实例。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int32|是|-|设备类型的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[DeviceType](#enum-devicetype)|设备类型实例。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取设备类型的值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前设备类型的值。|