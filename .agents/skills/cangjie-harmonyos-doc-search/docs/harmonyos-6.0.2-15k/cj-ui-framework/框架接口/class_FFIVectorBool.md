## class FFIVectorBool

```cangjie
public class FFIVectorBool {
    public init(vec: VectorBoolHandle)
    public init(size: Int64)
}
```

**功能：** FFI容器类型，供框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(VectorBoolHandle)

```cangjie
public init(vec: VectorBoolHandle)
```

**功能：** 创建FFIVectorBool类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vec|[VectorBoolHandle](#type-vectorboolhandle)|是|-|布尔类型数组指针。|

### init(Int64)

```cangjie
public init(size: Int64)
```

**功能：** 创建FFIVectorBool类型对象。

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
public func getElement(index: Int64): Bool
```

**功能：** 获取数组元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|元素值。|

### func getNativeHandle()

```cangjie
public func getNativeHandle(): VectorBoolHandle
```

**功能：** 获取布尔类型数组指针，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[VectorBoolHandle](#type-vectorboolhandle)|布尔类型数组指针。|

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

### func setElement(Int64, Bool)

```cangjie
public func setElement(index: Int64, value: Bool): Unit
```

**功能：** 替换数组中指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|
|value|Bool|是|-|替换元素。|