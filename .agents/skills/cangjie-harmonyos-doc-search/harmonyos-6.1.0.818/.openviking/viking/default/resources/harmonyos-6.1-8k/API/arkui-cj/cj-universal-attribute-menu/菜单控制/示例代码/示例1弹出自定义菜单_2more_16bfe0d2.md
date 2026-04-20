### 示例1（弹出自定义菜单）

该示例为通过bindMenu配置CustomBuilder弹出自定义菜单。

<!-- run -->

```cangjie

package ohos_app_cangjie_entry
import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    @Builder
    func builder() {
        Column {
            Button("Builder 内容")
                .width(300.px)
                .onClick({
                    evt => Hilog.info(1, "info", "Builder 中的按钮被点击")
                })
        }
        .width(300.px)
    }

    func build() {
        Column(space: 20) {
            Button("BindMenu").bindMenu(
                [
                    MenuElement(
                        value: "菜单1",
                        action: {
                            => Hilog.info(1, "info", "菜单1被点击")
                        }
                    ),
                    MenuElement(
                        value: "菜单2",
                        action: {
                            => Hilog.info(1, "info", "菜单2被点击")
                        }
                    )
                ]
            )

            Button("BindMenu-Custom")
                .bindMenu(builder: builder)
            Button("BindContextMenu-长按")
                .bindContextMenu(builder: builder, responseType: ResponseType.RightClick)
        }
    }
}
```

![uni_bind_menu](figures/uni_bind_menu.png)

### 示例2（弹出普通菜单）

该示例为bindMenu通过配置MenuElement弹出普通菜单。

<!-- run -->

```cangjie

package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_macro_manage.*
import ohos.hilog.*

@Entry
@Component
class EntryView {
    func build() {
        Scroll() {
            Column(space: 10) {
                Button("BindMenu").bindMenu(
                    [
                        MenuElement(
                            value: "菜单1",
                            action: {
                                => Hilog.info(1, "info", "MenuElement test: 菜单1被点击")
                            }
                        ),
                        MenuElement(
                            value: "菜单2",
                            action: {
                                => Hilog.info(1, "info", "MenuElement test: 菜单2被点击")
                            }
                        )
                    ]
                ).margin(left: 20, top: 20)

                Button("BindMenu").bindMenu(
                    [
                        MenuElement(
                            value: "菜单1",
                            action: {
                                => Hilog.info(1, "info", "MenuElement test: 菜单1被点击")
                            }
                        ),
                        MenuElement(
                            value: "菜单2",
                            action: {
                                => Hilog.info(1, "info", "MenuElement test: 菜单2被点击")
                            }
                        )
                    ]
                ).margin(left: 20)
            }
        }
    }
}
```

![uni_bind_menu](figures/uni_bind_menu.gif)