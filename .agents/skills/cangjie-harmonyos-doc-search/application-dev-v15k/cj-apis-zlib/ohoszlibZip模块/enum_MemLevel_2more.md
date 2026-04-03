## enum MemLevel

```cangjie
public enum MemLevel <: Equatable<MemLevel> & ToString {
    | MEM_LEVEL_MIN
    | MEM_LEVEL_DEFAULT
    | MEM_LEVEL_MAX
    | ...
}
```

**功能：** 压缩内存级别。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**父类型：**

- Equatable\<MemLevel>
- ToString

### MEM_LEVEL_DEFAULT

```cangjie
MEM_LEVEL_DEFAULT
```

**功能：** zip接口在压缩过程中默认使用内存。

**起始版本：** 19

### MEM_LEVEL_MAX

```cangjie
MEM_LEVEL_MAX
```

**功能：** zip接口在压缩过程中最大使用内存。

**起始版本：** 19

### MEM_LEVEL_MIN

```cangjie
MEM_LEVEL_MIN
```

**功能：** zip接口在压缩过程中最小使用内存。

**起始版本：** 19

### func !=(MemLevel)

```cangjie
public operator func !=(other: MemLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[MemLevel](#enum-memlevel)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(MemLevel)

```cangjie
public operator func ==(other: MemLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[MemLevel](#enum-memlevel)|是|另一个枚举值。|

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

## enum ParallelStrategy

```cangjie
public enum ParallelStrategy <: Equatable<ParallelStrategy> & ToString {
    | ParallelStrategySequential
    | ParallelStrategyParallelDecompression
    | ...
}
```

**功能：** 压缩并行策略。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**父类型：**

- Equatable\<ParallelStrategy>
- ToString

### ParallelStrategyParallelDecompression

```cangjie
ParallelStrategyParallelDecompression
```

**功能：** 表示并行解压。

**起始版本：** 20

### ParallelStrategySequential

```cangjie
ParallelStrategySequential
```

**功能：** 表示串行压缩和串行解压。

**起始版本：** 20

### func !=(ParallelStrategy)

```cangjie
public operator func !=(other: ParallelStrategy): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[ParallelStrategy](#enum-parallelstrategy)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ParallelStrategy)

```cangjie
public operator func ==(other: ParallelStrategy): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[ParallelStrategy](#enum-parallelstrategy)|是|另一个枚举值。|

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