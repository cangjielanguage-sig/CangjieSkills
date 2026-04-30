## enum ReadyState

```cangjie
public enum ReadyState <: Equatable<ReadyState> & ToString {
    | HAVE_NOTHING
    | HAVE_METADATA
    | HAVE_CURRENT_DATA
    | HAVE_FUTURE_DATA
    | HAVE_ENOUGH_DATA
    | ...
}
```

**功能：** 播放器的缓存状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<ReadyState>
- ToString

### HAVE_CURRENT_DATA

```cangjie
HAVE_CURRENT_DATA
```

**功能：** 表示只缓存到当前的播放进度。

**起始版本：** 19

### HAVE_ENOUGH_DATA

```cangjie
HAVE_ENOUGH_DATA
```

**功能：** 表示缓存了足够的数据，保证播放流畅。

**起始版本：** 19

### HAVE_FUTURE_DATA

```cangjie
HAVE_FUTURE_DATA
```

**功能：** 表示缓存时长超过了当前的播放进度, 但是仍有可能导致卡顿。

**起始版本：** 19

### HAVE_METADATA

```cangjie
HAVE_METADATA
```

**功能：** 表示只缓存了媒体元数据。

**起始版本：** 19

### HAVE_NOTHING

```cangjie
HAVE_NOTHING
```

**功能：** 表示没有缓存。

**起始版本：** 19

### func !=(ReadyState)

```cangjie
public operator func !=(other: ReadyState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ReadyState](#enum-readystate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ReadyState)

```cangjie
public operator func ==(other: ReadyState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ReadyState](#enum-readystate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|