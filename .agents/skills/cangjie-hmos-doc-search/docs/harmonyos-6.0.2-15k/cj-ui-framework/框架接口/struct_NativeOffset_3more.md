## struct NativeOffset

```cangjie
public struct NativeOffset {
    public NativeOffset(
        public let dx: NativeLength,
        public let dy: NativeLength
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let dx

```cangjie
public let dx: NativeLength
```

**功能：** UI框架使用。

**类型：** [NativeLength](#struct-nativelength)

**读写能力：** 只读

**起始版本：** 12

### let dy

```cangjie
public let dy: NativeLength
```

**功能：** UI框架使用。

**类型：** [NativeLength](#struct-nativelength)

**读写能力：** 只读

**起始版本：** 12

### NativeOffset(NativeLength, NativeLength)

```cangjie
public NativeOffset(
    public let dx: NativeLength,
    public let dy: NativeLength
)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dx|[NativeLength](#struct-nativelength)|是|-|水平方向偏移量。|
|dy|[NativeLength](#struct-nativelength)|是|-|竖直方向偏移量。|

## struct NativeOptionBool

```cangjie
public struct NativeOptionBool {
    public NativeOptionBool(
        public let hasValue: Bool,
        public let value: Bool
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
public let value: Bool
```

**功能：** UI框架使用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### NativeOptionBool(Bool, Bool)

```cangjie
public NativeOptionBool(
    public let hasValue: Bool,
    public let value: Bool
)
```

**功能：** 创建NativeOptionBool类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|Bool|是|-|数据值。|

## struct NativeOptionCArrInt32

```cangjie
public struct NativeOptionCArrInt32 {
    public NativeOptionCArrInt32(
        public let hasValue: Bool,
        public let value: CArrInt32
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
public let value: CArrInt32
```

**功能：** UI框架使用。

**类型：** [CArrInt32](#struct-carrint32)

**读写能力：** 只读

**起始版本：** 12

### NativeOptionCArrInt32(Bool, CArrInt32)

```cangjie
public NativeOptionCArrInt32(
    public let hasValue: Bool,
    public let value: CArrInt32
)
```

**功能：** 创建NativeOptionCArrInt32类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|[CArrInt32](#struct-carrint32)|是|-|值数据。|