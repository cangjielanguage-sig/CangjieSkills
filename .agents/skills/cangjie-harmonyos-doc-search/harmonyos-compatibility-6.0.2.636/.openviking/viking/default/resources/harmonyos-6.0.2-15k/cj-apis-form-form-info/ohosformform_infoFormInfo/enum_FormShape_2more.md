## enum FormShape

```cangjie
public enum FormShape <: Equatable<FormShape> & ToString {
    | RECT
    | CIRCLE
    | ...
}
```

**功能：** 定义卡片形状枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<FormShape>
- ToString

### Circle

```cangjie
Circle
```

**功能：** 圆形 form。

**起始版本：** 20

### Rect

```cangjie
Rect
```

**功能：** 方形 form。

**起始版本：** 20

### func !=(FormShape)

```cangjie
public operator func !=(other: FormShape): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormShape](#enum-formshape)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FormShape)

```cangjie
public operator func ==(other: FormShape): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormShape](#enum-formshape)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

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

## enum FormState

```cangjie
public enum FormState <: Equatable<FormState> & ToString {
    | Unknown
    | Default
    | Ready
    | ...
}
```

**功能：** 卡片状态枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<FormState>
- ToString

### Default

```cangjie
Default
```

**功能：** 表示默认状态。

**起始版本：** 20

### Ready

```cangjie
Ready
```

**功能：** 表示就绪状态。

**起始版本：** 20

### Unknown

```cangjie
Unknown
```

**功能：** 表示未知状态。

**起始版本：** 20

### func !=(FormState)

```cangjie
public operator func !=(other: FormState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormState](#enum-formstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FormState)

```cangjie
public operator func ==(other: FormState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormState](#enum-formstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

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