## enum AccCallBackType

```cangjie
public enum AccCallBackType <: Equatable<AccCallBackType> & Hashable & ToString {
    | ACCCALLBACKTYPE_ACCESSIBILITYSTATECHANGE
    | ACCCALLBACKTYPE_TOUCHGUIDESTATECHANGE
    | ...
}
```

**功能：** 监听的事件名。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AccCallBackType](#enum-acccallbacktype)>
- Hashable
- ToString

### ACCCALLBACKTYPE_ACCESSIBILITYSTATECHANGE

```cangjie
ACCCALLBACKTYPE_ACCESSIBILITYSTATECHANGE
```

**功能：** 'accessibilityStateChange'，即辅助应用启用状态变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACCCALLBACKTYPE_TOUCHGUIDESTATECHANGE

```cangjie
ACCCALLBACKTYPE_TOUCHGUIDESTATECHANGE
```

**功能：** 'touchGuideStateChange'，即触摸浏览启用状态变化事件。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(AccCallBackType)

```cangjie
public operator func !=(other: AccCallBackType): Bool
```

**功能：** 对监听的事件名进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AccCallBackType](#enum-acccallbacktype)|是|-|监听事件名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若监听的事件名不同，返回true，否则返回false。|

### func ==(AccCallBackType)

```cangjie
public operator func ==(other: AccCallBackType): Bool
```

**功能：** 对监听事件名进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AccCallBackType](#enum-acccallbacktype)|是|-|监听的事件名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若监听的事件名相同，返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取监听事件名的哈希值。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|监听事件名的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将监听事件名转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|监听事件名的字符串表示。|