## class If

```cangjie
public class If <: ComponentRender {
    public init(subcomponent: () -> Unit)
}
```

**功能：** if/else组件的定义结构体，供UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ComponentRender](#interface-componentrender)

### init(() -> Unit)

```cangjie
public init(subcomponent: () -> Unit)
```

**功能：** 创建If类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subcomponent|()->Unit|是|-|子组件。|

### static func branchId(Int32)

```cangjie
public static func branchId(value: Int32): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|-|

### static func getBranchId()

```cangjie
public static func getBranchId(): Int32
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|-|

### func genChild()

```cangjie
public func genChild(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func initial()

```cangjie
public func initial(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func pop()

```cangjie
public func pop(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func update()

```cangjie
public func update(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## struct NativeDimension

```cangjie
public struct NativeDimension {
    public NativeDimension(
        public let value: Float64,
        public let unit: Int32
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let unit

```cangjie
public let unit: Int32
```

**功能：** UI框架使用。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: Float64
```

**功能：** UI框架使用。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### NativeDimension(Float64, Int32)

```cangjie
public NativeDimension(
    public let value: Float64,
    public let unit: Int32
)
```

**功能：** 创建NativeDimension类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|像素值。|
|unit|Int32|是|-|单位|

## struct NativeLength

```cangjie
public struct NativeLength {
    public NativeLength(
        public let value: Float64,
        public let unitType: Int32
    )
}
```

**功能：** 框架内使用结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let unitType

```cangjie
public let unitType: Int32
```

**功能：** UI框架使用。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: Float64
```

**功能：** UI框架使用。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### NativeLength(Float64, Int32)

```cangjie
public NativeLength(
    public let value: Float64,
    public let unitType: Int32
)
```

**功能：** 创建NativeLength类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|像素值。|
|unitType|Int32|是|-|单位。|