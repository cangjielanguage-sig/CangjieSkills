## func createPhotoEditorExtensionContextFromJSValue(JSContext, JSValue)

```cangjie
public func createPhotoEditorExtensionContextFromJSValue(context: JSContext, input: JSValue): PhotoEditorExtensionContext
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[PhotoEditorExtensionContext](./cj-apis-ability.md#class-photoeditorextensioncontext)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoEditorExtensionContext](./cj-apis-ability.md#class-photoeditorextensioncontext)| 返回PhotoEditorExtensionContext类型实例。 |

## func createUIExtensionContextFromJSValue(JSContext, JSValue)

```cangjie
public func createUIExtensionContextFromJSValue(context: JSContext, input: JSValue): UIExtensionContext
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[UIExtensionContext](./cj-apis-ability.md#class-uiextensioncontext)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIExtensionContext](./cj-apis-ability.md#class-uiextensioncontext)| 返回UIExtensionContext类型实例。|

## interface JSSystemObjectInteropType

```cangjie
public interface JSSystemObjectInteropType<T> {
    static func fromJSValue(context: JSContext, input: JSValue): T
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** JS系统对象专用的拓展接口，以实现与JSValue的互转。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为仓颉对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

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