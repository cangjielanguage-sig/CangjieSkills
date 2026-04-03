## enum SecurityLevel

```cangjie
public enum SecurityLevel <: Equatable<SecurityLevel> & ToString {
    | NoneLevel
    | Secure
    | Warning
    | Dangerous
    | ...
}
```

**功能：** 当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**父类型：**

- Equatable\<SecurityLevel>
- ToString

### NoneLevel

```cangjie
NoneLevel
```

**功能：** 页面既不绝对安全，也不是不安全，即是中立。例如，部分scheme非http/https的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### Secure

```cangjie
Secure
```

**功能：** 页面安全，页面使用的是HTTPS协议，且使用了信任的证书。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### Warning

```cangjie
Warning
```

**功能：** 页面不安全。例如，使用HTTP协议或使用HTTPS协议但使用旧版TLS版本。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### Dangerous

```cangjie
Dangerous
```

**功能：** 页面不安全。尝试HTTPS并失败、页面未通过身份验证、页面上包含不安全活动内容的HTTPS、恶意软件、网络钓鱼或任何其他可能危险的严重安全问题。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### func !=(SecurityLevel)

```cangjie
public operator func !=(other: SecurityLevel): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SecurityLevel](#enum-securitylevel)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(SecurityLevel)

```cangjie
public operator func ==(other: SecurityLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SecurityLevel](#enum-securitylevel)|是|-|待比较的另一个枚举值。|

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|