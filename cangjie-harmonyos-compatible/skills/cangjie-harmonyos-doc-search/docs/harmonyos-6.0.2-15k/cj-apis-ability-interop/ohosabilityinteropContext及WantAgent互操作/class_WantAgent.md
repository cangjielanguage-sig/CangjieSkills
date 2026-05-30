## class WantAgent

```cangjie
extend WantAgent <: JSSystemObjectInteropType<WantAgent> {}
```

**功能：** 拓展[WantAgent](./cj-apis-ability.md#class-wantagent)类，可以和ArkTs互操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)\<[WantAgent](./cj-apis-ability.md#class-wantagent)>

### func toJSValue(JSContext): JSValue

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明               |
| :------ | :------ | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |

### static func fromJSValue(JSContext, JSValue): WantAgent

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): WantAgent
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[WantAgent](./cj-apis-ability.md#class-wantagent)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明               |
| :------ | :------ | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   | ArkTS互操作上下文。 |
| input    | [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 是 | ArkTS统一类型。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [WantAgent](./cj-apis-ability.md#class-wantagent) | 返回WantAgent类型实例。 |