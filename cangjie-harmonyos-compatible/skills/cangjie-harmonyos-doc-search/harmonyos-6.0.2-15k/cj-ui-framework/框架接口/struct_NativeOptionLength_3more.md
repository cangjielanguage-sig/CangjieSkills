## struct NativeOptionLength

```cangjie
public struct NativeOptionLength {
    public NativeOptionLength(
        public let hasValue: Bool,
        public let value: NativeLength
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let hasValue

```cangjie
public let hasValue: Bool
```

**功能：** UI框架使用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: NativeLength
```

**功能：** UI框架使用。

**类型：** [NativeLength](#struct-nativelength)

**读写能力：** 只读

**起始版本：** 12

### NativeOptionLength(Bool, NativeLength)

```cangjie
public NativeOptionLength(
    public let hasValue: Bool,
    public let value: NativeLength
)
```

**功能：** 创建NativeOptionLength类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|[NativeLength](#struct-nativelength)|是|-|值数据。|

## struct NativeOptionUInt32

```cangjie
public struct NativeOptionUInt32 {
    public NativeOptionUInt32(
        public let hasValue: Bool,
        public let value: UInt32
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let hasValue

```cangjie
public let hasValue: Bool
```

**功能：** UI框架使用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: UInt32
```

**功能：** UI框架使用。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### NativeOptionUInt32(Bool, UInt32)

```cangjie
public NativeOptionUInt32(
    public let hasValue: Bool,
    public let value: UInt32
)
```

**功能：** 创建NativeOptionUInt32类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|UInt32|是|-|值数据。|

## struct NativeRectangle

```cangjie
public struct NativeRectangle {
    public NativeRectangle(
        let x: Float64,
        let xUnit: Int32,
        let y: Float64,
        let yUnit: Int32,
        let width: Float64,
        let widthUnit: Int32,
        let height: Float64,
        let heightUnit: Int32
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### NativeRectangle(Float64, Int32, Float64, Int32, Float64, Int32, Float64, Int32)

```cangjie
public NativeRectangle(
    let x: Float64,
    let xUnit: Int32,
    let y: Float64,
    let yUnit: Int32,
    let width: Float64,
    let widthUnit: Int32,
    let height: Float64,
    let heightUnit: Int32
)
```

**功能：** 创建NativeRectangle类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|-|
|xUnit|Int32|是|-|-|
|y|Float64|是|-|-|
|yUnit|Int32|是|-|-|
|width|Float64|是|-|-|
|widthUnit|Int32|是|-|-|
|height|Float64|是|-|-|
|heightUnit|Int32|是|-|-|