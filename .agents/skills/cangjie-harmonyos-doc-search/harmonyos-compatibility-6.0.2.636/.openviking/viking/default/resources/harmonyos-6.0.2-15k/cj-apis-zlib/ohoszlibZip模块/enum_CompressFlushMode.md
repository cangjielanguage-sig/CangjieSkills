## enum CompressFlushMode

```cangjie
public enum CompressFlushMode <: Equatable<CompressFlushMode> & ToString {
    | NoFlush
    | PartialFlush
    | SyncFlush
    | FullFlush
    | Finish
    | Block
    | Trees
    | ...
}
```

**功能：** 压缩下刷模式。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**父类型：**

- Equatable\<CompressFlushMode>
- ToString

### Block

```cangjie
Block
```

**功能：** 允许更精确的控制。

**起始版本：** 20

### Finish

```cangjie
Finish
```

**功能：** 压缩或解压缩过程结束。

**起始版本：** 20

### FullFlush

```cangjie
FullFlush
```

**功能：** 压缩或解压缩过程结束。

**起始版本：** 20

### NoFlush

```cangjie
NoFlush
```

**功能：** 默认值，表示正常操作。

**起始版本：** 20

### PartialFlush

```cangjie
PartialFlush
```

**功能：** 在流中生成部分刷新点。

**起始版本：** 20

### SyncFlush

```cangjie
SyncFlush
```

**功能：** 在流中生成部分刷新点。

**起始版本：** 20

### Trees

```cangjie
Trees
```

**功能：** 实施过程中有特殊目的。

**起始版本：** 20

### func !=(CompressFlushMode)

```cangjie
public operator func !=(other: CompressFlushMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressFlushMode](#enum-compressflushmode)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CompressFlushMode)

```cangjie
public operator func ==(other: CompressFlushMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressFlushMode](#enum-compressflushmode)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|