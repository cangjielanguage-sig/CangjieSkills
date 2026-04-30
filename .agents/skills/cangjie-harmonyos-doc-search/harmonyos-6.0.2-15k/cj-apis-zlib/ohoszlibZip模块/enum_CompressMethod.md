## enum CompressMethod

```cangjie
public enum CompressMethod <: Equatable<CompressMethod> & ToString {
    | Deflated
    | ...
}
```

**功能：** 压缩方法。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**父类型：**

- Equatable\<CompressMethod>
- ToString

### Deflated

```cangjie
Deflated
```

**功能：** 压缩方法。

**起始版本：** 20

### func !=(CompressMethod)

```cangjie
public operator func !=(other: CompressMethod): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressMethod](#enum-compressmethod)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CompressMethod)

```cangjie
public operator func ==(other: CompressMethod): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[CompressMethod](#enum-compressmethod)|是|另一个枚举值。|

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