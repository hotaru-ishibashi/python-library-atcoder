import sys
import functools
import inspect
import threading
_local = threading.local()
_local.depth = 0
def debug_recursive(func):
    sig = inspect.signature(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 深さ・インデント
        depth = getattr(_local, 'depth', 0)
        indent = "    " * depth
        # 引数名 = 値 の形に変換
        bound = sig.bind_partial(*args)  # kwargs は無視
        bound.apply_defaults()
        arg_str = ", ".join(f"{k}={v}" for k, v in bound.arguments.items())
        # 呼び出しログ
        print(f"{indent}→ {func.__name__}({arg_str})", file=sys.stderr)
        # 深さを増加
        _local.depth = depth + 1
        try:
            result = func(*args, **kwargs)
        finally:
            # 戻す
            _local.depth = depth
        # 戻りログ
        print(f"{indent}← result = {result}", file=sys.stderr)
        return result
    return wrapper