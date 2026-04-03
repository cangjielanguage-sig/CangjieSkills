# ohos.rpc.interop（IRemoteObject互操作）

本模块提供[RemoteObject](#class-remoteobject)及[RemoteProxy](#class-remoteproxy)进行互操作的能力。

## 导入模块

```cangjie
import kit.IPCKit.*
```

## func fromJSValue(JSContext, JSValue)

```cangjie
public func fromJSValue(context: JSContext, input: JSValue): IRemoteObject
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为IRemoteObject类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是|-|ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteObject](./cj-apis-rpc.md#interface-iremoteobject)|返回IRemoteObject类型实例。|

## interface SystemObjectInteropTypeToJS

```cangjie
public interface SystemObjectInteropTypeToJS {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 提供转换为ArkTS统一类型的接口。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) |是|-|ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) |返回ArkTS统一类型。|

## class RemoteObject

```cangjie
extend RemoteObject <: SystemObjectInteropTypeToJS {}
```

**功能：** 实现远程对象。服务提供者必须继承此类。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**父类型：**

- [SystemObjectInteropTypeToJS](#interface-systemobjectinteroptypetojs)

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：**转换为ArkTS统一类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明               |
| :------ | :------ | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |

## class RemoteProxy

```cangjie
extend RemoteProxy <: SystemObjectInteropTypeToJS {}
```

**功能：** 实现IRemoteObject代理对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**父类型：**

- [SystemObjectInteropTypeToJS](#interface-systemobjectinteroptypetojs)

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：**转换为ArkTS统一类型。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明               |
| :------ | :------ | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |
