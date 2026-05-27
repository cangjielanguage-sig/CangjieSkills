# ohos.image.interop（图片处理互操作）

本模块提供[PixelMap](./cj-apis-image.md#class-pixelmap)进行互操作的能力。

## 导入模块

```cangjie
import kit.ImageKit.*
```

## interface JSSystemObjectInteropType

```cangjie
public interface JSSystemObjectInteropType {
    static func fromJSValue(context: JSContext, input: JSValue): PixelMap
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 提供[PixelMap](./cj-apis-image.md#class-pixelmap)进行互操作的能力。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): PixelMap
```

**功能：** 从JSValue转换为[PixelMap](./cj-apis-image.md#class-pixelmap)类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](./cj-apis-image.md#class-pixelmap)|返回 PixelMap 类型实例。|

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|返回ArkTS统一类型。|

## class PixelMap

```cangjie
extend PixelMap <: JSSystemObjectInteropType {}
```

**功能：** 拓展[PixelMap](./cj-apis-image.md#class-pixelmap)类，可以和ArkTs互操作。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): PixelMap
```

**功能：** 从JSValue转换为[PixelMap](./cj-apis-image.md#class-pixelmap)类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](./cj-apis-image.md#class-pixelmap)|返回PixelMap类型实例。|

### func toJSValue(JSContext): JSValue

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 默认值 |说明               |
| :------ | :------ | :---- | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是 | - | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |
