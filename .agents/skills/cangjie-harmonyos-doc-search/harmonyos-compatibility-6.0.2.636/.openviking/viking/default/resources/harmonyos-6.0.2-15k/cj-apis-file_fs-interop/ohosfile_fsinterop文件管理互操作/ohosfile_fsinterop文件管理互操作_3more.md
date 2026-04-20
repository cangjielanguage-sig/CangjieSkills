# ohos.file_fs.interop（文件管理互操作）

本模块提供File、RandomAccessFile以及Stream进行互操作的能力。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## interface JSSystemObjectInteropType

```cangjie
public interface JSSystemObjectInteropType<T> {
    static func fromJSValue(context: JSContext, input: JSValue): T
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** JS系统对象专用的拓展接口，以实现与[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)的互转。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为仓颉对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

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

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)| ArkTS统一类型。|