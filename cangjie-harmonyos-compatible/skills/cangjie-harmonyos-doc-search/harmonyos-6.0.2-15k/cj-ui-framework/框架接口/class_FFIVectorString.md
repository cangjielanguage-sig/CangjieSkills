## class FFIVectorString

```cangjie
public class FFIVectorString {
    public init(vec: VectorStringHandle)
    public init(size: Int64)
}
```

**功能：** FFI容器类型，供框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(VectorStringHandle)

```cangjie
public init(vec: VectorStringHandle)
```

**功能：** 创建FFIVectorString类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vec|VectorStringHandle|是|-|字符串类型数组指针。|

### init(Int64)

```cangjie
public init(size: Int64)
```

**功能：** 创建FFIVectorString类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int64|是|-|字符串数组元素。|

### func free()

```cangjie
public func free(): Unit
```

**功能：** 释放字符串数组，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func getElement(Int64)

```cangjie
public func getElement(index: Int64): String
```

**功能：** 获取字符串数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|元素值。|

### func getNativeHandle()

```cangjie
public func getNativeHandle(): VectorStringHandle
```

**功能：** 获取字符串数组指针，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|VectorStringHandle|字符串数组指针。|

### func getSize()

```cangjie
public func getSize(): Int64
```

**功能：** 获取字符串数组长度，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|字符串数组长度。|

### func setElement(Int64, String)

```cangjie
public func setElement(index: Int64, value: String): Unit
```

**功能：** 替换字符串数组指定索引的元素，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|索引值。|
|value|String|是|-|替换元素。|