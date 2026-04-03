## struct FFiCheckboxGroupResult

```cangjie
public struct FFiCheckboxGroupResult {
    public FFiCheckboxGroupResult(
        public let status: Int32,
        public let size: Int64,
        public let nameBuffer: CPointer<CString>
    )
}
```

**功能：** 多选框群组，用于控制多选框全选或者不全选状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let nameBuffer

```cangjie
public let nameBuffer: CPointer<CString>
```

**功能：** 群组内所有被选中的多选框名称。

**类型：** CPointer\< [CString](./cj-common-types.md#string)>

**读写能力：** 只读

**起始版本：** 12

### let size

```cangjie
public let size: Int64
```

**功能：** UI框架使用。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let status

```cangjie
public let status: Int32
```

**功能：** 选中状态。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### FFiCheckboxGroupResult(Int32, Int64, CPointer\<CString>)

```cangjie
public FFiCheckboxGroupResult(
    public let status: Int32,
    public let size: Int64,
    public let nameBuffer: CPointer<CString>
)
```

**功能：** 创建FFiCheckboxGroupResult类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|Int32|是|-|选中状态。|
|size|Int64|是|-|被选中的多选框数量。|
|nameBuffer|CPointer\< [CString](./cj-common-types.md#string)>|是|-|群组内所有被选中的多选框名称列表。|