## enum CompressLevel

```cangjie
public enum CompressLevel <: Equatable<CompressLevel> & ToString {
    | COMPRESS_LEVEL_NO_COMPRESSION
    | COMPRESS_LEVEL_BEST_SPEED
    | COMPRESS_LEVEL_BEST_COMPRESSION
    | COMPRESS_LEVEL_DEFAULT_COMPRESSION
    | ...
}
```

**功能：** 压缩速度级别。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**父类型：**

- Equatable\<CompressLevel>
- ToString

### COMPRESS_LEVEL_BEST_COMPRESSION

```cangjie
COMPRESS_LEVEL_BEST_COMPRESSION
```

**功能：** 最佳压缩等级。

**起始版本：** 19

### COMPRESS_LEVEL_BEST_SPEED

```cangjie
COMPRESS_LEVEL_BEST_SPEED
```

**功能：** 最佳速度压缩等级。

**起始版本：** 19

### COMPRESS_LEVEL_DEFAULT_COMPRESSION

```cangjie
COMPRESS_LEVEL_DEFAULT_COMPRESSION
```

**功能：** 默认压缩等级。

**起始版本：** 19

### COMPRESS_LEVEL_NO_COMPRESSION

```cangjie
COMPRESS_LEVEL_NO_COMPRESSION
```

**功能：** 压缩率为0压缩等级。

**起始版本：** 19

### func !=(CompressLevel)

```cangjie
public operator func !=(other: CompressLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressLevel](#enum-compresslevel)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CompressLevel)

```cangjie
public operator func ==(other: CompressLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressLevel](#enum-compresslevel)|是|另一个枚举值。|

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