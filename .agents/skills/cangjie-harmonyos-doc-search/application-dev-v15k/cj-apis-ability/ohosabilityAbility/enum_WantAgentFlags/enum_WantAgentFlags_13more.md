## enum WantAgentFlags

```cangjie
public enum WantAgentFlags <: Equatable<WantAgentFlags> & ToString {
    | ONE_TIME_FLAG
    | NO_BUILD_FLAG
    | CANCEL_PRESENT_FLAG
    | UPDATE_PRESENT_FLAG
    | CONSTANT_FLAG
    | REPLACE_ELEMENT
    | REPLACE_ACTION
    | REPLACE_URI
    | REPLACE_ENTITIES
    | REPLACE_BUNDLE
    | ...
}
```

**功能：** 表示使用[WantAgent](#class-wantagent)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<WantAgentFlags>

- ToString

### CANCEL_PRESENT_FLAG

```cangjie
CANCEL_PRESENT_FLAG
```

**功能：** 在生成一个新的WantAgent对象前取消已存在的一个WantAgent对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CONSTANT_FLAG

```cangjie
CONSTANT_FLAG
```

**功能：** WantAgent是不可变的。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### NO_BUILD_FLAG

```cangjie
NO_BUILD_FLAG
```

**功能：** 如果描述WantAgent对象不存在，则不创建它，直接返回null。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### ONE_TIME_FLAG

```cangjie
ONE_TIME_FLAG
```

**功能：** WantAgent仅能使用一次。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### REPLACE_ACTION

```cangjie
REPLACE_ACTION
```

**功能：** 当前Want中的action属性可被WantAgent.trigger()中Want的action属性取代。当前版本暂不支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### REPLACE_BUNDLE

```cangjie
REPLACE_BUNDLE
```

**功能：** 当前Want中的bundleName属性可被WantAgent.trigger()中Want的bundleName属性取代。当前版本暂不支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### REPLACE_ELEMENT

```cangjie
REPLACE_ELEMENT
```

**功能：** 当前Want中的element属性可被WantAgent.trigger()中Want的element属性取代。当前版本暂不支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### REPLACE_ENTITIES

```cangjie
REPLACE_ENTITIES
```

**功能：** 当前Want中的entities属性可被WantAgent.trigger()中Want的entities属性取代。当前版本暂不支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### REPLACE_URI

```cangjie
REPLACE_URI
```

**功能：** 当前Want中的uri属性可被WantAgent.trigger()中Want的uri属性取代。当前版本暂不支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### UPDATE_PRESENT_FLAG

```cangjie
UPDATE_PRESENT_FLAG
```

**功能：** 使用新的WantAgent的额外数据替换已存在的WantAgent中的额外数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(WantAgentFlags)

```cangjie
public operator func !=(other: WantAgentFlags): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WantAgentFlags](#enum-wantagentflags)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(WantAgentFlags)

```cangjie
public operator func ==(other: WantAgentFlags): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WantAgentFlags](#enum-wantagentflags)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|