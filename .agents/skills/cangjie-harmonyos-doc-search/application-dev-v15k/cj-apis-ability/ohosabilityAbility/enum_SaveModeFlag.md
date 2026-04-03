## enum SaveModeFlag

```cangjie
public enum SaveModeFlag <: Equatable<SaveModeFlag> & ToString {
    | SAVE_WITH_FILE
    | SAVE_WITH_SHARED_MEMORY
    | ...
}
```

**功能：** 状态保存标志，[enableAppRecovery](#func-enableapprecoveryrestartflag-saveoccasionflag-savemodeflag)接口状态保存方式的参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<SaveModeFlag>

- ToString

### SAVE_WITH_FILE

```cangjie
SAVE_WITH_FILE
```

**功能：** 每次状态保存都会写入到本地文件缓存。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SAVE_WITH_SHARED_MEMORY

```cangjie
SAVE_WITH_SHARED_MEMORY
```

**功能：** 状态先保存在内存中，应用故障退出时写入到本地文件缓存。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func !=(SaveModeFlag)

```cangjie
public operator func !=(other: SaveModeFlag): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SaveModeFlag](#enum-savemodeflag)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SaveModeFlag)

```cangjie
public operator func ==(other: SaveModeFlag): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SaveModeFlag](#enum-savemodeflag)|是|-|另一个枚举值。|

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