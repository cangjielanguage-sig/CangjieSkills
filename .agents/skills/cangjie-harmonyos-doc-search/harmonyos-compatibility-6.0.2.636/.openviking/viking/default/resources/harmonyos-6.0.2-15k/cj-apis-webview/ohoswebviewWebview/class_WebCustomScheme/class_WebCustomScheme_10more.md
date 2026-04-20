## class WebCustomScheme

```cangjie
public class WebCustomScheme {
    public var isCodeCacheSupported: Bool = false
    public var isCspBypassing: Bool = true
    public var isDisplayIsolated: Bool = true
    public var isLocal: Bool = true
    public var isSecure: Bool = true
    public var isStandard: Bool = true
    public var isSupportCORS: Bool = true
    public var isSupportFetch: Bool = true
    public var schemeName: String
    public init(schemeName: String)
}
```

**功能：** 表示自定义协议配置。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**示例：**

```cangjie
let webScheme: WebCustomScheme = WebCustomScheme("myapp")
```

### var isCodeCacheSupported

```cangjie
public var isCodeCacheSupported: Bool = false
```

**功能：** 设置了该选项的scheme的js资源是否支持生成code cache。true表示设置了该选项的scheme的js资源支持生成code cache，false表示设置了该选项的scheme的js资源不支持生成code cache。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isCspBypassing

```cangjie
public var isCspBypassing: Bool = true
```

**功能：** 设置了该选项的scheme可以绕过内容安全策略（CSP）检查。true表示设置了该选项的scheme可以绕过内容安全策略（CSP）检查，false表示设置了该选项的scheme不可以绕过内容安全策略（CSP）检查。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isDisplayIsolated

```cangjie
public var isDisplayIsolated: Bool = true
```

**功能：** 设置了该选项的scheme的内容是否只能从相同scheme的其他内容中显示或访问。true表示设置了该选项的scheme的内容只能从相同scheme的其他内容中显示或访问，false表示设置了该选项的scheme的内容不是只能从相同scheme的其他内容中显示或访问。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isLocal

```cangjie
public var isLocal: Bool = true
```

**功能：** 设置了该选项的scheme是否将使用与“file”协议相同的安全规则来处理。true表示设置了该选项的scheme将使用与“file”协议相同的安全规则来处理，false表示设置了该选项的scheme不使用与“file”协议相同的安全规则来处理。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isSecure

```cangjie
public var isSecure: Bool = true
```

**功能：** 设置了该选项的scheme是否将使用与应用于“https”的安全规则相同的安全规则来处理。true表示设置了该选项的scheme将使用与应用于“https”的安全规则相同的安全规则来处理，false表示设置了该选项的scheme不使用与应用于“https”的安全规则相同的安全规则来处理。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isStandard

```cangjie
public var isStandard: Bool = true
```

**功能：** 设置了该选项的scheme是否将作为标准scheme进行处理。标准scheme需要符合RFC 1738第3.1节中定义的URL规范化和解析规则。true表示设置了该选项的scheme将作为标准scheme进行处理，false表示设置了该选项的scheme不作为标准scheme进行处理。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isSupportCORS

```cangjie
public var isSupportCORS: Bool = true
```

**功能：** 是否支持跨域请求。true表示支持跨域请求，false表示不支持跨域请求。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var isSupportFetch

```cangjie
public var isSupportFetch: Bool = true
```

**功能：** 是否支持fetch请求。true表示支持fetch请求，false表示不支持fetch请求。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var schemeName

```cangjie
public var schemeName: String
```

**功能：** 自定义协议名称。最大长度为32，其字符仅支持小写字母、数字、'.'、'+'、'-'，同时需要以字母开头。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20