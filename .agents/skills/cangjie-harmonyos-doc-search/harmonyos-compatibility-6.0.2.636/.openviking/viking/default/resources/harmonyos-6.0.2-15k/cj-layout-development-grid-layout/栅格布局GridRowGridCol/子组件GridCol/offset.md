### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

- 当类型为Int32时，子组件偏移相同列数。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        @State
        var bgColors: Array<Color> = [Color(213, 213, 213), Color(150, 150, 150), Color(0, 74, 175), Color(39, 135, 217),
            Color(61, 157, 180), Color(23, 169, 141), Color(255, 192, 0), Color(170, 10, 33)];
        func build() {
            GridRow() {
                ForEach(
                    bgColors,
                    itemGeneratorFunc: {
                        color: Color, index: Int64 => GridCol(offset: 2) {
                            Row() {
                                Text(index.toString())
                            }.width(100.percent).height(50.vp)
                        }.backgroundColor(color)
                    }
                )
            }
        }
    }
    ```

    ![Grid10](figures/Grid10.png)

    栅格默认分成12列，每一个子组件默认占1列，偏移2列，每个子组件及间距共占3列，一行放四个子组件。

- 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置,各个尺寸下数值可不同。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        @State
        var bgColors: Array<Color> = [Color(213, 213, 213), Color(150, 150, 150), Color(0, 74, 175), Color(39, 135, 217),
            Color(61, 157, 180), Color(23, 169, 141), Color(255, 192, 0), Color(170, 10, 33)];
        func build() {
            GridRow() {
                ForEach(
                    bgColors,
                    itemGeneratorFunc: {
                        color: Color, index: Int64 => GridCol() {
                            Row() {
                                Text(index.toString())
                            }.width(100.percent).height(50.vp)
                        }.backgroundColor(color).offset(GridColColumnOption(xs: 1, sm: 2, md: 3, lg: 4, xl: 12, xxl: 12))
                    }
                )
            }
        }
    }
    ```

    ![Grid11](figures/Grid11.PNG)