### class FocusControl

```cangjie
public class FocusControl {}
```

**功能：** 焦点控制模块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### static func requestFocus(String)

```cangjie
public static func requestFocus(keyValue: String): Bool
```

**功能：** 方法语句中可使用的全局接口，调用此接口可以主动让焦点转移至参数指定的组件上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| keyValue | String | 是 | \- | 目标组件使用接口key(value: string)或id(value: string)绑定的字符串。<br>返回是否成功给目标组件申请到焦点。若参数指向的目标组件存在，且目标组件可获焦，则返回true，否则返回false。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| Bool | 返回是否成功给目标组件申请到焦点。若参数指向的目标组件存在，且目标组件可获焦，则返回true，否则返回false。|