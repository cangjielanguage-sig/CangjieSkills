## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

- 设置span。

    ```cangjie
    GridCol( span: 2 ){}
    GridCol( span:GridColColumnOption(xs: 1, sm:2, md:3, lg:4, xl:12, xxl: 12) ){}
    GridCol(){}.span(2)
    GridCol(){}.span(GridColColumnOption(xs:1, sm:2, md:3, lg:4, xl:12, xxl: 12))
    ```

- 设置offset。

    ```cangjie
    GridCol( gridColOffset: 2 ){}
    GridCol( gridColOffset:GridColColumnOption(xs: 1, sm:2, md:3, lg:4, xl:12, xxl: 12) ){}
    GridCol(){}.gridColOffset((GridColColumnOption(xs:1, sm:2, md:3, lg:4, xl:12,     xxl: 12)))
    ```

- 设置order。

    ```cangjie
    GridCol( order: 2 ){}
    GridCol( order:GridColColumnOption(xs: 1, sm:2, md:3, lg:4, xl:12, xxl: 12) ){}
    GridCol(){}.order(2)
    GridCol(){}.order(GridColColumnOption(xs:1, sm:2, md:3, lg:4, xl:12, xxl: 12))
    ```

### span

子组件占栅格布局的列数，决定了子组件的宽度，默认为1。

- 当类型为Int32时，子组件在所有尺寸设备下占用的列数相同。

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
            GridRow(columns: 8) {
                ForEach(
                    bgColors,
                    itemGeneratorFunc: {
                        color: Color, index: Int64 => GridCol(span: 2) {
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

    ![Grid8](figures/Grid8.png)

- 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。

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
            GridRow(columns: 8) {
                ForEach(
                    bgColors,
                    itemGeneratorFunc: {
                        color: Color, index: Int64 => GridCol() {
                            Row() {
                                Text(index.toString())
                            }.width(100.percent).height(50.vp)
                        }.backgroundColor(color).span(GridColColumnOption(xs: 1, sm: 2, md: 3, lg: 4, xl: 12, xxl: 12))
                    }
                )
            }
        }
    }
    ```

    ![Grid9](figures/Grid9.PNG)