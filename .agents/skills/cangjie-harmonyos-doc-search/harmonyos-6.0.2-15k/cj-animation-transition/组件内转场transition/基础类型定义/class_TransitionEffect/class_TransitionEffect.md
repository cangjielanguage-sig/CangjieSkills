### class TransitionEffect

```cangjie
public class TransitionEffect {
    public static let IDENTITY: TransitionEffect
    public static let OPACITY: TransitionEffect
    public static let SLIDE: TransitionEffect
    public static let SLIDE_SWITCH: TransitionEffect
}
```

**功能：** 以函数形式指定转场效果类型。

> **说明：**
>
> - TransitionEffect可通过combine函数实现多个转场效果的组合，可以为每个效果分别指定animation参数，且前一效果的animation的参数也可适用于后一效果。例如，TransitionEffect.OPACITY.animation(AnimateParam(duration: 1000)).combine(TransitionEffect.translate(TranslateOptions(x:100)))，则时长为1000ms的动画参数对OPACITY和translate均生效。
> - 动画参数的生效顺序为：本TransitionEffect指定的animation参数 > 前面的TransitionEffect指定的animation参数 > 触发该组件出现消失的animateTo中的动画参数。
> - 如果未使用animateTo触发转场动画且TransitionEffect中也无animation参数，则该组件直接出现或者消失。
> - TransitionEffect中指定的属性值如与默认值相同，则该属性不会产生转场动画。如TransitionEffect.opacity(1.0).animation(AnimateParam(duration: 1000))，由于opacity默认值也为1.0，未产生透明度动画，该组件直接出现或者消失。
> - 更详细的关于scale、rotate效果的介绍可参考[图形变换](./cj-universal-attribute-transform.md)。
> - 如果在动画范围([animateTo](./cj-animation-animateto.md)、[animation](./cj-animation-animation.md))内触发组件的上下树或可见性([Visibility](./cj-universal-attribute-visibility.md))改变，而根组件没有配置transition，会给该组件加上默认透明度转场，即TransitionEffect.OPACITY，动画参数跟随所处动画环境的参数。如不需要可通过主动配置TransitionEffect.IDENTITY来禁用，使该组件直接出现或消失。
> - 当通过删除整棵子树的方式触发消失转场，如需看到完整的消失转场过程，需要保证被删除子树的根组件的有充足的消失转场时间，见[示例3](#示例代码3设置父子组件为transition)。
> - 下述提供的静态函数用于构造TransitionEffect对象，而非静态函数作用于构造好的TransitionEffect对象，以指定多种转场效果的组合效果和动画参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12