#### RESIZE_CONTAIN_BOTTOM_RIGHT

```cangjie
RESIZE_CONTAIN_BOTTOM_RIGHT
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持右侧对齐，当组件高方向有剩余时，内容与组件保持底部对齐。

![renderfit_resize_contain_bottom_right](figures/renderfit_resize_contain_bottom_right.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_COVER

```cangjie
RESIZE_COVER
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。

![renderfit_resize_cover](figures/renderfit_resize_cover.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_COVER_TOP_LEFT

```cangjie
RESIZE_COVER_TOP_LEFT
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持左侧对齐，显示内容的左侧部分。当内容高方向有剩余时，内容与组件保持顶部对齐，显示内容的顶侧部分。

![renderfit_resize_cover_top_left](figures/renderfit_resize_cover_top_left.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### RESIZE_COVER_BOTTOM_RIGHT

```cangjie
RESIZE_COVER_BOTTOM_RIGHT
```

**功能：** 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持右侧对齐，显示内容的右侧部分。当内容高方向有剩余时，内容与组件保持底部对齐，显示内容的底侧部分。

![renderfit_resize_cover_bottom_right](figures/renderfit_resize_cover_bottom_right.png)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> - 示意图中，蓝色区域表示内容，橙黄色区域表示节点大小。
> - 不同的内容填充方式在宽高动画过程中效果不一致，开发者需要选择合适的内容填充方式以实现需要的动画效果。