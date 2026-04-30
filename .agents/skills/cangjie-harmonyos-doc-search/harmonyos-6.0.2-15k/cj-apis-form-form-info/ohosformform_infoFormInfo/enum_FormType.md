## enum FormType

```cangjie
public enum FormType <: Equatable<FormType> & ToString {
    | Js
    | Ets
    | ...
}
```

**功能：** 支持的卡片类型枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<FormType>
- ToString

### Ets

```cangjie
Ets
```

**功能：** 卡片类型为ArkTS。

**起始版本：** 20

### Js

```cangjie
Js
```

**功能：** 卡片类型为JS。

**起始版本：** 20

### func !=(FormType)

```cangjie
public operator func !=(other: FormType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormType](#enum-formtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FormType)

```cangjie
public operator func ==(other: FormType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FormType](#enum-formtype)|是|-|另一个枚举值。|

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