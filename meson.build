project('Dear ImGui', 'cpp')

incdir = include_directories('/Users/jamie/imgui/backends', '/Users/jamie/imgui')

glfw_lib = subproject('glfw').get_variable('glfw_dep')
gl = dependency('gl')

files = files(
    'opengl_glfw_example.cpp',
    '/Users/jamie/imgui/imgui.cpp',
    '/Users/jamie/imgui/imgui_draw.cpp',
    '/Users/jamie/imgui/imgui_tables.cpp',
    '/Users/jamie/imgui/imgui_demo.cpp',
    '/Users/jamie/imgui/imgui_widgets.cpp',
    '/Users/jamie/imgui/imgui/backends/imgui_impl_glfw.cpp',
    '/Users/jamie/imgui/imgui/backends/imgui_impl_opengl3.cpp',
)

executable('example', files, include_directories : incdir, dependencies = [glfw_lib, gl])

files = files(
    'main.cpp',
    '/Users/jamie/imgui/imgui.cpp',
    '/Users/jamie/imgui/imgui_draw.cpp',
    '/Users/jamie/imgui/imgui_tables.cpp',
    '/Users/jamie/imgui/imgui_demo.cpp',
    '/Users/jamie/imgui/imgui_widgets.cpp',
    '/Users/jamie/imgui/imgui/backends/imgui_impl_glfw.cpp',
    '/Users/jamie/imgui/imgui/backends/imgui_impl_opengl3.cpp',
)