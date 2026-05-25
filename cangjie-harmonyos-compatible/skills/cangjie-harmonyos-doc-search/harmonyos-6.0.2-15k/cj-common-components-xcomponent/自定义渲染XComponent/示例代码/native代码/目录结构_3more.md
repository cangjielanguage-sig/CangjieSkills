#### 目录结构

![xcomponent_dir](figures/xcomponent_dir.png)

向项目中添加cpp目录。

#### common.h

```cpp
#ifndef NATIVE_XCOMPONENT_COMMON_H
#define NATIVE_XCOMPONENT_COMMON_H

#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <EGL/eglplatform.h>
#include <GLES3/gl3.h>

namespace NativeXComponentSample {
/**
 * Log print domain.
 */
const unsigned int LOG_PRINT_DOMAIN = 0xFF00;
} // namespace NativeXComponentSample
#endif // NATIVE_XCOMPONENT_COMMON_H
```

#### plugin_manager.h

```cpp
#ifndef NATIVE_XCOMPONENT_PLUGIN_MANAGER_H
#define NATIVE_XCOMPONENT_PLUGIN_MANAGER_H

#include <js_native_api.h>
#include <js_native_api_types.h>
#include <unordered_map>
#include <native_window/external_window.h>
#include "../render/plugin_render.h"

namespace NativeXComponentSample {
// PluginManager封装Native侧的绘制行为
class PluginManager {
public:
    ~PluginManager();
    static PluginRender* GetPluginRender(int64_t& id);
    static void* ChangeColor(int64_t surfaceId);
    static void* DrawPattern(int64_t surfaceId);
    static void* SetSurfaceId(int64_t surfaceId);
    static void* ChangeSurface(int64_t surfaceId, double width, double height);
    static void* DestroySurface(int64_t surfaceId);
    static bool GetXComponentHasDraw(int64_t surfaceId);
    static bool GetXComponentHasChangeColor(int64_t surfaceId);
public:
    static std::unordered_map<int64_t, PluginRender*> pluginRenderMap_;
    static std::unordered_map<int64_t, OHNativeWindow*> windowMap_;
};
} // namespace NativeXComponentSample
#endif // NATIVE_XCOMPONENT_PLUGIN_MANAGER_H
```