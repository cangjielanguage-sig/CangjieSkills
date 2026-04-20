## enum SwiperDisplayMode

```cangjie
public enum SwiperDisplayMode <: Equatable<SwiperDisplayMode> {
    | Stretch
    | ...
}
```

**功能：** Swiper在主轴上的尺寸大小模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SwiperDisplayMode](#enum-swiperdisplaymode)>

### Stretch

```cangjie
Stretch
```

**功能：** Swiper滑动一页的宽度为Swiper组件自身的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SwiperDisplayMode)

```cangjie
public operator func ==(other: SwiperDisplayMode): Bool
```

**功能：** 判断两个SwiperDisplayMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwiperDisplayMode](#enum-swiperdisplaymode)|是|-|要比较的另一个SwiperDisplayMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SwiperDisplayMode)

```cangjie
public operator func !=(other: SwiperDisplayMode): Bool
```

**功能：** 判断两个SwiperDisplayMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwiperDisplayMode](#enum-swiperdisplaymode)|是|-|要比较的另一个SwiperDisplayMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|