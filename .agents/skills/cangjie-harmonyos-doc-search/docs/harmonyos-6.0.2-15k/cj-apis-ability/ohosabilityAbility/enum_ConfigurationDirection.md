## enum ConfigurationDirection

```cangjie
public enum ConfigurationDirection <: Equatable<ConfigurationDirection> & ToString {
    | DIRECTION_NOT_SET
    | DIRECTION_VERTICAL
    | DIRECTION_HORIZONTAL
    | ...
}
```

**功能：** 表示屏幕方向。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**父类型：**

- Equatable\<ConfigurationDirection>

- ToString

### DIRECTION_HORIZONTAL

```cangjie
DIRECTION_HORIZONTAL
```

**功能：** 水平方向。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### DIRECTION_NOT_SET

```cangjie
DIRECTION_NOT_SET
```

**功能：** 未设置方向。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### DIRECTION_VERTICAL

```cangjie
DIRECTION_VERTICAL
```

**功能：** 垂直方向。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ConfigurationDirection)

```cangjie
public operator func !=(other: ConfigurationDirection): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationDirection](#enum-configurationdirection)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ConfigurationDirection)

```cangjie
public operator func ==(other: ConfigurationDirection): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationDirection](#enum-configurationdirection)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|