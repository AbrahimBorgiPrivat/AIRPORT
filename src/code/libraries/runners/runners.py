import importlib

from libraries.utils import path_config, runtime


def main(runtime_vars: dict):
    module_name = runtime_vars.get("module_name")
    function_name = runtime_vars.get("function_name")
    if not module_name or not function_name:
        raise ValueError("Both 'module_name' and 'function_name' must be defined in runtime JSON")

    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)
    if not function:
        raise ImportError(f"Function '{function_name}' not found in module '{module_name}'")

    return function(runtime_vars)


if __name__ == "__main__":
    path = path_config.RUNTIME_PATH / "simulations" / "runtime" / "passports.json"
    runtime_vars = runtime.load_runtime_vars(JSON_PATH=path)
    main(runtime_vars)
