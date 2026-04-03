## 布局位置

position、offset等属性影响了布局容器相对于自身或其他组件的位置。

|定位能力|应用场景|实现方式|
|:---|:---|:---|
|绝对定位|  对于不同尺寸的设备，使用绝对定位的适应性会比较差，在屏幕的适配上有缺陷。| 使用[position](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-location.md#func-positionlength-length)实现绝对定位，设置元素左上角相对于父容器左上角偏移位置。在布局容器中，设置该属性不影响父容器布局，仅在绘制时进行位置调整。|
|相对定位|相对定位不脱离文档流，即原位置依然保留，不影响元素本身的特性，仅相对于原位置进行偏移。|使用[offset](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-location.md#func-offsetlength-length)可以实现相对定位，设置元素相对于自身的偏移量。设置该属性，不影响父容器布局，仅在绘制时进行位置调整。|

## 对子元素的约束

- 拉伸：容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。

  [flexGrow](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-flexlayout.md#func-flexgrowfloat64)和[flexShrink](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-flexlayout.md#func-flexshrinkfloat64)属性：

    - flexGrow基于父容器的剩余空间分配来控制组件拉伸。

    - flexShrink设置父容器的压缩尺寸来控制组件压缩。

- 缩放：子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。

  [aspectRatio](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-layoutconstraints.md#func-aspectratiofloat64)属性指定当前组件的宽高比来控制缩放，公式为：aspectRatio=width/height。

- 占比：子组件的宽高按照预设的比例，随祖先容器组件发生变化。

  基于通用属性的两种实现方式：

    - 子组件的宽高设置为百分比。

      | 父组件与祖先组件宽高设置情况|   子组件百分比|
      |:---|:---|
      |父组件设置宽或高 & 祖先组件未指定父组件宽或高|参考父组件的宽高|
      |父组件设置宽或高 & 祖先组件指定父组件宽或高|参考祖先组件指定的父组件高|
      |父组件未设置宽或高 & 祖先组件指定父组件宽或高|参考祖先组件指定的父组宽高|
      |父组件未设置宽或高 & 祖先组件未指定父组件宽或高|  参考父组件的百分参照。由于父组件未指定宽高，该百分比参照传递自祖先组件|

    - [layoutWeight](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-size.md#func-layoutweightint32)属性，使得子元素自适应占满剩余空间。

- 隐藏：隐藏能力是指容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏，其中相同显示优先级的子组件同时显示或隐藏。
  通过[displayPriority](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-layoutconstraints.md#func-displaypriorityint32)属性来控制组件的显示和隐藏。