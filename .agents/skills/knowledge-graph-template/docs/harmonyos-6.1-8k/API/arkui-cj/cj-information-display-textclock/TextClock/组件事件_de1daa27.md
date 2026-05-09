## 组件事件

### func onDateChange(?(Int64) -> Unit)

```cangjie
public func onDateChange(callback: ?(Int64) -> Unit): This
```

**功能：** 提供日期变化回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?(Int64) -> Unit|是|-|日期变化时的回调函数。初始值：{ _ => }|