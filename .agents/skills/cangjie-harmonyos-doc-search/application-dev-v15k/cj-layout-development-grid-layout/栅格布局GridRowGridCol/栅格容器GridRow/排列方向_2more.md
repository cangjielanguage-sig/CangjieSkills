### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为GridRowDirection.Row（从左往右排列）或GridRowDirection.RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

- 子组件默认从左往右排列。

    ```cangjie
    GridRow(direction: GridRowDirection.GridRowRow ){}
    ```

    ![Grid4](figures/Grid4.png)

- 子组件从右往左排列。

    ```cangjie
    GridRow(direction: GridRowDirection.RowReverse ){}
    ```

    ![Grid5](figures/Grid5.png)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

- 当gutter类型为Length时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。

    ```cangjie
    GridRow( gutter: 10.vp ){}
    ```

    ![Grid6](figures/Grid6.png)

- 当gutter类型为GutterOption时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。

    ```cangjie
    GridRow( gutter: GutterOption(x: 20.vp, y: 50.vp) ){}
    ```

    ![Grid7](figures/Grid7.png)