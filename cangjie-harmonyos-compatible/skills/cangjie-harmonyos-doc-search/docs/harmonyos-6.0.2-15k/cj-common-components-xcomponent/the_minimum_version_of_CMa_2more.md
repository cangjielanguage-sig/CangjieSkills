# the minimum version of CMake.

cmake_minimum_required(VERSION 3.4.1)
project(XComponent)

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
add_definitions(-DOHOS_PLATFORM)

include_directories(
    ${NATIVERENDER_ROOT_PATH}
    ${NATIVERENDER_ROOT_PATH}/include
)

add_library(nativerender SHARED
    render/egl_core.cpp
    render/plugin_render.cpp
    manager/plugin_manager.cpp
    exportffi.cpp

# napi_init.cpp

)

find_library(
    # Sets the name of the path variable.
    EGL-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    EGL
)

find_library(
    # Sets the name of the path variable.
    GLES-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    GLESv3
)

find_library(
    # Sets the name of the path variable.
    hilog-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    hilog_ndk.z
)

find_library(
    # Sets the name of the path variable.
    libace-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    ace_ndk.z
)

find_library(
    # Sets the name of the path variable.
    libuv-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    uv
)

target_link_libraries(nativerender PUBLIC
    ${EGL-lib} ${GLES-lib} ${hilog-lib} ${libace-lib} ${libuv-lib} libnative_window.so)
```

#### exportffi.cpp

向仓颉暴露的ffi函数，是C++代码与仓颉代码的胶水层。

```cpp
#include <hilog/log.h>

#include "common/common.h"
#include "manager/plugin_manager.h"

#ifndef CJ_EXPORT
#ifdef WINDOWS_PLATFORM
#define CJ_EXPORT __declspec(dllexport)
#else
#define CJ_EXPORT __attribute__((visibility("default")))
#endif
#endif

namespace NativeXComponentSample {
EXTERN_C_START
CJ_EXPORT void FFIChangeColor(int64_t surfaceId)
{
    PluginManager::ChangeColor(surfaceId);
}

CJ_EXPORT void FFIDrawPattern(int64_t surfaceId)
{
    PluginManager::DrawPattern(surfaceId);
}

CJ_EXPORT void FFISetSurfaceId(int64_t surfaceId)
{
    PluginManager::SetSurfaceId(surfaceId);
}

CJ_EXPORT void FFIChangeSurface(int64_t surfaceId, double width, double height)
{
    PluginManager::ChangeSurface(surfaceId, width, height);
}

CJ_EXPORT void FFIDestroySurface(int64_t surfaceId)
{
    PluginManager::DestroySurface(surfaceId);
}

CJ_EXPORT bool FFIGetXComponentHasDraw(int64_t surfaceId)
{
    return PluginManager::GetXComponentHasDraw(surfaceId);
}

CJ_EXPORT bool FFIXComponentHasChangeColor(int64_t surfaceId)
{
    return PluginManager::GetXComponentHasChangeColor(surfaceId);
}
EXTERN_C_END

} // namespace NativeXComponentSample
```

### 配置构建

xcomponent_dir.png

native部分的产物libnativerender.so作为仓颉的依赖，需要被编译并打包到应用中。
要编译出C++的产物，需要修改对应module的build-profile.json5，向"builderOption"选项中添加以下配置。

```json
"externalNativeOptions": {
    "path": "./src/main/cpp/CMakeLists.txt",
    "arguments": "",
    "cppFlags": "",
    "abiFilters": ["arm64-v8a"]
},
```

以上配置可以在构建时编译出native产物，除此之外，还需要修改cjpm的配置，将native产物添加到仓颉的依赖中。

![xcomponent](figures/xcomponent.png)