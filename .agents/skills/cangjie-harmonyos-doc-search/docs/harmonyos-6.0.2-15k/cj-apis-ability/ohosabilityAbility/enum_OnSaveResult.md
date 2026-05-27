## enum OnSaveResult

```cangjie
public enum OnSaveResult <: Equatable<OnSaveResult> & ToString {
    | ALL_AGREE
    | CONTINUATION_REJECT
    | CONTINUATION_MISMATCH
    | RECOVERY_AGREE
    | RECOVERY_REJECT
    | ALL_REJECT
    | ...
}
```

**功能：** 保存应用数据的结果，该类型为枚举，可配合Ability的[onSaveState(reason, wantParam)](cj-apis-ability.md#func-onsavestatestatetype-string)方法完成相应的返回。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<OnSaveResult>

- ToString

### ALL_AGREE

```cangjie
ALL_AGREE
```

**功能：** 总是同意保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### ALL_REJECT

```cangjie
ALL_REJECT
```

**功能：** 总是拒绝保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CONTINUATION_MISMATCH

```cangjie
CONTINUATION_MISMATCH
```

**功能：** 迁移不匹配。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### CONTINUATION_REJECT

```cangjie
CONTINUATION_REJECT
```

**功能：** 拒绝迁移保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### RECOVERY_AGREE

```cangjie
RECOVERY_AGREE
```

**功能：** 同意恢复保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### RECOVERY_REJECT

```cangjie
RECOVERY_REJECT
```

**功能：** 拒绝恢复保存状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(OnSaveResult)

```cangjie
public operator func !=(other: OnSaveResult): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnSaveResult](#enum-onsaveresult)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(OnSaveResult)

```cangjie
public operator func ==(other: OnSaveResult): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnSaveResult](#enum-onsaveresult)|是|-|另一个枚举值。|

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