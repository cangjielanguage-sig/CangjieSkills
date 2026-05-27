## struct JSValue

```cangjie
public struct JSValue {}
```

**功能：** 一个ArkTS变量（弱类型，短生命周期）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

JSValue是ArkTS运行时统一类型，也是直接与ArkTS运行时交互的数据类型。

只有互操作接口可以创建JSValue，其生命周期在出栈（被创建时的栈）时结束，不能拷贝、捕获以及在非互操作函数返回。如果需要传递该变量，需要先转换，再以仓颉类型或是安全引用的形式传递。

### func asArray()

```cangjie
public func asArray(): JSArray
```

**功能：** 把一个 JSValue 转换为 JSArray 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSArray](#class-jsarray)|一个 ArkTS 数组的引用。|

### func asArray(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asArray(_: JSContext): JSArray
```

**功能：** 把一个 JSValue 转换为 JSArray 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArray](#class-jsarray)|一个 ArkTS 数组的引用。|

### func asArrayBuffer()

```cangjie
public func asArrayBuffer(): JSArrayBuffer
```

**功能：** 把一个 JSValue 转换为 JSArrayBuffer 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|一个ArkTS ArrayBuffer的引用。|

### func asArrayBuffer(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asArrayBuffer(_: JSContext): JSArrayBuffer
```

**功能：** 把一个 JSValue 转换为 JSArrayBuffer 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|一个ArkTS ArrayBuffer的引用。|

### func asBigInt()

```cangjie
public func asBigInt(): JSBigInt
```

**功能：** 把一个 JSValue 转换为 JSBigInt 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSBigInt](#class-jsbigint)|ArkTS bigint的引用。|

### func asBigInt(JSContext) <sub>(deprecated)</sub>

```cangjie
public func asBigInt(_: JSContext): JSBigInt
```

**功能：** 把一个 JSValue 转换为 JSBigInt 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSBigInt](#class-jsbigint)|ArkTS bigint的引用。|

### func asBoolean()

```cangjie
public func asBoolean(): JSBoolean
```

**功能：** 把一个 JSValue 转换为 JSBoolean 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSBoolean](#struct-jsboolean)|一个 ArkTS boolean。|

### func asClass()

```cangjie
public func asClass(): JSClass
```

**功能：** 把一个 JSValue 转换为 JSClass 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSClass](#class-jsclass)|一个ArkTS 类的引用。|