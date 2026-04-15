## class RandomAccessFileOptions

```cangjie
public class RandomAccessFileOptions {
    public var start: Option<Int64>
    public var end: Option<Int64>
    public init(
        start!: Option<Int64> = None,
        end!: Option<Int64> = None
    )
}
```

**功能：** 可选项类型，支持 createRandomAccessFile 接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var end

```cangjie
public var end: Option<Int64>
```

**功能：** 表示期望读取结束的位置，单位为字节。可选，默认文件末尾。

**类型：** Option\<Int64>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var start

```cangjie
public var start: Option<Int64>
```

**功能：** 表示期望读取文件的位置，单位为字节。可选，默认从当前位置开始读。

**类型：** Option\<Int64>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(Option\<Int64>, Option\<Int64>)

```cangjie
public init(
    start!: Option<Int64> = None,
    end!: Option<Int64> = None
)
```

**功能：** 构造RandomAccessFileOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Option\<Int64>|否|None|**命名参数。** 表示期望读取文件的位置，单位为字节。可选，默认从当前位置开始读。|
|end|Option\<Int64>|否|None|**命名参数。** 表示期望读取结束的位置，单位为字节。可选，默认文件末尾。|

## class ReaderIterator

```cangjie
public class ReaderIterator {}
```

**功能：** 文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法来构建一个ReaderIterator实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### func next()

```cangjie
public func next(): ReaderIteratorResult
```

**功能：** 获取迭代器下一项内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ReaderIteratorResult](#class-readeriteratorresult)|文件读取迭代器返回结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900005 | I/O error. |
  | 13900037 | No data available. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"
    let options: Options = Options(encoding: "utf-8")
    let readerIterator = FileIo.readLines(filePath, options: options)
    var result = readerIterator.next()
    while (!result.done) {
        Hilog.info(0, "test", "content: ${result.value}", "")
        result = readerIterator.next()
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## class ReaderIteratorResult

```cangjie
public class ReaderIteratorResult {
    public var done: Bool
    public var value: String
}
```

**功能：** 文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var done

```cangjie
public var done: Bool
```

**功能：**  迭代器是否已完成迭代。true：已完成迭代；false：未完成迭代。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var value

```cangjie
public var value: String
```

**功能：** 逐行读取的文件文本内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22