## enum Input

```cangjie
public enum Input <: ToString {
    | DEFAULT_INPUT_METHOD
    | ACTIVATED_INPUT_METHOD_SUB_MODE
    | ACTIVATED_INPUT_METHODS
    | SELECTOR_VISIBILITY_FOR_INPUT_METHOD
    | AUTO_CAPS_TEXT_INPUT
    | AUTO_PUNCTUATE_TEXT_INPUT
    | AUTO_REPLACE_TEXT_INPUT
    | SHOW_PASSWORD_TEXT_INPUT
    | ...
}
```

**功能：** 提供设置有关输入法信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### ACTIVATED_INPUT_METHODS

```cangjie
ACTIVATED_INPUT_METHODS
```

**功能：** 已激活的输入法的列表。该列表是一个字符串，由已激活的输入法的ID和输入法键盘类型组成。输入法ID后添加冒号':'连接，输入法的键盘类型后添加分号';'连接。用ima代表输入法ID，keyboardType代表键盘类型，示例格式是ima0:keyboardType0;keyboardType1;ima1:ima2:keyboardTypes0。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### ACTIVATED_INPUT_METHOD_SUB_MODE

```cangjie
ACTIVATED_INPUT_METHOD_SUB_MODE
```

**功能：** 默认输入法键盘类型及其ID。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AUTO_CAPS_TEXT_INPUT

```cangjie
AUTO_CAPS_TEXT_INPUT
```

**功能：** 是否为文本编辑器启用自动大写。值为0，表示不启用自动大写；值为1，表示启用自动大写。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AUTO_PUNCTUATE_TEXT_INPUT

```cangjie
AUTO_PUNCTUATE_TEXT_INPUT
```

**功能：** 是否为文本编辑器启用自动标点符号。自动标点符号使文本编辑器能够将两个空格转换为句点'.'和空格。值为0，表示不启用自动标点符号；值为1，表示启用自动标点符号。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AUTO_REPLACE_TEXT_INPUT

```cangjie
AUTO_REPLACE_TEXT_INPUT
```

**功能：** 是否为文本编辑器启用自动更正。自动更正使文本编辑器能够更正拼写错误。值为0，表示不启用自动更正；值为1，表示启用自动更正。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_INPUT_METHOD

```cangjie
DEFAULT_INPUT_METHOD
```

**功能：** 默认输入法及其ID。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SELECTOR_VISIBILITY_FOR_INPUT_METHOD

```cangjie
SELECTOR_VISIBILITY_FOR_INPUT_METHOD
```

**功能：** 输入法选择器是否可见。值为1，表示输入法选择器可见；值为0，表示输入法选择器不可见。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SHOW_PASSWORD_TEXT_INPUT

```cangjie
SHOW_PASSWORD_TEXT_INPUT
```

**功能：** 是否在文本编辑器中启用密码显示。密码显示使文本编辑器能够在用户键入密码字符时显示密码字符。值为0，表示不启用密码显示；值为1，表示启用密码显示。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置有关输入法信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置有关输入法信息的数据项。 |