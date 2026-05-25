### class Action

```cangjie
public class Action {
    public Action(
        let value!: String,
        let action!: () -> Unit
    )
}
```

**功能：** 用于配置弹窗按钮参数的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let value

```cangjie
let value: String
```

**功能：** 弹窗里主按钮的文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

#### let action

```cangjie
let action: () -> Unit
```

**功能：** 点击辅助按钮的回调函数。

**类型：** () -> Unit

**读写能力：** 只读

**起始版本：** 12

#### Action(String, () -> Unit)

```cangjie
public Action(let value!: String, let action!: () -> Unit)
```

**功能：** 构建一个Action类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|  String | 是 | \- | **命名参数。**  弹窗里主按钮的文本。 |
|action|  () -> Unit| 是 | \- | **命名参数。**  点击辅助按钮的回调函数。 |