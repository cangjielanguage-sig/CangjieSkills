# Navigation

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](./cj-navigation-switching-navdestination.md)的子组件），首页和非首页通过路由进行切换。

> **说明：**
>
> - Navigation嵌套使用Navigation时，内层Navigation的生命周期不和外层Navigation以及[全模态](./cj-universal-attribute-bindcontentcover.md)的生命周期进行联动。
> - NavDestination未设置主副标题并且没有返回键时，不显示标题栏。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含子组件。

## 创建组件

### init(() -> Unit)

```cangjie
public init(child!: () -> Unit = { => })
```

**功能：** 构造一个包含子组件的Navigation容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|() -> Unit|否|{ => }|**命名参数。** Navigation容器的子组件。|

### init(?NavPathStack, () -> Unit)

```cangjie
public init(pathInfos: ?NavPathStack, child!: () -> Unit = { => })
```

**功能：** 构造一个包含子组件的Navigation容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pathInfos|?[NavPathStack](#class-navpathstack)|是|- |绑定到Navigation组件的路由栈。|
|child|() -> Unit|否|{ => }|**命名参数。** Navigation容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。