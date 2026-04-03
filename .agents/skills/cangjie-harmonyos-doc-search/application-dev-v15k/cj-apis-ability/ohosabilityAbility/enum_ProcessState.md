## enum ProcessState

```cangjie
public enum ProcessState <: Equatable<ProcessState> & ToString {
    | STATE_CREATE
    | STATE_FOREGROUND
    | STATE_ACTIVE
    | STATE_BACKGROUND
    | STATE_DESTROY
    | ...
}
```

**功能：** 表示进程状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<ProcessState>

- ToString

### STATE_ACTIVE

```cangjie
STATE_ACTIVE
```

**功能：** 当进程在获焦的时候处于的状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### STATE_BACKGROUND

```cangjie
STATE_BACKGROUND
```

**功能：** 当进程处于后台不可见时处于的状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### STATE_CREATE

```cangjie
STATE_CREATE
```

**功能：** 当进程在创建中的时候处于的状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### STATE_DESTROY

```cangjie
STATE_DESTROY
```

**功能：** 当进程在销毁的时候处于的状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### STATE_FOREGROUND

```cangjie
STATE_FOREGROUND
```

**功能：** 当进程切换到前台的时候处于的状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ProcessState)

```cangjie
public operator func !=(other: ProcessState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProcessState](#enum-processstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ProcessState)

```cangjie
public operator func ==(other: ProcessState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProcessState](#enum-processstate)|是|-|另一个枚举值。|

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