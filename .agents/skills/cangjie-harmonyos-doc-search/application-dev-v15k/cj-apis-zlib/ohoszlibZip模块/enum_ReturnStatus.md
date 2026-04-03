## enum ReturnStatus

```cangjie
public enum ReturnStatus <: Equatable<ReturnStatus> & ToString {
    | Ok
    | StreamEnd
    | NeedDict
    | ...
}
```

**功能：** 函数返回状态。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**父类型：**

- Equatable\<ReturnStatus>
- ToString

### NeedDict

```cangjie
NeedDict
```

**功能：** 函数调用成功，表示需要预设字典才能继续解压缩。

**起始版本：** 20

### Ok

```cangjie
Ok
```

**功能：** 函数调用成功。

**起始版本：** 20

### StreamEnd

```cangjie
StreamEnd
```

**功能：** 函数调用成功，表示已处理了整个数据。

**起始版本：** 20

### func !=(ReturnStatus)

```cangjie
public operator func !=(other: ReturnStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[ReturnStatus](#enum-returnstatus)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ReturnStatus)

```cangjie
public operator func ==(other: ReturnStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|other|[ReturnStatus](#enum-returnstatus)|是|另一个枚举值。|

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