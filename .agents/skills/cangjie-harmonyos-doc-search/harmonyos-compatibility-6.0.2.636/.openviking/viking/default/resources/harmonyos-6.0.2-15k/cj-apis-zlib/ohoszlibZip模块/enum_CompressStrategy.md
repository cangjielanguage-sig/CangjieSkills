## enum CompressStrategy

```cangjie
public enum CompressStrategy <: Equatable<CompressStrategy> & ToString {
    | COMPRESS_STRATEGY_DEFAULT_STRATEGY
    | COMPRESS_STRATEGY_FILTERED
    | COMPRESS_STRATEGY_HUFFMAN_ONLY
    | COMPRESS_STRATEGY_RLE
    | COMPRESS_STRATEGY_FIXED
    | ...
}
```

**功能：** 压缩策略。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**父类型：**

- Equatable\<CompressStrategy>
- ToString

### COMPRESS_STRATEGY_DEFAULT_STRATEGY

```cangjie
COMPRESS_STRATEGY_DEFAULT_STRATEGY
```

**功能：** 常规数据策略。

**起始版本：** 19

### COMPRESS_STRATEGY_FILTERED

```cangjie
COMPRESS_STRATEGY_FILTERED
```

**功能：** 过滤器产生的数据压缩策略。

**起始版本：** 19

### COMPRESS_STRATEGY_FIXED

```cangjie
COMPRESS_STRATEGY_FIXED
```

**功能：** 固定的压缩策略。

**起始版本：** 19

### COMPRESS_STRATEGY_HUFFMAN_ONLY

```cangjie
COMPRESS_STRATEGY_HUFFMAN_ONLY
```

**功能：** 霍夫曼编码格式压缩策略。

**起始版本：** 19

### COMPRESS_STRATEGY_RLE

```cangjie
COMPRESS_STRATEGY_RLE
```

**功能：** 游标编码压缩策略。

**起始版本：** 19

### func !=(CompressStrategy)

```cangjie
public operator func !=(other: CompressStrategy): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressStrategy](#enum-compressstrategy)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CompressStrategy)

```cangjie
public operator func ==(other: CompressStrategy): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressStrategy](#enum-compressstrategy)|是|另一个枚举值。|

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