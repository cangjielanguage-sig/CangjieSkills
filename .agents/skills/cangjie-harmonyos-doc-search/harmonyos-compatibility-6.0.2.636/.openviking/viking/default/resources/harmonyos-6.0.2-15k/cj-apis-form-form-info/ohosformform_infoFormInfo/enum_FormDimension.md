## enum FormDimension

```cangjie
public enum FormDimension <: Equatable<FormDimension> & ToString {
    | Dimension12
    | Dimension22
    | Dimension24
    | Dimension44
    | Dimension21
    | Dimension11
    | Dimension64
    | ...
}
```

**功能：** 定义卡片尺寸枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<FormDimension>
- ToString

### Dimension11

```cangjie
Dimension11
```

**功能：** 高宽比 1 x 1 form。

**起始版本：** 20

### Dimension64

```cangjie
Dimension64
```

**功能：** 高宽比 6 x 4 form。

**起始版本：** 20

### Dimension12

```cangjie
Dimension12
```

**功能：** 高宽比 1 x 2 form。

**起始版本：** 20

### Dimension21

```cangjie
Dimension21
```

**功能：** 高宽比 2 x 1 form。

**起始版本：** 20

### Dimension22

```cangjie
Dimension22
```

**功能：** 高宽比 2 x 2 form。

**起始版本：** 20

### Dimension24

```cangjie
Dimension24
```

**功能：** 高宽比 2 x 4 form。

**起始版本：** 20

### Dimension44

```cangjie
Dimension44
```

**功能：** 高宽比 4 x 4 form。

**起始版本：** 20

### func !=(FormDimension)

```cangjie
public operator func !=(other: FormDimension): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormDimension](#enum-formdimension)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FormDimension)

```cangjie
public operator func ==(other: FormDimension): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormDimension](#enum-formdimension)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取卡片枚举对应的值。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int32|卡片枚举对应的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|