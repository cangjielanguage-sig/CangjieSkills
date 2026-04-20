### func onPaste(?PasteEventCallback)

```cangjie
public func onPaste(callback: ?PasteEventCallback): This
```

**功能：** 完成粘贴前，触发事件。

> **说明：**
>
> 开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[PasteEventCallback](#type-pasteeventcallback)|是|-|回调函数，完成粘贴前，触发回调。PasteEvent：定义用户粘贴事件。<br>初始值：{ _ => }。|

### func onDidChange(?OnDidChangeCallback)

```cangjie
public func onDidChange(callback: ?OnDidChangeCallback): This
```

**功能：** 组件执行增删操作后，触发事件。文本实际未发生增删时，不触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[OnDidChangeCallback](#type-ondidchangecallback)|是|-|回调函数，组件执行增删操作后，触发回调。文本实际未发生增删时，不触发该回调。参数：图文变化前后的内容范围。<br>初始值：{ rangeBefore: TextRange, rangeAfter: TextRange => }。|