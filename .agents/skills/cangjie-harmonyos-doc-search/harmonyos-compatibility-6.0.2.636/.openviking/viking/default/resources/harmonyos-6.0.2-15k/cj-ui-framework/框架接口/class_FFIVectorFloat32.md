## class FFIVectorFloat32

```cangjie
public class FFIVectorFloat32 {
    public init(vec: VectorFloat32Handle)
    public init(size: Int64)
}
```

**功能：** FFI容器类型，供框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(VectorFloat32Handle)

```cangjie
public init(vec: VectorFloat32Handle)
```

**功能：** 创建FFIVectorFloat32类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vec|[VectorFloat32Handle](#type-vectorfloat32handle)|是|-|浮点类型数组指针。|

### init(Int64)

```cangjie
public init(size: Int64)
```

**功能：** 创建FFIVectorFloat32类型对象。

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
public func getElement(index: Int64): Float32
```

**功能：** 获取数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|元素值。|

### func getNativeHandle()

```cangjie
public func getNativeHandle(): VectorFloat32Handle
```

**功能：** 获取浮点类型数组指针，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[VectorFloat32Handle](#type-vectorfloat32handle)|浮点类型数组指针。|

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

### func setElement(Int64, Float32)

```cangjie
public func setElement(index: Int64, value: Float32): Unit
```

**功能：** 替换数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|
|value|Float32|是|-|替换元素。|