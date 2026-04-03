## enum ShowMode

```cangjie
public enum ShowMode <: Equatable<ShowMode> & ToString {
    | WINDOW
    | EMBEDDED_FULL
    | ...
}
```

**功能：** ShowMode说明。用于表示拉起原子化服务的展示模式。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**父类型：**

- Equatable\<ShowMode>

- ToString

### EMBEDDED_FULL

```cangjie
EMBEDDED_FULL
```

**功能：** 指示嵌入式全屏拉起模式。值为：1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### WINDOW

```cangjie
WINDOW
```

**功能：** 指示独立窗口拉起模式。值为：0。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ShowMode)

```cangjie
public operator func !=(other: ShowMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShowMode](#enum-showmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ShowMode)

```cangjie
public operator func ==(other: ShowMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShowMode](#enum-showmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取当前枚举的所表示的值。用于表示拉起原子化服务的展示模式。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前枚举所表示的值。|

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