# RelativeContainer

相对布局组件，用于复杂场景中元素对齐的布局。

> **说明：**
>
> 相对布局容器内的子组件的margin含义不同于通用属性的[margin](cj-universal-attribute-size.md#func-marginlength)，其含义为到该方向上的锚点的距离。若该方向上没有锚点，则该方向的margin不生效。

## 子组件

支持多个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个RelativeContainer组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个RelativeContainer组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func barrier(Array\<BarrierStyle>)

```cangjie
public func barrier(value: Array<BarrierStyle>): This
```

**功能：** 设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[BarrierStyle](#class-barrierstyle)>|是|-|RelativeContainer容器内的屏障。|

### func barrier(Array\<LocalizedBarrierStyle>)

```cangjie
public func barrier(value: Array<LocalizedBarrierStyle>): This
```

**功能：** 设置RelativeContainer容器内的屏障，Array中每个项目即为一条barrier。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[LocalizedBarrierStyle](#class-localizedbarrierstyle)>|是|-|RelativeContainer容器内的屏障。|

### func guideLine(Array\<GuideLineStyle>)

```cangjie
public func guideLine(value: Array<GuideLineStyle>): This
```

**功能：** 设置RelativeContainer容器内的辅助线，Array中每个项目即为一条guideline。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[GuideLineStyle](#class-guidelinestyle)>|是|-|RelativeContainer容器内的辅助线。|