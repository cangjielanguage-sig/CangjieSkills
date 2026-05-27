# 框架接口

此页面记录UI框架使用的公开接口，应用开发者禁止使用，否则会产生无法预期的结果。

## func bind((CustomView) -> ViewBuilder, CustomView)

```cangjie
public func bind(builder: (CustomView) -> ViewBuilder, thisView: CustomView)
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见[bind函数使用](../../../FAQ/source_zh_cn/55-ui-bind.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview))->[ViewBuilder](#class-viewbuilder)|是|-|@Builder修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

## func bind\<T1>((CustomView, ObservedProperty\<T1>) -> ViewBuilder, CustomView)

```cangjie
public func bind<T1>(builder: (CustomView, ObservedProperty<T1>) -> ViewBuilder, thisView: CustomView)
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见[bind函数使用](../../../FAQ/source_zh_cn/55-ui-bind.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview),[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T1>)->[ViewBuilder](#class-viewbuilder)|是|-|@Builder修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

## func bind\<T1, T2>((CustomView, ObservedProperty\<T1>, ObservedProperty\<T2>) -> ViewBuilder, CustomView)

```cangjie
public func bind<T1, T2>(builder: (CustomView, ObservedProperty<T1>,
    ObservedProperty<T2>) -> ViewBuilder, thisView: CustomView)
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见[bind函数使用](../../../FAQ/source_zh_cn/55-ui-bind.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview),[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T1>,[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T2>)->[ViewBuilder](#class-viewbuilder)|是|-|@Builder修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|

## func bind\<T1, T2, T3>((CustomView, ObservedProperty\<T1>, ObservedProperty\<T2>, ObservedProperty\<T3>) -> ViewBuilder, CustomView)

```cangjie
public func bind<T1, T2, T3>(builder: (CustomView, ObservedProperty<T1>, ObservedProperty<T2>,
    ObservedProperty<T3>) -> ViewBuilder, thisView: CustomView)
```

**功能：** 用于将@Builder修饰的函数与自定义组件对象进行绑定。详情见[bind函数使用](../../../FAQ/source_zh_cn/55-ui-bind.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|([CustomView](#class-customview),[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T1>,[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T2>,[ObservedProperty](./cj-state-rendering-componentstatemanagement.md#class-observedproperty)\<T3>)->[ViewBuilder](#class-viewbuilder)|是|-|@Builder修饰的函数类型。|
|thisView|[CustomView](#class-customview)|是|-|当前自定义组件对象（一般为this）。|