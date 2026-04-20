## enum CallerType

```cangjie
public enum CallerType <: Equatable<CallerType> {
    | RELEASE
    | ...
}
```

**功能：** releaseCall事件类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- Equatable\<CallerType>

### RELEASE

```cangjie
RELEASE
```

**功能：** release类型的releaseCall事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(CallerType)

```cangjie
public operator func !=(other: CallerType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallerType](#enum-callertype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CallerType)

```cangjie
public operator func ==(other: CallerType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallerType](#enum-callertype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|