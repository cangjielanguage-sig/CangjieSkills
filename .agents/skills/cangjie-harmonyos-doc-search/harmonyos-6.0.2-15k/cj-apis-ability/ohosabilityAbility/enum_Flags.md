## enum Flags

```cangjie
public enum Flags <: Equatable<Flags> & ToString {
    | FLAG_AUTH_READ_URI_PERMISSION
    | FLAG_AUTH_WRITE_URI_PERMISSION
    | FLAG_AUTH_PERSISTABLE_URI_PERMISSION
    | FLAG_INSTALL_ON_DEMAND
    | FLAG_START_WITHOUT_TIPS
    | ...
}
```

**功能：** Flags说明。用于表示处理[Want](#class-want)的方式。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**父类型：**

- Equatable\<Flags>

- ToString

### FLAG_AUTH_PERSISTABLE_URI_PERMISSION

```cangjie
FLAG_AUTH_PERSISTABLE_URI_PERMISSION
```

**功能：** 指示该URI可被接收方持久化。该字段仅在平板类设备上生效。值为：0x00000040。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### FLAG_AUTH_READ_URI_PERMISSION

```cangjie
FLAG_AUTH_READ_URI_PERMISSION
```

**功能：** 指示对URI执行读取操作的授权。值为：0x00000001。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### FLAG_AUTH_WRITE_URI_PERMISSION

```cangjie
FLAG_AUTH_WRITE_URI_PERMISSION
```

**功能：** 指示对URI执行写入操作的授权。值为：0x00000002。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### FLAG_INSTALL_ON_DEMAND

```cangjie
FLAG_INSTALL_ON_DEMAND
```

**功能：** 如果未安装指定的功能，请安装该功能。值为：0x00000800。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### FLAG_START_WITHOUT_TIPS

```cangjie
FLAG_START_WITHOUT_TIPS
```

**功能：** 如果隐式启动能力不能匹配任何应用程序，则不会弹出提示对话框。值为：0x40000000。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func !=(Flags)

```cangjie
public operator func !=(other: Flags): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Flags](#enum-flags)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(Flags)

```cangjie
public operator func ==(other: Flags): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Flags](#enum-flags)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取当前枚举的所表示的值。用于表示处理[Want](#class-want)的方式。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|当前枚举所表示的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|