## 组件事件

### func onChange((Bool) -> Unit)

```cangjie
public func onChange(callback: (Bool)->Unit): This
```

**功能：** 当选中状态发生变化时，触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|当选中状态发生变化时，触发该回调。<br>\- Bool值为true时，表示已选中。<br>\- Bool值为false时，表示未选中。|

## 基础类型定义

### class CheckBoxConfiguration

```cangjie
public class CheckBoxConfiguration {
    public CheckBoxConfiguration(
        public var name!: String,
        public var selected!: Bool,
        public var triggerChange!: (Bool)->Unit
    )
}
```

**功能：** CheckBox基本状态配置类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var name

```cangjie
public var name: String
```

**功能：** 当前多选框名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### var selected

```cangjie
public var selected: Bool
```

**功能：** 指示多选框是否被选中。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

#### var triggerChange

```cangjie
public var triggerChange:(Bool) -> Unit
```

**功能：** 触发多选框选中状态变化。

**类型：** (Bool)->Unit

**读写能力：** 可读写

**起始版本：** 19

#### CheckBoxConfiguration(String, Bool, (Bool) -> Unit)

```cangjie
public CheckBoxConfiguration(
    public var name!: String,
    public var selected!: Bool,
    public var triggerChange!: (Bool)->Unit
)
```

**功能：** 构造一个多选框状态信息类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| **命名参数。** 当前多选框名称。|
|selected|Bool|是|-| **命名参数。** 指示多选框是否被选中。<br/>如果select属性没有设置初始值是false。<br/>如果设置select属性，此值与设置select属性的值相同。|
|triggerChange|(Bool)->Unit|是|-| **命名参数。** 触发多选框选中状态变化。<br/>为true时，表示从未选中变为选中。为false时，表示从选中变为未选中。|