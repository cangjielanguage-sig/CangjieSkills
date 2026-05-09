## 基础类型定义

### class CheckboxGroupResult

```cangjie
public class CheckboxGroupResult {
    public var name: Array<String>
    public var status: SelectStatus
    public init(
        status: SelectStatus,
        name: Array<String>
    )
}
```

**功能：** 多选框群组选中状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var name

```cangjie
public var name: Array<String>
```

**功能：** 群组内所有被选中的多选框名称。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var status

```cangjie
public var status: SelectStatus
```

**功能：** 选中状态。

**类型：** [SelectStatus](./cj-common-types.md#enum-selectstatus)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(SelectStatus, Array\<String>)

```cangjie
public init(
    status: SelectStatus,
    name: Array<String>
)
```

**功能：** 构造多选框群组选中状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|[SelectStatus](./cj-common-types.md#enum-selectstatus)|是|-|选中状态。|
|name|Array\<String>|是|-|群组内所有被选中的多选框名称。|

### type OnCheckboxGroupChangeCallback

```cangjie
public type OnCheckboxGroupChangeCallback = (CheckboxGroupResult) -> Unit
```

**功能：** (CheckboxGroupResult) -> Unit 的类型别名。

**类型：** ([CheckboxGroupResult](#class-checkboxgroupresult)) -> Unit