## interface SystemObjectInteropTypeToJS

```cangjie
public interface SystemObjectInteropTypeToJS {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 系统对象专用的拓展接口，以实现与[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)的互转。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉对象转换成[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)| ArkTS统一类型。|

## class Context

```cangjie
extend Context <: SystemObjectInteropTypeToJS {}
```

**功能：** 拓展[Context](./cj-apis-ability.md#class-context)类，可以和ArkTs互操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**父类型：**

- [SystemObjectInteropTypeToJS](#interface-systemobjectinteroptypetojs)

### func toJSValue(JSContext): JSValue

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 默认值 |说明               |
| :------ | :------ | :---- | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是 | - | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |