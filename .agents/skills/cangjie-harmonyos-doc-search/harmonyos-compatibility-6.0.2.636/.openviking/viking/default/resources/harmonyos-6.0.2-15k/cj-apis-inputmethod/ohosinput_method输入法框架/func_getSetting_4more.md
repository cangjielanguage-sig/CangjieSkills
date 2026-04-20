## func getSetting()

```cangjie
public func getSetting(): InputMethodSetting
```

**功能：** 获取客户端设置实例[InputMethodSetting](#class-inputmethodsetting)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[InputMethodSetting](#class-inputmethodsetting)|返回当前客户端设置实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 12800007 |setter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let inputMethodSetting = getSetting()
```

## func getSystemInputMethodConfigAbility()

```cangjie
public func getSystemInputMethodConfigAbility(): ElementName
```

**功能：** 获取系统输入法设置界面Ability信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[ElementName](../AbilityKit/cj-apis-ability.md#class-elementname)|系统输入法设置界面Ability的ElementName。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800008|input method manager service error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let inputMethodConfig = getSystemInputMethodConfigAbility()
```

## class CursorInfo

```cangjie
public class CursorInfo {
    public CursorInfo(
        public let left: Float64,
        public let top: Float64,
        public let width: Float64,
        public let height: Float64
    )
}
```

**功能：** 光标信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let height

```cangjie
public let height: Float64
```

**功能：** 光标的高度。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let left

```cangjie
public let left: Float64
```

**功能：** 光标的left坐标。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let top

```cangjie
public let top: Float64
```

**功能：** 光标的top坐标。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let width

```cangjie
public let width: Float64
```

**功能：** 光标的宽度。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### CursorInfo(Float64, Float64, Float64, Float64)

```cangjie
public CursorInfo(
    public let left: Float64,
    public let top: Float64,
    public let width: Float64,
    public let height: Float64
)
```

**功能：** 构建光标信息的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Float64|是|-|光标的left坐标。|
|top|Float64|是|-|光标的top坐标。|
|width|Float64|是|-|光标的宽度。|
|height|Float64|是|-|光标的高度。|

## class FunctionKey

```cangjie
public class FunctionKey {
    public FunctionKey(
        public let enterKeyType: EnterKeyType
    )
}
```

**功能：** 输入法功能键类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let enterKeyType

```cangjie
public let enterKeyType: EnterKeyType
```

**功能：** 输入法Enter键类型。

**类型：** [EnterKeyType](#enum-enterkeytype)

**读写能力：** 只读

**起始版本：** 19

### FunctionKey(EnterKeyType)

```cangjie
public FunctionKey(
    public let enterKeyType: EnterKeyType
)
```

**功能：** 构建输入法功能键类型的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enterKeyType|[EnterKeyType](#enum-enterkeytype)|是|-|输入法Enter键类型。|