### func scrollable(Bool)

```cangjie
public func scrollable(isScrollable: Bool): This
```

**功能：** 设置是否可以通过滑动页面进行页面切换。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isScrollable|Bool|是|-|是否可以通过滑动页面进行页面切换。<br>初始值：true，可以通过滑动页面进行页面切换。为false时不可滑动切换页面。|

### func vertical(Bool)

```cangjie
public func vertical(isVertical: Bool): This
```

**功能：** 设置是否为纵向Tab。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isVertical|Bool|是|-|是否为纵向Tab。<br> 初始值：false，横向Tabs，为true时纵向Tabs。<br> 尽量保持每一个页面中的子组件尺寸大小一致，避免滑动页面时出现页面切换动画跳动现象。|