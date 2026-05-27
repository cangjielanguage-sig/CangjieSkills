### SHOW_MODE_KEY

```cangjie
SHOW_MODE_KEY
```

**功能：** 指示展示模式，值为枚举类型[ShowMode](#enum-showmode)。值为：ohos.extra.param.key.showMode。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SUB_PACKAGE_NAME

```cangjie
SUB_PACKAGE_NAME
```

**功能：** 指示子包名。值为：ohos.param.atomicservice.subpackageName。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### SUPPORT_CONTINUE_PAGE_STACK_KEY

```cangjie
SUPPORT_CONTINUE_PAGE_STACK_KEY
```

**功能：** 指示在跨端迁移过程中是否迁移页面栈信息，默认值为true，自动迁移页面栈信息。值为：ohos.extra.param.key.supportContinuePageStack。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### SUPPORT_CONTINUE_SOURCE_EXIT_KEY

```cangjie
SUPPORT_CONTINUE_SOURCE_EXIT_KEY
```

**功能：** 指示跨端迁移源端应用是否退出，默认值为true，源端应用自动退出。值为：ohos.extra.param.key.supportContinueSourceExit。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func !=(Params)

```cangjie
public operator func !=(other: Params): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Params](#enum-params)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(Params)

```cangjie
public operator func ==(other: Params): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Params](#enum-params)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): String
```

**功能：** 获取当前枚举的所表示的值。供[Want](#class-want)的Params操作使用。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举所表示的值。|

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