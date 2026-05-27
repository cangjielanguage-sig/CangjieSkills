## 组件事件

### func onChange((CheckboxGroupResult) -> Unit)

```cangjie
public func onChange(callback: (CheckboxGroupResult) -> Unit): This
```

**功能：** CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([CheckboxGroupResult](#class-checkboxgroupresult))->Unit|是|-|多选框群组的信息。|

## 基础类型定义

### class CheckboxGroupResult

```cangjie
public class CheckboxGroupResult {
    public CheckboxGroupResult(
        public var status: SelectStatus,
        public var name: ArrayList<String>
    )
}
```

**功能：** 多选框群组选中状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var name

```cangjie
public var name: ArrayList<String>
```

**功能：** 群组内所有被选中的多选框名称。

**类型：** ArrayList\<String>

**读写能力：** 可读写

**起始版本：** 12

#### var status

```cangjie
public var status: SelectStatus
```

**功能：** 选中状态。

**类型：** [SelectStatus](#enum-selectstatus)

**读写能力：** 可读写

**起始版本：** 12

#### CheckboxGroupResult(SelectStatus, ArrayList\<String>)

```cangjie
public CheckboxGroupResult(
    public var status: SelectStatus,
    public var name: ArrayList<String>
)
```

**功能：** 构造多选框群组选中状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|[SelectStatus](#enum-selectstatus)|是|-|选中状态。|
|name|ArrayList\<String>|是|-|群组内所有被选中的多选框名称。|

### enum SelectStatus

```cangjie
public enum SelectStatus {
    | All
    | Part
    | None
}
```

**功能：** 多选框选择状态类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### All

```cangjie
All
```

**功能：** 群组多选择框全部选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Part

```cangjie
Part
```

**功能：** 群组多选择框部分选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### None

```cangjie
None
```

**功能：** 群组多选择框全部没有选择。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12