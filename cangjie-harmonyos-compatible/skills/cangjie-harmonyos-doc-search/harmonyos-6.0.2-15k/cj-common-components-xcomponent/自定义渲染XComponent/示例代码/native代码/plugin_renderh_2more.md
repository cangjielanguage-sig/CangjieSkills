#### plugin_render.h

```cpp
#ifndef NATIVE_XCOMPONENT_PLUGIN_RENDER_H
#define NATIVE_XCOMPONENT_PLUGIN_RENDER_H

#include <ace/xcomponent/native_interface_xcomponent.h>
#include <native_window/external_window.h>
#include "egl_core.h"

namespace NativeXComponentSample {
class PluginRender {
public:
    explicit PluginRender(int64_t& id);
    ~PluginRender()
    {
        if (eglCore_ != nullptr) {
            eglCore_->Release();
            delete eglCore_;
            eglCore_ = nullptr;
        }
    }
    void ChangeColor();
    void DrawPattern();
    int32_t HasDraw();
    int32_t HasChangedColor();
    void InitNativeWindow(OHNativeWindow* window);
    void UpdateNativeWindowSize(int width, int height);
private:
    EGLCore* eglCore_;
    int64_t id_;
    int32_t hasDraw_;
    int32_t hasChangeColor_;
};
} // namespace NativeXComponentSample
#endif // NATIVE_XCOMPONENT_PLUGIN_RENDER_H
```

#### plugin_render.cpp

``` cpp
#include <cstdint>
#include "plugin_render.h"
#include <cstdint>
#include "plugin_render.h"

namespace NativeXComponentSample {

PluginRender::PluginRender(int64_t& id)
{
    this->id_ = id;
    this->eglCore_ = new EGLCore();
    hasDraw_ = 0;
    hasChangeColor_ = 0;
}

void PluginRender::ChangeColor()
{
    eglCore_->ChangeColor(hasChangeColor_);
}

void PluginRender::DrawPattern()
{
    eglCore_->Draw(hasDraw_);
}

void PluginRender::InitNativeWindow(OHNativeWindow *window)
{
    eglCore_->EglContextInit(window);
}

void PluginRender::UpdateNativeWindowSize(int width, int height)
{
    eglCore_->UpdateSize(width, height);
    if (!hasChangeColor_ && !hasDraw_) {
        eglCore_->Background();
    }
}

int32_t PluginRender::HasDraw()
{
    return hasDraw_;
}

int32_t PluginRender::HasChangedColor()
{
    return hasChangeColor_;
}
} // namespace NativeXComponentSample
```

#### CMakeLists.txt

```text