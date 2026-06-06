## enum WebDownloadState

```cangjie
public enum WebDownloadState <: Equatable<WebDownloadState> & ToString {
    | IN_PROGRESS
    | COMPLETE
    | CANCELED
    | INTERRUPTED
    | PENDING
    | PAUSED
    | UNKNOWN
    | ...
}
```

**功能：** 下载任务的状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<WebDownloadState>
- ToString

### CANCELED

```cangjie
CANCELED
```

**功能：** 下载任务已经被取消。

**起始版本：** 19

### COMPLETE

```cangjie
COMPLETE
```

**功能：** 获取下载的进度，100代表下载完成。

**起始版本：** 19

### INTERRUPTED

```cangjie
INTERRUPTED
```

**功能：** 下载任务被中断。

**起始版本：** 19

### IN_PROGRESS

```cangjie
IN_PROGRESS
```

**功能：** 下载任务正在进行中。

**起始版本：** 19

### PAUSED

```cangjie
PAUSED
```

**功能：** 下载任务已经被暂停。

**起始版本：** 19

### PENDING

```cangjie
PENDING
```

**功能：** 下载任务等待开始。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 下载任务未知状态。

**起始版本：** 19

### func !=(WebDownloadState)

```cangjie
public operator func !=(other: WebDownloadState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebDownloadState](#enum-webdownloadstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(WebDownloadState)

```cangjie
public operator func ==(other: WebDownloadState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebDownloadState](#enum-webdownloadstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串表示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|