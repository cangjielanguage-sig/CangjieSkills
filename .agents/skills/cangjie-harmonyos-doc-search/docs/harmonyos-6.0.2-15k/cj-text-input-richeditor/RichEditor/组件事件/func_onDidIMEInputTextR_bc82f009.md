### func onDidIMEInput((TextRange) -> Unit)

```cangjie
public func onDidIMEInput(callback: (TextRange) -> Unit): This
```

**功能：** 输入法输入完成后，触发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([TextRange](#class-textrange)) -> Unit|是|-|TextRange为输入法本次输入内容的范围。输入法完成输入时的回调。|