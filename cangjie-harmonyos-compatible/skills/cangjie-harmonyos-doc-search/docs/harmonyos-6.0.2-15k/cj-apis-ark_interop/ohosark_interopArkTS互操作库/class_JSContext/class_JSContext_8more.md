## class JSContext

```cangjie
public class JSContext {}
```

**功能：** 一个单线程执行的 ArkTS 互操作上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

JSContext和ArkTS运行时是一一对应的关系，其主要目标是创建JSValue和安全引用、管理ArkTS侧引用的仓颉对象的生命周期。

一个JSContext持有一个ArkTS运行时的弱引用，这个JSContext不会影响ArkTS运行时的生命周期，当ArkTS运行时失效后使用这个JSContext会抛出仓颉异常。

### prop env

```cangjie
public prop env: JSEnv
```

**功能：** ArkTS 互操作上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** JSEnv

**读写能力：** 只读

### prop global

```cangjie
public prop global: JSObject
```

**功能：** js全局环境变量 globalThis。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** [JSObject](#class-jsobject)

**读写能力：** 只读

### func array(Array\<JSValue>)

```cangjie
public func array(arr: Array<JSValue>): JSArray
```

**功能：** 创建一个 ArkTS 数组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arr|Array\<[JSValue](#struct-jsvalue)>|是|-|ArkTS 数组的引用。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArray](#class-jsarray)|ArkTS 数组|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.array([])
    return result.toJSValue()
}
```

### func arrayBuffer(Int32)

```cangjie
public func arrayBuffer(length: Int32): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|Int32|是|-|内存块大小。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.arrayBuffer(Int32(10))
    return result.toJSValue()
}
```

### func arrayBuffer(Array\<Byte>)

```cangjie
public func arrayBuffer(data: Array<Byte>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Byte>|是|-|仓颉数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.arrayBuffer([1, 2, 3, 4, 5])
    return result.toJSValue()
}
```

### func arrayBuffer(Array\<Int8>)

```cangjie
public func arrayBuffer(data: Array<Int8>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int8>|是|-|仓颉数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

### func arrayBuffer(Array\<Int16>)

```cangjie
public func arrayBuffer(data: Array<Int16>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int16>|是|-|仓颉数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|