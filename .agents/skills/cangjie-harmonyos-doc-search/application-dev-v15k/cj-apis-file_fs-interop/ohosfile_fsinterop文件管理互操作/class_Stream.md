## class Stream

```cangjie
extend Stream <: JSSystemObjectInteropType<Stream> {}
```

**功能：** 文件流，在调用Stream的方法前，需要先通过[FileFs.createStream](./cj-apis-file_fs.md#static-func-createstreamstring-string)方法或者[FileFs.fdopenStream](./cj-apis-file_fs.md#static-func-fdopenstreamint32-string)来构建一个Stream实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)\<[Stream](./cj-apis-file_fs.md#class-stream)>

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为ArkTS统一类型。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 默认值 |说明               |
| :------ | :------ | :---- | :---- | :------------------ |
| context   | [JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext) | 是 | - | ArkTS互操作上下文。 |

**返回值：**

| 类型        | 说明            |
| :---------- | :-------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): Stream
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[Stream](./cj-apis-file_fs.md#class-stream)类型。

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
| [Stream](./cj-apis-file_fs.md#class-stream) | 返回Stream类型实例。|