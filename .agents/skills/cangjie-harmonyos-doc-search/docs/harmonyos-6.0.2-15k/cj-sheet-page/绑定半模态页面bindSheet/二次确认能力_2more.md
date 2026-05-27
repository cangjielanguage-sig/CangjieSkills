## 二次确认能力

推荐使用onWillDismiss接口，此接口支持在回调中处理二次确认，或自定义关闭行为。

```cangjie
// 第一步：声明onWillDismiss回调
onWillDismiss: {
    // 第二步：确认二次回调交互能力，此处用AlertDialog提示 "是否需要关闭半模态"
    dismissSheetAction: DismissSheetAction => {
        AlertDialog.show(
            AlertDialogParamWithButtons(
                "text",
                title: '是否选择关闭半模态',
                primaryButton: AlertDialogButtonOptions(
                    value: 'cancel',
                    action: {
                        => AppLog.info("Callback when the cancel button is clicked")
                    }
                ),
                secondaryButton: AlertDialogButtonOptions(
                    value: 'ok',
                    // 第三步：确认关闭半模态逻辑所在，此处为AlertDialog的Button回调
                    action: {
                        => {
                            // 第四步：上述第三步逻辑触发的时候，调用dismiss()关闭半模态
                            dismissSheetAction.dismiss(),
                            AppLog.info("Callback when the ok button is clicked")
                        }
                    }
                ),
                cancel: {
                    => AppLog.info("AlertDialog Closed callbacks")
                }
            )
        )
    }
}
```

![page](figures/page.gif)

## 屏蔽部分关闭行为

由于声明了onWillDismiss接口，半模态的关闭行为都需要dismiss处理。可以通过if等逻辑自定义处理关闭逻辑。

下述示例显示半模态页面只在下滑的时候关闭。

```cangjie
onWillDismiss: {
    dismissSheetAction: DismissSheetAction => {
        if (dismissSheetAction.reason == DismissReason.SLIDE_DOWN) {
            DismissSheetAction.dismiss() // 注册dismiss行为
        }
    }
}
```

同理可以结合onWillSpringBackWhenDismiss接口实现更好的下滑体验。

类比onWillDismiss，在声明了onWillSpringBackWhenDismiss后，半模态下滑时的回弹操作需要使用 SpringBackAction.springBack()处理，无此逻辑则不会回弹。

具体代码如下，在半模态下滑的时候无需回弹。

```cangjie
onWillDismiss: {
    dismissSheetAction: DismissSheetAction => {
        if (dismissSheetAction.reason == DismissReason.SLIDE_DOWN) {
            dismissSheetAction.dismiss() // 注册dismiss行为
        }
    }
}

onWillSpringBackWhenDismiss: {
    springBackAction: SpringBackAction => {
        // 没有注册springBack, 下拉半模态页面无回弹行为
    }
}
```