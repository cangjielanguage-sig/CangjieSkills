### class SelectedParams<sup>(deprecated)</sup>

```cangjie
public class SelectedParams {
    public var selected: UInt32
    public var selectedchangeEvent:(UInt32) -> Unit
    public init(selected!: UInt32 = 0)
    public init(selected!: (UInt32, (UInt32) -> Unit) = ( 0, {value => }))
}
```

**功能：** 记录选择结果参数的结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selected

```cangjie
public var selected: UInt32
```

**功能：** 选择结果所在结果数组的下标。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selectedchangeEvent

```cangjie
public var selectedchangeEvent:(UInt32) -> Unit
```

**功能：** 选择结果改变时回调的事件。

**类型：** (UInt32)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(UInt32)

```cangjie
public init(selected!: UInt32 = 0)
```

**功能：** 构建选择结果参数结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selected|UInt32|否|0| **命名参数。** 组件选择的结果下标。|

#### init((UInt32,(UInt32) -> Unit))

```cangjie
public init(selected!: (UInt32, (UInt32) -> Unit) = ( 0, {_ =>}))
```

**功能：** 构建选择结果参数结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selected|(UInt32,(UInt32)->Unit)|否|(0, {_ =>})| **命名参数。** 组件多个选择的结果下标。|

### class SelectedsParams<sup>(deprecated)</sup>

```cangjie
public class SelectedsParams {
    public var selecteds: Option<Array<UInt32>>
    public var selectedschangeEvent:(Array<UInt32>) -> Unit
    public init(selecteds!: ?Array<UInt32> = None)
    public init(selecteds!: (?Array<UInt32>, (Array<UInt32>) -> Unit) = ( None, {values => }))
}
```

**功能：** 记录选择结果参数的结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selecteds

```cangjie
public var selecteds: Option<Array<UInt32>>
```

**功能：** 选择结果所在结果数组的下标。

**类型：** Option\<Array\<UInt32>>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selectedschangeEvent

```cangjie
public var selectedschangeEvent:(Array<UInt32>) -> Unit
```

**功能：** 选择结果改变时回调的事件。

**类型：** (Array\<UInt32>)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(?Array\<UInt32>)

```cangjie
public init(selecteds!: ?Array<UInt32> = None)
```

**功能：** 创建SelectedsParams结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selecteds|?Array\<UInt32>|否|None| **命名参数。** 选择结果所在结果数组的下标。|

#### init((?Array\<UInt32>,(Array\<UInt32>) -> Unit))

```cangjie
public init(selecteds!: (?Array<UInt32>, (Array<UInt32>) -> Unit) = ( None, {_ =>}))
```

**功能：** 创建SelectedsParams结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selecteds|(?Array\<UInt32>,(Array\<UInt32>)->Unit)|否|(None, {_ =>})| **命名参数。** 选择结果所在结果数组的下标。|