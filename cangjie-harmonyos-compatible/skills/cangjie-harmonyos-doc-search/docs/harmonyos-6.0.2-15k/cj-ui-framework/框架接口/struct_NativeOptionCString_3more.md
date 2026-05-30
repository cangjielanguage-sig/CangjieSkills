## struct NativeOptionCString

```cangjie
public struct NativeOptionCString {
    public NativeOptionCString(
        public let hasValue: Bool,
        public let value: CString
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
public let value: CString
```

**功能：** UI框架使用。

**类型：**  [CString](./cj-common-types.md#string)

**读写能力：** 只读

**起始版本：** 12

### NativeOptionCString(Bool, CString)

```cangjie
public NativeOptionCString(
    public let hasValue: Bool,
    public let value: CString
)
```

**功能：** 创建NativeOptionCString类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value| [CString](./cj-common-types.md#string)|是|-|值数据。|

### func free()

```cangjie
public func free()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## struct NativeOptionCallBack

```cangjie
public struct NativeOptionCallBack {
    public NativeOptionCallBack(
        public let hasValue: Bool,
        public let value: Int64
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
public let value: Int64
```

**功能：** UI框架使用。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### NativeOptionCallBack(Bool, Int64)

```cangjie
public NativeOptionCallBack(
    public let hasValue: Bool,
    public let value: Int64
)
```

**功能：** 创建NativeOptionCallBack类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|Int64|是|-|值数据。|

## struct NativeOptionFloat32

```cangjie
public struct NativeOptionFloat32 {
    public NativeOptionFloat32(
        public let hasValue: Bool,
        public let value: Float32
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
public let value: Float32
```

**功能：** UI框架使用。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### NativeOptionFloat32(Bool, Float32)

```cangjie
public NativeOptionFloat32(
    public let hasValue: Bool,
    public let value: Float32
)
```

**功能：** 创建NativeOptionFloat32类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hasValue|Bool|是|-|标记是否为空值。|
|value|Float32|是|-|值数据。|