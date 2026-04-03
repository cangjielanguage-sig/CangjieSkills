## enum IMFEventType

```cangjie
public enum IMFEventType <: ToString {
    | InsertText
    | DeleteLeft
    | DeleteRight
    | SendKeyboardStatus
    | SendFunctionKey
    | MoveCursor
    | HandleExtendAction
    | GetLeftTextOfCursor
    | GetRightTextOfCursor
    | GetTextIndexAtCursor
    | SelectByRange
    | SelectByMovement
    | ImeChange
    | ...
}
```

**功能：** 回调函数的事件类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**父类型：**

- ToString

### DeleteLeft

```cangjie
DeleteLeft
```

**功能：** 向左删除事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### DeleteRight

```cangjie
DeleteRight
```

**功能：** 向右删除事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### GetLeftTextOfCursor

```cangjie
GetLeftTextOfCursor
```

**功能：** 获取光标左侧指定长度文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### GetRightTextOfCursor

```cangjie
GetRightTextOfCursor
```

**功能：** 获取光标右侧指定长度文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### GetTextIndexAtCursor

```cangjie
GetTextIndexAtCursor
```

**功能：** 获取光标处文本索引事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### HandleExtendAction

```cangjie
HandleExtendAction
```

**功能：** 发送扩展编辑操作事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### ImeChange

```cangjie
ImeChange
```

**功能：** 输入法及子类型变化监听事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### InsertText

```cangjie
InsertText
```

**功能：** 插入文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### MoveCursor

```cangjie
MoveCursor
```

**功能：** 移动光标事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### SelectByMovement

```cangjie
SelectByMovement
```

**功能：** 按光标移动方向选中文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### SelectByRange

```cangjie
SelectByRange
```

**功能：** 按范围选中文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### SendFunctionKey

```cangjie
SendFunctionKey
```

**功能：** 发送功能键事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### SendKeyboardStatus

```cangjie
SendKeyboardStatus
```

**功能：** 发送输入法软键盘状态事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调函数类型的字符串表示。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|回调函数类型的字符串表示。|