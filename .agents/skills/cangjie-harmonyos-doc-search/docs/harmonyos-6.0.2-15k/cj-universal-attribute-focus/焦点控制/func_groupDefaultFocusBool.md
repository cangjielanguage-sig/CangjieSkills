## func groupDefaultFocus(Bool)

```cangjie
public func groupDefaultFocus(isGroupDefaultFocus: Bool): This
```

**功能：** 设置当前组件是否为当前组件所在容器获焦时的默认焦点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| isGroupDefaultFocus | Bool | 是 | - | 当前组件是否为当前组件所在容器获焦时的默认焦点，仅在初次创建容器节点第一次获焦时生效。true表示当前组件为所在容器获焦时的默认焦点，false表示当前组件不是所在容器获焦时的默认焦点。<br>初始值：false <br>**说明：**<br>必须与tabIndex联合使用，当某个容器设置了[tabIndex](./cj-universal-attribute-focus.md#func-tabindexint32)，且容器内某子组件或容器自身设置了groupDefaultFocus(true)，当该容器首次TAB键获焦时，会自动将焦点转移至该指定的组件上。若容器内（包含容器本身）有多个组件设置了groupDefaultFocus(true)，则以组件树深度遍历找到的第一个组件为最终结果。|