# 创建瀑布流（WaterFlow）

[瀑布流](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-waterflow.md)常用于展示图片信息，尤其在购物和资讯类应用中。

ArkUI提供了WaterFlow容器组件，用于构建瀑布流布局。WaterFlow组件支持条件渲染、循环渲染和懒加载等方式生成子组件。

## 布局与约束

瀑布流支持横向和纵向布局。在纵向布局中，可以通过[columnsTemplate](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-waterflow.md#func-columnstemplatestring)设置列数；在横向布局中，可以通过rowsTemplate设置行数。

在瀑布流的纵向布局中，第一行的子节点按从左到右顺序排列，从第二行开始，每个子节点将放置在当前总高度最小的列。如果多个列的总高度相同，则按照从左到右的顺序填充。如下图：

![waterflow1](./figures/waterflow1.png)

在瀑布流的横向布局中，每个子节点都会放置在当前总宽度最小的行。若多行总宽度相同，则按照从上到下的顺序进行填充。

![waterflow2](./figures/waterflow2.png)