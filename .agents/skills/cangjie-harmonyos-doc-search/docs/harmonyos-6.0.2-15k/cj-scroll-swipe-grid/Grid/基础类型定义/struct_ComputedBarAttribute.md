### struct ComputedBarAttribute

```cangjie
public struct ComputedBarAttribute {
    public ComputedBarAttribute (
        public let totalOffset: Float64,
        public let totalLength: Float64
    )
}
```

**功能：** 滚动条位置和长度对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let totalLength

```cangjie
public let totalLength: Float64
```

**功能：** Grid内容总长度，单位px。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### let totalOffset

```cangjie
public let totalOffset: Float64
```

**功能：** Grid内容相对显示区域的总偏移，单位px。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### ComputedBarAttribute(Float64, Float64)

```cangjie
public ComputedBarAttribute (
    public let totalOffset: Float64,
    public let totalLength: Float64
)
```

**功能：** 创建一个ComputedBarAttribute类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|totalOffset|Float64|是|-|Grid内容相对显示区域的总偏移，单位px。|
|totalLength|Float64|是|-|Grid内容总长度，单位px。|