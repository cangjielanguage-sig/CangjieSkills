## func expandSafeArea(Array\<SafeAreaType>, Array\<SafeAreaEdge>)

```cangjie
public func expandSafeArea(types!: [SafeAreaType.SYSTEM, SafeAreaType.CUTOUT, SafeAreaType.KEYBOARD], edges!: Array<SafeAreaEdge> =[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM, SafeAreaEdge.START, SafeAreaEdge.END]): This
```

**功能：** 设置控制组件扩展其安全区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| types | Array\<[SafeAreaType](./cj-universal-attribute-expandsafearea.md#enum-safeareatype)>| 否 | [SafeAreaType.SYSTEM, SafeAreaType.CUTOUT, SafeAreaType.KEYBOARD] | **命名参数。**  配置扩展安全区域的类型。<br> 未添加metadata配置项时，页面不避让挖孔, CUTOUT类型不生效。 |
| edges | Array\<[SafeAreaEdge](./cj-universal-attribute-expandsafearea.md#enum-safeareaedge)> | 否 | [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM, SafeAreaEdge.START, SafeAreaEdge.END] | **命名参数。**  配置扩展安全区域的方向。<br>扩展至所有非安全区域。|

> **说明：**
>
> - 设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高时，扩展安全区域的方向只支持[SafeAreaEdge.TOP, SafeAreaEdge.START]，扩展后的组件尺寸保持不变。
> - 安全区域不会限制内部组件的布局和大小，不会裁剪内部组件。
> - 当父容器是滚动容器时，设置expandSafeArea属性不生效。
> - 设置expandSafeArea()时，不传参，走默认值处理；设置expandSafeArea([],[])时，相当于入参是空数组，此时设置expandSafeArea属性不生效。
> - 组件设置expandSafeArea之后生效的条件为：
> - 1.type为SafeAreaType.KEYBOARD时默认生效，组件不避让键盘。
> - 2.设置其他type，组件的边界与安全区域重合时组件能够延伸到安全区域下。例如：设备顶部状态栏高度100，那么组件在屏幕中的绝对位置需要为0 <= y <= 100。
> - 组件延伸到安全区域下，在安全区域处的事件，如点击事件等可能会被系统拦截，优先给状态栏等系统组件响应。
> - 滚动类容器内的组件不建议设置expandSafeArea属性，如果设置，需要按照组件嵌套关系，将当前节点到滚动类祖先容器间所有直接节点设置expandSafeArea属性，否则expandSafeArea属性在滚动后可能会失效，写法参考示例。
> - expandSafeArea属性仅作用于当前组件，不会向父组件或子组件传递，因此使用过程中，所有相关组件均需配置。
> - 在同时设置了expandSafeArea和position属性时，position属性会先生效，expandSafeArea属性会后生效。对于未设置position、offset等绘制属性的组件，如果组件边界没有和避让区重叠，设置expandSafeArea属性不生效，如弹窗和半模态组件。
> - 对于expandSafeArea属性无法生效的场景，若要将组件部署在避让区，需要手动调整组件的坐标。