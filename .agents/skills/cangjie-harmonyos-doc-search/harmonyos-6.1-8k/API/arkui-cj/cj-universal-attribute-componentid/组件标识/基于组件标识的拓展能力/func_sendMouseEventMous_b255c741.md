### func sendMouseEvent(MouseEvent)

```cangjie
public func sendMouseEvent(event: MouseEvent): Bool
```

**功能：** 发送鼠标事件。此接口仅用于对应用的测试。由于耗时长，不建议使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|名称|类型|必填|默认值|说明|
| :-------   | :---------- | :------- | :-------- | :----------|
| event | [MouseEvent](./cj-common-types.md#class-mouseevent) | 是  | -  | 鼠标事件，event参数见[MouseEvent](./cj-common-types.md#class-mouseevent)介绍。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| Bool | 事件发送失败时返回false，其余情况返回true。|