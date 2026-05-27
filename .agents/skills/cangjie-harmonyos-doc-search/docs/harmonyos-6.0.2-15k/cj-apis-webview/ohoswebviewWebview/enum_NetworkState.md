## enum NetworkState

```cangjie
public enum NetworkState <: Equatable<NetworkState> & ToString {
    | EMPTY
    | IDLE
    | LOADING
    | NETWORK_ERROR
    | ...
}
```

**功能：** 播放器的网络状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<NetworkState>
- ToString

### EMPTY

```cangjie
EMPTY
```

**功能：** 播放器还没有开始下载数据。

**起始版本：** 19

### IDLE

```cangjie
IDLE
```

**功能：** 播放器网络状态空闲，比如媒体分片下载完成，下一个分片还没有开始下载。

**起始版本：** 19

### LOADING

```cangjie
LOADING
```

**功能：** 播放器正在下载媒体数据。

**起始版本：** 19

### NETWORK_ERROR

```cangjie
NETWORK_ERROR
```

**功能：** 发生了网络错误。

**起始版本：** 19

### func !=(NetworkState)

```cangjie
public operator func !=(other: NetworkState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NetworkState](#enum-networkstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(NetworkState)

```cangjie
public operator func ==(other: NetworkState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NetworkState](#enum-networkstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|