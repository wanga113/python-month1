def calculate(a, op, b):
    """返回计算结果，如果除零返回 None"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return None
        return a / b
    else:
        return None   # 非法运算符
def main():
    print("=== 命令行计算器 ===")
    print("支持运算：+  -  *  /   输入 q 退出")
    while True:
        expr = input(">>> ").strip()
        if expr.lower() == 'q':
            print("拜拜～")
            break
        # 简易解析：按空格分割成 3 份
        parts = expr.split()
        if len(parts) != 3:
            print("格式错误！请按：数字 运算符 数字")
            continue
        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("输入的不是合法数字！")
            continue
        result = calculate(num1, op, num2)
        if result is None:
            print("出错：除零或非法运算符")
        else:
            # 保留 2 位小数，去掉末尾多余的 0
            print("=", round(result, 2))
if __name__ == "__main__":
    main()