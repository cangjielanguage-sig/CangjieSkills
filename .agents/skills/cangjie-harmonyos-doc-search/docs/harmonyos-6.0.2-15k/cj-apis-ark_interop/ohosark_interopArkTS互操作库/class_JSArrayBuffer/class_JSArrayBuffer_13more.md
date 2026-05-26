## class JSArrayBuffer

```cangjie
public class JSArrayBuffer <: JSHeapObject {}
```

**功能：** JSArrayBuffer 对象用来表示通用的原始二进制数据缓冲区。通过创建 JS ArrayBuffer 对象，可以获取对象字节长度，转换为仓颉数组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSHeapObject](#class-jsheapobject)

### prop byteLength

```cangjie
public prop byteLength: Int32
```

**功能：** ArrayBuffer 的字节数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** Int32

**读写能力：** 只读

### func readBytes()

```cangjie
public func readBytes(): Array<Byte>
```

**功能：** 读取二进制数据，转换为仓颉数组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Byte>|仓颉数组。|

### func toArrayBufferJSValue()

```cangjie
public func toArrayBufferJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 ArrayBuffer 的 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func toFloat32Array()

```cangjie
public func toFloat32Array(): Array<Float32>
```

**功能：** 转换为仓颉数组 Array\<Float32>。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|仓颉数组。|

### func toFloat32ArrayJSValue()

```cangjie
public func toFloat32ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Float32Array 的 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func toFloat64Array()

```cangjie
public func toFloat64Array(): Array<Float64>
```

**功能：** 转换为仓颉数组 Array\<Float64>。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|仓颉数组。|

### func toFloat64ArrayJSValue()

```cangjie
public func toFloat64ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Float64Array 的 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func toInt16Array()

```cangjie
public func toInt16Array(): Array<Int16>
```

**功能：** 转换为仓颉数组 Array\<Int16>。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int16>|仓颉数组。|

### func toInt16ArrayJSValue()

```cangjie
public func toInt16ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Int16Array 的 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func toInt32Array()

```cangjie
public func toInt32Array(): Array<Int32>
```

**功能：** 转换为仓颉数组 Array\<Int32>。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|仓颉数组。|

### func toInt32ArrayJSValue()

```cangjie
public func toInt32ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Int32Array 的 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

### func toInt64Array()

```cangjie
public func toInt64Array(): Array<Int64>
```

**功能：** 转换为仓颉数组 Array\<Int64>。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int64>|仓颉数组。|