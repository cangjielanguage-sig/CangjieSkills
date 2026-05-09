## 组件事件

### func onChange(?(Float64) -> Unit)

```cangjie
public func onChange(callback: ?(Float64) -> Unit): This
```

**功能：** 操作评分条的评星发生改变时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?(Float64)->Unit|是|-|评分条的评分。<br>初始值：{ _ => }。|