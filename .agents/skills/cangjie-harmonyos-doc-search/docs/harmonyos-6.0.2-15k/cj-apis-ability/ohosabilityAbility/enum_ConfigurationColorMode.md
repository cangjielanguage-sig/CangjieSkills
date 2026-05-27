## enum ConfigurationColorMode

```cangjie
public enum ConfigurationColorMode <: Equatable<ConfigurationColorMode> & ToString {
    | COLOR_MODE_NOT_SET
    | COLOR_MODE_DARK
    | COLOR_MODE_LIGHT
    | ...
}
```

**功能：** 表示颜色模式。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**父类型：**

- Equatable\<ConfigurationColorMode>

- ToString

### COLOR_MODE_DARK

```cangjie
COLOR_MODE_DARK
```

**功能：** 深色模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### COLOR_MODE_LIGHT

```cangjie
COLOR_MODE_LIGHT
```

**功能：** 浅色模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### COLOR_MODE_NOT_SET

```cangjie
COLOR_MODE_NOT_SET
```

**功能：** 未设置颜色模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ConfigurationColorMode)

```cangjie
public operator func !=(other: ConfigurationColorMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationColorMode](#enum-configurationcolormode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ConfigurationColorMode)

```cangjie
public operator func ==(other: ConfigurationColorMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationColorMode](#enum-configurationcolormode)|是|-|另一个枚举值。|

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