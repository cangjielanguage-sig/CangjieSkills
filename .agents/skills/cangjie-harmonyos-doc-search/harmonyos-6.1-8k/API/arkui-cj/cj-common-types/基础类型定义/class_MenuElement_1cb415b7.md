## class MenuElement

```cangjie
public class MenuElement {
    public init(value!: ?ResourceStr, action!: () -> Unit)
}
```

**功能：** 配置菜单项图标和文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceStr, () -> Unit)

```cangjie
public init(value!: ?ResourceStr, action!: () -> Unit)
```

**功能：** 创建MenuElement对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 菜单项文本。|
|action|() -> Unit|是|-|**命名参数。** 点击菜单项的事件回调。|