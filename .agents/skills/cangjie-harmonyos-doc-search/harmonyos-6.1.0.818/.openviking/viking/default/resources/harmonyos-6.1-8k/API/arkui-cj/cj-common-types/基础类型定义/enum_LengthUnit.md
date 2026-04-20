## enum LengthUnit

```cangjie
public enum LengthUnit <: Equatable<LengthUnit> {
    | Px
    | Vp
    | Fp
    | Percent
    | Lpx
    | ...
}
```

**功能：** 长度单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：** Equatable\<[LengthUnit](#enum-lengthunit)>

### Px

```cangjie
Px
```

**功能：** 基本像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Vp

```cangjie
Vp
```

**功能：** 屏幕密度单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Fp

```cangjie
Fp
```

**功能：** 字体像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Percent

```cangjie
Percent
```

**功能：** 百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Lpx

```cangjie
Lpx
```

**功能：** 逻辑像素单位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(LengthUnit)

```cangjie
public operator func !=(other: LengthUnit): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LengthUnit](#enum-lengthunit)|是|-|要比较的另一个LengthUnit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(LengthUnit)

```cangjie
public operator func ==(other: LengthUnit): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LengthUnit](#enum-lengthunit)|是|-|要比较的另一个LengthUnit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取LengthUnit的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|LengthUnit的值。|

### static func parse(Int32)

```cangjie
public static func parse(value: Int32): LengthUnit
```

**功能：** 解析Int32值为LengthUnit。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|要解析的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[LengthUnit](#enum-lengthunit)|解析后的LengthUnit。|