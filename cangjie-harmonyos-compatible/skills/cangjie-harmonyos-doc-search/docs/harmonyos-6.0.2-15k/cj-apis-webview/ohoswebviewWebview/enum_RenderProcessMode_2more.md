## enum RenderProcessMode

```cangjie
public enum RenderProcessMode <: Equatable<RenderProcessMode> & ToString {
    | SINGLE
    | MULTIPLE
    | ...
}
```

**功能：** ArkWeb渲染子进程模式类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<RenderProcessMode>
- ToString

### MULTIPLE

```cangjie
MULTIPLE
```

**功能：** ArkWeb多渲染子进程模式。该模式下，每个Web一个渲染子进程。

**起始版本：** 19

### SINGLE

```cangjie
SINGLE
```

**功能：** ArkWeb单渲染子进程模式。该模式下，多个Web复用一个渲染子进程。

**起始版本：** 19

### func !=(RenderProcessMode)

```cangjie
public operator func !=(other: RenderProcessMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RenderProcessMode](#enum-renderprocessmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(RenderProcessMode)

```cangjie
public operator func ==(other: RenderProcessMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RenderProcessMode](#enum-renderprocessmode)|是|-|另一个枚举值。|

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

## enum SecureDnsMode

```cangjie
public enum SecureDnsMode <: Equatable<SecureDnsMode> & ToString {
    | SECURE_ONLY
    | AUTO
    | OFF
    | ...
}
```

**功能：** Web组件使用HTTPDNS的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<SecureDnsMode>
- ToString

### AUTO

```cangjie
AUTO
```

**功能：** 自动模式，用于解析的设定dns服务器不可用时，可自动回落至系统DNS。

**起始版本：** 19

### OFF

```cangjie
OFF
```

**功能：** 不使用HTTPDNS，可以用于撤销之前使用的HTTPDNS配置。

**起始版本：** 19

### SECURE_ONLY

```cangjie
SECURE_ONLY
```

**功能：** 强制使用设定的HTTPDNS服务器进行域名解析。

**起始版本：** 19

### func !=(SecureDnsMode)

```cangjie
public operator func !=(other: SecureDnsMode): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SecureDnsMode](#enum-securednsmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(SecureDnsMode)

```cangjie
public operator func ==(other: SecureDnsMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SecureDnsMode](#enum-securednsmode)|是|-|待比较的另一个枚举值。|

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