## struct ReaderIteratorResult

```cangjie
public struct ReaderIteratorResult {}
```

**功能：** 文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### let done

```cangjie
public let done: Bool
```

**功能：** 迭代器是否已完成迭代。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: String
```

**功能：** 逐行读取的文件文本内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 只读

**起始版本：** 12