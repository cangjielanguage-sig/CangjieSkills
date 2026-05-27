## enum OperationType

```cangjie
public enum OperationType <: Equatable<OperationType> & ToString {
    | UNKNOWN_TYPE
    | START_ABILITY
    | START_ABILITIES
    | START_SERVICE
    | SEND_COMMON_EVENT
    | ...
}
```

**功能：** 表示操作[WantAgent](#class-wantagent)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<OperationType>

- ToString

### SEND_COMMON_EVENT

```cangjie
SEND_COMMON_EVENT
```

**功能：** 发送一个公共事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### START_ABILITIES

```cangjie
START_ABILITIES
```

**功能：** 开启多个有页面的Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### START_ABILITY

```cangjie
START_ABILITY
```

**功能：** 开启一个有页面的Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### START_SERVICE

```cangjie
START_SERVICE
```

**功能：** 开启一个无页面的Ability（仅在FA模型下生效）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### UNKNOWN_TYPE

```cangjie
UNKNOWN_TYPE
```

**功能：** 不识别的类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(OperationType)

```cangjie
public operator func !=(other: OperationType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OperationType](#enum-operationtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(OperationType)

```cangjie
public operator func ==(other: OperationType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OperationType](#enum-operationtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|