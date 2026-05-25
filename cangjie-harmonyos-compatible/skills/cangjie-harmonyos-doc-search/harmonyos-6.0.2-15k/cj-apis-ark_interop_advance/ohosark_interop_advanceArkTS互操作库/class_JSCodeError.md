## class JSCodeError

```cangjie
public class JSCodeError <: JSInteropException {
    public let code:?Int32
    public let jsError: String
    public let jsStack: Array<String>
    public init(jsMessage: String, jsStack: Array<String>)
}
```

**功能：** ArkTS 代码里的异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### let code

```cangjie
public let code:?Int32
```

**功能：** 异常错误码。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** ?Int32

**读写能力：** 只读

### let jsError

```cangjie
public let jsError: String
```

**功能：** 异常消息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** String

**读写能力：** 只读

### let jsStack

```cangjie
public let jsStack: Array<String>
```

**功能：** 异常栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** Array\<String>

**读写能力：** 只读

### init(String, Array\<String>)

```cangjie
public init(jsMessage: String, jsStack: Array<String>)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|jsMessage|String|是|-|ArkTS 异常消息。|
|jsStack|Array\<String>|是|-|ArkTS 异常栈。|