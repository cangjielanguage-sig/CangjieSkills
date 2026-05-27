## class FFIVectorUInt8

```cangjie
public class FFIVectorUInt8 {
    public init(vec: VectorUInt8Handle)
    public init(size: Int64)
}
```

**功能：** FFI容器类型，供框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(VectorUInt8Handle)

```cangjie
public init(vec: VectorUInt8Handle)
```

**功能：** 创建FFIVectorUInt8类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vec|[VectorUInt8Handle](#type-vectoruint8handle)|是|-|无符号整型数组指针。|

### init(Int64)

```cangjie
public init(size: Int64)
```

**功能：** 创建FFIVectorUInt8类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int64|是|-|数组长度。|

### func free()

```cangjie
public func free(): Unit
```

**功能：** 释放数组，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func getElement(Int64)

```cangjie
public func getElement(index: Int64): UInt8
```

**功能：** 获取无符号整型数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt8|元素值。|

### func getNativeHandle()

```cangjie
public func getNativeHandle(): VectorUInt8Handle
```

**功能：** 获取无符号整型数组指针，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[VectorUInt8Handle](#type-vectoruint8handle)|无符号整型数组指针|

### func getSize()

```cangjie
public func getSize(): Int64
```

**功能：** 获取数组长度，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|数组长度。|

### func setElement(Int64, UInt8)

```cangjie
public func setElement(index: Int64, value: UInt8): Unit
```

**功能：** 替换无符号整型数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|
|value|UInt8|是|-|替换元素。|