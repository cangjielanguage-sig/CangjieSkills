import { CJHybridComponent } from '@cangjie/cjhybridcomponent';

@Entry
@Component
struct __WRAPPER_STRUCT__ {
  build() {
    Row() {
      CJHybridComponent({
        library: "__PACKAGE_NAME__",
        component: "__COMPONENT_NAME__"
      })
    }
    .height('100%')
    .width('100%')
  }
}
