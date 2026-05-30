# 鼠标光标控制

控制鼠标光标的显示样式。

## class CursorControl

```cangjie
public class CursorControl {}
```

**功能：** 鼠标光标控制模块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func setCursor(PointerStyle)

```cangjie
public static func setCursor(pointerStyle: PointerStyle): Unit
```

**功能：** 方法语句中可使用的全局接口，调用此接口可以更改当前的鼠标光标样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| pointerStyle | [PointerStyle](./cj-universal-attribute-cursor.md#enum-pointerstyle) | 是 | \- | 设置的鼠标样式。 |

### static func restoreDefault()

```cangjie
public static func restoreDefault(): Unit
```

**功能：** 方法语句中可使用的全局接口，调用此接口可以将鼠标光标恢复成默认的箭头光标样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19