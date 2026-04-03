### init(TabsController, () -> Unit)

```cangjie
public init(
    controller: TabsController,
    child: () -> Unit
)
```

**功能：** 创建一个Tabs容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|[TabsController](#class-tabscontroller)|是|-|设置Tabs控制器。<br> 初始值：TabsController()|
|child|()->Unit|是|-|声明容器内的子组件。<br> 初始值：{ => }|

### init(Int32, () -> Unit)

```cangjie
public init(
    index: Int32,
    child: () -> Unit
)
```

**功能：** 创建一个Tabs容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|设置当前显示页签的索引。<br> 初始值：0 <br> **说明：**<br> 设置为小于0的值时按默认值显示。可选值为[0, TabContent子节点数量-1]。直接修改index跳页时，切换动效不生效。 使用TabController的changeIndex时，默认生效切换动效，可以设置animationDuration为0关闭动画。|
|child|()->Unit|是|-|声明容器内的子组件。<br> 初始值：{ => }|

### init(() -> Unit)

```cangjie
public init(
    child: () -> Unit
)
```

**功能：** 创建一个Tabs容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。<br> 初始值：{ => }|