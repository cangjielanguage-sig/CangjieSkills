## class SubWindowOptions

```cangjie
public class SubWindowOptions {
    public SubWindowOptions (
    public let title!: String,
    public let decorEnabled!: Bool,
    public var isModal!: Bool = false
    )
}
```

**功能：** 子窗口创建参数。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### let title

```cangjie
public let title: String
```

**功能：** 表示子窗口标题。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let decorEnabled

```cangjie
public let decorEnabled: Bool
```

**功能：** 表示子窗口是否显示装饰。true表示子窗口显示装饰，false表示子窗口不显示装饰。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### var isModal

```cangjie
public var isModal: Bool = false
```

**功能：** 设置子窗口是否启用模态属性。true表示子窗口启用模态属性，其父级窗口不能响应用户操作，false表示子窗口禁用模态属性，其父级窗口能响应用户操作。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### SubWindowOptions(String, Bool, Bool)

```cangjie
public SubWindowOptions (
public let title!: String,
public let decorEnabled!: Bool,
public var isModal!: Bool = false
)
```

**功能：** 构建一个SubWindowOptions类型的对象。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-| **命名参数。** 子窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。|
|decorEnabled|Bool|是|-| **命名参数。** 子窗口是否显示装饰。true表示子窗口显示装饰，false表示子窗口不显示装饰。|
|isModal|Bool|否|false| **命名参数。** 子窗口是否启用模态属性。true表示子窗口启用模态属性，其父级窗口不能响应用户操作，false表示子窗口禁用模态属性，其父级窗口能响应用户操作。|