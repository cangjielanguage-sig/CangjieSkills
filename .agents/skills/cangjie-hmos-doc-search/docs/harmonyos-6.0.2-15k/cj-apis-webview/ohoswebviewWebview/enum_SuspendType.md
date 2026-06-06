## enum SuspendType

```cangjie
public enum SuspendType <: Equatable<SuspendType> & ToString {
    | ENTER_BACK_FORWARD_CACHE
    | ENTER_BACKGROUND
    | AUTO_CLEANUP
    | ...
}
```

**功能：** 表示播放器的挂起类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<SuspendType>
- ToString

### AUTO_CLEANUP

```cangjie
AUTO_CLEANUP
```

**功能：** 系统自动清理。

**起始版本：** 19

### ENTER_BACKGROUND

```cangjie
ENTER_BACKGROUND
```

**功能：** 页面进后台。

**起始版本：** 19

### ENTER_BACK_FORWARD_CACHE

```cangjie
ENTER_BACK_FORWARD_CACHE
```

**功能：** 页面进BFCache。

**起始版本：** 19

### func !=(SuspendType)

```cangjie
public operator func !=(other: SuspendType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SuspendType](#enum-suspendtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SuspendType)

```cangjie
public operator func ==(other: SuspendType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SuspendType](#enum-suspendtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取播放器挂起类型枚举的整数值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|播放器挂起类型枚举的整数值。|

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