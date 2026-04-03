# 组件标识

id为组件的唯一标识，在整个应用内唯一。本模块提供组件标识相关接口，可以获取指定id组件的属性，也提供向指定id组件发送事件的功能。

> **说明：**
>
> 若同一个组件设置了多个id或者key，最后设置的生效。

## func id(String)

```cangjie
public func id(value: String): This
```

**功能：** 组件的唯一标识，唯一性由使用者保证。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|组件的唯一标识，唯一性由使用者保证。|

## func key(String)

```cangjie
public func key(value: String): This
```

**功能：** 组件的唯一标识，唯一性由使用者保证。

此接口仅用于对应用的测试。与id同时使用时，后赋值的属性会覆盖先赋值的属性，建议仅设置id。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|组件的唯一标识，唯一性由使用者保证。|

## func getInspectorByKey(String)

```cangjie
public func getInspectorByKey(id: String): String
```

**功能：** 获取指定id的组件的所有属性，不包括子组件信息。此接口仅用于对应用的测试。由于耗时长，不建议使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :-------   | :---------- | :------- | :-------- | :----------|
| id   | String   | 是   |  - | 要获取属性的组件id。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| String   | 组件属性列表的JSON字符串。<br>**说明：** <br>字符串信息包含组件的tag、id、位置信息(相对于窗口左上角的坐标)以及用于测试检查的组件所包含的相关属性信息。   |

## func getInspectorTree()

```cangjie
public func getInspectorTree(): String
```

**功能：** 获取组件树及组件属性。此接口仅用于对应用的测试。由于耗时长，不建议使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
| :-------   | :---------- |
| String  | 组件树及组件属性列表的JSON对象。 |

## func sendEventByKey(String, IntNative, String)

```cangjie
public func sendEventByKey(id: String, action: IntNative, params: String): Bool
```

**功能：** 给指定id的组件发送事件。此接口仅用于对应用的测试。由于耗时长，不建议使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :-------   | :---------- | :------- | :-------- | :----------|
| id     | String | 是    |  - | 要触发事件的组件的id。 |
| action | IntNative | 是  | - | 要触发的事件类型，目前支持取值：<br/>- 点击事件Click: 10。<br/>- 长按事件LongClick: 11。|
| params | String | 是    | - | 事件参数，无参数传空字符串 ""。|

**返回值：**

|类型|说明|
| :-------   | :---------- |
| Bool   | 找不到指定id的组件时返回false，其余情况返回true。 |

## func sendTouchEvent(TouchObject)

```cangjie
public func sendTouchEvent(event: TouchObject): Bool
```

**功能：** 发送触摸事件。此接口仅用于对应用的测试。由于耗时长，不建议使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :-------   | :---------- | :------- | :-------- | :----------|
| event | [TouchObject](./cj-universal-event-touch.md#class-touchobject) | 是   | - | 触发触摸事件的位置，event参数见[TouchEvent](./cj-universal-event-touch.md#class-touchevent)中TouchObject的介绍。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| Bool | 事件发送失败时时返回false，其余情况返回true。|