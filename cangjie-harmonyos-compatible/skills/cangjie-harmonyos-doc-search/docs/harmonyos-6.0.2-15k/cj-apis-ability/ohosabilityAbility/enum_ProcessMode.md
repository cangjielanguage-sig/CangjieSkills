## enum ProcessMode

```cangjie
public enum ProcessMode <: Equatable<ProcessMode> & ToString {
    | NEW_PROCESS_ATTACH_TO_PARENT
    | NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM
    | ATTACH_TO_STATUS_BAR_ITEM
    | ...
}
```

**功能：** 进程模式。该功能仅在平板类设备上生效。
ProcessMode作为StartOptions的一个属性，仅在[UIAbilityContext.startAbility](#func-startabilitywant-startoptions)中生效，用来指定目标Ability的进程模式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<ProcessMode>

- ToString

### ATTACH_TO_STATUS_BAR_ITEM

```cangjie
ATTACH_TO_STATUS_BAR_ITEM
```

**功能：** 启动Ability，并绑定该Ability所在进程到状态栏图标上。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### NEW_PROCESS_ATTACH_TO_PARENT

```cangjie
NEW_PROCESS_ATTACH_TO_PARENT
```

**功能：** 创建一个新进程，并在该进程上启动Ability。该进程会跟随父进程退出。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM

```cangjie
NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM
```

**功能：** 创建一个新进程，在该进程上启动Ability，并绑定该进程到状态栏图标上。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(ProcessMode)

```cangjie
public operator func !=(other: ProcessMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProcessMode](#enum-processmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ProcessMode)

```cangjie
public operator func ==(other: ProcessMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProcessMode](#enum-processmode)|是|-|另一个枚举值。|

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