|BlurStyle.COMPONENT_ULTRA_THICK| **命名参数。** 弹窗背板模糊材质。|
|transition|?[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)|否|None| **命名参数。** 菜单显示和退出的过渡效果。<br> **说明：**<br> 菜单退出动效过程中，进行横竖屏切换，菜单会避让。二级菜单不继承自定义动效。弹出过程可以点击二级菜单，退出动效执行过程不允许点击二级菜单。<br> 详细描述见TransitionEffect对象说明。|
|title|?String|否|None| **命名参数。** 菜单标题。<br> 初始值：2in1设备为true，其他设备为false。|
|showInSubWindow|?Bool|否|None| **命名参数。** 是否在子窗口显示菜单。<br>**说明：**<br> 仅在content设置为Array\<MenuElement> 时生效。|