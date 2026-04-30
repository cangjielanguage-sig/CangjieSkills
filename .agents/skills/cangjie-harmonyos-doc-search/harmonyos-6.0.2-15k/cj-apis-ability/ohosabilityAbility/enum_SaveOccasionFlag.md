## enum SaveOccasionFlag

```cangjie
public enum SaveOccasionFlag <: Equatable<SaveOccasionFlag> & ToString {
    | SAVE_WHEN_ERROR
    | SAVE_WHEN_BACKGROUND
    | ...
}
```

**功能：** 保存条件标志，[enableAppRecovery](#func-enableapprecoveryrestartflag-saveoccasionflag-savemodeflag)接口状态保存时的选项参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<SaveOccasionFlag>

- ToString

### SAVE_WHEN_BACKGROUND

```cangjie
SAVE_WHEN_BACKGROUND
```

**功能：** 当应用切入后台时保存。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SAVE_WHEN_ERROR

```cangjie
SAVE_WHEN_ERROR
```

**功能：** 当发生应用故障时保存。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(SaveOccasionFlag)

```cangjie
public operator func !=(other: SaveOccasionFlag): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SaveOccasionFlag](#enum-saveoccasionflag)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SaveOccasionFlag)

```cangjie
public operator func ==(other: SaveOccasionFlag): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SaveOccasionFlag](#enum-saveoccasionflag)|是|-|另一个枚举值。|

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