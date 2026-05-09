## class UserInfo

```cangjie
public class UserInfo <: ToString {
    public init()
    public init(userName: String)
    public init(userName: String, passWord: String)
    public init(userName: String, passWord: Option<String>)
}
```

功能：[UserInfo](url_package_classes.md#class-userinfo) 表示 URL 中用户名和密码信息。

> **注意：**
>
> RFC 3986 明确指出，任何场景下，明文保存用户信息存在被泄露风险，所以建议不要在 URL 中明文保存用户信息。

父类型：

- ToString

### init()

```cangjie
public init()
```

功能：创建 [UserInfo](url_package_classes.md#class-userinfo) 实例。

### init(String)

```cangjie
public init(userName: String)
```

功能：根据用户名创建 [UserInfo](url_package_classes.md#class-userinfo) 实例。

参数：

- userName: String - 用户名。

### init(String, Option\<String>)

```cangjie
public init(userName: String, passWord: Option<String>)
```

功能：根据用户名和密码创建 [UserInfo](url_package_classes.md#class-userinfo) 实例。
参数：

- userName: String - 用户名。
- passWord: Option\<String> - 密码，用 Option\<String> 类型表示。

### init(String, String)

```cangjie
public init(userName: String, passWord: String)
```

功能：根据用户名和密码创建 [UserInfo](url_package_classes.md#class-userinfo) 实例。
参数：

- userName: String - 用户名。
- passWord: String - 密码。

### func password()

```cangjie
public func password(): Option<String>
```

功能：获取密码信息。

> **注意：**
>
> RFC 3986 明确指出，任何场景下，明文保存用户信息存在被泄露风险，所以建议不要在 URL 中明文保存用户信息。

返回值：

- Option\<String> - 将密码以 Option\<String> 形式返回。

### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [UserInfo](url_package_classes.md#class-userinfo) 实例转换为字符串。

返回值：

- String - 当前 [UserInfo](url_package_classes.md#class-userinfo) 实例的字符串表示。

### func username()

```cangjie
public func username(): String
```

功能：获取用户名信息。

返回值：

- String - 字符串类型的用户名。