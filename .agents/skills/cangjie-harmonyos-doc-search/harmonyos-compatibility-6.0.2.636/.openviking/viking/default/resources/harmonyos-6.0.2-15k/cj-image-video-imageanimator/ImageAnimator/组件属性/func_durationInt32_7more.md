### func duration(Int32)

```cangjie
public func duration(value: Int32): This
```

**功能：** 设置播放时长。

> **说明：**
>
> 当Images中任意一帧图片设置了单独的duration后，该属性设置无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|播放时长。value为0时，不播放图片。value的改变只会在下一次循环开始时生效。<br>单位：毫秒。<br>初始值：1000ms。|

### func fillMode(FillMode)

```cangjie
public func fillMode(value: FillMode): This
```

**功能：** 设置当前播放方向下，动画开始前和结束后的状态。

> **说明：**
>
> 动画结束后的状态由fillMode和reverse属性共同决定。例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正播的最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FillMode](./cj-common-types.md#enum-fillmode)|是|-|当前播放方向下，动画开始前和结束后的状态。<br>初始值：FillMode.Forwards。|

### func fixedSize(Bool)

```cangjie
public func fixedSize(value: Bool): This
```

**功能：** 设置图片大小是否固定为组件大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|设置图片大小是否固定为组件大小。<br>true表示图片大小与组件大小一致，此时设置图片的width、height、top 和left属性是无效的。<br>false表示每一张图片的width 、height 、top和left属性都要单独设置。<br>初始值：true。|

### func images(Array\<ImageFrameInfo>)

```cangjie
public func images(images: Array<ImageFrameInfo>): This
```

**功能：** 设置图片帧信息集合。不支持动态更新。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|images|Array\<[ImageFrameInfo](#class-imageframeinfo)>|是|-|设置图片帧信息集合。每一帧的帧信息(ImageFrameInfo)包含图片路径、图片大小、图片位置和图片播放时长信息，详见ImageFrameInfo属性说明。<br>初始值：[]。|

### func iterations(Int32)

```cangjie
public func iterations(iterations: Int32): This
```

**功能：** 设置播放次数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|iterations|Int32|是|-|播放次数，默认播放一次，设置为-1时表示无限次播放。<br>初始值：1。|

### func preDecode(Int32)

```cangjie
@Deprecated
public func preDecode(value: Int32): This
```

**功能：** 设置图片大小是否固定为组件大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|预解码的图片数量。例如该值设为2，则播放当前页时会提前加载后面两张图片至缓存以提升性能。<br>初始值：0。|

### func reverse(Bool)

```cangjie
public func reverse(isReverse: Bool): This
```

**功能：** 设置播放方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isReverse|Bool|是|-|播放方向。<br>false表示从第1张图片播放到最后1张图片，<br>true表示从最后1张图片播放到第1张图片。<br>初始值：false。|