# ohos.net.connection.interop（网络连接管理互操作）

本模块提供NetHandle进行互操作的能力。

## 导入模块

```cangjie
import kit.NetworkKit.*
```

## interface JSSystemObjectInteropType

```cangjie
public interface JSSystemObjectInteropType<T> {
    static func fromJSValue(context: JSContext, input: JSValue): T
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** JS系统对象专用的拓展接口，以实现与[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)的互转。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为仓颉对象。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|T|仓颉对象。|

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉对象转换成[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)| ArkTS统一类型。|

## class NetHandle

```cangjie
extend NetHandle <: JSSystemObjectInteropType<NetHandle> {}
```

**功能：** 拓展[NetHandle](./cj-apis-net-connection.md#class-nethandle)类，可以和ArkTs互操作。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)\<[NetHandle](./cj-apis-net-connection.md#class-nethandle)>

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): NetHandle
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[NetHandle](./cj-apis-net-connection.md#class-nethandle)类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明               |
| :------ | :------ | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   | ArkTS互操作上下文。 |
| input    | [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 是 | ArkTS统一类型。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [NetHandle](./cj-apis-net-connection.md#class-nethandle) | 返回NetHandle类型实例。 |
