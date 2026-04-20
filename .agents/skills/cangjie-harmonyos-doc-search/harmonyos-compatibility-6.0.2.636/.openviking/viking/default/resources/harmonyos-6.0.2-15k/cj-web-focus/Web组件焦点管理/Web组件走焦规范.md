## Web组件走焦规范

根据走焦的触发方式，可以分为主动走焦和被动走焦，Web组件走焦规范详情请参见[ArkUI走焦规范](../arkui-cj/cj-common-events-focus-event.md#走焦规范)。

### 主动走焦

指开发者或用户主观行为导致的焦点移动。包括：使用requestFocus申请焦点、外接键盘的按键走焦（TAB键/Shift+TAB键）、点击申请焦点（手势/鼠标/触摸板）等导致的焦点转移。

- requestFocus

    详见[Web组件与ArkUI组件焦点控制](#web组件与arkui组件焦点控制)，可以主动将焦点转移到Web组件上。

- 按键走焦

    - 支持ArkWeb与其他组件通过TAB键、Shift+TAB键走焦。
    - 支持ArkWeb内部网页元素通过TAB键、Shift+TAB键走焦，网页元素走焦完成后，抛回ArkUI继续框架侧走焦。

- 点击申请获焦

    开发者或用户可通过手势、鼠标或触摸板点击Web组件，使其主动获得焦点。当具体点击到Web组件内的某个元素时，该元素能够获得焦点，例如，点击网页内的输入框，可使其从不可编辑状态转变为可编辑状态，并激活输入法。

### 被动走焦

被动走焦指焦点因系统获其他操作而转移，无需开发者直接干预，是焦点系统的默认行为。

目前会被动走焦的场景有：

- 组件删除：当焦点所在的Web组件被移除时，系统会按照先向后再向前的原则，将焦点转移至相邻的同级组件。倘若所有同级组件均无法获取焦点，则焦点将被释放，并提示其父级组件接管焦点处理。
- 属性变更：如果将处于焦点状态的组件的focusable或enabled属性设置为false，或者将visibility属性设置为不可见，系统会自动将焦点转移到其他可获得焦点的组件上，转移方式同组件删除。
- Web组件不可见：ArkWeb获焦后，应用前后台切换、页面切换、Navigation导航等场景，ArkWeb会失焦再获焦。
- Web组件加载网页：ArkWeb通过src、loadUrl、loadData加载网页，默认会获取焦点，但如果此时web组件为不可获焦状态则会获焦失败（常见的不可获焦状态原因有：过场动画过程中父组件不可获焦、应用侧设置了web组件或其父组件不可获焦属性等），应用侧可以调用主动请求焦点接口[requestFocus](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-requestfocus)再次尝试使web组件获焦。当获焦成功后，应用侧onFocus、w3c focus事件均会上报。
- autofocus样式：设置了autofocus样式的元素网页完成加载时默认获焦。若该元素支持文字输入，则输入框会有光标闪烁，但不拉起软键盘。
- 菜单弹出：ArkUI的overlay属性类型组件默认抢焦，在与此类组件结合的ArkWeb场景中（[menu](../../API_Reference/source_zh_cn/arkui-cj/cj-menu-menu.md)、[datepicker](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-datepicker.md)、下拉框、弹窗等），ArkWeb均会失焦。