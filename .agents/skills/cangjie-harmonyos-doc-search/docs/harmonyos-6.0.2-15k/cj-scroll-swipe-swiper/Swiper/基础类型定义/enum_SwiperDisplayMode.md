### enum SwiperDisplayMode

```cangjie
public enum SwiperDisplayMode {
    | STRETCH
    | AUTO_LINEAR
}
```

**功能：** Swiper在主轴上的尺寸大小模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### STRETCH

```cangjie
STRETCH
```

**功能：** Swiper滑动一页的宽度为Swiper组件自身的宽度。

**起始版本：** 19

#### AUTO_LINEAR<sup>deprecated</sup>

```cangjie
AUTO_LINEAR
```

**功能：** Swiper滑动一页的宽度为视窗内最左侧子组件的宽度。已废弃，建议使用[Scroller.scrollto](./cj-scroll-swipe-scroll.md#func-scrolltoindexint32-bool-scrollalign-length)代替。

**起始版本：** 19