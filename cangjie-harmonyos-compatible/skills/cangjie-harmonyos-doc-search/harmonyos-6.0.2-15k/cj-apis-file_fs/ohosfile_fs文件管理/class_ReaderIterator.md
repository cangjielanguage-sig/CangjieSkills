## class ReaderIterator

```cangjie
public class ReaderIterator {}
```

**功能：** 文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法来构建一个ReaderIterator实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### func next()

```cangjie
public func next(): ReaderIteratorResult
```

**功能：** 取迭代器下一项内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ReaderIteratorResult](#struct-readeriteratorresult)|文件读取迭代器返回结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。