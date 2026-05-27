## enum ConfigurationScreenDensity

```cangjie
public enum ConfigurationScreenDensity <: Equatable<ConfigurationScreenDensity> & ToString {
    | SCREEN_DENSITY_NOT_SET
    | SCREEN_DENSITY_SDPI
    | SCREEN_DENSITY_MDPI
    | SCREEN_DENSITY_LDPI
    | SCREEN_DENSITY_XLDPI
    | SCREEN_DENSITY_XXLDPI
    | SCREEN_DENSITY_XXXLDPI
    | ...
}
```

**功能：** 表示屏幕像素。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**父类型：**

- Equatable\<ConfigurationScreenDensity>

- ToString

### SCREEN_DENSITY_LDPI

```cangjie
SCREEN_DENSITY_LDPI
```

**功能：** 屏幕像素密度为'LDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_MDPI

```cangjie
SCREEN_DENSITY_MDPI
```

**功能：** 屏幕像素密度为'MDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_NOT_SET

```cangjie
SCREEN_DENSITY_NOT_SET
```

**功能：** 未设置屏幕像素密度。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_SDPI

```cangjie
SCREEN_DENSITY_SDPI
```

**功能：** 屏幕像素密度为'SDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_XLDPI

```cangjie
SCREEN_DENSITY_XLDPI
```

**功能：** 屏幕像素密度为'XLDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_XXLDPI

```cangjie
SCREEN_DENSITY_XXLDPI
```

**功能：** 屏幕像素密度为'XXLDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SCREEN_DENSITY_XXXLDPI

```cangjie
SCREEN_DENSITY_XXXLDPI
```

**功能：** 屏幕像素密度为'XXXLDPI'。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ConfigurationScreenDensity)

```cangjie
public operator func !=(other: ConfigurationScreenDensity): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationScreenDensity](#enum-configurationscreendensity)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ConfigurationScreenDensity)

```cangjie
public operator func ==(other: ConfigurationScreenDensity): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ConfigurationScreenDensity](#enum-configurationscreendensity)|是|-|另一个枚举值。|

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