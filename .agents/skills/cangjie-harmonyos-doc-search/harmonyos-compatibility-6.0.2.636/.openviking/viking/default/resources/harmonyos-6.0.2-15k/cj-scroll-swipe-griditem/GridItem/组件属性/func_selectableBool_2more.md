### func selectable(Bool)

```cangjie
public func selectable(value: Bool): This
```

**功能：** 设置当前GridItem元素是否可以被鼠标框选。外层Grid容器的鼠标框选开启时，GridItem的框选才生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|当前GridItem元素是否可以被鼠标框选。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。<br/>初始值：true。|

### func selected(Bool)

```cangjie
public func selected(value: Bool): This
```

**功能：** 设置当前GridItem选中状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|当前GridItem选中状态。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。<br/>初始值：false。|