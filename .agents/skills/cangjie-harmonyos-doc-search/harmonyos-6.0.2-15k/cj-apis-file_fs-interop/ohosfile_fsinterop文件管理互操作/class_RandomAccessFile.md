## class RandomAccessFile

```cangjie
extend RandomAccessFile <: JSSystemObjectInteropType<RandomAccessFile> {}
```

**功能：** 随机读写文件流，在调用RandomAccessFile的方法前，需要先通过[createRandomAccessFile](./cj-apis-file_fs.md#static-func-createrandomaccessfilefile-int64)方法来构建一个RandomAccessFile实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**父类型：**

- [JSSystemObjectInteropType](#interface-jssystemobjectinteroptype)\<[RandomAccessFile](./cj-apis-file_fs.md#class-randomaccessfile)>

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

**返回值：**

| 类型        | 说明                                                         |
| :---------- | :----------------------------------------------------------- |
| [JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue) | 返回ArkTS统一类型。 |

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): RandomAccessFile
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[RandomAccessFile](./cj-apis-file_fs.md#class-randomaccessfile)类型。

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
| [RandomAccessFile](./cj-apis-file_fs.md#class-randomaccessfile) | 返回RandomAccessFile类型实例。|