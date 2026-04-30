### func interval(UInt32)

```cangjie
public func interval(value: UInt32): This
```

**功能：** 设置使用自动播放时播放的时间间隔。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|自动播放时播放的时间间隔。当小于[duration](#func-durationuint32)属性值时，翻页完成后会立即开始下一次轮播。<br>初始值：3000。<br>单位：毫秒。<br>设置小于0的值时，按照初始值处理。|

### func itemSpace(Length)

```cangjie
public func itemSpace(value: Length): This
```

**功能：** 设置子组件与子组件之间间隙。不支持设置百分比。

类型为Int64、Float64时，默认单位vp。类型为string时，需要显式指定像素单位，如'10px'；未指定像素单位时，如'10'，单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|子组件与子组件之间间隙。<br/> 类型为Int64、Float64时，默认单位vp。<br>当设置数值小于0或超出Swiper组件宽度范围时，按照初始值处理。<br>初始值：0。|

### func loop(Bool)

```cangjie
public func loop(value: Bool): This
```

**功能：** 设置是否开启循环。设置为true时表示开启循环，在LazyForEach懒循环加载模式下，加载的组件数量建议大于5个。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否开启循环。true为开启循环，false为不开启循环<br>初始值：true。|

### func nestedScroll(SwiperNestedScrollMode)

```cangjie
public func nestedScroll(value: SwiperNestedScrollMode): This
```

**功能：** 设置Swiper组件和父组件的嵌套滚动模式。loop为true时Swiper组件没有边缘，不会触发父组件嵌套滚动。

> **说明：**
>
> 由于Swiper的抛滑动画逻辑和其它滚动类组件不同（Swiper一次只能滑动一页，抛滑时做翻页动画），当Swiper内嵌套其它滚动组件时，如果Swiper的翻页动画已经启动，将无法接受子节点上传的滚动偏移量。这时Swiper的翻页动画和子节点的边缘效果动画会同时执行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SwiperNestedScrollMode](./cj-common-types.md#enum-swipernestedscrollmode)|是|-|Swiper组件和父组件的嵌套滚动模式。<br/>初始值：SwiperNestedScrollMode.SELF_ONLY。|