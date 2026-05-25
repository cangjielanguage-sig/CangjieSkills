## class Action

```cangjie
public class Action {
    public Action(
        let value!: String,
        let action!: () -> Unit
    )
}
```

**功能：** 弹出菜单项参数。

**起始版本：** 12

### var action

```cangjie
let action: () -> Unit
```

**功能：** 点击菜单项的事件回调。

**类型：** () -> Unit

**读写能力：** 只读

**起始版本：** 12

### var value

```cangjie
let value: String
```

**功能：** 菜单项文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### Action(String, () -> Unit)

```cangjie
public Action(
    let value!: String,
    let action!: () -> Unit
)
```

**功能：** 创建 Action 对象。

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|\-| **命名参数。** 菜单项文本。|
|action|() -> Unit|是|\-| **命名参数。** 点击菜单项的事件回调。|