## class AuthCallback

```cangjie
public class AuthCallback {
    public AuthCallback(
        public let onResult: (code: Int32, result: ?AuthResult) -> Unit,
        public let onRequestRedirected: (request: Want) -> Unit,
        public let onRequestContinued!: Option<() -> Unit>
    ) {}
}
```

**功能：** 认证器回调类。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

### let onResult

```cangjie
public let onResult: (code: Int32, result: ?AuthResult) -> Unit
```

**功能：** 通知请求结果。

**类型：** ([code](cj-apis-common_event_manager.md#let-code): Int32, result: ?[AuthResult](#class-authresult))->Unit

**读写能力：** 只读

**起始版本：** 19

### let onRequestRedirected

```cangjie
public let onRequestRedirected: (request: Want) -> Unit
```

**功能：** 通知请求被跳转。

**类型：** [Want](../AbilityKit/cj-apis-ability.md#class-want)->Unit

**读写能力：** 只读

**起始版本：** 19

### let onRequestContinued

```cangjie
public let onRequestContinued: Option<() -> Unit>
```

**功能：** 通知请求被继续处理。

**类型：** Option\<()->Unit>

**读写能力：** 只读

**起始版本：** 19

### AuthCallback((Int32, ?AuthResult) -> Unit, (Want) -> Unit, Option\<() -> Unit>)

```cangjie
public AuthCallback(
    public let onResult: (code: Int32, result: ?AuthResult) -> Unit,
    public let onRequestRedirected: (request: Want) -> Unit,
    public let onRequestContinued!: Option<() -> Unit>
)
```

**功能：** 构建AuthCallback实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onResult|([code](cj-apis-common_event_manager.md#let-code): Int32, result: ?[AuthResult](#class-authresult))|是|-|通知请求结果。|
|onRequestRedirected|[Want](../AbilityKit/cj-apis-ability.md#class-want)->Unit|是|-|通知请求被跳转。|
|onRequestContinued|Option\<()->Unit>|是|-| **命名参数。** 通知请求被继续处理。|

## class AuthResult

```cangjie
public class AuthResult {
    public AuthResult (
        public var account!: ?AppAccountInfo = None,
        public var tokenInfo!: ?AuthTokenInfo = None
    )
}
```

**功能：** 表示认证结果信息。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var account

```cangjie
public var account: ?AppAccountInfo = None
```

**功能：** 令牌所属的账号信息，默认为空。

**类型：** ?[AppAccountInfo](#class-appaccountinfo)

**读写能力：** 可读写

**起始版本：** 19

### var tokenInfo

```cangjie
public var tokenInfo: ?AuthTokenInfo = None
```

**功能：** 令牌信息，默认为空。

**类型：** ?[AuthTokenInfo](#class-authtokeninfo)

**读写能力：** 可读写

**起始版本：** 19

### AuthResult(?AppAccountInfo, ?AuthTokenInfo)

```cangjie
public AuthResult (
    public var account!: ?AppAccountInfo = None,
    public var tokenInfo!: ?AuthTokenInfo = None
)
```

**功能：** 构建AuthResult实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|account|?[AppAccountInfo](#class-appaccountinfo)|否|None| **命名参数。** 令牌所属的账号信息，默认为空。|
|tokenInfo|?[AuthTokenInfo](#class-authtokeninfo)|否|None| **命名参数。** 令牌信息，默认为空。|