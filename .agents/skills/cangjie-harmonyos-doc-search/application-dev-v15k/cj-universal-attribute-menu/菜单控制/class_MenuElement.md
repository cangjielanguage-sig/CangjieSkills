## class MenuElement

```cangjie
public class MenuElement {
    public init(
        value: String,
        action: () -> Unit,
        icon!: String = "",
        enabled!: Bool = false
    )
}
```

**功能：** 配置菜单项图标和文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(String, () -> Unit, String, Bool)

```cangjie
public init(
    value: String,
    action: () -> Unit,
    icon!: String = "",
    enabled!: Bool = false
)
```

**功能：** 创建 MenuElement 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|\-|菜单项文本。|
|action|()->Unit|是|\-|点击菜单项的事件回调。|
|icon|String|否|""| **命名参数。** 菜单项图标。|
|enabled|Bool|否|false| **命名参数。** 菜单条目是否可进行交互。|