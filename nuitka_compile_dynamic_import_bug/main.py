import pkgutil

import nuitka_compile_dynamic_import_bug.custom_package

if __name__ == '__main__':
    pkg_full_path = nuitka_compile_dynamic_import_bug.custom_package.__path__

    for item in pkgutil.iter_modules(pkg_full_path):
        if item.ispkg:
            continue

        # Way 1: find spec and get loader
        # # The loader object knows how to do it.
        # print('Finder: ', item.module_finder)
        # module_spec = item.module_finder.find_spec(item.name)
        # if module_spec is None:
        #     print("failed to load module spec", item.name)
        #     continue

        # module_loader = module_spec.loader
        # if module_loader is None:
        #     print("failed to load module loader", item.name)
        #     continue

        # Way 2:  find module
        module_loader = item.module_finder.find_module(item.name)
        print(module_loader)

        plugin_module = module_loader.load_module(item.name)
        print('Plugin module: ', plugin_module)
