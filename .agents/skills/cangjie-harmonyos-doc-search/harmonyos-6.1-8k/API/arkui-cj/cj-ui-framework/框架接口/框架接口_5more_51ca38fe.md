# 框架接口

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

本页面描述UI框架使用的公开接口。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func bind((CustomView) -> ViewBuilder, CustomView)

```cangjie
public func bind(builder: (CustomView) -> ViewBuilder, thisView: CustomView): () -> Unit
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见bind函数使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview))->ViewBuilder|是|-|[@Builder](../../arkui-cj/paradigm/cj-macro-builder.md)修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

**返回值：**

|类型|说明|
|:----|:----|
|() -> Unit|返回builder函数。|

> **说明：**
>
> bind推荐在使用属性[title](./cj-navigation-switching-navdestination.md#func-titlecustombuilder-navigationtitleoptions)、[tabBar](./cj-navigation-switching-tabcontent.md#func-tabbarcustombuilder)以及构造[MenuItemGroup对象](./cj-menu-menuitemgroup.md#initcustombuilder-custombuilder----unit)时使用。

## func bind\<T1>((CustomView,ObservedProperty\<T1>) -> ViewBuilder, CustomView)

```cangjie
public func bind<T1>(builder: (CustomView, ObservedProperty<T1>) -> ViewBuilder, thisView: CustomView): (T1) -> Unit
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见bind函数使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview),ObservedProperty\<T1>)->ViewBuilder|是|-|[@Builder](../../arkui-cj/paradigm/cj-macro-builder.md)修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

**返回值：**

|类型|说明|
|:----|:----|
|(T1) -> Unit|返回builder函数。|

> **说明：**
>
> bind推荐在使用属性[title](./cj-navigation-switching-navdestination.md#func-titlecustombuilder-navigationtitleoptions)、[tabBar](./cj-navigation-switching-tabcontent.md#func-tabbarcustombuilder)以及构造[MenuItemGroup对象](./cj-menu-menuitemgroup.md#initcustombuilder-custombuilder----unit)时使用。

## func bind\<T1, T2>((CustomView,ObservedProperty\<T1>,ObservedProperty\<T2>) -> ViewBuilder, CustomView)

```cangjie
public func bind<T1, T2>(
    builder: (CustomView, ObservedProperty<T1>, ObservedProperty<T2>) -> ViewBuilder,
    thisView: CustomView
): (T1, T2) -> Unit
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见bind函数使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview),ObservedProperty\<T1>,ObservedProperty\<T2>)->ViewBuilder|是|-|[@Builder](../../arkui-cj/paradigm/cj-macro-builder.md)修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

**返回值：**

|类型|说明|
|:----|:----|
|(T1, T2) -> Unit|返回builder函数。|

> **说明：**
>
> bind推荐在使用属性[title](./cj-navigation-switching-navdestination.md#func-titlecustombuilder-navigationtitleoptions)、[tabBar](./cj-navigation-switching-tabcontent.md#func-tabbarcustombuilder)以及构造[MenuItemGroup对象](./cj-menu-menuitemgroup.md#initcustombuilder-custombuilder----unit)时使用。