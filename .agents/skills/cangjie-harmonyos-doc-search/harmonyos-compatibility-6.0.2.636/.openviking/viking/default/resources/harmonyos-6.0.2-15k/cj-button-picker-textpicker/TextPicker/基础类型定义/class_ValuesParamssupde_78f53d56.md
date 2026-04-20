### class ValuesParams<sup>(deprecated)</sup>

```cangjie
public class ValuesParams {
    public var values: Option<Array<String>>
    public var valueschangeEvent:(Array<String>) -> Unit
    public init(values!: ?Array<String> = None)
    public init(values!: (?Array<String>, (Array<String>) -> Unit) = (None, {values => }))
}
```

**功能：** 记录文本选择器组件参数的结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var values

```cangjie
public var values: Option<Array<String>>
```

**功能：** 文本选择器的值参数。

**类型：** Option\<Array\<String>>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var valueschangeEvent

```cangjie
public var valueschangeEvent:(Array<String>) -> Unit
```

**功能：** 文本选择器值改变时回调的事件。

**类型：** (Array\<String>)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(?Array\<String>)

```cangjie
public init(values!: ?Array<String> = None)
```

**功能：** 构建文本选择器组件参数结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|?Array\<String>|否|None| **命名参数。** 构建ValueParams结构体。|

#### init((?Array\<String>,(Array\<String>) -> Unit))

```cangjie
public init(values!: (?Array<String>, (Array<String>) -> Unit) = (None, {_ =>}))
```

**功能：** 构建文本选择器组件参数结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|(?Array\<String>,(Array\<String>)->Unit)|否|(None, {_ =>})| **命名参数。** 构建ValueParams结构体。|