### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

- 当类型为Int32时，子组件在任何尺寸下排序次序一致。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            GridRow() {
                GridCol(order: 4) {
                    Row() {
                        Text('1')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color(213, 213, 213))
                GridCol(order: 3) {
                    Row() {
                        Text('2')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color(150, 150, 150))
                GridCol(order: 2) {
                    Row() {
                        Text('3')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color(0, 74, 175))
                GridCol(order: 1) {
                    Row() {
                        Text('4')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color(39, 135, 217))
            }
        }
    }
    ```

    ![Grid12](figures/Grid12.png)

- 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234：sm为2341，md为3412，lg为2431。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class EntryView {
        func build() {
            GridRow() {
                GridCol() {
                    Row() {
                        Text('1')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color.RED).order(GridColColumnOption(xs: 1, sm: 5, md: 3, lg: 7, xl: 12, xxl: 12))
                GridCol() {
                    Row() {
                        Text('2')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color.ORANGE).order(GridColColumnOption(xs: 2, sm: 2, md: 6, lg: 1, xl: 12, xxl: 12))
                GridCol() {
                    Row() {
                        Text('3')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color.YELLOW).order(GridColColumnOption(xs: 3, sm: 3, md: 1, lg: 6, xl: 12, xxl: 12))
                GridCol() {
                    Row() {
                        Text('4')
                    }.width(100.percent).height(50.vp)
                }.backgroundColor(Color.GREEN).order(GridColColumnOption(xs: 4, sm: 4, md: 2, lg: 5, xl: 12, xxl: 12))
            }
        }
    }
    ```

    ![Grid13](figures/Grid13.PNG)