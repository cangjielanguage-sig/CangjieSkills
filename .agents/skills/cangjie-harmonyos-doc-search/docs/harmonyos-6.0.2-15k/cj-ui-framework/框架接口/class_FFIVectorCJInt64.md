## class FFIVectorCJInt64

```cangjie
public class FFIVectorCJInt64 {
    public init(vec: VectorCJInt64Handle)
    public init(size: Int64)
}
```

**功能：** FFI容器类型，供框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(VectorCJInt64Handle)

```cangjie
public init(vec: VectorCJInt64Handle)
```

**功能：** 创建FFIVectorCJInt64类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vec|[VectorCJInt64Handle](#type-vectorcjint64handle)|是|-|整型类型数组指针。|

### init(Int64)

```cangjie
public init(size: Int64)
```

**功能：** 创建FFIVectorCJInt64类型对象。

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

### func getNativeHandle()

```cangjie
public func getNativeHandle(): VectorCJInt64Handle
```

**功能：** 获取整型类型数组指针，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[VectorCJInt64Handle](#type-vectorcjint64handle)|整型类型数组指针。|

### func setElement(Int64, Int64)

```cangjie
public func setElement(index: Int64, value: Int64): Unit
```

**功能：** 替换数组中指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|
|value|Int64|是|-|替换元素。|