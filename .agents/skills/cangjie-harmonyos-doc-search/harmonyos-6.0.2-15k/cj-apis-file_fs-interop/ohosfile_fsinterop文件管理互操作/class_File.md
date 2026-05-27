## class File

```cangjie
extend File <: JSSystemObjectInteropType<File> {}
```

**功能：** 由open接口打开的File对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)\<[File](./cj-apis-file_fs.md#class-file)>

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

> **说明：**
>
> 类型转换后会发生所有权转移，旧对象将不可用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 默认值 |说明               |
| :------ | :------ | :---- | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是 | - | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): File
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[File](./cj-apis-file_fs.md#class-file)类型。

> **说明：**
>
> 类型转换后会发生所有权转移，旧对象将不可用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 默认值 |说明               |
| :------ | :------ | :---- | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是   |- |ArkTS互操作上下文。 |
| input    | [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 是 |-|ArkTS统一类型。 |

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [File](./cj-apis-file_fs.md#class-file) | 返回File类型实例。|